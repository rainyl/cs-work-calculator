# -*- coding: utf-8 -*-

# author: rainyl
# date: 2019-03-06
# all rights reserved

from src.MainWindow import MainWindow
from PyQt5.QtWidgets import QApplication
import sys


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
