import tkinter as tk
from tkinter import ttk
from tkinter.constants import VERTICAL

import settings
from app import root
from report.stackoverflow import Question, StackOverflowReport


class ActionBar:
    def __init__(self, master) -> None:
        self.num_of_page = settings.SOF_NUM_OF_PAGE
        self.page_size = settings.SOF_PAGE_SIZE

        self.func_bt_exec = None

        self.tk_frame = tk.Frame(master)
        self.var_NOP = tk.IntVar(value=self.num_of_page)
        self.var_PS = tk.IntVar(value=self.page_size)

        self.tk_NOP = tk.Label(self.tk_frame, text="Num of page")
        self.ttk_NOP = ttk.Entry(self.tk_frame, width=15, textvariable=self.var_NOP)
        self.tk_PS = tk.Label(self.tk_frame, text="Page size")
        self.ttk_PS = ttk.Entry(self.tk_frame, width=15, textvariable=self.var_PS)
        self.tk_bt_exec = tk.Button(
            self.tk_frame, width=10, text="Exec", command=self.func_bt_exec
        )

    def rebuild_button(self):
        self.tk_bt_exec = tk.Button(
            self.tk_frame, width=10, text="Exec", command=self.func_bt_exec
        )

    def build(self):
        self.tk_frame.grid(column=0, row=0)
        self.tk_NOP.grid(column=0, row=0, sticky="W")
        self.ttk_NOP.grid(column=1, row=0)
        self.tk_PS.grid(column=0, row=1, sticky="W")
        self.ttk_PS.grid(column=1, row=1)
        self.tk_bt_exec.grid(column=2, row=0, rowspan=2, sticky="NWS")

    def update_variable(self):
        self.num_of_page = self.var_NOP.get()
        self.page_size = self.var_PS.get()

    def destroy(self):
        self.ttk_PS.grid_forget()
        self.tk_PS.grid_forget()
        self.ttk_PS.grid_forget()
        self.tk_NOP.grid_forget()
        self.tk_frame.grid_forget()
        self.tk_bt_exec.grid_forget()


class ReportTable:
    report_head_map = {
        "No": dict(width=10, entry=tk.Label),
        "title": dict(width=15, entry=tk.Text),
        "content": dict(width=35, entry=tk.Text),
        "vote": dict(width=7, entry=tk.Label),
        "answer": dict(width=7, entry=tk.Label),
        "view": dict(width=7, entry=tk.Label),
    }

    def __init__(self, master, report: StackOverflowReport = None) -> None:
        self.index_column = settings.SOF_INDEX_COLUMN
        self.report_header = (
            [self.index_column] if self.index_column is not None else []
        ) + Question.ATTRIBUTES
        self.report = report

        self.tk_table = tk.Frame(master)
        self.tk_heads = []
        self.tk_bodies = []

    def build(self):
        self.tk_table.grid(column=0, row=3, sticky="EW")

        for i, value in enumerate(self.report_header):
            width = self.report_head_map[value]["width"]
            entry = self.report_head_map[value]["entry"]
            tk_head = tk.Label(
                self.tk_table, width=width, text=value, borderwidth=1, relief="solid"
            )
            tk_head.grid(column=i, row=3)
            self.tk_heads.append(tk_head)
        if self.report is not None:
            self.build_body()

    def build_body(self):
        self.tk_table_body = tk.Frame(self.tk_table)
        self.tk_table_body.grid(column=0, columnspan=7, row=4, sticky="NEWS")
        for record in self.report.reportBody:
            tk_records = []
            for i, value in enumerate(record):
                width = self.report_head_map[self.report_header[i]]["width"]
                tk_body = tk.Label(
                    self.tk_table_body,
                    width=width,
                    text=value,
                    borderwidth=1,
                    relief="solid",
                )
                tk_body.grid(column=i, row=4 + len(self.tk_bodies))
                tk_records.append(tk_body)
            self.tk_bodies.append(tk_records)

    def rebuild_body(self):
        self.destroy_body()
        self.build_body()

    def destroy(self):
        self.destroy_body()
        for tk in self.tk_heads:
            tk.grid_forget()
        self.tk_table.grid_forget()

    def destroy_body(self):
        if not self.tk_bodies:
            return
        self.tk_table_body.grid_forget()
        for records in self.tk_bodies:
            for tk in records:
                tk.grid_forget()


def make_homepage():
    action_bar = ActionBar(root)
    report_table = ReportTable(root)

    def exec():
        nonlocal action_bar, report_table

        print("Start Exec")
        action_bar.update_variable()
        report_table.report = StackOverflowReport(
            numOfPage=action_bar.num_of_page,
            pageSize=action_bar.page_size,
            indexColumn=settings.SOF_INDEX_COLUMN,
        )
        print("Building body")
        report_table.rebuild_body()
        print("Done")

    action_bar.func_bt_exec = exec
    action_bar.rebuild_button()
    action_bar.build()
    report_table.build()

    # tk_table_body_scroll = ttk.Scrollbar(root, orient="vertical", orient='vertical')
    # tk_table_body_scroll.pack(side = "right", fill = tk.X)
    # tk_table_body_scroll.config(command=report_table.tk_table.)

    # num_of_page = settings.SOF_NUM_OF_PAGE
    # page_size = settings.SOF_PAGE_SIZE
    # index_column = settings.SOF_INDEX_COLUMN
    # report: StackOverflowReport = None

    # def make_action_bar(master):
    #     nonlocal num_of_page, page_size

    #     tk_frame = tk.Frame(master).grid(column=0, row=0)
    #     tk_num_of_page = tk.IntVar(value=num_of_page)
    #     tk_page_size = tk.IntVar(value=page_size)

    #     tk.Label(tk_frame, text="Num of page").grid(column=0, row=0, sticky="W")
    #     ttk.Entry(tk_frame, width=15, textvariable=tk_num_of_page).grid(column=1, row=0)
    #     tk.Label(tk_frame, text="Page size").grid(column=0, row=1, sticky="W")
    #     ttk.Entry(tk_frame, width=15, textvariable=tk_page_size).grid(column=1, row=1)

    #     def update_variable():
    #         nonlocal num_of_page, page_size, tk_num_of_page, tk_page_size

    #         num_of_page = tk_num_of_page.get()
    #         page_size = tk_page_size.get()

    #     def run():
    #         nonlocal num_of_page, page_size, report

    #         update_variable()
    #         print("num_of_page", num_of_page, "page_size", page_size)
    #         report = StackOverflowReport(numOfPage=num_of_page, pageSize=page_size)

    #     tk.Button(tk_frame, width=10, text="Exec", command=run).grid(
    #         column=2, row=0, rowspan=2, sticky="NWS"
    #     )

    # def make_report_body(master):
    #     nonlocal report, index_column

    #     tk_body = tk.Frame(master).grid(column=0, row=3, sticky="EW")

    #     report_header = (
    #         [index_column] if index_column is not None else []
    #     ) + Question.ATTRIBUTES
    #     for i, value in enumerate(report_header):
    #         width = tk_body_map[value]["width"]
    #         entry = tk_body_map[value]["entry"]
    #         tk.Label(
    #             tk_body, width=width, text=value, borderwidth=3, relief="solid"
    #         ).grid(column=i, row=3)
    #     if report is None:
    #         return tk_body
    #     for j, record in enumerate(report.reportBody):
    #         for i, value in enumerate(record):
    #             tk.Label(
    #                 tk_body, width=width, text=value, borderwidth=1, relief="solid"
    #             ).grid(column=i, row=4 + j)

    #     return tk_body

    # make_action_bar(root)
    # make_report_body(root)
