import res.res


class Colorful(object):
    @classmethod
    def getButtonQSS(cls, normalColor, normalTextColor, hoverColor, hoverTextColor, pressedColor, pressedTextColor):
        QSSList = []
        QSSList.append(u"QPushButton {border-style:none;padding:10px;border-radius:5px;color:%s;background:%s;}" % (normalTextColor, normalColor))
        QSSList.append("QPushButton:hover {color:%s;background:%s;}" % (hoverTextColor, hoverColor))
        QSSList.append("QPushButton:pressed {color:%s;background:%s;}" % (pressedTextColor, pressedColor))

        return " ".join(QSSList)

    @classmethod
    def getEditQSS(cls, normalColor, focusColor):
        QSSList = []
        QSSList.append('''
            QLineEdit, QTextEdit {
                border-style:none;
                padding:6px;
                border-radius:5px;
                border:2px solid %s;
                }''' % (str(normalColor)))
        QSSList.append('''
            QLineEdit:focus, QTextEdit:focus {
                border:2px solid %s;
                }''' % (str(focusColor)))

        return " ".join(QSSList)

    # setBarQss(ui->bar1, "#E8EDF2", "#E74C3C");
    # setBarQss(ui->bar2, "#E8EDF2", "#1ABC9C");
    @classmethod
    def getProgressBarQSS(cls, normalColor, chunkColor, barHeight=8, barRadius=8):
        QSSList = []
        QSSList.append("QProgressBar {font:9pt;height:%spx;background:%s;border-radius:%spx;text-align:center;border:1px solid %s;}" % (barHeight, normalColor, barRadius, str(normalColor)))
        QSSList.append("QProgressBar:chunk {border-radius:%spx;background-color:%s;}" % (barRadius, chunkColor))

        return " ".join(QSSList)

    @classmethod
    def getSilderQSS(cls, normalColor, grooveColor, handleColor, sliderHeight=8, sliderRadius=4, handleWidth=13, handleRadius=6, handleOffset=3):
        QSSList = []
        QSSList.append("QSlider::groove:horizontal,QSlider::add-page:horizontal{height:%spx;border-radius:%spx;background:%s;}" % (sliderHeight, sliderRadius, normalColor))
        QSSList.append("QSlider::sub-page:horizontal{height:%spx;border-radius:%spx;background:%s;}" % (sliderHeight, sliderRadius, grooveColor))
        QSSList.append("QSlider::handle:horizontal{width:%spx;margin-top:-%spx;margin-bottom:-%spx;border-radius:%spx;background:qradialgradient(spread:pad,cx:0.5,cy:0.5,radius:0.5,fx:0.5,fy:0.5,stop:0.6 #FFFFFF,stop:0.8 %s);}" % (handleWidth, handleOffset, handleOffset, handleRadius, handleColor))

        return " ".join(QSSList)
    @classmethod
    def getMenuQSS(cls, normalColor, normalTextColor, selectedColor, selectedTextColor):
        QSSList = []
        # QSSList.append('''QMenuBar {background-color: %s;border:8px}''' % (normalColor))
        QSSList.append('''QMenuBar::item{color:%s;background-color:%s;margin:0px;padding:3px 10px;border-radius:5px}''' % (normalTextColor, normalColor))
        QSSList.append('''QMenu, QMenuBar {color:#000000;background-color: #FFFFFF;border: 1px solid white;}''')
        # QSSList.append('''QMenu::item {background-color: transparent;padding:4px 55px;margin:3px 0px;}''')
        QSSList.append('''QMenu::item:selected, QMenuBar::item:selected {color:%s;background-color: %s;}''' % (selectedTextColor, selectedColor))

        return " ".join(QSSList)

    @classmethod
    def getWindowQSS(cls):
        QSSList = []
        QSSList.append('''
            QWidget, QMainWindow {
                background-color: #FFFFFF;
            }
        ''')
        return " ".join(QSSList)

    @classmethod
    def getDialogQSS(cls, normalColor):
        QSSList = []
        QSSList.append('''QColorDialog, QFileDialog, QMessageBox {background-color: %s;min-width:80px;}''' % (normalColor))

        return " ".join(QSSList)

    @classmethod
    def getTableQSS(cls):
        QSSList = []
        QSSList.append('''
            QScrollBar{
                background:#FFFFFF;
                padding-top:20px;
                padding-bottom:20px;
                padding-left:3px;
                padding-right:3px;
                border-left:1px solid #d7d7d7;
                }
        ''')
        QSSList.append('''
            QScrollBar::handle {
                background:#dbdbdb;
                border-radius:6px;
                min-height:80px;
                }
        ''')
        QSSList.append('''
            QScrollBar::handle:hover{
                background:#d0d0d0;
                }
        ''')
        # QSSList.append('''
        #     QScrollBar::add-line:{
        #         background:#FFFFFF center no-repeat;
        #         }
        # ''')
        # QSSList.append('''
        #     QScrollBar::sub-line{
        #         background:#FFFFFF center no-repeat;
        #         }
        # ''')

        return " ".join(QSSList)

    @classmethod
    def getSpinboxQSS(cls):
        QSSList = []
        QSSList.append('''
            QTimeEdit,QDoubleSpinBox,QSpinBox{
            }
        ''')

        QSSList.append('''
            QTimeEdit::up-button,QDoubleSpinBox::up-button,QSpinBox::up-button {
                subcontrol-origin:border;
                subcontrol-position:right;
                border-image: url(:/images/plus);
                width: 23px;
                height: 23px;
            }''')

        QSSList.append('''
            QTimeEdit::down-button,QDoubleSpinBox::down-button,QSpinBox::down-button {
                subcontrol-origin:border;
                subcontrol-position:left;
                border-image: url(:/images/minus);
                width: 23px;
                height: 23px;
            }
    ''')

        QSSList.append('''
            QTimeEdit::up-button:pressed,QDoubleSpinBox::up-button:pressed,QSpinBox::up-button:pressed{
                subcontrol-origin:border;
                subcontrol-position:right;
                border-image: url(:/images/pluspressed);
                width: 23px;
                height: 23px;
            }''')

        QSSList.append('''
            QTimeEdit::down-button:pressed,QDoubleSpinBox::down-button:pressed,QSpinBox::down-button:pressed{
                subcontrol-position:left;
                image: url(:/images/minuspressed);
                width: 23px;
                height: 23px;
            }''')

        return " ".join(QSSList)


class DarkBlue(object):
    def __init__(self):
        pass

    @classmethod
    def get_qss(cls):
        QSSList = []
        QSSList.append('''
            QLineEdit,QTextEdit,QPlainTextEdit,QSpinBox,QDoubleSpinBox,QComboBox,QDateEdit,QTimeEdit,QDateTimeEdit{
                border:1px solid #132743;
                border-radius:3px;
                padding:2px;
                background:none;
                selection-background-color:#133050;
                selection-color:#7AAFE3;
            }
        ''')
        QSSList.append('''
        QLineEdit:focus,QTextEdit:focus,QPlainTextEdit:focus,QSpinBox:focus,QDoubleSpinBox:focus,QComboBox:focus,QDateEdit:focus,QTimeEdit:focus,QDateTimeEdit:focus,QLineEdit:hover,QTextEdit:hover,QPlainTextEdit:hover,QSpinBox:hover,QDoubleSpinBox:hover,QComboBox:hover,QDateEdit:hover,QTimeEdit:hover,QDateTimeEdit:hover{
border:1px solid #132743;
}
        ''')
        QSSList.append('''
        QLineEdit:focus,QTextEdit:focus,QPlainTextEdit:focus,QSpinBox:focus,QDoubleSpinBox:focus,QComboBox:focus,QDateEdit:focus,QTimeEdit:focus,QDateTimeEdit:focus,QLineEdit:hover,QTextEdit:hover,QPlainTextEdit:hover,QSpinBox:hover,QDoubleSpinBox:hover,QComboBox:hover,QDateEdit:hover,QTimeEdit:hover,QDateTimeEdit:hover{
border:1px solid #132743;
}
        ''')

        return " ".join(QSSList)
