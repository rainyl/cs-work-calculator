from src.Ui_MainWindow import Ui_MainWindow
from src.config import Ledt, Chkb, Spbx, Others
from src.generator import Generator
from src.score import Calculator
from PyQt5.QtWidgets import QMessageBox, QLineEdit, QTableWidgetItem, QLCDNumber
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QTimer
import logging
import sys


class MainWindow(Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.config_args = Others.config_args
        self.timer = QTimer()
        self.timer_count = None

        self.init_slots()

        self.problems = None
        self.answers = []

    def init_window(self):
        pass

    def init_slots(self):
        # 全局
        self.timer.timeout.connect(self.on_timer_timeout)
        # 全局结束

        # 设置页面
        self.ledt_amount.editingFinished.connect(self.on_ledt_edited)
        self.ledt_less_than.editingFinished.connect(self.on_ledt_edited)
        self.ledt_item_num.editingFinished.connect(self.on_ledt_edited)
        self.ledt_operator.editingFinished.connect(self.on_ledt_edited)
        self.ledt_decimal.editingFinished.connect(self.on_ledt_edited)

        self.spbx_timer.editingFinished.connect(self.on_spbx_edited)

        self.chkb_decimal.stateChanged.connect(self.on_chkb_decimal_changed)

        self.btn_save.clicked.connect(self.on_btn_save_clicked)
        self.btn_cancel.clicked.connect(self.on_btn_calcel_clicked)
        # 设置页面结束

        # 生成页面
        self.btn_generate.clicked.connect(self.on_btn_generate_clicked)
        self.btn_submit.clicked.connect(self.on_btn_submit_clicked)
        # 生成页面结束

        # 分数页面开始
        self.btn_again.clicked.connect(self.on_btn_again_clicked)
        self.btn_exit.clicked.connect(self.on_btn_exit_clicked)
        # 分数页面结束

    # 设置页面
    def on_btn_save_clicked(self):
        pass

    def on_btn_calcel_clicked(self):
        self.config_args = {}
        self.ledt_amount.clear()
        self.ledt_less_than.clear()
        self.ledt_item_num.clear()
        self.ledt_operator.clear()
        logging.warning(len(self.config_args))

    def on_ledt_edited(self):
        sender = self.sender()
        if sender.objectName() == Ledt.ledt_operator:
            operators = sender.text().split(",")
            self.config_args[sender.objectName()] = operators
        else:
            try:
                self.config_args[sender.objectName()] = int(sender.text())
            except:
                QMessageBox.warning(self, "Warning", "Input Error!")

        logging.warning(self.config_args)

    def on_spbx_edited(self):
        sender = self.sender()
        if sender.objectName() == Spbx.spbx_timer:
            print("spinbox edit finished")
            self.config_args[Spbx.spbx_timer] = sender.value()
            self.timer_count = self.config_args[Spbx.spbx_timer]

    def on_chkb_decimal_changed(self, state):
        if state == Qt.Checked:
            self.config_args[self.sender().objectName()] = True
            self.ledt_decimal.setDisabled(False)
        else:
            self.config_args[self.sender().objectName()] = False
            self.ledt_decimal.setDisabled(True)

        logging.warning(self.config_args)
    # 设置页面结束

    # 生成页面槽函数
    def on_btn_generate_clicked(self):
        if self.is_config_ok():
            self.problems = []
            if len(self.config_args) == 0:
                QMessageBox.warning(self, "Warning", "please set args in settings first")
            else:
                generator = Generator(self.config_args)
                self.problems = generator.generate()
                logging.warning(self.problems)

            self.table_problems.setRowCount(0)
            self.table_problems.setRowCount(self.config_args[Ledt.ledt_amount])
            self.table_problems.setHorizontalHeaderLabels(['题目', '解答'])
            # self.table_problems.clearContents()
            for e in self.problems:
                row = self.problems.index(e)
                e_ = [str(i) for i in e]
                self.table_problems.setItem(row, 0, QTableWidgetItem("   ".join(e_) + "   =   "))
                self.table_problems.setCellWidget(row, 1, QLineEdit())
        self.timer.start(1000)

    def on_btn_submit_clicked(self):
        self.answers = []
        for row in range(self.table_problems.rowCount()):
            ledt = self.table_problems.cellWidget(row, 1)
            if ledt is not None:
                ans = ledt.text()
                if len(ans) != 0:
                    self.answers.append(float(ans) if self.config_args[Chkb.chkb_decimal] else int(ans))
                else:
                    self.answers.append(None)
            else:
                logging.warning("ledt is None")

        self.timer.stop()
        self.set_ledt()

    def set_table_icon(self, answers):
        for i in range(len(answers)):
            if answers[i][0] == answers[i][1]:
                self.table_problems.setItem(i, 2, QTableWidgetItem(QIcon(":/icons/right"), " "))
            else:
                self.table_problems.setItem(i, 2, QTableWidgetItem(QIcon(":/icons/wrong"), " "))

    # 生成页面结束

    # 评测页面开始
    def on_btn_again_clicked(self):
        self.on_btn_generate_clicked()

    def on_btn_exit_clicked(self):
        sys.exit(0)

    def set_ledt(self):
        if self.problems is None or len(self.problems) == 0:
            QMessageBox.warning(self, "Warning", "Generate first!!!")
        else:
            calculator = Calculator(self.problems, self.answers)
            score = calculator.score()
            rate = calculator.rate()
            self.ledt_score.setText(str(score))
            self.ledt_correct_rate.setText(str(rate*100) + ' %')

            ans = calculator.answers_calculated
            self.set_table_icon(ans)
    # 评测页面结束

    # timer
    def on_timer_timeout(self):
        if self.timer_count is None or self.config_args[Spbx.spbx_timer] == 0:
            return
        if self.timer_count == 0:
            QMessageBox.warning(self, "Warning", "time up")
            self.on_btn_submit_clicked()
            return
        self.timer_count = self.timer_count - 1
        self.lcd_timer.display(self.timer_count)
        # self.lbl_timer_generator.setText("<b"str(self.timer_count))

    # 判断配置是否正确
    def is_config_ok(self):
        keys = self.config_args.keys()
        # 暂时简单用参数名称数量判断，，，详细太麻烦了
        # TODO 详细参数判断与错误提示
        if len(keys) != 7:
            QMessageBox.warning(self, "Warning", "Config Error!!!")
            return False
        return True
