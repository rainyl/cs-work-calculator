from src.qss import *


class FlatDark(object):
    @classmethod
    def get_qss(cls):
        qss = '''
        QPalette{background:#2E2F30;}*{outline:0px;color:#BEC0C2;}

        QWidget[form="true"],QLabel[frameShape="1"]{
        border:1px solid #67696B;
        border-radius:0px;
        }
        
        QWidget[form="bottom"]{
        background:#404244;
        }
        
        QWidget[form="bottom"] .QFrame{
        border:1px solid #BEC0C2;
        }
        
        QWidget[form="bottom"] QLabel,QWidget[form="title"] QLabel{
        border-radius:0px;
        color:#BEC0C2;
        background:none;
        border-style:none;
        }
        
        QWidget[form="title"],QWidget[nav="left"],QWidget[nav="top"] QAbstractButton{
        border-style:none;
        border-radius:0px;
        padding:5px;
        color:#BEC0C2;
        background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #404244,stop:1 #404244);
        }
        
        QWidget[nav="top"] QAbstractButton:hover,QWidget[nav="top"] QAbstractButton:pressed,QWidget[nav="top"] QAbstractButton:checked{
        border-style:solid;
        border-width:0px 0px 2px 0px;
        padding:4px 4px 2px 4px;
        border-color:#00BB9E;
        background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #262829,stop:1 #262829);
        }
        
        QWidget[nav="left"] QAbstractButton{
        border-radius:0px;
        color:#BEC0C2;
        background:none;
        border-style:none;
        }
        
        QWidget[nav="left"] QAbstractButton:hover{
        color:#FFFFFF;
        background-color:#00BB9E;
        }
        
        QWidget[nav="left"] QAbstractButton:checked,QWidget[nav="left"] QAbstractButton:pressed{
        color:#BEC0C2;
        border-style:solid;
        border-width:0px 0px 0px 2px;
        padding:4px 4px 4px 2px;
        border-color:#00BB9E;
        background-color:#2E2F30;
        }
        
        QWidget[video="true"] QLabel{
        color:#BEC0C2;
        border:1px solid #67696B;
        background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #404244,stop:1 #404244);
        }
        
        QWidget[video="true"] QLabel:focus{
        border:1px solid #00BB9E;
        background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #262829,stop:1 #262829);
        }
        
        QLineEdit,QTextEdit,QPlainTextEdit,QSpinBox,QDoubleSpinBox,QComboBox,QDateEdit,QTimeEdit,QDateTimeEdit{
        border:1px solid #67696B;
        border-radius:3px;
        padding:2px;
        background:none;
        selection-background-color:#404244;
        selection-color:#BEC0C2;
        }
        
        QLineEdit:focus,QTextEdit:focus,QPlainTextEdit:focus,QSpinBox:focus,QDoubleSpinBox:focus,QComboBox:focus,QDateEdit:focus,QTimeEdit:focus,QDateTimeEdit:focus,QLineEdit:hover,QTextEdit:hover,QPlainTextEdit:hover,QSpinBox:hover,QDoubleSpinBox:hover,QComboBox:hover,QDateEdit:hover,QTimeEdit:hover,QDateTimeEdit:hover{
        border:1px solid #67696B;
        }
        
        QLineEdit[echoMode="2"]{
        lineedit-password-character:9679;
        }
        
        .QFrame{
        border:1px solid #67696B;
        border-radius:3px;
        }
        
        .QGroupBox{
        border:1px solid #67696B;
        border-radius:5px;
        margin-top:3ex;
        }
        
        .QGroupBox::title{
        subcontrol-origin:margin;
        position:relative;
        left:10px;
        }
        
        .QPushButton,.QToolButton{
        border-style:none;
        border:1px solid #67696B;
        color:#BEC0C2;
        padding:5px;
        min-height:15px;
        border-radius:5px;
        background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #404244,stop:1 #404244);
        }
        
        .QPushButton:hover,.QToolButton:hover{
        background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #262829,stop:1 #262829);
        }
        
        .QPushButton:pressed,.QToolButton:pressed{
        background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #404244,stop:1 #404244);
        }
        
        .QToolButton::menu-indicator{
        image:None;
        }
        
        QToolButton#btnMenu,QPushButton#btnMenu_Min,QPushButton#btnMenu_Max,QPushButton#btnMenu_Close{
        border-radius:3px;
        color:#BEC0C2;
        padding:3px;
        margin:0px;
        background:none;
        border-style:none;
        }
        
        QToolButton#btnMenu:hover,QPushButton#btnMenu_Min:hover,QPushButton#btnMenu_Max:hover{
        color:#FFFFFF;
        margin:1px 1px 2px 1px;
        background-color:rgba(51,127,209,230);
        }
        
        QPushButton#btnMenu_Close:hover{
        color:#FFFFFF;
        margin:1px 1px 2px 1px;
        background-color:rgba(238,0,0,128);
        }
        
        QRadioButton::indicator{
        width:15px;
        height:15px;
        }
        
        QRadioButton::indicator::unchecked{
        image:url(:/qss/flatblack/radiobutton_unchecked.png);
        }
        
        QRadioButton::indicator::unchecked:disabled{
        image:url(:/qss/flatblack/radiobutton_unchecked_disable.png);
        }
        
        QRadioButton::indicator::checked{
        image:url(:/qss/flatblack/radiobutton_checked.png);
        }
        
        QRadioButton::indicator::checked:disabled{
        image:url(:/qss/flatblack/radiobutton_checked_disable.png);
        }
        
        QGroupBox::indicator,QTreeWidget::indicator,QListWidget::indicator{
        padding:0px -3px 0px 3px;
        }
        
        QCheckBox::indicator,QGroupBox::indicator,QTreeWidget::indicator,QListWidget::indicator{
        width:13px;
        height:13px;
        }
        
        QCheckBox::indicator:unchecked,QGroupBox::indicator:unchecked,QTreeWidget::indicator:unchecked,QListWidget::indicator:unchecked{
        image:url(:/qss/flatblack/checkbox_unchecked.png);
        }
        
        QCheckBox::indicator:unchecked:disabled,QGroupBox::indicator:unchecked:disabled,QTreeWidget::indicator:unchecked:disabled,QListWidget::indicator:disabled{
        image:url(:/qss/flatblack/checkbox_unchecked_disable.png);
        }
        
        QCheckBox::indicator:checked,QGroupBox::indicator:checked,QTreeWidget::indicator:checked,QListWidget::indicator:checked{
        image:url(:/qss/flatblack/checkbox_checked.png);
        }
        
        QCheckBox::indicator:checked:disabled,QGroupBox::indicator:checked:disabled,QTreeWidget::indicator:checked:disabled,QListWidget::indicator:checked:disabled{
        image:url(:/qss/flatblack/checkbox_checked_disable.png);
        }
        
        QCheckBox::indicator:indeterminate,QGroupBox::indicator:indeterminate,QTreeWidget::indicator:indeterminate,QListWidget::indicator:indeterminate{
        image:url(:/qss/flatblack/checkbox_parcial.png);
        }
        
        QCheckBox::indicator:indeterminate:disabled,QGroupBox::indicator:indeterminate:disabled,QTreeWidget::indicator:indeterminate:disabled,QListWidget::indicator:indeterminate:disabled{
        image:url(:/qss/flatblack/checkbox_parcial_disable.png);
        }
        
        QTimeEdit::up-button,QDateEdit::up-button,QDateTimeEdit::up-button,QDoubleSpinBox::up-button,QSpinBox::up-button{
        image:url(:/qss/flatblack/add_top.png);
        width:10px;
        height:10px;
        padding:2px 5px 0px 0px;
        }
        
        QTimeEdit::down-button,QDateEdit::down-button,QDateTimeEdit::down-button,QDoubleSpinBox::down-button,QSpinBox::down-button{
        image:url(:/qss/flatblack/add_bottom.png);
        width:10px;
        height:10px;
        padding:0px 5px 2px 0px;
        }
        
        QTimeEdit::up-button:pressed,QDateEdit::up-button:pressed,QDateTimeEdit::up-button:pressed,QDoubleSpinBox::up-button:pressed,QSpinBox::up-button:pressed{
        top:-2px;
        }
          
        QTimeEdit::down-button:pressed,QDateEdit::down-button:pressed,QDateTimeEdit::down-button:pressed,QDoubleSpinBox::down-button:pressed,QSpinBox::down-button:pressed,QSpinBox::down-button:pressed{
        bottom:-2px;
        }
        
        QComboBox::down-arrow,QDateEdit[calendarPopup="true"]::down-arrow,QTimeEdit[calendarPopup="true"]::down-arrow,QDateTimeEdit[calendarPopup="true"]::down-arrow{
        image:url(:/qss/flatblack/add_bottom.png);
        width:10px;
        height:10px;
        right:2px;
        }
        
        QComboBox::drop-down,QDateEdit::drop-down,QTimeEdit::drop-down,QDateTimeEdit::drop-down{
        subcontrol-origin:padding;
        subcontrol-position:top right;
        width:15px;
        border-left-width:0px;
        border-left-style:solid;
        border-top-right-radius:3px;
        border-bottom-right-radius:3px;
        border-left-color:#67696B;
        }
        
        QComboBox::drop-down:on{
        top:1px;
        }
        
        QMenuBar::item{
        color:#BEC0C2;
        background-color:#404244;
        margin:0px;
        padding:3px 10px;
        }
        
        QMenu,QMenuBar,QMenu:disabled,QMenuBar:disabled{
        color:#BEC0C2;
        background-color:#404244;
        border:1px solid #67696B;
        margin:0px;
        }
        
        QMenu::item{
        padding:3px 20px;
        }
        
        QMenu::indicator{
        width:13px;
        height:13px;
        }
        
        QMenu::item:selected,QMenuBar::item:selected{
        color:#BEC0C2;
        border:0px solid #67696B;
        background:#262829;
        }
        
        QMenu::separator{
        height:1px;
        background:#67696B;
        }
        
        QProgressBar{
        min-height:10px;
        background:#404244;
        border-radius:5px;
        text-align:center;
        border:1px solid #404244;
        }
        
        QProgressBar:chunk{
        border-radius:5px;
        background-color:#67696B;
        }
        
        QSlider::groove:horizontal{
        background:#404244;
        height:8px;
        border-radius:4px;
        }
        
        QSlider::add-page:horizontal{
        background:#404244;
        height:8px;
        border-radius:4px;
        }
        
        QSlider::sub-page:horizontal{
        background:#67696B;
        height:8px;
        border-radius:4px;
        }
        
        QSlider::handle:horizontal{
        width:13px;
        margin-top:-3px;
        margin-bottom:-3px;
        border-radius:6px;
        background:qradialgradient(spread:pad,cx:0.5,cy:0.5,radius:0.5,fx:0.5,fy:0.5,stop:0.6 #2E2F30,stop:0.8 #67696B);
        }
        
        QSlider::groove:vertical{
        width:8px;
        border-radius:4px;
        background:#404244;
        }
        
        QSlider::add-page:vertical{
        width:8px;
        border-radius:4px;
        background:#404244;
        }
        
        QSlider::sub-page:vertical{
        width:8px;
        border-radius:4px;
        background:#67696B;
        }
        
        QSlider::handle:vertical{
        height:14px;
        margin-left:-3px;
        margin-right:-3px;
        border-radius:6px;
        background:qradialgradient(spread:pad,cx:0.5,cy:0.5,radius:0.5,fx:0.5,fy:0.5,stop:0.6 #2E2F30,stop:0.8 #67696B);
        }
        
        QScrollBar:horizontal{
        background:#404244;
        padding:0px;
        border-radius:6px;
        max-height:12px;
        }
        
        QScrollBar::handle:horizontal{
        background:#262829;
        min-width:50px;
        border-radius:6px;
        }
        
        QScrollBar::handle:horizontal:hover{
        background:#67696B;
        }
        
        QScrollBar::handle:horizontal:pressed{
        background:#67696B;
        }
        
        QScrollBar::add-page:horizontal{
        background:none;
        }
        
        QScrollBar::sub-page:horizontal{
        background:none;
        }
        
        QScrollBar::add-line:horizontal{
        background:none;
        }
        
        QScrollBar::sub-line:horizontal{
        background:none;
        }
        
        QScrollBar:vertical{
        background:#404244;
        padding:0px;
        border-radius:6px;
        max-width:12px;
        }
        
        QScrollBar::handle:vertical{
        background:#262829;
        min-height:50px;
        border-radius:6px;
        }
        
        QScrollBar::handle:vertical:hover{
        background:#67696B;
        }
        
        QScrollBar::handle:vertical:pressed{
        background:#67696B;
        }
        
        QScrollBar::add-page:vertical{
        background:none;
        }
        
        QScrollBar::sub-page:vertical{
        background:none;
        }
        
        QScrollBar::add-line:vertical{
        background:none;
        }
        
        QScrollBar::sub-line:vertical{
        background:none;
        }
        
        QScrollArea{
        border:0px;
        }
        
        QTreeView,QListView,QTableView,QTableWidget,QTabWidget::pane{
        border:1px solid #67696B;
        selection-background-color:#262829;
        selection-color:#BEC0C2;
        alternate-background-color:#262829;
        gridline-color:#67696B;
        }
        
        QTreeView::branch:closed:has-children{
        margin:4px;
        border-image:url(:/qss/flatblack/branch_open.png);
        }
        
        QTreeView::branch:open:has-children{
        margin:4px;
        border-image:url(:/qss/flatblack/branch_close.png);
        }
        
        QTreeView,QListView,QTableView,QTableWidget,QSplitter::handle,QTreeView::branch{
        background:#2E2F30;
        }
        
        QTableView,QTableWidget::item:selected,QListView::item:selected,QTreeView::item:selected{
        color:#BEC0C2;
        background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #404244,stop:1 #404244);
        }
        
        QTableView,QTableWidget::item:hover,QListView::item:hover,QTreeView::item:hover{
        color:#BEC0C2;
        background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #262829,stop:1 #262829);
        }
        
        QTableView,QTableWidget::item,QListView::item,QTreeView::item{
        padding:1px;
        margin:0px;
        }
        
        QHeaderView::section,QTableCornerButton:section{
        padding:3px;
        margin:0px;
        color:#BEC0C2;
        border:1px solid #67696B;
        border-left-width:0px;
        border-right-width:1px;
        border-top-width:0px;
        border-bottom-width:1px;
        background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #262829,stop:1 #262829);
        }
        
        QTabBar::tab{
        border:1px solid #67696B;
        color:#BEC0C2;
        margin:0px;
        background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #262829,stop:1 #262829);
        }
        
        QTabBar::tab:selected,QTabBar::tab:hover{
        border-style:solid;
        border-color:#00BB9E;
        background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #404244,stop:1 #404244);
        }
        
        QTabBar::tab:top,QTabBar::tab:bottom{
        padding:3px 8px 3px 8px;
        }
        
        QTabBar::tab:left,QTabBar::tab:right{
        padding:8px 3px 8px 3px;
        }
        
        QTabBar::tab:top:selected,QTabBar::tab:top:hover{
        border-width:2px 0px 0px 0px;
        }
        
        QTabBar::tab:right:selected,QTabBar::tab:right:hover{
        border-width:0px 0px 0px 2px;
        }
        
        QTabBar::tab:bottom:selected,QTabBar::tab:bottom:hover{
        border-width:0px 0px 2px 0px;
        }
        
        QTabBar::tab:left:selected,QTabBar::tab:left:hover{
        border-width:0px 2px 0px 0px;
        }
        
        QTabBar::tab:first:top:selected,QTabBar::tab:first:top:hover,QTabBar::tab:first:bottom:selected,QTabBar::tab:first:bottom:hover{
        border-left-width:1px;
        border-left-color:#67696B;
        }
        
        QTabBar::tab:first:left:selected,QTabBar::tab:first:left:hover,QTabBar::tab:first:right:selected,QTabBar::tab:first:right:hover{
        border-top-width:1px;
        border-top-color:#67696B;
        }
        
        QTabBar::tab:last:top:selected,QTabBar::tab:last:top:hover,QTabBar::tab:last:bottom:selected,QTabBar::tab:last:bottom:hover{
        border-right-width:1px;
        border-right-color:#67696B;
        }
        
        QTabBar::tab:last:left:selected,QTabBar::tab:last:left:hover,QTabBar::tab:last:right:selected,QTabBar::tab:last:right:hover{
        border-bottom-width:1px;
        border-bottom-color:#67696B;
        }
        
        QStatusBar::item{
        border:0px solid #404244;
        border-radius:3px;
        }
        
        QToolBox::tab,QGroupBox#gboxDevicePanel,QGroupBox#gboxDeviceTitle,QFrame#gboxDevicePanel,QFrame#gboxDeviceTitle{
        padding:3px;
        border-radius:5px;
        color:#BEC0C2;
        background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #404244,stop:1 #404244);
        }
        
        QToolTip{
        border:0px solid #BEC0C2;
        padding:1px;
        color:#BEC0C2;
        background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #404244,stop:1 #404244);
        }
        
        QToolBox::tab:selected{
        background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #262829,stop:1 #262829);
        }
        
        QPrintPreviewDialog QToolButton{
        border:0px solid #BEC0C2;
        border-radius:0px;
        margin:0px;
        padding:3px;
        background:none;
        }
        
        QColorDialog QPushButton,QFileDialog QPushButton{
        min-width:80px;
        }
        
        QToolButton#qt_calendar_prevmonth{
        icon-size:0px;
        min-width:20px;
        image:url(:/qss/flatblack/calendar_prevmonth.png);
        }
        
        QToolButton#qt_calendar_nextmonth{
        icon-size:0px;
        min-width:20px;
        image:url(:/qss/flatblack/calendar_nextmonth.png);
        }
        
        QToolButton#qt_calendar_prevmonth,QToolButton#qt_calendar_nextmonth,QToolButton#qt_calendar_monthbutton,QToolButton#qt_calendar_yearbutton{
        border:0px solid #BEC0C2;
        border-radius:3px;
        margin:3px 3px 3px 3px;
        padding:3px;
        background:none;
        }
        
        QToolButton#qt_calendar_prevmonth:hover,QToolButton#qt_calendar_nextmonth:hover,QToolButton#qt_calendar_monthbutton:hover,QToolButton#qt_calendar_yearbutton:hover,QToolButton#qt_calendar_prevmonth:pressed,QToolButton#qt_calendar_nextmonth:pressed,QToolButton#qt_calendar_monthbutton:pressed,QToolButton#qt_calendar_yearbutton:pressed{
        border:1px solid #67696B;
        }
        
        QCalendarWidget QSpinBox#qt_calendar_yearedit{
        margin:2px;
        }
        
        QCalendarWidget QToolButton::menu-indicator{
        image:None;
        }
        
        QCalendarWidget QTableView,QTableWidget{
        border-width:0px;
        }
        
        QCalendarWidget QWidget#qt_calendar_navigationbar{
        border:1px solid #67696B;
        border-width:1px 1px 0px 1px;
        background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #404244,stop:1 #404244);
        }
        
        QComboBox QAbstractItemView::item{
        min-height:20px;
        min-width:10px;
        }
        
        QTableView,QTableWidget[model="true"]::item{
        padding:0px;
        margin:0px;
        }
        
        QTableView,QTableWidget QLineEdit,QTableView,QTableWidget QComboBox,QTableView,QTableWidget QSpinBox,QTableView,QTableWidget QDoubleSpinBox,QTableView,QTableWidget QDateEdit,QTableView,QTableWidget QTimeEdit,QTableView,QTableWidget QDateTimeEdit{
        border-width:0px;
        border-radius:0px;
        }
        
        QTableView,QTableWidget QLineEdit:focus,QTableView,QTableWidget QComboBox:focus,QTableView,QTableWidget QSpinBox:focus,QTableView,QTableWidget QDoubleSpinBox:focus,QTableView,QTableWidget QDateEdit:focus,QTableView,QTableWidget QTimeEdit:focus,QTableView,QTableWidget QDateTimeEdit:focus{
        border-width:0px;
        border-radius:0px;
        }
        
        QLineEdit,QTextEdit,QPlainTextEdit,QSpinBox,QDoubleSpinBox,QComboBox,QDateEdit,QTimeEdit,QDateTimeEdit{
        background:#2E2F30;
        }
        
        *:disabled{
        background:#2E2F30;
        border-color:#404244;
        }
        
        /*TextColor:#BEC0C2*/
        /*PanelColor:#2E2F30*/
        /*BorderColor:#67696B*/
        /*NormalColorStart:#404244*/
        /*NormalColorEnd:#404244*/
        /*DarkColorStart:#262829*/
        /*DarkColorEnd:#262829*/
        /*HighColor:#00BB9E*/
                '''
        return qss


class DarkBlue(object):
    @classmethod
    def get_qss(cls):
        qss = '''
        QPalette{background:#0E1A32;}*{outline:0px;color:#7AAFE3;}
        
        QWidget[form="true"],QLabel[frameShape="1"]{
        border:1px solid #132743;
        border-radius:0px;
        }
        
        QWidget[form="bottom"]{
        background:#133050;
        }
        
        QWidget[form="bottom"] .QFrame{
        border:1px solid #7AAFE3;
        }
        
        QWidget[form="bottom"] QLabel,QWidget[form="title"] QLabel{
        border-radius:0px;
        color:#7AAFE3;
        background:none;
        border-style:none;
        }
        
        QWidget[form="title"],QWidget[nav="left"],QWidget[nav="top"] QAbstractButton{
        border-style:none;
        border-radius:0px;
        padding:5px;
        color:#7AAFE3;
        background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #133050,stop:1 #133050);
        }
        
        QWidget[nav="top"] QAbstractButton:hover,QWidget[nav="top"] QAbstractButton:pressed,QWidget[nav="top"] QAbstractButton:checked{
        border-style:solid;
        border-width:0px 0px 2px 0px;
        padding:4px 4px 2px 4px;
        border-color:#00BB9E;
        background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #033967,stop:1 #033967);
        }
        
        QWidget[nav="left"] QAbstractButton{
        border-radius:0px;
        color:#7AAFE3;
        background:none;
        border-style:none;
        }
        
        QWidget[nav="left"] QAbstractButton:hover{
        color:#FFFFFF;
        background-color:#00BB9E;
        }
        
        QWidget[nav="left"] QAbstractButton:checked,QWidget[nav="left"] QAbstractButton:pressed{
        color:#7AAFE3;
        border-style:solid;
        border-width:0px 0px 0px 2px;
        padding:4px 4px 4px 2px;
        border-color:#00BB9E;
        background-color:#0E1A32;
        }
        
        QWidget[video="true"] QLabel{
        color:#7AAFE3;
        border:1px solid #132743;
        background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #133050,stop:1 #133050);
        }
        
        QWidget[video="true"] QLabel:focus{
        border:1px solid #00BB9E;
        background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #033967,stop:1 #033967);
        }
        
        QLineEdit,QTextEdit,QPlainTextEdit,QSpinBox,QDoubleSpinBox,QComboBox,QDateEdit,QTimeEdit,QDateTimeEdit{
        border:1px solid #132743;
        border-radius:3px;
        padding:2px;
        background:none;
        selection-background-color:#133050;
        selection-color:#7AAFE3;
        }
        
        QLineEdit:focus,QTextEdit:focus,QPlainTextEdit:focus,QSpinBox:focus,QDoubleSpinBox:focus,QComboBox:focus,QDateEdit:focus,QTimeEdit:focus,QDateTimeEdit:focus,QLineEdit:hover,QTextEdit:hover,QPlainTextEdit:hover,QSpinBox:hover,QDoubleSpinBox:hover,QComboBox:hover,QDateEdit:hover,QTimeEdit:hover,QDateTimeEdit:hover{
        border:1px solid #132743;
        }
        
        QLineEdit[echoMode="2"]{
        lineedit-password-character:9679;
        }
        
        .QFrame{
        border:1px solid #132743;
        border-radius:3px;
        }
        
        .QGroupBox{
        border:1px solid #132743;
        border-radius:5px;
        margin-top:3ex;
        }
        
        .QGroupBox::title{
        subcontrol-origin:margin;
        position:relative;
        left:10px;
        }
        
        .QPushButton,.QToolButton{
        border-style:none;
        border:1px solid #132743;
        color:#7AAFE3;
        padding:5px;
        min-height:15px;
        border-radius:5px;
        background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #133050,stop:1 #133050);
        }
        
        .QPushButton:hover,.QToolButton:hover{
        background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #033967,stop:1 #033967);
        }
        
        .QPushButton:pressed,.QToolButton:pressed{
        background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #133050,stop:1 #133050);
        }
        
        .QToolButton::menu-indicator{
        image:None;
        }
        
        QToolButton#btnMenu,QPushButton#btnMenu_Min,QPushButton#btnMenu_Max,QPushButton#btnMenu_Close{
        border-radius:3px;
        color:#7AAFE3;
        padding:3px;
        margin:0px;
        background:none;
        border-style:none;
        }
        
        QToolButton#btnMenu:hover,QPushButton#btnMenu_Min:hover,QPushButton#btnMenu_Max:hover{
        color:#FFFFFF;
        margin:1px 1px 2px 1px;
        background-color:rgba(51,127,209,230);
        }
        
        QPushButton#btnMenu_Close:hover{
        color:#FFFFFF;
        margin:1px 1px 2px 1px;
        background-color:rgba(238,0,0,128);
        }
        
        QRadioButton::indicator{
        width:15px;
        height:15px;
        }
        
        QRadioButton::indicator::unchecked{
        image:url(:/qss/darkblue/radiobutton_unchecked.png);
        }
        
        QRadioButton::indicator::unchecked:disabled{
        image:url(:/qss/darkblue/radiobutton_unchecked_disable.png);
        }
        
        QRadioButton::indicator::checked{
        image:url(:/qss/darkblue/radiobutton_checked.png);
        }
        
        QRadioButton::indicator::checked:disabled{
        image:url(:/qss/darkblue/radiobutton_checked_disable.png);
        }
        
        QGroupBox::indicator,QTreeWidget::indicator,QListWidget::indicator{
        padding:0px -3px 0px 3px;
        }
        
        QCheckBox::indicator,QGroupBox::indicator,QTreeWidget::indicator,QListWidget::indicator{
        width:13px;
        height:13px;
        }
        
        QCheckBox::indicator:unchecked,QGroupBox::indicator:unchecked,QTreeWidget::indicator:unchecked,QListWidget::indicator:unchecked{
        image:url(:/qss/darkblue/checkbox_unchecked.png);
        }
        
        QCheckBox::indicator:unchecked:disabled,QGroupBox::indicator:unchecked:disabled,QTreeWidget::indicator:unchecked:disabled,QListWidget::indicator:disabled{
        image:url(:/qss/darkblue/checkbox_unchecked_disable.png);
        }
        
        QCheckBox::indicator:checked,QGroupBox::indicator:checked,QTreeWidget::indicator:checked,QListWidget::indicator:checked{
        image:url(:/qss/darkblue/checkbox_checked.png);
        }
        
        QCheckBox::indicator:checked:disabled,QGroupBox::indicator:checked:disabled,QTreeWidget::indicator:checked:disabled,QListWidget::indicator:checked:disabled{
        image:url(:/qss/darkblue/checkbox_checked_disable.png);
        }
        
        QCheckBox::indicator:indeterminate,QGroupBox::indicator:indeterminate,QTreeWidget::indicator:indeterminate,QListWidget::indicator:indeterminate{
        image:url(:/qss/darkblue/checkbox_parcial.png);
        }
        
        QCheckBox::indicator:indeterminate:disabled,QGroupBox::indicator:indeterminate:disabled,QTreeWidget::indicator:indeterminate:disabled,QListWidget::indicator:indeterminate:disabled{
        image:url(:/qss/darkblue/checkbox_parcial_disable.png);
        }
        
        QTimeEdit::up-button,QDateEdit::up-button,QDateTimeEdit::up-button,QDoubleSpinBox::up-button,QSpinBox::up-button{
        image:url(:/qss/darkblue/add_top.png);
        width:10px;
        height:10px;
        padding:2px 5px 0px 0px;
        }
        
        QTimeEdit::down-button,QDateEdit::down-button,QDateTimeEdit::down-button,QDoubleSpinBox::down-button,QSpinBox::down-button{
        image:url(:/qss/darkblue/add_bottom.png);
        width:10px;
        height:10px;
        padding:0px 5px 2px 0px;
        }
        
        QTimeEdit::up-button:pressed,QDateEdit::up-button:pressed,QDateTimeEdit::up-button:pressed,QDoubleSpinBox::up-button:pressed,QSpinBox::up-button:pressed{
        top:-2px;
        }
          
        QTimeEdit::down-button:pressed,QDateEdit::down-button:pressed,QDateTimeEdit::down-button:pressed,QDoubleSpinBox::down-button:pressed,QSpinBox::down-button:pressed,QSpinBox::down-button:pressed{
        bottom:-2px;
        }
        
        QComboBox::down-arrow,QDateEdit[calendarPopup="true"]::down-arrow,QTimeEdit[calendarPopup="true"]::down-arrow,QDateTimeEdit[calendarPopup="true"]::down-arrow{
        image:url(:/qss/darkblue/add_bottom.png);
        width:10px;
        height:10px;
        right:2px;
        }
        
        QComboBox::drop-down,QDateEdit::drop-down,QTimeEdit::drop-down,QDateTimeEdit::drop-down{
        subcontrol-origin:padding;
        subcontrol-position:top right;
        width:15px;
        border-left-width:0px;
        border-left-style:solid;
        border-top-right-radius:3px;
        border-bottom-right-radius:3px;
        border-left-color:#132743;
        }
        
        QComboBox::drop-down:on{
        top:1px;
        }
        
        QMenuBar::item{
        color:#7AAFE3;
        background-color:#133050;
        margin:0px;
        padding:3px 10px;
        }
        
        QMenu,QMenuBar,QMenu:disabled,QMenuBar:disabled{
        color:#7AAFE3;
        background-color:#133050;
        border:1px solid #132743;
        margin:0px;
        }
        
        QMenu::item{
        padding:3px 20px;
        }
        
        QMenu::indicator{
        width:13px;
        height:13px;
        }
        
        QMenu::item:selected,QMenuBar::item:selected{
        color:#7AAFE3;
        border:0px solid #132743;
        background:#033967;
        }
        
        QMenu::separator{
        height:1px;
        background:#132743;
        }
        
        QProgressBar{
        min-height:10px;
        background:#133050;
        border-radius:5px;
        text-align:center;
        border:1px solid #133050;
        }
        
        QProgressBar:chunk{
        border-radius:5px;
        background-color:#132743;
        }
        
        QSlider::groove:horizontal{
        background:#133050;
        height:8px;
        border-radius:4px;
        }
        
        QSlider::add-page:horizontal{
        background:#133050;
        height:8px;
        border-radius:4px;
        }
        
        QSlider::sub-page:horizontal{
        background:#132743;
        height:8px;
        border-radius:4px;
        }
        
        QSlider::handle:horizontal{
        width:13px;
        margin-top:-3px;
        margin-bottom:-3px;
        border-radius:6px;
        background:qradialgradient(spread:pad,cx:0.5,cy:0.5,radius:0.5,fx:0.5,fy:0.5,stop:0.6 #0E1A32,stop:0.8 #132743);
        }
        
        QSlider::groove:vertical{
        width:8px;
        border-radius:4px;
        background:#133050;
        }
        
        QSlider::add-page:vertical{
        width:8px;
        border-radius:4px;
        background:#133050;
        }
        
        QSlider::sub-page:vertical{
        width:8px;
        border-radius:4px;
        background:#132743;
        }
        
        QSlider::handle:vertical{
        height:14px;
        margin-left:-3px;
        margin-right:-3px;
        border-radius:6px;
        background:qradialgradient(spread:pad,cx:0.5,cy:0.5,radius:0.5,fx:0.5,fy:0.5,stop:0.6 #0E1A32,stop:0.8 #132743);
        }
        
        QScrollBar:horizontal{
        background:#133050;
        padding:0px;
        border-radius:6px;
        max-height:12px;
        }
        
        QScrollBar::handle:horizontal{
        background:#033967;
        min-width:50px;
        border-radius:6px;
        }
        
        QScrollBar::handle:horizontal:hover{
        background:#132743;
        }
        
        QScrollBar::handle:horizontal:pressed{
        background:#132743;
        }
        
        QScrollBar::add-page:horizontal{
        background:none;
        }
        
        QScrollBar::sub-page:horizontal{
        background:none;
        }
        
        QScrollBar::add-line:horizontal{
        background:none;
        }
        
        QScrollBar::sub-line:horizontal{
        background:none;
        }
        
        QScrollBar:vertical{
        background:#133050;
        padding:0px;
        border-radius:6px;
        max-width:12px;
        }
        
        QScrollBar::handle:vertical{
        background:#033967;
        min-height:50px;
        border-radius:6px;
        }
        
        QScrollBar::handle:vertical:hover{
        background:#132743;
        }
        
        QScrollBar::handle:vertical:pressed{
        background:#132743;
        }
        
        QScrollBar::add-page:vertical{
        background:none;
        }
        
        QScrollBar::sub-page:vertical{
        background:none;
        }
        
        QScrollBar::add-line:vertical{
        background:none;
        }
        
        QScrollBar::sub-line:vertical{
        background:none;
        }
        
        QScrollArea{
        border:0px;
        }
        
        QTreeView,QListView,QTableView,QTableWidget,QTabWidget::pane{
        border:1px solid #132743;
        selection-background-color:#033967;
        selection-color:#7AAFE3;
        alternate-background-color:#033967;
        gridline-color:#132743;
        }
        
        QTreeView::branch:closed:has-children{
        margin:4px;
        border-image:url(:/qss/darkblue/branch_open.png);
        }
        
        QTreeView::branch:open:has-children{
        margin:4px;
        border-image:url(:/qss/darkblue/branch_close.png);
        }
        
        QTreeView,QListView,QTableView,QTableWidget,QSplitter::handle,QTreeView::branch{
        background:#0E1A32;
        }
        
        QTableView,QTableWidget::item:selected,QListView::item:selected,QTreeView::item:selected{
        color:#7AAFE3;
        background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #133050,stop:1 #133050);
        }
        
        QTableView,QTableWidget::item:hover,QListView::item:hover,QTreeView::item:hover{
        color:#7AAFE3;
        background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #033967,stop:1 #033967);
        }
        
        QTableView,QTableWidget::item,QListView::item,QTreeView::item{
        padding:1px;
        margin:0px;
        }
        
        QHeaderView::section,QTableCornerButton:section{
        padding:3px;
        margin:0px;
        color:#7AAFE3;
        border:1px solid #132743;
        border-left-width:0px;
        border-right-width:1px;
        border-top-width:0px;
        border-bottom-width:1px;
        background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #033967,stop:1 #033967);
        }
        
        QTabBar::tab{
        border:1px solid #132743;
        color:#7AAFE3;
        margin:0px;
        background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #033967,stop:1 #033967);
        }
        
        QTabBar::tab:selected,QTabBar::tab:hover{
        border-style:solid;
        border-color:#00BB9E;
        background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #133050,stop:1 #133050);
        }
        
        QTabBar::tab:top,QTabBar::tab:bottom{
        padding:3px 8px 3px 8px;
        }
        
        QTabBar::tab:left,QTabBar::tab:right{
        padding:8px 3px 8px 3px;
        }
        
        QTabBar::tab:top:selected,QTabBar::tab:top:hover{
        border-width:2px 0px 0px 0px;
        }
        
        QTabBar::tab:right:selected,QTabBar::tab:right:hover{
        border-width:0px 0px 0px 2px;
        }
        
        QTabBar::tab:bottom:selected,QTabBar::tab:bottom:hover{
        border-width:0px 0px 2px 0px;
        }
        
        QTabBar::tab:left:selected,QTabBar::tab:left:hover{
        border-width:0px 2px 0px 0px;
        }
        
        QTabBar::tab:first:top:selected,QTabBar::tab:first:top:hover,QTabBar::tab:first:bottom:selected,QTabBar::tab:first:bottom:hover{
        border-left-width:1px;
        border-left-color:#132743;
        }
        
        QTabBar::tab:first:left:selected,QTabBar::tab:first:left:hover,QTabBar::tab:first:right:selected,QTabBar::tab:first:right:hover{
        border-top-width:1px;
        border-top-color:#132743;
        }
        
        QTabBar::tab:last:top:selected,QTabBar::tab:last:top:hover,QTabBar::tab:last:bottom:selected,QTabBar::tab:last:bottom:hover{
        border-right-width:1px;
        border-right-color:#132743;
        }
        
        QTabBar::tab:last:left:selected,QTabBar::tab:last:left:hover,QTabBar::tab:last:right:selected,QTabBar::tab:last:right:hover{
        border-bottom-width:1px;
        border-bottom-color:#132743;
        }
        
        QStatusBar::item{
        border:0px solid #133050;
        border-radius:3px;
        }
        
        QToolBox::tab,QGroupBox#gboxDevicePanel,QGroupBox#gboxDeviceTitle,QFrame#gboxDevicePanel,QFrame#gboxDeviceTitle{
        padding:3px;
        border-radius:5px;
        color:#7AAFE3;
        background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #133050,stop:1 #133050);
        }
        
        QToolTip{
        border:0px solid #7AAFE3;
        padding:1px;
        color:#7AAFE3;
        background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #133050,stop:1 #133050);
        }
        
        QToolBox::tab:selected{
        background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #033967,stop:1 #033967);
        }
        
        QPrintPreviewDialog QToolButton{
        border:0px solid #7AAFE3;
        border-radius:0px;
        margin:0px;
        padding:3px;
        background:none;
        }
        
        QColorDialog QPushButton,QFileDialog QPushButton{
        min-width:80px;
        }
        
        QToolButton#qt_calendar_prevmonth{
        icon-size:0px;
        min-width:20px;
        image:url(:/qss/darkblue/calendar_prevmonth.png);
        }
        
        QToolButton#qt_calendar_nextmonth{
        icon-size:0px;
        min-width:20px;
        image:url(:/qss/darkblue/calendar_nextmonth.png);
        }
        
        QToolButton#qt_calendar_prevmonth,QToolButton#qt_calendar_nextmonth,QToolButton#qt_calendar_monthbutton,QToolButton#qt_calendar_yearbutton{
        border:0px solid #7AAFE3;
        border-radius:3px;
        margin:3px 3px 3px 3px;
        padding:3px;
        background:none;
        }
        
        QToolButton#qt_calendar_prevmonth:hover,QToolButton#qt_calendar_nextmonth:hover,QToolButton#qt_calendar_monthbutton:hover,QToolButton#qt_calendar_yearbutton:hover,QToolButton#qt_calendar_prevmonth:pressed,QToolButton#qt_calendar_nextmonth:pressed,QToolButton#qt_calendar_monthbutton:pressed,QToolButton#qt_calendar_yearbutton:pressed{
        border:1px solid #132743;
        }
        
        QCalendarWidget QSpinBox#qt_calendar_yearedit{
        margin:2px;
        }
        
        QCalendarWidget QToolButton::menu-indicator{
        image:None;
        }
        
        QCalendarWidget QTableView,QTableWidget{
        border-width:0px;
        }
        
        QCalendarWidget QWidget#qt_calendar_navigationbar{
        border:1px solid #132743;
        border-width:1px 1px 0px 1px;
        background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #133050,stop:1 #133050);
        }
        
        QComboBox QAbstractItemView::item{
        min-height:20px;
        min-width:10px;
        }
        
        QTableView,QTableWidget[model="true"]::item{
        padding:0px;
        margin:0px;
        }
        
        QTableView,QTableWidget QLineEdit,QTableView,QTableWidget QComboBox,QTableView,QTableWidget QSpinBox,QTableView,QTableWidget QDoubleSpinBox,QTableView,QTableWidget QDateEdit,QTableView,QTableWidget QTimeEdit,QTableView,QTableWidget QDateTimeEdit{
        border-width:0px;
        border-radius:0px;
        }
        
        QTableView,QTableWidget QLineEdit:focus,QTableView,QTableWidget QComboBox:focus,QTableView,QTableWidget QSpinBox:focus,QTableView,QTableWidget QDoubleSpinBox:focus,QTableView,QTableWidget QDateEdit:focus,QTableView,QTableWidget QTimeEdit:focus,QTableView,QTableWidget QDateTimeEdit:focus{
        border-width:0px;
        border-radius:0px;
        }
        
        QLineEdit,QTextEdit,QPlainTextEdit,QSpinBox,QDoubleSpinBox,QComboBox,QDateEdit,QTimeEdit,QDateTimeEdit{
        background:#0E1A32;
        }
        
        *:disabled{
        background:#0E1A32;
        border-color:#133050;
        }
        
        /*TextColor:#7AAFE3*/
        /*PanelColor:#0E1A32*/
        /*BorderColor:#132743*/
        /*NormalColorStart:#133050*/
        /*NormalColorEnd:#133050*/
        /*DarkColorStart:#033967*/
        /*DarkColorEnd:#033967*/
        /*HighColor:#00BB9E*/
                '''
        return qss


class Blue(object):
    @classmethod
    def get_qss(cls):
        qss = '''
        QPalette{background:#CFDDEE;}*{outline:0px;color:#324C6C;}

        QWidget[form="true"],QLabel[frameShape="1"]{
        border:1px solid #7F9AB8;
        border-radius:0px;
        }
        
        QWidget[form="bottom"]{
        background:#C0D3EB;
        }
        
        QWidget[form="bottom"] .QFrame{
        border:1px solid #324C6C;
        }
        
        QWidget[form="bottom"] QLabel,QWidget[form="title"] QLabel{
        border-radius:0px;
        color:#324C6C;
        background:none;
        border-style:none;
        }
        
        QWidget[form="title"],QWidget[nav="left"],QWidget[nav="top"] QAbstractButton{
        border-style:none;
        border-radius:0px;
        padding:5px;
        color:#324C6C;
        background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #C0D3EB,stop:1 #BCCFE7);
        }
        
        QWidget[nav="top"] QAbstractButton:hover,QWidget[nav="top"] QAbstractButton:pressed,QWidget[nav="top"] QAbstractButton:checked{
        border-style:solid;
        border-width:0px 0px 2px 0px;
        padding:4px 4px 2px 4px;
        border-color:#00BB9E;
        background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #D2E3F5,stop:1 #CADDF3);
        }
        
        QWidget[nav="left"] QAbstractButton{
        border-radius:0px;
        color:#324C6C;
        background:none;
        border-style:none;
        }
        
        QWidget[nav="left"] QAbstractButton:hover{
        color:#FFFFFF;
        background-color:#00BB9E;
        }
        
        QWidget[nav="left"] QAbstractButton:checked,QWidget[nav="left"] QAbstractButton:pressed{
        color:#324C6C;
        border-style:solid;
        border-width:0px 0px 0px 2px;
        padding:4px 4px 4px 2px;
        border-color:#00BB9E;
        background-color:#CFDDEE;
        }
        
        QWidget[video="true"] QLabel{
        color:#324C6C;
        border:1px solid #7F9AB8;
        background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #C0D3EB,stop:1 #BCCFE7);
        }
        
        QWidget[video="true"] QLabel:focus{
        border:1px solid #00BB9E;
        background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #D2E3F5,stop:1 #CADDF3);
        }
        
        QLineEdit,QTextEdit,QPlainTextEdit,QSpinBox,QDoubleSpinBox,QComboBox,QDateEdit,QTimeEdit,QDateTimeEdit{
        border:1px solid #7F9AB8;
        border-radius:3px;
        padding:2px;
        background:none;
        selection-background-color:#C0D3EB;
        selection-color:#324C6C;
        }
        
        QLineEdit:focus,QTextEdit:focus,QPlainTextEdit:focus,QSpinBox:focus,QDoubleSpinBox:focus,QComboBox:focus,QDateEdit:focus,QTimeEdit:focus,QDateTimeEdit:focus,QLineEdit:hover,QTextEdit:hover,QPlainTextEdit:hover,QSpinBox:hover,QDoubleSpinBox:hover,QComboBox:hover,QDateEdit:hover,QTimeEdit:hover,QDateTimeEdit:hover{
        border:1px solid #7F9AB8;
        }
        
        QLineEdit[echoMode="2"]{
        lineedit-password-character:9679;
        }
        
        .QFrame{
        border:1px solid #7F9AB8;
        border-radius:3px;
        }
        
        .QGroupBox{
        border:1px solid #7F9AB8;
        border-radius:5px;
        margin-top:3ex;
        }
        
        .QGroupBox::title{
        subcontrol-origin:margin;
        position:relative;
        left:10px;
        }
        
        .QPushButton,.QToolButton{
        border-style:none;
        border:1px solid #7F9AB8;
        color:#324C6C;
        padding:5px;
        min-height:15px;
        border-radius:5px;
        background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #C0D3EB,stop:1 #BCCFE7);
        }
        
        .QPushButton:hover,.QToolButton:hover{
        background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #D2E3F5,stop:1 #CADDF3);
        }
        
        .QPushButton:pressed,.QToolButton:pressed{
        background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #C0D3EB,stop:1 #BCCFE7);
        }
        
        .QToolButton::menu-indicator{
        image:None;
        }
        
        QToolButton#btnMenu,QPushButton#btnMenu_Min,QPushButton#btnMenu_Max,QPushButton#btnMenu_Close{
        border-radius:3px;
        color:#324C6C;
        padding:3px;
        margin:0px;
        background:none;
        border-style:none;
        }
        
        QToolButton#btnMenu:hover,QPushButton#btnMenu_Min:hover,QPushButton#btnMenu_Max:hover{
        color:#FFFFFF;
        margin:1px 1px 2px 1px;
        background-color:rgba(51,127,209,230);
        }
        
        QPushButton#btnMenu_Close:hover{
        color:#FFFFFF;
        margin:1px 1px 2px 1px;
        background-color:rgba(238,0,0,128);
        }
        
        QRadioButton::indicator{
        width:15px;
        height:15px;
        }
        
        QRadioButton::indicator::unchecked{
        image:url(:/qss/blue/radiobutton_unchecked.png);
        }
        
        QRadioButton::indicator::unchecked:disabled{
        image:url(:/qss/blue/radiobutton_unchecked_disable.png);
        }
        
        QRadioButton::indicator::checked{
        image:url(:/qss/blue/radiobutton_checked.png);
        }
        
        QRadioButton::indicator::checked:disabled{
        image:url(:/qss/blue/radiobutton_checked_disable.png);
        }
        
        QGroupBox::indicator,QTreeWidget::indicator,QListWidget::indicator{
        padding:0px -3px 0px 3px;
        }
        
        QCheckBox::indicator,QGroupBox::indicator,QTreeWidget::indicator,QListWidget::indicator{
        width:13px;
        height:13px;
        }
        
        QCheckBox::indicator:unchecked,QGroupBox::indicator:unchecked,QTreeWidget::indicator:unchecked,QListWidget::indicator:unchecked{
        image:url(:/qss/blue/checkbox_unchecked.png);
        }
        
        QCheckBox::indicator:unchecked:disabled,QGroupBox::indicator:unchecked:disabled,QTreeWidget::indicator:unchecked:disabled,QListWidget::indicator:disabled{
        image:url(:/qss/blue/checkbox_unchecked_disable.png);
        }
        
        QCheckBox::indicator:checked,QGroupBox::indicator:checked,QTreeWidget::indicator:checked,QListWidget::indicator:checked{
        image:url(:/qss/blue/checkbox_checked.png);
        }
        
        QCheckBox::indicator:checked:disabled,QGroupBox::indicator:checked:disabled,QTreeWidget::indicator:checked:disabled,QListWidget::indicator:checked:disabled{
        image:url(:/qss/blue/checkbox_checked_disable.png);
        }
        
        QCheckBox::indicator:indeterminate,QGroupBox::indicator:indeterminate,QTreeWidget::indicator:indeterminate,QListWidget::indicator:indeterminate{
        image:url(:/qss/blue/checkbox_parcial.png);
        }
        
        QCheckBox::indicator:indeterminate:disabled,QGroupBox::indicator:indeterminate:disabled,QTreeWidget::indicator:indeterminate:disabled,QListWidget::indicator:indeterminate:disabled{
        image:url(:/qss/blue/checkbox_parcial_disable.png);
        }
        
        QTimeEdit::up-button,QDateEdit::up-button,QDateTimeEdit::up-button,QDoubleSpinBox::up-button,QSpinBox::up-button{
        image:url(:/qss/blue/add_top.png);
        width:10px;
        height:10px;
        padding:2px 5px 0px 0px;
        }
        
        QTimeEdit::down-button,QDateEdit::down-button,QDateTimeEdit::down-button,QDoubleSpinBox::down-button,QSpinBox::down-button{
        image:url(:/qss/blue/add_bottom.png);
        width:10px;
        height:10px;
        padding:0px 5px 2px 0px;
        }
        
        QTimeEdit::up-button:pressed,QDateEdit::up-button:pressed,QDateTimeEdit::up-button:pressed,QDoubleSpinBox::up-button:pressed,QSpinBox::up-button:pressed{
        top:-2px;
        }
          
        QTimeEdit::down-button:pressed,QDateEdit::down-button:pressed,QDateTimeEdit::down-button:pressed,QDoubleSpinBox::down-button:pressed,QSpinBox::down-button:pressed,QSpinBox::down-button:pressed{
        bottom:-2px;
        }
        
        QComboBox::down-arrow,QDateEdit[calendarPopup="true"]::down-arrow,QTimeEdit[calendarPopup="true"]::down-arrow,QDateTimeEdit[calendarPopup="true"]::down-arrow{
        image:url(:/qss/blue/add_bottom.png);
        width:10px;
        height:10px;
        right:2px;
        }
        
        QComboBox::drop-down,QDateEdit::drop-down,QTimeEdit::drop-down,QDateTimeEdit::drop-down{
        subcontrol-origin:padding;
        subcontrol-position:top right;
        width:15px;
        border-left-width:0px;
        border-left-style:solid;
        border-top-right-radius:3px;
        border-bottom-right-radius:3px;
        border-left-color:#7F9AB8;
        }
        
        QComboBox::drop-down:on{
        top:1px;
        }
        
        QMenuBar::item{
        color:#324C6C;
        background-color:#C0D3EB;
        margin:0px;
        padding:3px 10px;
        }
        
        QMenu,QMenuBar,QMenu:disabled,QMenuBar:disabled{
        color:#324C6C;
        background-color:#C0D3EB;
        border:1px solid #7F9AB8;
        margin:0px;
        }
        
        QMenu::item{
        padding:3px 20px;
        }
        
        QMenu::indicator{
        width:13px;
        height:13px;
        }
        
        QMenu::item:selected,QMenuBar::item:selected{
        color:#324C6C;
        border:0px solid #7F9AB8;
        background:#D2E3F5;
        }
        
        QMenu::separator{
        height:1px;
        background:#7F9AB8;
        }
        
        QProgressBar{
        min-height:10px;
        background:#C0D3EB;
        border-radius:5px;
        text-align:center;
        border:1px solid #C0D3EB;
        }
        
        QProgressBar:chunk{
        border-radius:5px;
        background-color:#7F9AB8;
        }
        
        QSlider::groove:horizontal{
        background:#C0D3EB;
        height:8px;
        border-radius:4px;
        }
        
        QSlider::add-page:horizontal{
        background:#C0D3EB;
        height:8px;
        border-radius:4px;
        }
        
        QSlider::sub-page:horizontal{
        background:#7F9AB8;
        height:8px;
        border-radius:4px;
        }
        
        QSlider::handle:horizontal{
        width:13px;
        margin-top:-3px;
        margin-bottom:-3px;
        border-radius:6px;
        background:qradialgradient(spread:pad,cx:0.5,cy:0.5,radius:0.5,fx:0.5,fy:0.5,stop:0.6 #CFDDEE,stop:0.8 #7F9AB8);
        }
        
        QSlider::groove:vertical{
        width:8px;
        border-radius:4px;
        background:#C0D3EB;
        }
        
        QSlider::add-page:vertical{
        width:8px;
        border-radius:4px;
        background:#C0D3EB;
        }
        
        QSlider::sub-page:vertical{
        width:8px;
        border-radius:4px;
        background:#7F9AB8;
        }
        
        QSlider::handle:vertical{
        height:14px;
        margin-left:-3px;
        margin-right:-3px;
        border-radius:6px;
        background:qradialgradient(spread:pad,cx:0.5,cy:0.5,radius:0.5,fx:0.5,fy:0.5,stop:0.6 #CFDDEE,stop:0.8 #7F9AB8);
        }
        
        QScrollBar:horizontal{
        background:#C0D3EB;
        padding:0px;
        border-radius:6px;
        max-height:12px;
        }
        
        QScrollBar::handle:horizontal{
        background:#CADDF3;
        min-width:50px;
        border-radius:6px;
        }
        
        QScrollBar::handle:horizontal:hover{
        background:#7F9AB8;
        }
        
        QScrollBar::handle:horizontal:pressed{
        background:#7F9AB8;
        }
        
        QScrollBar::add-page:horizontal{
        background:none;
        }
        
        QScrollBar::sub-page:horizontal{
        background:none;
        }
        
        QScrollBar::add-line:horizontal{
        background:none;
        }
        
        QScrollBar::sub-line:horizontal{
        background:none;
        }
        
        QScrollBar:vertical{
        background:#C0D3EB;
        padding:0px;
        border-radius:6px;
        max-width:12px;
        }
        
        QScrollBar::handle:vertical{
        background:#CADDF3;
        min-height:50px;
        border-radius:6px;
        }
        
        QScrollBar::handle:vertical:hover{
        background:#7F9AB8;
        }
        
        QScrollBar::handle:vertical:pressed{
        background:#7F9AB8;
        }
        
        QScrollBar::add-page:vertical{
        background:none;
        }
        
        QScrollBar::sub-page:vertical{
        background:none;
        }
        
        QScrollBar::add-line:vertical{
        background:none;
        }
        
        QScrollBar::sub-line:vertical{
        background:none;
        }
        
        QScrollArea{
        border:0px;
        }
        
        QTreeView,QListView,QTableView,QTableWidget,QTabWidget::pane{
        border:1px solid #7F9AB8;
        selection-background-color:#D2E3F5;
        selection-color:#324C6C;
        alternate-background-color:#CADDF3;
        gridline-color:#7F9AB8;
        }
        
        QTreeView::branch:closed:has-children{
        margin:4px;
        border-image:url(:/qss/blue/branch_open.png);
        }
        
        QTreeView::branch:open:has-children{
        margin:4px;
        border-image:url(:/qss/blue/branch_close.png);
        }
        
        QTreeView,QListView,QTableView,QTableWidget,QSplitter::handle,QTreeView::branch{
        background:#CFDDEE;
        }
        
        QTableView,QTableWidget::item:selected,QListView::item:selected,QTreeView::item:selected{
        color:#324C6C;
        background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #C0D3EB,stop:1 #BCCFE7);
        }
        
        QTableView,QTableWidget::item:hover,QListView::item:hover,QTreeView::item:hover{
        color:#324C6C;
        background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #D2E3F5,stop:1 #CADDF3);
        }
        
        QTableView,QTableWidget::item,QListView::item,QTreeView::item{
        padding:1px;
        margin:0px;
        }
        
        QHeaderView::section,QTableCornerButton:section{
        padding:3px;
        margin:0px;
        color:#324C6C;
        border:1px solid #7F9AB8;
        border-left-width:0px;
        border-right-width:1px;
        border-top-width:0px;
        border-bottom-width:1px;
        background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #D2E3F5,stop:1 #CADDF3);
        }
        
        QTabBar::tab{
        border:1px solid #7F9AB8;
        color:#324C6C;
        margin:0px;
        background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #D2E3F5,stop:1 #CADDF3);
        }
        
        QTabBar::tab:selected,QTabBar::tab:hover{
        border-style:solid;
        border-color:#00BB9E;
        background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #C0D3EB,stop:1 #BCCFE7);
        }
        
        QTabBar::tab:top,QTabBar::tab:bottom{
        padding:3px 8px 3px 8px;
        }
        
        QTabBar::tab:left,QTabBar::tab:right{
        padding:8px 3px 8px 3px;
        }
        
        QTabBar::tab:top:selected,QTabBar::tab:top:hover{
        border-width:2px 0px 0px 0px;
        }
        
        QTabBar::tab:right:selected,QTabBar::tab:right:hover{
        border-width:0px 0px 0px 2px;
        }
        
        QTabBar::tab:bottom:selected,QTabBar::tab:bottom:hover{
        border-width:0px 0px 2px 0px;
        }
        
        QTabBar::tab:left:selected,QTabBar::tab:left:hover{
        border-width:0px 2px 0px 0px;
        }
        
        QTabBar::tab:first:top:selected,QTabBar::tab:first:top:hover,QTabBar::tab:first:bottom:selected,QTabBar::tab:first:bottom:hover{
        border-left-width:1px;
        border-left-color:#7F9AB8;
        }
        
        QTabBar::tab:first:left:selected,QTabBar::tab:first:left:hover,QTabBar::tab:first:right:selected,QTabBar::tab:first:right:hover{
        border-top-width:1px;
        border-top-color:#7F9AB8;
        }
        
        QTabBar::tab:last:top:selected,QTabBar::tab:last:top:hover,QTabBar::tab:last:bottom:selected,QTabBar::tab:last:bottom:hover{
        border-right-width:1px;
        border-right-color:#7F9AB8;
        }
        
        QTabBar::tab:last:left:selected,QTabBar::tab:last:left:hover,QTabBar::tab:last:right:selected,QTabBar::tab:last:right:hover{
        border-bottom-width:1px;
        border-bottom-color:#7F9AB8;
        }
        
        QStatusBar::item{
        border:0px solid #C0D3EB;
        border-radius:3px;
        }
        
        QToolBox::tab,QGroupBox#gboxDevicePanel,QGroupBox#gboxDeviceTitle,QFrame#gboxDevicePanel,QFrame#gboxDeviceTitle{
        padding:3px;
        border-radius:5px;
        color:#324C6C;
        background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #C0D3EB,stop:1 #BCCFE7);
        }
        
        QToolTip{
        border:0px solid #324C6C;
        padding:1px;
        color:#324C6C;
        background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #C0D3EB,stop:1 #BCCFE7);
        }
        
        QToolBox::tab:selected{
        background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #D2E3F5,stop:1 #CADDF3);
        }
        
        QPrintPreviewDialog QToolButton{
        border:0px solid #324C6C;
        border-radius:0px;
        margin:0px;
        padding:3px;
        background:none;
        }
        
        QColorDialog QPushButton,QFileDialog QPushButton{
        min-width:80px;
        }
        
        QToolButton#qt_calendar_prevmonth{
        icon-size:0px;
        min-width:20px;
        image:url(:/qss/blue/calendar_prevmonth.png);
        }
        
        QToolButton#qt_calendar_nextmonth{
        icon-size:0px;
        min-width:20px;
        image:url(:/qss/blue/calendar_nextmonth.png);
        }
        
        QToolButton#qt_calendar_prevmonth,QToolButton#qt_calendar_nextmonth,QToolButton#qt_calendar_monthbutton,QToolButton#qt_calendar_yearbutton{
        border:0px solid #324C6C;
        border-radius:3px;
        margin:3px 3px 3px 3px;
        padding:3px;
        background:none;
        }
        
        QToolButton#qt_calendar_prevmonth:hover,QToolButton#qt_calendar_nextmonth:hover,QToolButton#qt_calendar_monthbutton:hover,QToolButton#qt_calendar_yearbutton:hover,QToolButton#qt_calendar_prevmonth:pressed,QToolButton#qt_calendar_nextmonth:pressed,QToolButton#qt_calendar_monthbutton:pressed,QToolButton#qt_calendar_yearbutton:pressed{
        border:1px solid #7F9AB8;
        }
        
        QCalendarWidget QSpinBox#qt_calendar_yearedit{
        margin:2px;
        }
        
        QCalendarWidget QToolButton::menu-indicator{
        image:None;
        }
        
        QCalendarWidget QTableView,QTableWidget{
        border-width:0px;
        }
        
        QCalendarWidget QWidget#qt_calendar_navigationbar{
        border:1px solid #7F9AB8;
        border-width:1px 1px 0px 1px;
        background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #C0D3EB,stop:1 #BCCFE7);
        }
        
        QComboBox QAbstractItemView::item{
        min-height:20px;
        min-width:10px;
        }
        
        QTableView,QTableWidget[model="true"]::item{
        padding:0px;
        margin:0px;
        }
        
        QTableView,QTableWidget QLineEdit,QTableView,QTableWidget QComboBox,QTableView,QTableWidget QSpinBox,QTableView,QTableWidget QDoubleSpinBox,QTableView,QTableWidget QDateEdit,QTableView,QTableWidget QTimeEdit,QTableView,QTableWidget QDateTimeEdit{
        border-width:0px;
        border-radius:0px;
        }
        
        QTableView,QTableWidget QLineEdit:focus,QTableView,QTableWidget QComboBox:focus,QTableView,QTableWidget QSpinBox:focus,QTableView,QTableWidget QDoubleSpinBox:focus,QTableView,QTableWidget QDateEdit:focus,QTableView,QTableWidget QTimeEdit:focus,QTableView,QTableWidget QDateTimeEdit:focus{
        border-width:0px;
        border-radius:0px;
        }
        
        QLineEdit,QTextEdit,QPlainTextEdit,QSpinBox,QDoubleSpinBox,QComboBox,QDateEdit,QTimeEdit,QDateTimeEdit{
        background:#CFDDEE;
        }
        
        *:disabled{
        background:#CFDDEE;
        border-color:#C0D3EB;
        }
        
        
        /*TextColor:#324C6C*/
        /*PanelColor:#CFDDEE*/
        /*BorderColor:#7F9AB8*/
        /*NormalColorStart:#C0D3EB*/
        /*NormalColorEnd:#BCCFE7*/
        /*DarkColorStart:#D2E3F5*/
        /*DarkColorEnd:#CADDF3*/
        /*HighColor:#00BB9E*/
                '''

        return qss


class Bf(object):
    @classmethod
    def get_qss(cls):
        qss = '''
        QPalette{background:#2A2C32;}*{outline:0px;color:#FFFFFE;}
        
        QWidget[form="true"],QLabel[frameShape="1"]{
        border:1px solid #2A2C32;
        border-radius:0px;
        }
        
        QWidget[form="bottom"]{
        background:#383A42;
        }
        
        QWidget[form="bottom"] .QFrame{
        border:1px solid #FFFFFE;
        }
        
        QWidget[form="bottom"] QLabel,QWidget[form="title"] QLabel{
        border-radius:0px;
        color:#FFFFFE;
        background:none;
        border-style:none;
        }
        
        QWidget[form="title"],QWidget[nav="left"],QWidget[nav="top"] QAbstractButton{
        border-style:none;
        border-radius:0px;
        padding:5px;
        color:#FFFFFE;
        background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #383A42,stop:1 #383A42);
        }
        
        QWidget[nav="top"] QAbstractButton:hover,QWidget[nav="top"] QAbstractButton:pressed,QWidget[nav="top"] QAbstractButton:checked{
        border-style:solid;
        border-width:0px 0px 2px 0px;
        padding:4px 4px 2px 4px;
        border-color:#2C72F2;
        background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #181818,stop:1 #181818);
        }
        
        QWidget[nav="left"] QAbstractButton{
        border-radius:0px;
        color:#FFFFFE;
        background:none;
        border-style:none;
        }
        
        QWidget[nav="left"] QAbstractButton:hover{
        color:#FFFFFF;
        background-color:#2C72F2;
        }
        
        QWidget[nav="left"] QAbstractButton:checked,QWidget[nav="left"] QAbstractButton:pressed{
        color:#FFFFFE;
        border-style:solid;
        border-width:0px 0px 0px 2px;
        padding:4px 4px 4px 2px;
        border-color:#2C72F2;
        background-color:#2A2C32;
        }
        
        QWidget[video="true"] QLabel{
        color:#FFFFFE;
        border:1px solid #2A2C32;
        background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #383A42,stop:1 #383A42);
        }
        
        QWidget[video="true"] QLabel:focus{
        border:1px solid #2C72F2;
        background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #181818,stop:1 #181818);
        }
        
        QLineEdit,QTextEdit,QPlainTextEdit,QSpinBox,QDoubleSpinBox,QComboBox,QDateEdit,QTimeEdit,QDateTimeEdit{
        border:1px solid #2A2C32;
        border-radius:3px;
        padding:2px;
        background:none;
        selection-background-color:#383A42;
        selection-color:#FFFFFE;
        }
        
        QLineEdit:focus,QTextEdit:focus,QPlainTextEdit:focus,QSpinBox:focus,QDoubleSpinBox:focus,QComboBox:focus,QDateEdit:focus,QTimeEdit:focus,QDateTimeEdit:focus,QLineEdit:hover,QTextEdit:hover,QPlainTextEdit:hover,QSpinBox:hover,QDoubleSpinBox:hover,QComboBox:hover,QDateEdit:hover,QTimeEdit:hover,QDateTimeEdit:hover{
        border:1px solid #2A2C32;
        }
        
        QLineEdit[echoMode="2"]{
        lineedit-password-character:9679;
        }
        
        .QFrame{
        border:1px solid #2A2C32;
        border-radius:3px;
        }
        
        .QGroupBox{
        border:1px solid #2A2C32;
        border-radius:5px;
        margin-top:3ex;
        }
        
        .QGroupBox::title{
        subcontrol-origin:margin;
        position:relative;
        left:10px;
        }
        
        .QPushButton,.QToolButton{
        border-style:none;
        border:1px solid #2A2C32;
        color:#FFFFFE;
        padding:5px;
        min-height:15px;
        border-radius:5px;
        background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #383A42,stop:1 #383A42);
        }
        
        .QPushButton:hover,.QToolButton:hover{
        background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #181818,stop:1 #181818);
        }
        
        .QPushButton:pressed,.QToolButton:pressed{
        background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #383A42,stop:1 #383A42);
        }
        
        .QToolButton::menu-indicator{
        image:None;
        }
        
        QToolButton#btnMenu,QPushButton#btnMenu_Min,QPushButton#btnMenu_Max,QPushButton#btnMenu_Close{
        border-radius:3px;
        color:#FFFFFE;
        padding:3px;
        margin:0px;
        background:none;
        border-style:none;
        }
        
        QToolButton#btnMenu:hover,QPushButton#btnMenu_Min:hover,QPushButton#btnMenu_Max:hover{
        color:#FFFFFF;
        margin:1px 1px 2px 1px;
        background-color:rgba(51,127,209,230);
        }
        
        QPushButton#btnMenu_Close:hover{
        color:#FFFFFF;
        margin:1px 1px 2px 1px;
        background-color:rgba(238,0,0,128);
        }
        
        QRadioButton::indicator{
        width:15px;
        height:15px;
        }
        
        QRadioButton::indicator::unchecked{
        image:url(:/qss/bf/radiobutton_unchecked.png);
        }
        
        QRadioButton::indicator::unchecked:disabled{
        image:url(:/qss/bf/radiobutton_unchecked_disable.png);
        }
        
        QRadioButton::indicator::checked{
        image:url(:/qss/bf/radiobutton_checked.png);
        }
        
        QRadioButton::indicator::checked:disabled{
        image:url(:/qss/bf/radiobutton_checked_disable.png);
        }
        
        QGroupBox::indicator,QTreeWidget::indicator,QListWidget::indicator{
        padding:0px -3px 0px 3px;
        }
        
        QCheckBox::indicator,QGroupBox::indicator,QTreeWidget::indicator,QListWidget::indicator{
        width:13px;
        height:13px;
        }
        
        QCheckBox::indicator:unchecked,QGroupBox::indicator:unchecked,QTreeWidget::indicator:unchecked,QListWidget::indicator:unchecked{
        image:url(:/qss/bf/checkbox_unchecked.png);
        }
        
        QCheckBox::indicator:unchecked:disabled,QGroupBox::indicator:unchecked:disabled,QTreeWidget::indicator:unchecked:disabled,QListWidget::indicator:disabled{
        image:url(:/qss/bf/checkbox_unchecked_disable.png);
        }
        
        QCheckBox::indicator:checked,QGroupBox::indicator:checked,QTreeWidget::indicator:checked,QListWidget::indicator:checked{
        image:url(:/qss/bf/checkbox_checked.png);
        }
        
        QCheckBox::indicator:checked:disabled,QGroupBox::indicator:checked:disabled,QTreeWidget::indicator:checked:disabled,QListWidget::indicator:checked:disabled{
        image:url(:/qss/bf/checkbox_checked_disable.png);
        }
        
        QCheckBox::indicator:indeterminate,QGroupBox::indicator:indeterminate,QTreeWidget::indicator:indeterminate,QListWidget::indicator:indeterminate{
        image:url(:/qss/bf/checkbox_parcial.png);
        }
        
        QCheckBox::indicator:indeterminate:disabled,QGroupBox::indicator:indeterminate:disabled,QTreeWidget::indicator:indeterminate:disabled,QListWidget::indicator:indeterminate:disabled{
        image:url(:/qss/bf/checkbox_parcial_disable.png);
        }
        
        QTimeEdit::up-button,QDateEdit::up-button,QDateTimeEdit::up-button,QDoubleSpinBox::up-button,QSpinBox::up-button{
        image:url(:/qss/bf/add_top.png);
        width:10px;
        height:10px;
        padding:2px 5px 0px 0px;
        }
        
        QTimeEdit::down-button,QDateEdit::down-button,QDateTimeEdit::down-button,QDoubleSpinBox::down-button,QSpinBox::down-button{
        image:url(:/qss/bf/add_bottom.png);
        width:10px;
        height:10px;
        padding:0px 5px 2px 0px;
        }
        
        QTimeEdit::up-button:pressed,QDateEdit::up-button:pressed,QDateTimeEdit::up-button:pressed,QDoubleSpinBox::up-button:pressed,QSpinBox::up-button:pressed{
        top:-2px;
        }
          
        QTimeEdit::down-button:pressed,QDateEdit::down-button:pressed,QDateTimeEdit::down-button:pressed,QDoubleSpinBox::down-button:pressed,QSpinBox::down-button:pressed,QSpinBox::down-button:pressed{
        bottom:-2px;
        }
        
        QComboBox::down-arrow,QDateEdit[calendarPopup="true"]::down-arrow,QTimeEdit[calendarPopup="true"]::down-arrow,QDateTimeEdit[calendarPopup="true"]::down-arrow{
        image:url(:/qss/bf/add_bottom.png);
        width:10px;
        height:10px;
        right:2px;
        }
        
        QComboBox::drop-down,QDateEdit::drop-down,QTimeEdit::drop-down,QDateTimeEdit::drop-down{
        subcontrol-origin:padding;
        subcontrol-position:top right;
        width:15px;
        border-left-width:0px;
        border-left-style:solid;
        border-top-right-radius:3px;
        border-bottom-right-radius:3px;
        border-left-color:#2A2C32;
        }
        
        QComboBox::drop-down:on{
        top:1px;
        }
        
        QMenuBar::item{
        color:#FFFFFE;
        background-color:#383A42;
        margin:0px;
        padding:3px 10px;
        }
        
        QMenu,QMenuBar,QMenu:disabled,QMenuBar:disabled{
        color:#FFFFFE;
        background-color:#383A42;
        border:1px solid #2A2C32;
        margin:0px;
        }
        
        QMenu::item{
        padding:3px 20px;
        }
        
        QMenu::indicator{
        width:13px;
        height:13px;
        }
        
        QMenu::item:selected,QMenuBar::item:selected{
        color:#FFFFFE;
        border:0px solid #2A2C32;
        background:#181818;
        }
        
        QMenu::separator{
        height:1px;
        background:#2A2C32;
        }
        
        QProgressBar{
        min-height:10px;
        background:#383A42;
        border-radius:5px;
        text-align:center;
        border:1px solid #383A42;
        }
        
        QProgressBar:chunk{
        border-radius:5px;
        background-color:#2A2C32;
        }
        
        QSlider::groove:horizontal{
        background:#383A42;
        height:8px;
        border-radius:4px;
        }
        
        QSlider::add-page:horizontal{
        background:#383A42;
        height:8px;
        border-radius:4px;
        }
        
        QSlider::sub-page:horizontal{
        background:#2A2C32;
        height:8px;
        border-radius:4px;
        }
        
        QSlider::handle:horizontal{
        width:13px;
        margin-top:-3px;
        margin-bottom:-3px;
        border-radius:6px;
        background:qradialgradient(spread:pad,cx:0.5,cy:0.5,radius:0.5,fx:0.5,fy:0.5,stop:0.6 #2A2C32,stop:0.8 #2A2C32);
        }
        
        QSlider::groove:vertical{
        width:8px;
        border-radius:4px;
        background:#383A42;
        }
        
        QSlider::add-page:vertical{
        width:8px;
        border-radius:4px;
        background:#383A42;
        }
        
        QSlider::sub-page:vertical{
        width:8px;
        border-radius:4px;
        background:#2A2C32;
        }
        
        QSlider::handle:vertical{
        height:14px;
        margin-left:-3px;
        margin-right:-3px;
        border-radius:6px;
        background:qradialgradient(spread:pad,cx:0.5,cy:0.5,radius:0.5,fx:0.5,fy:0.5,stop:0.6 #2A2C32,stop:0.8 #2A2C32);
        }
        
        QScrollBar:horizontal{
        background:#383A42;
        padding:0px;
        border-radius:6px;
        max-height:12px;
        }
        
        QScrollBar::handle:horizontal{
        background:#181818;
        min-width:50px;
        border-radius:6px;
        }
        
        QScrollBar::handle:horizontal:hover{
        background:#2A2C32;
        }
        
        QScrollBar::handle:horizontal:pressed{
        background:#2A2C32;
        }
        
        QScrollBar::add-page:horizontal{
        background:none;
        }
        
        QScrollBar::sub-page:horizontal{
        background:none;
        }
        
        QScrollBar::add-line:horizontal{
        background:none;
        }
        
        QScrollBar::sub-line:horizontal{
        background:none;
        }
        
        QScrollBar:vertical{
        background:#383A42;
        padding:0px;
        border-radius:6px;
        max-width:12px;
        }
        
        QScrollBar::handle:vertical{
        background:#181818;
        min-height:50px;
        border-radius:6px;
        }
        
        QScrollBar::handle:vertical:hover{
        background:#2A2C32;
        }
        
        QScrollBar::handle:vertical:pressed{
        background:#2A2C32;
        }
        
        QScrollBar::add-page:vertical{
        background:none;
        }
        
        QScrollBar::sub-page:vertical{
        background:none;
        }
        
        QScrollBar::add-line:vertical{
        background:none;
        }
        
        QScrollBar::sub-line:vertical{
        background:none;
        }
        
        QScrollArea{
        border:0px;
        }
        
        QTreeView,QListView,QTableView,QTabWidget::pane{
        border:1px solid #2A2C32;
        selection-background-color:#181818;
        selection-color:#FFFFFE;
        alternate-background-color:#181818;
        gridline-color:#2A2C32;
        }
        
        QTreeView::branch:closed:has-children{
        margin:4px;
        border-image:url(:/qss/bf/branch_open.png);
        }
        
        QTreeView::branch:open:has-children{
        margin:4px;
        border-image:url(:/qss/bf/branch_close.png);
        }
        
        QTreeView,QListView,QTableView,QSplitter::handle,QTreeView::branch{
        background:#2A2C32;
        }
        
        QTableView::item:selected,QListView::item:selected,QTreeView::item:selected{
        color:#FFFFFE;
        background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #383A42,stop:1 #383A42);
        }
        
        QTableView::item:hover,QListView::item:hover,QTreeView::item:hover{
        color:#FFFFFE;
        background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #181818,stop:1 #181818);
        }
        
        QTableView::item,QListView::item,QTreeView::item{
        padding:1px;
        margin:0px;
        }
        
        QHeaderView::section,QTableCornerButton:section{
        padding:3px;
        margin:0px;
        color:#FFFFFE;
        border:1px solid #2A2C32;
        border-left-width:0px;
        border-right-width:1px;
        border-top-width:0px;
        border-bottom-width:1px;
        background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #181818,stop:1 #181818);
        }
        
        QTabBar::tab{
        border:1px solid #2A2C32;
        color:#FFFFFE;
        margin:0px;
        background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #181818,stop:1 #181818);
        }
        
        QTabBar::tab:selected,QTabBar::tab:hover{
        border-style:solid;
        border-color:#2C72F2;
        background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #383A42,stop:1 #383A42);
        }
        
        QTabBar::tab:top,QTabBar::tab:bottom{
        padding:3px 8px 3px 8px;
        }
        
        QTabBar::tab:left,QTabBar::tab:right{
        padding:8px 3px 8px 3px;
        }
        
        QTabBar::tab:top:selected,QTabBar::tab:top:hover{
        border-width:2px 0px 0px 0px;
        }
        
        QTabBar::tab:right:selected,QTabBar::tab:right:hover{
        border-width:0px 0px 0px 2px;
        }
        
        QTabBar::tab:bottom:selected,QTabBar::tab:bottom:hover{
        border-width:0px 0px 2px 0px;
        }
        
        QTabBar::tab:left:selected,QTabBar::tab:left:hover{
        border-width:0px 2px 0px 0px;
        }
        
        QTabBar::tab:first:top:selected,QTabBar::tab:first:top:hover,QTabBar::tab:first:bottom:selected,QTabBar::tab:first:bottom:hover{
        border-left-width:1px;
        border-left-color:#2A2C32;
        }
        
        QTabBar::tab:first:left:selected,QTabBar::tab:first:left:hover,QTabBar::tab:first:right:selected,QTabBar::tab:first:right:hover{
        border-top-width:1px;
        border-top-color:#2A2C32;
        }
        
        QTabBar::tab:last:top:selected,QTabBar::tab:last:top:hover,QTabBar::tab:last:bottom:selected,QTabBar::tab:last:bottom:hover{
        border-right-width:1px;
        border-right-color:#2A2C32;
        }
        
        QTabBar::tab:last:left:selected,QTabBar::tab:last:left:hover,QTabBar::tab:last:right:selected,QTabBar::tab:last:right:hover{
        border-bottom-width:1px;
        border-bottom-color:#2A2C32;
        }
        
        QStatusBar::item{
        border:0px solid #383A42;
        border-radius:3px;
        }
        
        QToolBox::tab,QGroupBox#gboxDevicePanel,QGroupBox#gboxDeviceTitle,QFrame#gboxDevicePanel,QFrame#gboxDeviceTitle{
        padding:3px;
        border-radius:5px;
        color:#FFFFFE;
        background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #383A42,stop:1 #383A42);
        }
        
        QToolTip{
        border:0px solid #FFFFFE;
        padding:1px;
        color:#FFFFFE;
        background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #383A42,stop:1 #383A42);
        }
        
        QToolBox::tab:selected{
        background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #181818,stop:1 #181818);
        }
        
        QPrintPreviewDialog QToolButton{
        border:0px solid #FFFFFE;
        border-radius:0px;
        margin:0px;
        padding:3px;
        background:none;
        }
        
        QColorDialog QPushButton,QFileDialog QPushButton{
        min-width:80px;
        }
        
        QToolButton#qt_calendar_prevmonth{
        icon-size:0px;
        min-width:20px;
        image:url(:/qss/bf/calendar_prevmonth.png);
        }
        
        QToolButton#qt_calendar_nextmonth{
        icon-size:0px;
        min-width:20px;
        image:url(:/qss/bf/calendar_nextmonth.png);
        }
        
        QToolButton#qt_calendar_prevmonth,QToolButton#qt_calendar_nextmonth,QToolButton#qt_calendar_monthbutton,QToolButton#qt_calendar_yearbutton{
        border:0px solid #FFFFFE;
        border-radius:3px;
        margin:3px 3px 3px 3px;
        padding:3px;
        background:none;
        }
        
        QToolButton#qt_calendar_prevmonth:hover,QToolButton#qt_calendar_nextmonth:hover,QToolButton#qt_calendar_monthbutton:hover,QToolButton#qt_calendar_yearbutton:hover,QToolButton#qt_calendar_prevmonth:pressed,QToolButton#qt_calendar_nextmonth:pressed,QToolButton#qt_calendar_monthbutton:pressed,QToolButton#qt_calendar_yearbutton:pressed{
        border:1px solid #2A2C32;
        }
        
        QCalendarWidget QSpinBox#qt_calendar_yearedit{
        margin:2px;
        }
        
        QCalendarWidget QToolButton::menu-indicator{
        image:None;
        }
        
        QCalendarWidget QTableView{
        border-width:0px;
        }
        
        QCalendarWidget QWidget#qt_calendar_navigationbar{
        border:1px solid #2A2C32;
        border-width:1px 1px 0px 1px;
        background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #383A42,stop:1 #383A42);
        }
        
        QComboBox QAbstractItemView::item{
        min-height:20px;
        min-width:10px;
        }
        
        QTableView[model="true"]::item{
        padding:0px;
        margin:0px;
        }
        
        QTableView QLineEdit,QTableView QComboBox,QTableView QSpinBox,QTableView QDoubleSpinBox,QTableView QDateEdit,QTableView QTimeEdit,QTableView QDateTimeEdit{
        border-width:0px;
        border-radius:0px;
        }
        
        QTableView QLineEdit:focus,QTableView QComboBox:focus,QTableView QSpinBox:focus,QTableView QDoubleSpinBox:focus,QTableView QDateEdit:focus,QTableView QTimeEdit:focus,QTableView QDateTimeEdit:focus{
        border-width:0px;
        border-radius:0px;
        }
        
        QLineEdit,QTextEdit,QPlainTextEdit,QSpinBox,QDoubleSpinBox,QComboBox,QDateEdit,QTimeEdit,QDateTimeEdit{
        background:#2A2C32;
        }
        
        *:disabled{
        background:#2A2C32;
        border-color:#383A42;
        }
        
        /*TextColor:#FFFFFE*/
        /*PanelColor:#2A2C32*/
        /*BorderColor:#2A2C32*/
        /*NormalColorStart:#383A42*/
        /*NormalColorEnd:#383A42*/
        /*DarkColorStart:#181818*/
        /*DarkColorEnd:#181818*/
        /*HighColor:#2C72F2*/
        '''
        return qss


class FlatWhite(object):
    @classmethod
    def get_qss(cls):
        qss = '''
        QPalette{background:#FFFFFF;}*{outline:0px;color:#57595B;}
        
        QWidget[form="true"],QLabel[frameShape="1"]{
        border:1px solid #B6B6B6;
        border-radius:0px;
        }
        
        QWidget[form="bottom"]{
        background:#E4E4E4;
        }
        
        QWidget[form="bottom"] .QFrame{
        border:1px solid #57595B;
        }
        
        QWidget[form="bottom"] QLabel,QWidget[form="title"] QLabel{
        border-radius:0px;
        color:#57595B;
        background:none;
        border-style:none;
        }
        
        QWidget[form="title"],QWidget[nav="left"],QWidget[nav="top"] QAbstractButton{
        border-style:none;
        border-radius:0px;
        padding:5px;
        color:#57595B;
        background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #E4E4E4,stop:1 #E4E4E4);
        }
        
        QWidget[nav="top"] QAbstractButton:hover,QWidget[nav="top"] QAbstractButton:pressed,QWidget[nav="top"] QAbstractButton:checked{
        border-style:solid;
        border-width:0px 0px 2px 0px;
        padding:4px 4px 2px 4px;
        border-color:#00BB9E;
        background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #F6F6F6,stop:1 #F6F6F6);
        }
        
        QWidget[nav="left"] QAbstractButton{
        border-radius:0px;
        color:#57595B;
        background:none;
        border-style:none;
        }
        
        QWidget[nav="left"] QAbstractButton:hover{
        color:#FFFFFF;
        background-color:#00BB9E;
        }
        
        QWidget[nav="left"] QAbstractButton:checked,QWidget[nav="left"] QAbstractButton:pressed{
        color:#57595B;
        border-style:solid;
        border-width:0px 0px 0px 2px;
        padding:4px 4px 4px 2px;
        border-color:#00BB9E;
        background-color:#FFFFFF;
        }
        
        QWidget[video="true"] QLabel{
        color:#57595B;
        border:1px solid #B6B6B6;
        background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #E4E4E4,stop:1 #E4E4E4);
        }
        
        QWidget[video="true"] QLabel:focus{
        border:1px solid #00BB9E;
        background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #F6F6F6,stop:1 #F6F6F6);
        }
        
        QLineEdit,QTextEdit,QPlainTextEdit,QSpinBox,QDoubleSpinBox,QComboBox,QDateEdit,QTimeEdit,QDateTimeEdit{
        border:1px solid #B6B6B6;
        border-radius:3px;
        padding:2px;
        background:none;
        selection-background-color:#E4E4E4;
        selection-color:#57595B;
        }
        
        QLineEdit:focus,QTextEdit:focus,QPlainTextEdit:focus,QSpinBox:focus,QDoubleSpinBox:focus,QComboBox:focus,QDateEdit:focus,QTimeEdit:focus,QDateTimeEdit:focus,QLineEdit:hover,QTextEdit:hover,QPlainTextEdit:hover,QSpinBox:hover,QDoubleSpinBox:hover,QComboBox:hover,QDateEdit:hover,QTimeEdit:hover,QDateTimeEdit:hover{
        border:1px solid #B6B6B6;
        }
        
        QLineEdit[echoMode="2"]{
        lineedit-password-character:9679;
        }
        
        .QFrame{
        border:1px solid #B6B6B6;
        border-radius:3px;
        }
        
        .QGroupBox{
        border:1px solid #B6B6B6;
        border-radius:5px;
        margin-top:3ex;
        }
        
        .QGroupBox::title{
        subcontrol-origin:margin;
        position:relative;
        left:10px;
        }
        
        .QPushButton,.QToolButton{
        border-style:none;
        border:1px solid #B6B6B6;
        color:#57595B;
        padding:5px;
        min-height:15px;
        border-radius:5px;
        background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #E4E4E4,stop:1 #E4E4E4);
        }
        
        .QPushButton:hover,.QToolButton:hover{
        background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #F6F6F6,stop:1 #F6F6F6);
        }
        
        .QPushButton:pressed,.QToolButton:pressed{
        background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #E4E4E4,stop:1 #E4E4E4);
        }
        
        .QToolButton::menu-indicator{
        image:None;
        }
        
        QToolButton#btnMenu,QPushButton#btnMenu_Min,QPushButton#btnMenu_Max,QPushButton#btnMenu_Close{
        border-radius:3px;
        color:#57595B;
        padding:3px;
        margin:0px;
        background:none;
        border-style:none;
        }
        
        QToolButton#btnMenu:hover,QPushButton#btnMenu_Min:hover,QPushButton#btnMenu_Max:hover{
        color:#FFFFFF;
        margin:1px 1px 2px 1px;
        background-color:rgba(51,127,209,230);
        }
        
        QPushButton#btnMenu_Close:hover{
        color:#FFFFFF;
        margin:1px 1px 2px 1px;
        background-color:rgba(238,0,0,128);
        }
        
        QRadioButton::indicator{
        width:15px;
        height:15px;
        }
        
        QRadioButton::indicator::unchecked{
        image:url(:/qss/flatwhite/radiobutton_unchecked.png);
        }
        
        QRadioButton::indicator::unchecked:disabled{
        image:url(:/qss/flatwhite/radiobutton_unchecked_disable.png);
        }
        
        QRadioButton::indicator::checked{
        image:url(:/qss/flatwhite/radiobutton_checked.png);
        }
        
        QRadioButton::indicator::checked:disabled{
        image:url(:/qss/flatwhite/radiobutton_checked_disable.png);
        }
        
        QGroupBox::indicator,QTreeWidget::indicator,QListWidget::indicator{
        padding:0px -3px 0px 3px;
        }
        
        QCheckBox::indicator,QGroupBox::indicator,QTreeWidget::indicator,QListWidget::indicator{
        width:13px;
        height:13px;
        }
        
        QCheckBox::indicator:unchecked,QGroupBox::indicator:unchecked,QTreeWidget::indicator:unchecked,QListWidget::indicator:unchecked{
        image:url(:/qss/flatwhite/checkbox_unchecked.png);
        }
        
        QCheckBox::indicator:unchecked:disabled,QGroupBox::indicator:unchecked:disabled,QTreeWidget::indicator:unchecked:disabled,QListWidget::indicator:disabled{
        image:url(:/qss/flatwhite/checkbox_unchecked_disable.png);
        }
        
        QCheckBox::indicator:checked,QGroupBox::indicator:checked,QTreeWidget::indicator:checked,QListWidget::indicator:checked{
        image:url(:/qss/flatwhite/checkbox_checked.png);
        }
        
        QCheckBox::indicator:checked:disabled,QGroupBox::indicator:checked:disabled,QTreeWidget::indicator:checked:disabled,QListWidget::indicator:checked:disabled{
        image:url(:/qss/flatwhite/checkbox_checked_disable.png);
        }
        
        QCheckBox::indicator:indeterminate,QGroupBox::indicator:indeterminate,QTreeWidget::indicator:indeterminate,QListWidget::indicator:indeterminate{
        image:url(:/qss/flatwhite/checkbox_parcial.png);
        }
        
        QCheckBox::indicator:indeterminate:disabled,QGroupBox::indicator:indeterminate:disabled,QTreeWidget::indicator:indeterminate:disabled,QListWidget::indicator:indeterminate:disabled{
        image:url(:/qss/flatwhite/checkbox_parcial_disable.png);
        }
        
        QTimeEdit::up-button,QDateEdit::up-button,QDateTimeEdit::up-button,QDoubleSpinBox::up-button,QSpinBox::up-button{
        image:url(:/qss/flatwhite/add_top.png);
        width:10px;
        height:10px;
        padding:2px 5px 0px 0px;
        }
        
        QTimeEdit::down-button,QDateEdit::down-button,QDateTimeEdit::down-button,QDoubleSpinBox::down-button,QSpinBox::down-button{
        image:url(:/qss/flatwhite/add_bottom.png);
        width:10px;
        height:10px;
        padding:0px 5px 2px 0px;
        }
        
        QTimeEdit::up-button:pressed,QDateEdit::up-button:pressed,QDateTimeEdit::up-button:pressed,QDoubleSpinBox::up-button:pressed,QSpinBox::up-button:pressed{
        top:-2px;
        }
          
        QTimeEdit::down-button:pressed,QDateEdit::down-button:pressed,QDateTimeEdit::down-button:pressed,QDoubleSpinBox::down-button:pressed,QSpinBox::down-button:pressed,QSpinBox::down-button:pressed{
        bottom:-2px;
        }
        
        QComboBox::down-arrow,QDateEdit[calendarPopup="true"]::down-arrow,QTimeEdit[calendarPopup="true"]::down-arrow,QDateTimeEdit[calendarPopup="true"]::down-arrow{
        image:url(:/qss/flatwhite/add_bottom.png);
        width:10px;
        height:10px;
        right:2px;
        }
        
        QComboBox::drop-down,QDateEdit::drop-down,QTimeEdit::drop-down,QDateTimeEdit::drop-down{
        subcontrol-origin:padding;
        subcontrol-position:top right;
        width:15px;
        border-left-width:0px;
        border-left-style:solid;
        border-top-right-radius:3px;
        border-bottom-right-radius:3px;
        border-left-color:#B6B6B6;
        }
        
        QComboBox::drop-down:on{
        top:1px;
        }
        
        QMenuBar::item{
        color:#57595B;
        background-color:#E4E4E4;
        margin:0px;
        padding:3px 10px;
        }
        
        QMenu,QMenuBar,QMenu:disabled,QMenuBar:disabled{
        color:#57595B;
        background-color:#E4E4E4;
        border:1px solid #B6B6B6;
        margin:0px;
        }
        
        QMenu::item{
        padding:3px 20px;
        }
        
        QMenu::indicator{
        width:13px;
        height:13px;
        }
        
        QMenu::item:selected,QMenuBar::item:selected{
        color:#57595B;
        border:0px solid #B6B6B6;
        background:#F6F6F6;
        }
        
        QMenu::separator{
        height:1px;
        background:#B6B6B6;
        }
        
        QProgressBar{
        min-height:10px;
        background:#E4E4E4;
        border-radius:5px;
        text-align:center;
        border:1px solid #E4E4E4;
        }
        
        QProgressBar:chunk{
        border-radius:5px;
        background-color:#B6B6B6;
        }
        
        QSlider::groove:horizontal{
        background:#E4E4E4;
        height:8px;
        border-radius:4px;
        }
        
        QSlider::add-page:horizontal{
        background:#E4E4E4;
        height:8px;
        border-radius:4px;
        }
        
        QSlider::sub-page:horizontal{
        background:#B6B6B6;
        height:8px;
        border-radius:4px;
        }
        
        QSlider::handle:horizontal{
        width:13px;
        margin-top:-3px;
        margin-bottom:-3px;
        border-radius:6px;
        background:qradialgradient(spread:pad,cx:0.5,cy:0.5,radius:0.5,fx:0.5,fy:0.5,stop:0.6 #FFFFFF,stop:0.8 #B6B6B6);
        }
        
        QSlider::groove:vertical{
        width:8px;
        border-radius:4px;
        background:#E4E4E4;
        }
        
        QSlider::add-page:vertical{
        width:8px;
        border-radius:4px;
        background:#E4E4E4;
        }
        
        QSlider::sub-page:vertical{
        width:8px;
        border-radius:4px;
        background:#B6B6B6;
        }
        
        QSlider::handle:vertical{
        height:14px;
        margin-left:-3px;
        margin-right:-3px;
        border-radius:6px;
        background:qradialgradient(spread:pad,cx:0.5,cy:0.5,radius:0.5,fx:0.5,fy:0.5,stop:0.6 #FFFFFF,stop:0.8 #B6B6B6);
        }
        
        QScrollBar:horizontal{
        background:#E4E4E4;
        padding:0px;
        border-radius:6px;
        max-height:12px;
        }
        
        QScrollBar::handle:horizontal{
        background:#F6F6F6;
        min-width:50px;
        border-radius:6px;
        }
        
        QScrollBar::handle:horizontal:hover{
        background:#B6B6B6;
        }
        
        QScrollBar::handle:horizontal:pressed{
        background:#B6B6B6;
        }
        
        QScrollBar::add-page:horizontal{
        background:none;
        }
        
        QScrollBar::sub-page:horizontal{
        background:none;
        }
        
        QScrollBar::add-line:horizontal{
        background:none;
        }
        
        QScrollBar::sub-line:horizontal{
        background:none;
        }
        
        QScrollBar:vertical{
        background:#E4E4E4;
        padding:0px;
        border-radius:6px;
        max-width:12px;
        }
        
        QScrollBar::handle:vertical{
        background:#F6F6F6;
        min-height:50px;
        border-radius:6px;
        }
        
        QScrollBar::handle:vertical:hover{
        background:#B6B6B6;
        }
        
        QScrollBar::handle:vertical:pressed{
        background:#B6B6B6;
        }
        
        QScrollBar::add-page:vertical{
        background:none;
        }
        
        QScrollBar::sub-page:vertical{
        background:none;
        }
        
        QScrollBar::add-line:vertical{
        background:none;
        }
        
        QScrollBar::sub-line:vertical{
        background:none;
        }
        
        QScrollArea{
        border:0px;
        }
        
        QTreeView,QListView,QTableView,QTabWidget::pane{
        border:1px solid #B6B6B6;
        selection-background-color:#F6F6F6;
        selection-color:#57595B;
        alternate-background-color:#F6F6F6;
        gridline-color:#B6B6B6;
        }
        
        QTreeView::branch:closed:has-children{
        margin:4px;
        border-image:url(:/qss/flatwhite/branch_open.png);
        }
        
        QTreeView::branch:open:has-children{
        margin:4px;
        border-image:url(:/qss/flatwhite/branch_close.png);
        }
        
        QTreeView,QListView,QTableView,QSplitter::handle,QTreeView::branch{
        background:#FFFFFF;
        }
        
        QTableView::item:selected,QListView::item:selected,QTreeView::item:selected{
        color:#57595B;
        background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #E4E4E4,stop:1 #E4E4E4);
        }
        
        QTableView::item:hover,QListView::item:hover,QTreeView::item:hover{
        color:#57595B;
        background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #F6F6F6,stop:1 #F6F6F6);
        }
        
        QTableView::item,QListView::item,QTreeView::item{
        padding:1px;
        margin:0px;
        }
        
        QHeaderView::section,QTableCornerButton:section{
        padding:3px;
        margin:0px;
        color:#57595B;
        border:1px solid #B6B6B6;
        border-left-width:0px;
        border-right-width:1px;
        border-top-width:0px;
        border-bottom-width:1px;
        background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #F6F6F6,stop:1 #F6F6F6);
        }
        
        QTabBar::tab{
        border:1px solid #B6B6B6;
        color:#57595B;
        margin:0px;
        background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #F6F6F6,stop:1 #F6F6F6);
        }
        
        QTabBar::tab:selected,QTabBar::tab:hover{
        border-style:solid;
        border-color:#00BB9E;
        background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #E4E4E4,stop:1 #E4E4E4);
        }
        
        QTabBar::tab:top,QTabBar::tab:bottom{
        padding:3px 8px 3px 8px;
        }
        
        QTabBar::tab:left,QTabBar::tab:right{
        padding:8px 3px 8px 3px;
        }
        
        QTabBar::tab:top:selected,QTabBar::tab:top:hover{
        border-width:2px 0px 0px 0px;
        }
        
        QTabBar::tab:right:selected,QTabBar::tab:right:hover{
        border-width:0px 0px 0px 2px;
        }
        
        QTabBar::tab:bottom:selected,QTabBar::tab:bottom:hover{
        border-width:0px 0px 2px 0px;
        }
        
        QTabBar::tab:left:selected,QTabBar::tab:left:hover{
        border-width:0px 2px 0px 0px;
        }
        
        QTabBar::tab:first:top:selected,QTabBar::tab:first:top:hover,QTabBar::tab:first:bottom:selected,QTabBar::tab:first:bottom:hover{
        border-left-width:1px;
        border-left-color:#B6B6B6;
        }
        
        QTabBar::tab:first:left:selected,QTabBar::tab:first:left:hover,QTabBar::tab:first:right:selected,QTabBar::tab:first:right:hover{
        border-top-width:1px;
        border-top-color:#B6B6B6;
        }
        
        QTabBar::tab:last:top:selected,QTabBar::tab:last:top:hover,QTabBar::tab:last:bottom:selected,QTabBar::tab:last:bottom:hover{
        border-right-width:1px;
        border-right-color:#B6B6B6;
        }
        
        QTabBar::tab:last:left:selected,QTabBar::tab:last:left:hover,QTabBar::tab:last:right:selected,QTabBar::tab:last:right:hover{
        border-bottom-width:1px;
        border-bottom-color:#B6B6B6;
        }
        
        QStatusBar::item{
        border:0px solid #E4E4E4;
        border-radius:3px;
        }
        
        QToolBox::tab,QGroupBox#gboxDevicePanel,QGroupBox#gboxDeviceTitle,QFrame#gboxDevicePanel,QFrame#gboxDeviceTitle{
        padding:3px;
        border-radius:5px;
        color:#57595B;
        background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #E4E4E4,stop:1 #E4E4E4);
        }
        
        QToolTip{
        border:0px solid #57595B;
        padding:1px;
        color:#57595B;
        background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #E4E4E4,stop:1 #E4E4E4);
        }
        
        QToolBox::tab:selected{
        background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #F6F6F6,stop:1 #F6F6F6);
        }
        
        QPrintPreviewDialog QToolButton{
        border:0px solid #57595B;
        border-radius:0px;
        margin:0px;
        padding:3px;
        background:none;
        }
        
        QColorDialog QPushButton,QFileDialog QPushButton{
        min-width:80px;
        }
        
        QToolButton#qt_calendar_prevmonth{
        icon-size:0px;
        min-width:20px;
        image:url(:/qss/flatwhite/calendar_prevmonth.png);
        }
        
        QToolButton#qt_calendar_nextmonth{
        icon-size:0px;
        min-width:20px;
        image:url(:/qss/flatwhite/calendar_nextmonth.png);
        }
        
        QToolButton#qt_calendar_prevmonth,QToolButton#qt_calendar_nextmonth,QToolButton#qt_calendar_monthbutton,QToolButton#qt_calendar_yearbutton{
        border:0px solid #57595B;
        border-radius:3px;
        margin:3px 3px 3px 3px;
        padding:3px;
        background:none;
        }
        
        QToolButton#qt_calendar_prevmonth:hover,QToolButton#qt_calendar_nextmonth:hover,QToolButton#qt_calendar_monthbutton:hover,QToolButton#qt_calendar_yearbutton:hover,QToolButton#qt_calendar_prevmonth:pressed,QToolButton#qt_calendar_nextmonth:pressed,QToolButton#qt_calendar_monthbutton:pressed,QToolButton#qt_calendar_yearbutton:pressed{
        border:1px solid #B6B6B6;
        }
        
        QCalendarWidget QSpinBox#qt_calendar_yearedit{
        margin:2px;
        }
        
        QCalendarWidget QToolButton::menu-indicator{
        image:None;
        }
        
        QCalendarWidget QTableView{
        border-width:0px;
        }
        
        QCalendarWidget QWidget#qt_calendar_navigationbar{
        border:1px solid #B6B6B6;
        border-width:1px 1px 0px 1px;
        background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #E4E4E4,stop:1 #E4E4E4);
        }
        
        QComboBox QAbstractItemView::item{
        min-height:20px;
        min-width:10px;
        }
        
        QTableView[model="true"]::item{
        padding:0px;
        margin:0px;
        }
        
        QTableView QLineEdit,QTableView QComboBox,QTableView QSpinBox,QTableView QDoubleSpinBox,QTableView QDateEdit,QTableView QTimeEdit,QTableView QDateTimeEdit{
        border-width:0px;
        border-radius:0px;
        }
        
        QTableView QLineEdit:focus,QTableView QComboBox:focus,QTableView QSpinBox:focus,QTableView QDoubleSpinBox:focus,QTableView QDateEdit:focus,QTableView QTimeEdit:focus,QTableView QDateTimeEdit:focus{
        border-width:0px;
        border-radius:0px;
        }
        
        QLineEdit,QTextEdit,QPlainTextEdit,QSpinBox,QDoubleSpinBox,QComboBox,QDateEdit,QTimeEdit,QDateTimeEdit{
        background:#FFFFFF;
        }
        
        *:disabled{
        background:#FFFFFF;
        border-color:#E4E4E4;
        }
        
        /*TextColor:#57595B*/
        /*PanelColor:#FFFFFF*/
        /*BorderColor:#B6B6B6*/
        /*NormalColorStart:#E4E4E4*/
        /*NormalColorEnd:#E4E4E4*/
        /*DarkColorStart:#F6F6F6*/
        /*DarkColorEnd:#F6F6F6*/
        /*HighColor:#00BB9E*/
                '''
        return qss


class LightBlue(object):
    @classmethod
    def get_qss(cls):
        qss = '''
        QPalette{background:#EAF7FF;}*{outline:0px;color:#386487;}
        
        QWidget[form="true"],QLabel[frameShape="1"]{
        border:1px solid #C0DCF2;
        border-radius:0px;
        }
        
        QWidget[form="bottom"]{
        background:#DEF0FE;
        }
        
        QWidget[form="bottom"] .QFrame{
        border:1px solid #386487;
        }
        
        QWidget[form="bottom"] QLabel,QWidget[form="title"] QLabel{
        border-radius:0px;
        color:#386487;
        background:none;
        border-style:none;
        }
        
        QWidget[form="title"],QWidget[nav="left"],QWidget[nav="top"] QAbstractButton{
        border-style:none;
        border-radius:0px;
        padding:5px;
        color:#386487;
        background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #DEF0FE,stop:1 #C0DEF6);
        }
        
        QWidget[nav="top"] QAbstractButton:hover,QWidget[nav="top"] QAbstractButton:pressed,QWidget[nav="top"] QAbstractButton:checked{
        border-style:solid;
        border-width:0px 0px 2px 0px;
        padding:4px 4px 2px 4px;
        border-color:#00BB9E;
        background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #F2F9FF,stop:1 #DAEFFF);
        }
        
        QWidget[nav="left"] QAbstractButton{
        border-radius:0px;
        color:#386487;
        background:none;
        border-style:none;
        }
        
        QWidget[nav="left"] QAbstractButton:hover{
        color:#FFFFFF;
        background-color:#00BB9E;
        }
        
        QWidget[nav="left"] QAbstractButton:checked,QWidget[nav="left"] QAbstractButton:pressed{
        color:#386487;
        border-style:solid;
        border-width:0px 0px 0px 2px;
        padding:4px 4px 4px 2px;
        border-color:#00BB9E;
        background-color:#EAF7FF;
        }
        
        QWidget[video="true"] QLabel{
        color:#386487;
        border:1px solid #C0DCF2;
        background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #DEF0FE,stop:1 #C0DEF6);
        }
        
        QWidget[video="true"] QLabel:focus{
        border:1px solid #00BB9E;
        background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #F2F9FF,stop:1 #DAEFFF);
        }
        
        QLineEdit,QTextEdit,QPlainTextEdit,QSpinBox,QDoubleSpinBox,QComboBox,QDateEdit,QTimeEdit,QDateTimeEdit{
        border:1px solid #C0DCF2;
        border-radius:3px;
        padding:2px;
        background:none;
        selection-background-color:#DEF0FE;
        selection-color:#386487;
        }
        
        QLineEdit:focus,QTextEdit:focus,QPlainTextEdit:focus,QSpinBox:focus,QDoubleSpinBox:focus,QComboBox:focus,QDateEdit:focus,QTimeEdit:focus,QDateTimeEdit:focus,QLineEdit:hover,QTextEdit:hover,QPlainTextEdit:hover,QSpinBox:hover,QDoubleSpinBox:hover,QComboBox:hover,QDateEdit:hover,QTimeEdit:hover,QDateTimeEdit:hover{
        border:1px solid #C0DCF2;
        }
        
        QLineEdit[echoMode="2"]{
        lineedit-password-character:9679;
        }
        
        .QFrame{
        border:1px solid #C0DCF2;
        border-radius:3px;
        }
        
        .QGroupBox{
        border:1px solid #C0DCF2;
        border-radius:5px;
        margin-top:3ex;
        }
        
        .QGroupBox::title{
        subcontrol-origin:margin;
        position:relative;
        left:10px;
        }
        
        .QPushButton,.QToolButton{
        border-style:none;
        border:1px solid #C0DCF2;
        color:#386487;
        padding:5px;
        min-height:15px;
        border-radius:5px;
        background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #DEF0FE,stop:1 #C0DEF6);
        }
        
        .QPushButton:hover,.QToolButton:hover{
        background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #F2F9FF,stop:1 #DAEFFF);
        }
        
        .QPushButton:pressed,.QToolButton:pressed{
        background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #DEF0FE,stop:1 #C0DEF6);
        }
        
        .QToolButton::menu-indicator{
        image:None;
        }
        
        QToolButton#btnMenu,QPushButton#btnMenu_Min,QPushButton#btnMenu_Max,QPushButton#btnMenu_Close{
        border-radius:3px;
        color:#386487;
        padding:3px;
        margin:0px;
        background:none;
        border-style:none;
        }
        
        QToolButton#btnMenu:hover,QPushButton#btnMenu_Min:hover,QPushButton#btnMenu_Max:hover{
        color:#FFFFFF;
        margin:1px 1px 2px 1px;
        background-color:rgba(51,127,209,230);
        }
        
        QPushButton#btnMenu_Close:hover{
        color:#FFFFFF;
        margin:1px 1px 2px 1px;
        background-color:rgba(238,0,0,128);
        }
        
        QRadioButton::indicator{
        width:15px;
        height:15px;
        }
        
        QRadioButton::indicator::unchecked{
        image:url(:/qss/lightblue/radiobutton_unchecked.png);
        }
        
        QRadioButton::indicator::unchecked:disabled{
        image:url(:/qss/lightblue/radiobutton_unchecked_disable.png);
        }
        
        QRadioButton::indicator::checked{
        image:url(:/qss/lightblue/radiobutton_checked.png);
        }
        
        QRadioButton::indicator::checked:disabled{
        image:url(:/qss/lightblue/radiobutton_checked_disable.png);
        }
        
        QGroupBox::indicator,QTreeWidget::indicator,QListWidget::indicator{
        padding:0px -3px 0px 3px;
        }
        
        QCheckBox::indicator,QGroupBox::indicator,QTreeWidget::indicator,QListWidget::indicator{
        width:13px;
        height:13px;
        }
        
        QCheckBox::indicator:unchecked,QGroupBox::indicator:unchecked,QTreeWidget::indicator:unchecked,QListWidget::indicator:unchecked{
        image:url(:/qss/lightblue/checkbox_unchecked.png);
        }
        
        QCheckBox::indicator:unchecked:disabled,QGroupBox::indicator:unchecked:disabled,QTreeWidget::indicator:unchecked:disabled,QListWidget::indicator:disabled{
        image:url(:/qss/lightblue/checkbox_unchecked_disable.png);
        }
        
        QCheckBox::indicator:checked,QGroupBox::indicator:checked,QTreeWidget::indicator:checked,QListWidget::indicator:checked{
        image:url(:/qss/lightblue/checkbox_checked.png);
        }
        
        QCheckBox::indicator:checked:disabled,QGroupBox::indicator:checked:disabled,QTreeWidget::indicator:checked:disabled,QListWidget::indicator:checked:disabled{
        image:url(:/qss/lightblue/checkbox_checked_disable.png);
        }
        
        QCheckBox::indicator:indeterminate,QGroupBox::indicator:indeterminate,QTreeWidget::indicator:indeterminate,QListWidget::indicator:indeterminate{
        image:url(:/qss/lightblue/checkbox_parcial.png);
        }
        
        QCheckBox::indicator:indeterminate:disabled,QGroupBox::indicator:indeterminate:disabled,QTreeWidget::indicator:indeterminate:disabled,QListWidget::indicator:indeterminate:disabled{
        image:url(:/qss/lightblue/checkbox_parcial_disable.png);
        }
        
        QTimeEdit::up-button,QDateEdit::up-button,QDateTimeEdit::up-button,QDoubleSpinBox::up-button,QSpinBox::up-button{
        image:url(:/qss/lightblue/add_top.png);
        width:10px;
        height:10px;
        padding:2px 5px 0px 0px;
        }
        
        QTimeEdit::down-button,QDateEdit::down-button,QDateTimeEdit::down-button,QDoubleSpinBox::down-button,QSpinBox::down-button{
        image:url(:/qss/lightblue/add_bottom.png);
        width:10px;
        height:10px;
        padding:0px 5px 2px 0px;
        }
        
        QTimeEdit::up-button:pressed,QDateEdit::up-button:pressed,QDateTimeEdit::up-button:pressed,QDoubleSpinBox::up-button:pressed,QSpinBox::up-button:pressed{
        top:-2px;
        }
          
        QTimeEdit::down-button:pressed,QDateEdit::down-button:pressed,QDateTimeEdit::down-button:pressed,QDoubleSpinBox::down-button:pressed,QSpinBox::down-button:pressed,QSpinBox::down-button:pressed{
        bottom:-2px;
        }
        
        QComboBox::down-arrow,QDateEdit[calendarPopup="true"]::down-arrow,QTimeEdit[calendarPopup="true"]::down-arrow,QDateTimeEdit[calendarPopup="true"]::down-arrow{
        image:url(:/qss/lightblue/add_bottom.png);
        width:10px;
        height:10px;
        right:2px;
        }
        
        QComboBox::drop-down,QDateEdit::drop-down,QTimeEdit::drop-down,QDateTimeEdit::drop-down{
        subcontrol-origin:padding;
        subcontrol-position:top right;
        width:15px;
        border-left-width:0px;
        border-left-style:solid;
        border-top-right-radius:3px;
        border-bottom-right-radius:3px;
        border-left-color:#C0DCF2;
        }
        
        QComboBox::drop-down:on{
        top:1px;
        }
        
        QMenuBar::item{
        color:#386487;
        background-color:#DEF0FE;
        margin:0px;
        padding:3px 10px;
        }
        
        QMenu,QMenuBar,QMenu:disabled,QMenuBar:disabled{
        color:#386487;
        background-color:#DEF0FE;
        border:1px solid #C0DCF2;
        margin:0px;
        }
        
        QMenu::item{
        padding:3px 20px;
        }
        
        QMenu::indicator{
        width:13px;
        height:13px;
        }
        
        QMenu::item:selected,QMenuBar::item:selected{
        color:#386487;
        border:0px solid #C0DCF2;
        background:#F2F9FF;
        }
        
        QMenu::separator{
        height:1px;
        background:#C0DCF2;
        }
        
        QProgressBar{
        min-height:10px;
        background:#DEF0FE;
        border-radius:5px;
        text-align:center;
        border:1px solid #DEF0FE;
        }
        
        QProgressBar:chunk{
        border-radius:5px;
        background-color:#C0DCF2;
        }
        
        QSlider::groove:horizontal{
        background:#DEF0FE;
        height:8px;
        border-radius:4px;
        }
        
        QSlider::add-page:horizontal{
        background:#DEF0FE;
        height:8px;
        border-radius:4px;
        }
        
        QSlider::sub-page:horizontal{
        background:#C0DCF2;
        height:8px;
        border-radius:4px;
        }
        
        QSlider::handle:horizontal{
        width:13px;
        margin-top:-3px;
        margin-bottom:-3px;
        border-radius:6px;
        background:qradialgradient(spread:pad,cx:0.5,cy:0.5,radius:0.5,fx:0.5,fy:0.5,stop:0.6 #EAF7FF,stop:0.8 #C0DCF2);
        }
        
        QSlider::groove:vertical{
        width:8px;
        border-radius:4px;
        background:#DEF0FE;
        }
        
        QSlider::add-page:vertical{
        width:8px;
        border-radius:4px;
        background:#DEF0FE;
        }
        
        QSlider::sub-page:vertical{
        width:8px;
        border-radius:4px;
        background:#C0DCF2;
        }
        
        QSlider::handle:vertical{
        height:14px;
        margin-left:-3px;
        margin-right:-3px;
        border-radius:6px;
        background:qradialgradient(spread:pad,cx:0.5,cy:0.5,radius:0.5,fx:0.5,fy:0.5,stop:0.6 #EAF7FF,stop:0.8 #C0DCF2);
        }
        
        QScrollBar:horizontal{
        background:#DEF0FE;
        padding:0px;
        border-radius:6px;
        max-height:12px;
        }
        
        QScrollBar::handle:horizontal{
        background:#DAEFFF;
        min-width:50px;
        border-radius:6px;
        }
        
        QScrollBar::handle:horizontal:hover{
        background:#C0DCF2;
        }
        
        QScrollBar::handle:horizontal:pressed{
        background:#C0DCF2;
        }
        
        QScrollBar::add-page:horizontal{
        background:none;
        }
        
        QScrollBar::sub-page:horizontal{
        background:none;
        }
        
        QScrollBar::add-line:horizontal{
        background:none;
        }
        
        QScrollBar::sub-line:horizontal{
        background:none;
        }
        
        QScrollBar:vertical{
        background:#DEF0FE;
        padding:0px;
        border-radius:6px;
        max-width:12px;
        }
        
        QScrollBar::handle:vertical{
        background:#DAEFFF;
        min-height:50px;
        border-radius:6px;
        }
        
        QScrollBar::handle:vertical:hover{
        background:#C0DCF2;
        }
        
        QScrollBar::handle:vertical:pressed{
        background:#C0DCF2;
        }
        
        QScrollBar::add-page:vertical{
        background:none;
        }
        
        QScrollBar::sub-page:vertical{
        background:none;
        }
        
        QScrollBar::add-line:vertical{
        background:none;
        }
        
        QScrollBar::sub-line:vertical{
        background:none;
        }
        
        QScrollArea{
        border:0px;
        }
        
        QTreeView,QListView,QTableView,QTabWidget::pane{
        border:1px solid #C0DCF2;
        selection-background-color:#F2F9FF;
        selection-color:#386487;
        alternate-background-color:#DAEFFF;
        gridline-color:#C0DCF2;
        }
        
        QTreeView::branch:closed:has-children{
        margin:4px;
        border-image:url(:/qss/lightblue/branch_open.png);
        }
        
        QTreeView::branch:open:has-children{
        margin:4px;
        border-image:url(:/qss/lightblue/branch_close.png);
        }
        
        QTreeView,QListView,QTableView,QSplitter::handle,QTreeView::branch{
        background:#EAF7FF;
        }
        
        QTableView::item:selected,QListView::item:selected,QTreeView::item:selected{
        color:#386487;
        background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #DEF0FE,stop:1 #C0DEF6);
        }
        
        QTableView::item:hover,QListView::item:hover,QTreeView::item:hover{
        color:#386487;
        background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #F2F9FF,stop:1 #DAEFFF);
        }
        
        QTableView::item,QListView::item,QTreeView::item{
        padding:1px;
        margin:0px;
        }
        
        QHeaderView::section,QTableCornerButton:section{
        padding:3px;
        margin:0px;
        color:#386487;
        border:1px solid #C0DCF2;
        border-left-width:0px;
        border-right-width:1px;
        border-top-width:0px;
        border-bottom-width:1px;
        background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #F2F9FF,stop:1 #DAEFFF);
        }
        
        QTabBar::tab{
        border:1px solid #C0DCF2;
        color:#386487;
        margin:0px;
        background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #F2F9FF,stop:1 #DAEFFF);
        }
        
        QTabBar::tab:selected,QTabBar::tab:hover{
        border-style:solid;
        border-color:#00BB9E;
        background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #DEF0FE,stop:1 #C0DEF6);
        }
        
        QTabBar::tab:top,QTabBar::tab:bottom{
        padding:3px 8px 3px 8px;
        }
        
        QTabBar::tab:left,QTabBar::tab:right{
        padding:8px 3px 8px 3px;
        }
        
        QTabBar::tab:top:selected,QTabBar::tab:top:hover{
        border-width:2px 0px 0px 0px;
        }
        
        QTabBar::tab:right:selected,QTabBar::tab:right:hover{
        border-width:0px 0px 0px 2px;
        }
        
        QTabBar::tab:bottom:selected,QTabBar::tab:bottom:hover{
        border-width:0px 0px 2px 0px;
        }
        
        QTabBar::tab:left:selected,QTabBar::tab:left:hover{
        border-width:0px 2px 0px 0px;
        }
        
        QTabBar::tab:first:top:selected,QTabBar::tab:first:top:hover,QTabBar::tab:first:bottom:selected,QTabBar::tab:first:bottom:hover{
        border-left-width:1px;
        border-left-color:#C0DCF2;
        }
        
        QTabBar::tab:first:left:selected,QTabBar::tab:first:left:hover,QTabBar::tab:first:right:selected,QTabBar::tab:first:right:hover{
        border-top-width:1px;
        border-top-color:#C0DCF2;
        }
        
        QTabBar::tab:last:top:selected,QTabBar::tab:last:top:hover,QTabBar::tab:last:bottom:selected,QTabBar::tab:last:bottom:hover{
        border-right-width:1px;
        border-right-color:#C0DCF2;
        }
        
        QTabBar::tab:last:left:selected,QTabBar::tab:last:left:hover,QTabBar::tab:last:right:selected,QTabBar::tab:last:right:hover{
        border-bottom-width:1px;
        border-bottom-color:#C0DCF2;
        }
        
        QStatusBar::item{
        border:0px solid #DEF0FE;
        border-radius:3px;
        }
        
        QToolBox::tab,QGroupBox#gboxDevicePanel,QGroupBox#gboxDeviceTitle,QFrame#gboxDevicePanel,QFrame#gboxDeviceTitle{
        padding:3px;
        border-radius:5px;
        color:#386487;
        background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #DEF0FE,stop:1 #C0DEF6);
        }
        
        QToolTip{
        border:0px solid #386487;
        padding:1px;
        color:#386487;
        background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #DEF0FE,stop:1 #C0DEF6);
        }
        
        QToolBox::tab:selected{
        background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #F2F9FF,stop:1 #DAEFFF);
        }
        
        QPrintPreviewDialog QToolButton{
        border:0px solid #386487;
        border-radius:0px;
        margin:0px;
        padding:3px;
        background:none;
        }
        
        QColorDialog QPushButton,QFileDialog QPushButton{
        min-width:80px;
        }
        
        QToolButton#qt_calendar_prevmonth{
        icon-size:0px;
        min-width:20px;
        image:url(:/qss/lightblue/calendar_prevmonth.png);
        }
        
        QToolButton#qt_calendar_nextmonth{
        icon-size:0px;
        min-width:20px;
        image:url(:/qss/lightblue/calendar_nextmonth.png);
        }
        
        QToolButton#qt_calendar_prevmonth,QToolButton#qt_calendar_nextmonth,QToolButton#qt_calendar_monthbutton,QToolButton#qt_calendar_yearbutton{
        border:0px solid #386487;
        border-radius:3px;
        margin:3px 3px 3px 3px;
        padding:3px;
        background:none;
        }
        
        QToolButton#qt_calendar_prevmonth:hover,QToolButton#qt_calendar_nextmonth:hover,QToolButton#qt_calendar_monthbutton:hover,QToolButton#qt_calendar_yearbutton:hover,QToolButton#qt_calendar_prevmonth:pressed,QToolButton#qt_calendar_nextmonth:pressed,QToolButton#qt_calendar_monthbutton:pressed,QToolButton#qt_calendar_yearbutton:pressed{
        border:1px solid #C0DCF2;
        }
        
        QCalendarWidget QSpinBox#qt_calendar_yearedit{
        margin:2px;
        }
        
        QCalendarWidget QToolButton::menu-indicator{
        image:None;
        }
        
        QCalendarWidget QTableView{
        border-width:0px;
        }
        
        QCalendarWidget QWidget#qt_calendar_navigationbar{
        border:1px solid #C0DCF2;
        border-width:1px 1px 0px 1px;
        background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #DEF0FE,stop:1 #C0DEF6);
        }
        
        QComboBox QAbstractItemView::item{
        min-height:20px;
        min-width:10px;
        }
        
        QTableView[model="true"]::item{
        padding:0px;
        margin:0px;
        }
        
        QTableView QLineEdit,QTableView QComboBox,QTableView QSpinBox,QTableView QDoubleSpinBox,QTableView QDateEdit,QTableView QTimeEdit,QTableView QDateTimeEdit{
        border-width:0px;
        border-radius:0px;
        }
        
        QTableView QLineEdit:focus,QTableView QComboBox:focus,QTableView QSpinBox:focus,QTableView QDoubleSpinBox:focus,QTableView QDateEdit:focus,QTableView QTimeEdit:focus,QTableView QDateTimeEdit:focus{
        border-width:0px;
        border-radius:0px;
        }
        
        QLineEdit,QTextEdit,QPlainTextEdit,QSpinBox,QDoubleSpinBox,QComboBox,QDateEdit,QTimeEdit,QDateTimeEdit{
        background:#EAF7FF;
        }
        
        *:disabled{
        background:#EAF7FF;
        border-color:#DEF0FE;
        }
        
        /*TextColor:#386487*/
        /*PanelColor:#EAF7FF*/
        /*BorderColor:#C0DCF2*/
        /*NormalColorStart:#DEF0FE*/
        /*NormalColorEnd:#C0DEF6*/
        /*DarkColorStart:#F2F9FF*/
        /*DarkColorEnd:#DAEFFF*/
        /*HighColor:#00BB9E*/
                '''
        return qss


class LightBlack(object):
    @classmethod
    def get_qss(cls):
        qss = '''
        QPalette{background:#616F76;}*{outline:0px;color:#E7ECF0;}
        
        QWidget[form="true"],QLabel[frameShape="1"]{
        border:1px solid #738393;
        border-radius:0px;
        }
        
        QWidget[form="bottom"]{
        background:#667481;
        }
        
        QWidget[form="bottom"] .QFrame{
        border:1px solid #E7ECF0;
        }
        
        QWidget[form="bottom"] QLabel,QWidget[form="title"] QLabel{
        border-radius:0px;
        color:#E7ECF0;
        background:none;
        border-style:none;
        }
        
        QWidget[form="title"],QWidget[nav="left"],QWidget[nav="top"] QAbstractButton{
        border-style:none;
        border-radius:0px;
        padding:5px;
        color:#E7ECF0;
        background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #667481,stop:1 #566373);
        }
        
        QWidget[nav="top"] QAbstractButton:hover,QWidget[nav="top"] QAbstractButton:pressed,QWidget[nav="top"] QAbstractButton:checked{
        border-style:solid;
        border-width:0px 0px 2px 0px;
        padding:4px 4px 2px 4px;
        border-color:#00BB9E;
        background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #778899,stop:1 #708090);
        }
        
        QWidget[nav="left"] QAbstractButton{
        border-radius:0px;
        color:#E7ECF0;
        background:none;
        border-style:none;
        }
        
        QWidget[nav="left"] QAbstractButton:hover{
        color:#FFFFFF;
        background-color:#00BB9E;
        }
        
        QWidget[nav="left"] QAbstractButton:checked,QWidget[nav="left"] QAbstractButton:pressed{
        color:#E7ECF0;
        border-style:solid;
        border-width:0px 0px 0px 2px;
        padding:4px 4px 4px 2px;
        border-color:#00BB9E;
        background-color:#616F76;
        }
        
        QWidget[video="true"] QLabel{
        color:#E7ECF0;
        border:1px solid #738393;
        background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #667481,stop:1 #566373);
        }
        
        QWidget[video="true"] QLabel:focus{
        border:1px solid #00BB9E;
        background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #778899,stop:1 #708090);
        }
        
        QLineEdit,QTextEdit,QPlainTextEdit,QSpinBox,QDoubleSpinBox,QComboBox,QDateEdit,QTimeEdit,QDateTimeEdit{
        border:1px solid #738393;
        border-radius:3px;
        padding:2px;
        background:none;
        selection-background-color:#667481;
        selection-color:#E7ECF0;
        }
        
        QLineEdit:focus,QTextEdit:focus,QPlainTextEdit:focus,QSpinBox:focus,QDoubleSpinBox:focus,QComboBox:focus,QDateEdit:focus,QTimeEdit:focus,QDateTimeEdit:focus,QLineEdit:hover,QTextEdit:hover,QPlainTextEdit:hover,QSpinBox:hover,QDoubleSpinBox:hover,QComboBox:hover,QDateEdit:hover,QTimeEdit:hover,QDateTimeEdit:hover{
        border:1px solid #738393;
        }
        
        QLineEdit[echoMode="2"]{
        lineedit-password-character:9679;
        }
        
        .QFrame{
        border:1px solid #738393;
        border-radius:3px;
        }
        
        .QGroupBox{
        border:1px solid #738393;
        border-radius:5px;
        margin-top:3ex;
        }
        
        .QGroupBox::title{
        subcontrol-origin:margin;
        position:relative;
        left:10px;
        }
        
        .QPushButton,.QToolButton{
        border-style:none;
        border:1px solid #738393;
        color:#E7ECF0;
        padding:5px;
        min-height:15px;
        border-radius:5px;
        background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #667481,stop:1 #566373);
        }
        
        .QPushButton:hover,.QToolButton:hover{
        background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #778899,stop:1 #708090);
        }
        
        .QPushButton:pressed,.QToolButton:pressed{
        background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #667481,stop:1 #566373);
        }
        
        .QToolButton::menu-indicator{
        image:None;
        }
        
        QToolButton#btnMenu,QPushButton#btnMenu_Min,QPushButton#btnMenu_Max,QPushButton#btnMenu_Close{
        border-radius:3px;
        color:#E7ECF0;
        padding:3px;
        margin:0px;
        background:none;
        border-style:none;
        }
        
        QToolButton#btnMenu:hover,QPushButton#btnMenu_Min:hover,QPushButton#btnMenu_Max:hover{
        color:#FFFFFF;
        margin:1px 1px 2px 1px;
        background-color:rgba(51,127,209,230);
        }
        
        QPushButton#btnMenu_Close:hover{
        color:#FFFFFF;
        margin:1px 1px 2px 1px;
        background-color:rgba(238,0,0,128);
        }
        
        QRadioButton::indicator{
        width:15px;
        height:15px;
        }
        
        QRadioButton::indicator::unchecked{
        image:url(:/qss/lightblack/radiobutton_unchecked.png);
        }
        
        QRadioButton::indicator::unchecked:disabled{
        image:url(:/qss/lightblack/radiobutton_unchecked_disable.png);
        }
        
        QRadioButton::indicator::checked{
        image:url(:/qss/lightblack/radiobutton_checked.png);
        }
        
        QRadioButton::indicator::checked:disabled{
        image:url(:/qss/lightblack/radiobutton_checked_disable.png);
        }
        
        QGroupBox::indicator,QTreeWidget::indicator,QListWidget::indicator{
        padding:0px -3px 0px 3px;
        }
        
        QCheckBox::indicator,QGroupBox::indicator,QTreeWidget::indicator,QListWidget::indicator{
        width:13px;
        height:13px;
        }
        
        QCheckBox::indicator:unchecked,QGroupBox::indicator:unchecked,QTreeWidget::indicator:unchecked,QListWidget::indicator:unchecked{
        image:url(:/qss/lightblack/checkbox_unchecked.png);
        }
        
        QCheckBox::indicator:unchecked:disabled,QGroupBox::indicator:unchecked:disabled,QTreeWidget::indicator:unchecked:disabled,QListWidget::indicator:disabled{
        image:url(:/qss/lightblack/checkbox_unchecked_disable.png);
        }
        
        QCheckBox::indicator:checked,QGroupBox::indicator:checked,QTreeWidget::indicator:checked,QListWidget::indicator:checked{
        image:url(:/qss/lightblack/checkbox_checked.png);
        }
        
        QCheckBox::indicator:checked:disabled,QGroupBox::indicator:checked:disabled,QTreeWidget::indicator:checked:disabled,QListWidget::indicator:checked:disabled{
        image:url(:/qss/lightblack/checkbox_checked_disable.png);
        }
        
        QCheckBox::indicator:indeterminate,QGroupBox::indicator:indeterminate,QTreeWidget::indicator:indeterminate,QListWidget::indicator:indeterminate{
        image:url(:/qss/lightblack/checkbox_parcial.png);
        }
        
        QCheckBox::indicator:indeterminate:disabled,QGroupBox::indicator:indeterminate:disabled,QTreeWidget::indicator:indeterminate:disabled,QListWidget::indicator:indeterminate:disabled{
        image:url(:/qss/lightblack/checkbox_parcial_disable.png);
        }
        
        QTimeEdit::up-button,QDateEdit::up-button,QDateTimeEdit::up-button,QDoubleSpinBox::up-button,QSpinBox::up-button{
        image:url(:/qss/lightblack/add_top.png);
        width:10px;
        height:10px;
        padding:2px 5px 0px 0px;
        }
        
        QTimeEdit::down-button,QDateEdit::down-button,QDateTimeEdit::down-button,QDoubleSpinBox::down-button,QSpinBox::down-button{
        image:url(:/qss/lightblack/add_bottom.png);
        width:10px;
        height:10px;
        padding:0px 5px 2px 0px;
        }
        
        QTimeEdit::up-button:pressed,QDateEdit::up-button:pressed,QDateTimeEdit::up-button:pressed,QDoubleSpinBox::up-button:pressed,QSpinBox::up-button:pressed{
        top:-2px;
        }
          
        QTimeEdit::down-button:pressed,QDateEdit::down-button:pressed,QDateTimeEdit::down-button:pressed,QDoubleSpinBox::down-button:pressed,QSpinBox::down-button:pressed,QSpinBox::down-button:pressed{
        bottom:-2px;
        }
        
        QComboBox::down-arrow,QDateEdit[calendarPopup="true"]::down-arrow,QTimeEdit[calendarPopup="true"]::down-arrow,QDateTimeEdit[calendarPopup="true"]::down-arrow{
        image:url(:/qss/lightblack/add_bottom.png);
        width:10px;
        height:10px;
        right:2px;
        }
        
        QComboBox::drop-down,QDateEdit::drop-down,QTimeEdit::drop-down,QDateTimeEdit::drop-down{
        subcontrol-origin:padding;
        subcontrol-position:top right;
        width:15px;
        border-left-width:0px;
        border-left-style:solid;
        border-top-right-radius:3px;
        border-bottom-right-radius:3px;
        border-left-color:#738393;
        }
        
        QComboBox::drop-down:on{
        top:1px;
        }
        
        QMenuBar::item{
        color:#E7ECF0;
        background-color:#667481;
        margin:0px;
        padding:3px 10px;
        }
        
        QMenu,QMenuBar,QMenu:disabled,QMenuBar:disabled{
        color:#E7ECF0;
        background-color:#667481;
        border:1px solid #738393;
        margin:0px;
        }
        
        QMenu::item{
        padding:3px 20px;
        }
        
        QMenu::indicator{
        width:13px;
        height:13px;
        }
        
        QMenu::item:selected,QMenuBar::item:selected{
        color:#E7ECF0;
        border:0px solid #738393;
        background:#778899;
        }
        
        QMenu::separator{
        height:1px;
        background:#738393;
        }
        
        QProgressBar{
        min-height:10px;
        background:#667481;
        border-radius:5px;
        text-align:center;
        border:1px solid #667481;
        }
        
        QProgressBar:chunk{
        border-radius:5px;
        background-color:#738393;
        }
        
        QSlider::groove:horizontal{
        background:#667481;
        height:8px;
        border-radius:4px;
        }
        
        QSlider::add-page:horizontal{
        background:#667481;
        height:8px;
        border-radius:4px;
        }
        
        QSlider::sub-page:horizontal{
        background:#738393;
        height:8px;
        border-radius:4px;
        }
        
        QSlider::handle:horizontal{
        width:13px;
        margin-top:-3px;
        margin-bottom:-3px;
        border-radius:6px;
        background:qradialgradient(spread:pad,cx:0.5,cy:0.5,radius:0.5,fx:0.5,fy:0.5,stop:0.6 #616F76,stop:0.8 #738393);
        }
        
        QSlider::groove:vertical{
        width:8px;
        border-radius:4px;
        background:#667481;
        }
        
        QSlider::add-page:vertical{
        width:8px;
        border-radius:4px;
        background:#667481;
        }
        
        QSlider::sub-page:vertical{
        width:8px;
        border-radius:4px;
        background:#738393;
        }
        
        QSlider::handle:vertical{
        height:14px;
        margin-left:-3px;
        margin-right:-3px;
        border-radius:6px;
        background:qradialgradient(spread:pad,cx:0.5,cy:0.5,radius:0.5,fx:0.5,fy:0.5,stop:0.6 #616F76,stop:0.8 #738393);
        }
        
        QScrollBar:horizontal{
        background:#667481;
        padding:0px;
        border-radius:6px;
        max-height:12px;
        }
        
        QScrollBar::handle:horizontal{
        background:#708090;
        min-width:50px;
        border-radius:6px;
        }
        
        QScrollBar::handle:horizontal:hover{
        background:#738393;
        }
        
        QScrollBar::handle:horizontal:pressed{
        background:#738393;
        }
        
        QScrollBar::add-page:horizontal{
        background:none;
        }
        
        QScrollBar::sub-page:horizontal{
        background:none;
        }
        
        QScrollBar::add-line:horizontal{
        background:none;
        }
        
        QScrollBar::sub-line:horizontal{
        background:none;
        }
        
        QScrollBar:vertical{
        background:#667481;
        padding:0px;
        border-radius:6px;
        max-width:12px;
        }
        
        QScrollBar::handle:vertical{
        background:#708090;
        min-height:50px;
        border-radius:6px;
        }
        
        QScrollBar::handle:vertical:hover{
        background:#738393;
        }
        
        QScrollBar::handle:vertical:pressed{
        background:#738393;
        }
        
        QScrollBar::add-page:vertical{
        background:none;
        }
        
        QScrollBar::sub-page:vertical{
        background:none;
        }
        
        QScrollBar::add-line:vertical{
        background:none;
        }
        
        QScrollBar::sub-line:vertical{
        background:none;
        }
        
        QScrollArea{
        border:0px;
        }
        
        QTreeView,QListView,QTableView,QTabWidget::pane{
        border:1px solid #738393;
        selection-background-color:#778899;
        selection-color:#E7ECF0;
        alternate-background-color:#708090;
        gridline-color:#738393;
        }
        
        QTreeView::branch:closed:has-children{
        margin:4px;
        border-image:url(:/qss/lightblack/branch_open.png);
        }
        
        QTreeView::branch:open:has-children{
        margin:4px;
        border-image:url(:/qss/lightblack/branch_close.png);
        }
        
        QTreeView,QListView,QTableView,QSplitter::handle,QTreeView::branch{
        background:#616F76;
        }
        
        QTableView::item:selected,QListView::item:selected,QTreeView::item:selected{
        color:#E7ECF0;
        background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #667481,stop:1 #566373);
        }
        
        QTableView::item:hover,QListView::item:hover,QTreeView::item:hover{
        color:#E7ECF0;
        background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #778899,stop:1 #708090);
        }
        
        QTableView::item,QListView::item,QTreeView::item{
        padding:1px;
        margin:0px;
        }
        
        QHeaderView::section,QTableCornerButton:section{
        padding:3px;
        margin:0px;
        color:#E7ECF0;
        border:1px solid #738393;
        border-left-width:0px;
        border-right-width:1px;
        border-top-width:0px;
        border-bottom-width:1px;
        background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #778899,stop:1 #708090);
        }
        
        QTabBar::tab{
        border:1px solid #738393;
        color:#E7ECF0;
        margin:0px;
        background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #778899,stop:1 #708090);
        }
        
        QTabBar::tab:selected,QTabBar::tab:hover{
        border-style:solid;
        border-color:#00BB9E;
        background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #667481,stop:1 #566373);
        }
        
        QTabBar::tab:top,QTabBar::tab:bottom{
        padding:3px 8px 3px 8px;
        }
        
        QTabBar::tab:left,QTabBar::tab:right{
        padding:8px 3px 8px 3px;
        }
        
        QTabBar::tab:top:selected,QTabBar::tab:top:hover{
        border-width:2px 0px 0px 0px;
        }
        
        QTabBar::tab:right:selected,QTabBar::tab:right:hover{
        border-width:0px 0px 0px 2px;
        }
        
        QTabBar::tab:bottom:selected,QTabBar::tab:bottom:hover{
        border-width:0px 0px 2px 0px;
        }
        
        QTabBar::tab:left:selected,QTabBar::tab:left:hover{
        border-width:0px 2px 0px 0px;
        }
        
        QTabBar::tab:first:top:selected,QTabBar::tab:first:top:hover,QTabBar::tab:first:bottom:selected,QTabBar::tab:first:bottom:hover{
        border-left-width:1px;
        border-left-color:#738393;
        }
        
        QTabBar::tab:first:left:selected,QTabBar::tab:first:left:hover,QTabBar::tab:first:right:selected,QTabBar::tab:first:right:hover{
        border-top-width:1px;
        border-top-color:#738393;
        }
        
        QTabBar::tab:last:top:selected,QTabBar::tab:last:top:hover,QTabBar::tab:last:bottom:selected,QTabBar::tab:last:bottom:hover{
        border-right-width:1px;
        border-right-color:#738393;
        }
        
        QTabBar::tab:last:left:selected,QTabBar::tab:last:left:hover,QTabBar::tab:last:right:selected,QTabBar::tab:last:right:hover{
        border-bottom-width:1px;
        border-bottom-color:#738393;
        }
        
        QStatusBar::item{
        border:0px solid #667481;
        border-radius:3px;
        }
        
        QToolBox::tab,QGroupBox#gboxDevicePanel,QGroupBox#gboxDeviceTitle,QFrame#gboxDevicePanel,QFrame#gboxDeviceTitle{
        padding:3px;
        border-radius:5px;
        color:#E7ECF0;
        background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #667481,stop:1 #566373);
        }
        
        QToolTip{
        border:0px solid #E7ECF0;
        padding:1px;
        color:#E7ECF0;
        background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #667481,stop:1 #566373);
        }
        
        QToolBox::tab:selected{
        background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #778899,stop:1 #708090);
        }
        
        QPrintPreviewDialog QToolButton{
        border:0px solid #E7ECF0;
        border-radius:0px;
        margin:0px;
        padding:3px;
        background:none;
        }
        
        QColorDialog QPushButton,QFileDialog QPushButton{
        min-width:80px;
        }
        
        QToolButton#qt_calendar_prevmonth{
        icon-size:0px;
        min-width:20px;
        image:url(:/qss/lightblack/calendar_prevmonth.png);
        }
        
        QToolButton#qt_calendar_nextmonth{
        icon-size:0px;
        min-width:20px;
        image:url(:/qss/lightblack/calendar_nextmonth.png);
        }
        
        QToolButton#qt_calendar_prevmonth,QToolButton#qt_calendar_nextmonth,QToolButton#qt_calendar_monthbutton,QToolButton#qt_calendar_yearbutton{
        border:0px solid #E7ECF0;
        border-radius:3px;
        margin:3px 3px 3px 3px;
        padding:3px;
        background:none;
        }
        
        QToolButton#qt_calendar_prevmonth:hover,QToolButton#qt_calendar_nextmonth:hover,QToolButton#qt_calendar_monthbutton:hover,QToolButton#qt_calendar_yearbutton:hover,QToolButton#qt_calendar_prevmonth:pressed,QToolButton#qt_calendar_nextmonth:pressed,QToolButton#qt_calendar_monthbutton:pressed,QToolButton#qt_calendar_yearbutton:pressed{
        border:1px solid #738393;
        }
        
        QCalendarWidget QSpinBox#qt_calendar_yearedit{
        margin:2px;
        }
        
        QCalendarWidget QToolButton::menu-indicator{
        image:None;
        }
        
        QCalendarWidget QTableView{
        border-width:0px;
        }
        
        QCalendarWidget QWidget#qt_calendar_navigationbar{
        border:1px solid #738393;
        border-width:1px 1px 0px 1px;
        background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #667481,stop:1 #566373);
        }
        
        QComboBox QAbstractItemView::item{
        min-height:20px;
        min-width:10px;
        }
        
        QTableView[model="true"]::item{
        padding:0px;
        margin:0px;
        }
        
        QTableView QLineEdit,QTableView QComboBox,QTableView QSpinBox,QTableView QDoubleSpinBox,QTableView QDateEdit,QTableView QTimeEdit,QTableView QDateTimeEdit{
        border-width:0px;
        border-radius:0px;
        }
        
        QTableView QLineEdit:focus,QTableView QComboBox:focus,QTableView QSpinBox:focus,QTableView QDoubleSpinBox:focus,QTableView QDateEdit:focus,QTableView QTimeEdit:focus,QTableView QDateTimeEdit:focus{
        border-width:0px;
        border-radius:0px;
        }
        
        QLineEdit,QTextEdit,QPlainTextEdit,QSpinBox,QDoubleSpinBox,QComboBox,QDateEdit,QTimeEdit,QDateTimeEdit{
        background:#616F76;
        }
        
        *:disabled{
        background:#616F76;
        border-color:#667481;
        }
        
        /*TextColor:#E7ECF0*/
        /*PanelColor:#616F76*/
        /*BorderColor:#738393*/
        /*NormalColorStart:#667481*/
        /*NormalColorEnd:#566373*/
        /*DarkColorStart:#778899*/
        /*DarkColorEnd:#708090*/
        /*HighColor:#00BB9E*/
                '''
        return qss
