# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'self.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5.QtWidgets import QMainWindow, QWidget, QStatusBar, QTabWidget, QTableWidgetItem, QVBoxLayout, QGridLayout, QLabel, QPushButton, QGroupBox, QLineEdit, QCheckBox, QFormLayout, QHBoxLayout, QTableWidget, QTextEdit
from PyQt5.QtCore import QMetaObject, QCoreApplication, QRegExp, QTimer, QDateTime
from PyQt5.QtGui import QRegExpValidator, QIntValidator, QIcon
from src.config import Ledt, Chkb, Txe, Others
from res.res import *


class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setup()
        self.regValidator = QRegExpValidator(QRegExp('(\+|\-|\*|\/){1, 4}'), self)

    def setup(self):
        self.setup_content()
        self.setup_global()
        self.setWindowIcon(QIcon(":/images/icon"))

    def setup_content(self):
        self.setup_generate()
        self.setup_score()
        self.setup_settings()
        self.setup_about()

        self.tab = QTabWidget(self)
        self.tab.addTab(self.grpbox_generate, 'generate')
        self.tab.addTab(self.grpbox_score, "score")
        self.tab.addTab(self.grpbox_settings, "settings")
        self.tab.addTab(self.txe_about, "about")

        self.vbox_layout = QVBoxLayout()
        self.vbox_layout.addWidget(self.tab)

    def setup_settings(self):
        _translate = QCoreApplication.translate
        # settings
        self.lbl_amount = QLabel("Amount")
        self.lbl_less_than = QLabel("Less than")
        self.lbl_item_num = QLabel("Item Num")
        self.lbl_operator = QLabel("Operators")
        self.lbl_decimal = QLabel("Decimals")

        self.ledt_amount = QLineEdit()
        self.ledt_amount.setValidator(QIntValidator(0, 1000))
        self.ledt_amount.setObjectName(Ledt.ledt_amount)
        self.ledt_amount.setStatusTip(_translate("The amount of the questions", "题目总数"))
        self.ledt_amount.setPlaceholderText(_translate("The amount of the questions", "题目总数"))
        self.ledt_less_than = QLineEdit()
        self.ledt_less_than.setValidator(QIntValidator(0, 10000))
        self.ledt_less_than.setObjectName(Ledt.ledt_less_than)
        self.ledt_less_than.setStatusTip(_translate("The nums will be less than", "多少以内"))
        self.ledt_less_than.setPlaceholderText(_translate("The nums will be less than", "多少以内"))
        self.ledt_item_num = QLineEdit()
        self.ledt_item_num.setValidator(QIntValidator(0, 10))
        self.ledt_item_num.setObjectName(Ledt.ledt_item_num)
        self.ledt_item_num.setStatusTip(_translate("How many items will there be in a question", "每道题目多少项"))
        self.ledt_item_num.setPlaceholderText(_translate("How many items will there be in a question", "每道题目多少项"))
        self.ledt_operator = QLineEdit()
        self.ledt_operator.setValidator(QRegExpValidator(QRegExp('(\+|\-|\*|\/|\%|\,){1,10}'), self))
        self.ledt_operator.setObjectName(Ledt.ledt_operator)
        self.ledt_operator.setToolTip(_translate("What operators will be use in the problems, separate by ','", "什么运算"))
        self.ledt_operator.setPlaceholderText(_translate("separate by ' , ' ", "英文半角逗号','分隔"))
        self.ledt_operator.setStatusTip(_translate("What operators will be use in the problems, separate by ','", "什么运算, 英文半角逗号分隔"))
        self.ledt_decimal = QLineEdit()
        self.ledt_decimal.setObjectName(Ledt.ledt_decimal)
        self.ledt_decimal.setValidator(QIntValidator(1, 5))
        self.ledt_decimal.setDisabled(True)
        self.ledt_decimal.setPlaceholderText(_translate("How many decimals", "小数位数"))
        self.ledt_decimal.setToolTip(_translate("How many decimals", "小数位数"))
        self.ledt_decimal.setStatusTip(_translate("How many decimals", "小数位数"))

        self.chkb_decimal = QCheckBox("Include decimals")
        self.chkb_decimal.setObjectName(Chkb.chkb_decimal)

        fmlt_left = QFormLayout()
        fmlt_left.addRow(self.lbl_amount, self.ledt_amount)
        fmlt_left.addRow(self.lbl_less_than, self.ledt_less_than)
        fmlt_left.addRow(self.chkb_decimal)

        fmlt_right = QFormLayout()
        fmlt_right.addRow(self.lbl_item_num, self.ledt_item_num)
        fmlt_right.addRow(self.lbl_operator, self.ledt_operator)
        fmlt_right.addRow(self.lbl_decimal, self.ledt_decimal)

        hbox_layout_up = QHBoxLayout()
        hbox_layout_up.addLayout(fmlt_left)
        hbox_layout_up.addLayout(fmlt_right)

        self.btn_save = QPushButton("&Save")
        self.btn_save.setObjectName("btn_save")
        self.btn_cancel = QPushButton("&Cancel")
        self.btn_cancel.setObjectName("btn_cancel")

        hbox_layout_down = QHBoxLayout()
        hbox_layout_down.addWidget(self.btn_save)
        hbox_layout_down.addWidget(self.btn_cancel)

        layout_settings = QGridLayout()
        layout_settings.addLayout(hbox_layout_up, 0, 0)
        layout_settings.setRowStretch(0, 10)
        layout_settings.setRowStretch(1, 6)
        layout_settings.addLayout(hbox_layout_down, 1, 0)
        self.grpbox_settings = QGroupBox(self)
        self.grpbox_settings.setLayout(layout_settings)
        # settings end

    def setup_generate(self):
        # generate begin
        self.btn_generate = QPushButton("&Generate")
        self.btn_submit = QPushButton('&Submit')

        lbl = QLabel("hi")
        ledt = QLineEdit()
        self.table_problems = QTableWidget()
        self.table_problems.setColumnCount(2)
        self.table_problems.setRowCount(1)
        self.table_problems.setSortingEnabled(False)
        self.table_problems.setHorizontalHeaderLabels(['题目', '解答'])
        self.table_problems.setCellWidget(0, 0, lbl)
        self.table_problems.setCellWidget(0, 1, ledt)
        self.table_problems.setColumnWidth(0, 200)

        btn_layout = QHBoxLayout()
        btn_layout.addWidget(self.btn_generate)
        btn_layout.addWidget(self.btn_submit)
        layout_generate = QVBoxLayout()
        layout_generate.addWidget(self.table_problems)
        layout_generate.addLayout(btn_layout)
        self.grpbox_generate = QGroupBox(self)
        self.grpbox_generate.setLayout(layout_generate)
        # geneate end

    def setup_score(self):
        # this time begin
        self.lbl_score = QLabel("Score")
        self.ledt_score = QLineEdit()
        self.ledt_score.setDisabled(True)
        self.lbl_cocrrect_rate = QLabel("Correct rate")
        self.ledt_correct_rate = QLineEdit()
        self.ledt_correct_rate.setDisabled(True)

        layout_left = QFormLayout()
        layout_left.addRow(self.lbl_score, self.ledt_score)
        layout_left.addRow(self.lbl_cocrrect_rate, self.ledt_correct_rate)
        self.grpbox_left = QGroupBox("This time")
        self.grpbox_left.setLayout(layout_left)
        # this time end

        # total begin
        self.lbl_score_total = QLabel("Score")
        self.ledt_score_all = QLineEdit()
        self.ledt_score_all.setDisabled(True)
        self.lbl_cocrrect_rate_total = QLabel("Correct rate")
        self.ledt_correct_rate_all = QLineEdit()
        self.ledt_correct_rate_all.setDisabled(True)

        layout_right = QFormLayout()
        layout_right.addRow(self.lbl_score_total, self.ledt_score_all)
        layout_right.addRow(self.lbl_cocrrect_rate_total, self.ledt_correct_rate_all)
        self.grpbox_right = QGroupBox("Total")
        self.grpbox_right.setLayout(layout_right)
        # total end

        hbox_layout = QHBoxLayout()
        hbox_layout.addWidget(self.grpbox_left)
        hbox_layout.addWidget(self.grpbox_right)

        # button function area begin
        self.btn_again = QPushButton("&Again")
        self.btn_exit = QPushButton("&Exit")

        btn_layout = QHBoxLayout()
        btn_layout.addWidget(self.btn_again)
        btn_layout.addWidget(self.btn_exit)
        # button function area end

        # global for score tab
        layout_score = QVBoxLayout()
        layout_score.addLayout(hbox_layout)
        layout_score.addLayout(btn_layout)
        self.grpbox_score = QGroupBox(self)
        self.grpbox_score.setLayout(layout_score)

    def setup_about(self):
        self.txe_about = QTextEdit()
        self.txe_about.setDisabled(True)
        self.txe_about.setText(Txe.about)


    def setup_global(self):
        self.setObjectName("MainWindow")
        self.resize(800, 600)
        layout = QGridLayout()
        layout.addLayout(self.vbox_layout, 0, 0)
        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setLayout(layout)
        self.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.timer = QTimer(self)
        self.timer.start(1000)
        # 时钟设置开始
        self.timer.timeout.connect(self.on_time_updated)
        # 时钟设置结束
        self.copyright = QLabel()
        self.copyright.setStatusTip("https://github.com/rainyl")
        self.statusbar.addPermanentWidget(self.copyright)

        self.retranslate_UI()
        QMetaObject.connectSlotsByName(self)

    def retranslate_UI(self):
        _translate = QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", Others.main_window_title))
        self.btn_generate.setText(_translate("generate", "生成"))
        self.btn_submit.setText(_translate("submit", "提交"))
        self.btn_again.setText(_translate("again", "再来一次"))
        self.btn_exit.setText(_translate("exit", "退出"))
        self.btn_save.setText(_translate("save", "保存"))
        self.btn_cancel.setText(_translate("cancel", "取消"))

        self.lbl_amount.setText(_translate("amount", "总数"))
        self.lbl_less_than.setText(_translate("less than", "小于"))
        self.lbl_item_num.setText(_translate("item num", "项数"))
        self.lbl_operator.setText(_translate("operators", "运算符"))
        self.chkb_decimal.setText(_translate("decimal", "小数"))
        self.lbl_decimal.setText(_translate("decimals", "小数位数"))
        self.lbl_score.setText(_translate("score", "分数"))
        self.lbl_score_total.setText(_translate("score", "分数"))
        self.lbl_cocrrect_rate.setText(_translate("correct rate", "正确率"))
        self.lbl_cocrrect_rate_total.setText(_translate("correct rate", "正确率"))

        self.grpbox_left.setTitle(_translate("this time", "本次"))
        self.grpbox_right.setTitle(_translate("total", "合计"))

        self.tab.setTabText(0, _translate("generate", "生成题目"))
        self.tab.setTabText(1, _translate("score", "分数"))
        self.tab.setTabText(2, _translate("settings", "设置"))
        self.tab.setTabText(3, _translate("about", "关于"))

    # 设置时间
    def on_time_updated(self):
        current_time = QDateTime.currentDateTime()
        self.copyright.setText(
            "<a href='https://github.com/rainyl'>©2019 Rainyl's Team All Rights Reserved " + "</a>" + current_time.toString(
                " hh:mm:ss"))

