import csv
import logging

import requests
from bs4 import BeautifulSoup
from requests import Response


class Report:
    def __init__(
        self,
        numOfPage: int,
        pageSize: int,
        url: str,
        indexColumn=None,
    ):
        self.url = url
        self.numOfPage = numOfPage
        self.pageSize = pageSize
        self.indexColumn = indexColumn

    def getPageResponse(self, **kwargs) -> Response:
        payload = self.getParams(**kwargs)
        resp = requests.get(self.url, params=payload)
        logging.info("resp %r %r", resp.url, payload)
        return resp

    def getPageSoup(self, **kwargs) -> BeautifulSoup:
        return BeautifulSoup(self.getPageResponse(**kwargs).content, "lxml")

    def getParams(self, **kwargs):
        raise NotImplementedError
        # return kwargs

    def saveAsCsv(self, outputFile="./output/report.csv") -> str:
        header = self.reportHeader
        body = self.reportBody
        body_len = self.numOfPage * self.pageSize

        if len(body) != body_len:
            logging.warning("Request %d insted of %d", len(body), body_len)
            body = body[:body_len]

        with open(outputFile, "w") as f:
            writer = csv.writer(f, quoting=csv.QUOTE_MINIMAL)

            writer.writerow(header)
            writer.writerows(body)
        return outputFile

    @property
    def reportHeader(self):
        raise NotImplementedError

    @property
    def reportBody():
        raise NotImplementedError
