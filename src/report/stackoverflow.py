from __future__ import annotations

import math
from typing import List

import requests
from bs4 import BeautifulSoup
from bs4.element import Tag

from .base import Report


class StackOverflowReport(Report):
    DEFAULT_PAGE_SIZE = 50

    def __init__(
        self,
        numOfPage=5,
        pageSize=15,
        url="https://stackoverflow.com/questions/tagged/python",
        indexColumn=None,
    ):
        super().__init__(
            numOfPage=numOfPage,
            pageSize=pageSize,
            url=url,
            indexColumn=indexColumn,
        )
        self.reportSize = numOfPage * pageSize

    def getPage(self, page) -> Page:
        return Page(self.getPageSoup(page=page))

    def getListQuestions(self) -> List[Question]:
        results = []
        for page in range(
            math.ceil(self.numOfPage * self.pageSize / self.DEFAULT_PAGE_SIZE)
        ):
            results.extend(self.getPage(page + 1).getQuestions())
        return results[: self.reportSize]
        # return [
        #     *self.getPage(page + 1).getQuestions()
        #     for page in range(
        #         math.ceil(self.numOfPage * self.pageSize / self.DEFAULT_PAGE_SIZE)
        #     )
        # ]

    def getListQuestionsAsList(self) -> List[list]:
        return [question.asList() for question in self.getListQuestions()]

    def getParams(self, **kwargs):
        return {"tab": "newest", "pagesize": self.pageSize, **kwargs}

    @property
    def reportHeader(self):
        return (
            [self.indexColumn] + Question.ATTRIBUTES
            if self.indexColumn
            else Question.ATTRIBUTES
        )

    @property
    def reportBody(self):
        return (
            [[i + 1, *values] for i, values in enumerate(self.getListQuestionsAsList())]
            if self.indexColumn
            else self.getListQuestionsAsList()
        )


class Page:
    def __init__(self, soup: BeautifulSoup):
        self.soup = soup

    def getQuestionTags(self) -> List[Tag]:
        return self.soup.find("div", attrs={"id": "questions"}).find_all(
            "div", attrs={"class": "question-summary"}
        )

    def getQuestions(self) -> List[Question]:
        return [Question(tag) for tag in self.getQuestionTags()]

    def getQuestionsAsList(self) -> List[list]:
        return [question.asList() for question in self.getQuestions()]


class Question:
    ATTRIBUTES = ["title", "content", "vote", "answer", "view"]

    def __init__(
        self,
        tag: Tag,
    ):
        self.tag = tag

        self.title = self.tag.find("a").contents[0].strip()
        self.content: str = str(
            (
                self.tag.find("div", attrs={"class": "excerpt"}).contents[0].strip()
            ).encode("utf-8")
        )[2:-1]
        self.vote = int(
            tag.find("span", attrs={"class": "vote-count-post"})
            .find("strong")
            .contents[0]
        )
        self.answer = int(
            (
                tag.find("div", attrs={"class": "unanswered"})
                or tag.find("div", attrs={"class": "answered"})
                or tag.find("div", attrs={"class": "answered-accepted"})
            )
            .find("strong")
            .contents[0]
        )
        self.view = int(
            (tag.find("div", attrs={"class": "views"}).contents)[0].strip()[:-6]
        )

    def asList(self) -> list:
        return [getattr(self, attr) for attr in self.ATTRIBUTES]
