# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'screen1LvfHeC.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QWidget)
from . import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 800)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background image: url(:/parkinglot/test3.png)")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(-30, 10, 1280, 800))
        self.label.setStyleSheet(u"background-image: url(:/parkinglot/test3.png);\n"
"background-repeat: no-repeat;          /* \ubc18\ubcf5 \ubc29\uc9c0 */\n"
"background-position: center;           /* \uc911\uc559 \ubc30\uce58 */\n"
"border-image: url(:/parkinglot/test3.png) 0 0 0 0 stretch stretch;\n"
"")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(360, 330, 71, 61))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(530, 140, 351, 51))
        font = QFont()
        font.setPointSize(28)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setTextFormat(Qt.TextFormat.AutoText)
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(190, 340, 71, 61))
        self.pushButton_2.setAutoFillBackground(False)
        icon = QIcon()
        icon.addFile(u":/parkinglot/003.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QSize(100, 100))
        self.pushButton_2.setAutoExclusive(False)
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(150, 540, 71, 61))
        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(370, 540, 71, 61))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1280, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(MainWindow.next_screen)
        self.pushButton_2.clicked.connect(MainWindow.next_screen)
        self.pushButton_3.clicked.connect(MainWindow.next_screen)
        self.pushButton_4.clicked.connect(MainWindow.next_screen)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\uc804\uae30\ucc28", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\ub2c8 \ucc28 \ubb54\ub370?", None))
        self.pushButton_2.setText("")
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\uc7a5\uc560\uc778", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\uacbd\ucc28", None))
    # retranslateUi

