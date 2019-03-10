from src.Ui_MainWindow import Ui_MainWindow
from src.config import Ledt
from PyQt5.QtCore import Qt
import logging


class SettingsTab(Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.init_slots()
        self.config_args = {}

    def init_window(self):
        pass

    def init_slots(self):
        self.ledt_amount.editingFinished.connect(self.on_ledt_edited)
        self.ledt_less_than.editingFinished.connect(self.on_ledt_edited)
        self.ledt_item_num.editingFinished.connect(self.on_ledt_edited)
        self.ledt_operator.editingFinished.connect(self.on_ledt_edited)

        self.chkb_decimal.stateChanged.connect(self.on_chkb_decimal_changed)

        self.btn_save.clicked.connect(self.on_btn_save_clicked)
        self.btn_cancel.clicked.connect(self.on_btn_calcel_clicked)

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
            self.config_args[sender.objectName()] = float(sender.text())

        logging.warning(self.config_args)

    def on_chkb_decimal_changed(self, state):
        if state == Qt.Checked:
            self.config_args[self.sender().objectName()] = True
        else:
            self.config_args[self.sender().objectName()] = False

        logging.warning(self.config_args)
