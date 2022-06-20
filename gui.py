# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QLayout, QLineEdit, QPushButton, QSizePolicy,
    QTextBrowser, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(834, 370)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMaximumSize(QSize(834, 370))
        self.verticalLayout_4 = QVBoxLayout(Dialog)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetFixedSize)
        self.lbl_ip_address = QLabel(Dialog)
        self.lbl_ip_address.setObjectName(u"lbl_ip_address")
        sizePolicy.setHeightForWidth(self.lbl_ip_address.sizePolicy().hasHeightForWidth())
        self.lbl_ip_address.setSizePolicy(sizePolicy)
        self.lbl_ip_address.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.lbl_ip_address)

        self.ip_address_txt = QLineEdit(Dialog)
        self.ip_address_txt.setObjectName(u"ip_address_txt")
        sizePolicy.setHeightForWidth(self.ip_address_txt.sizePolicy().hasHeightForWidth())
        self.ip_address_txt.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.ip_address_txt)

        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.label)

        self.start_port_txt = QLineEdit(Dialog)
        self.start_port_txt.setObjectName(u"start_port_txt")
        sizePolicy.setHeightForWidth(self.start_port_txt.sizePolicy().hasHeightForWidth())
        self.start_port_txt.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.start_port_txt)

        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.label_2)

        self.end_port_txt = QLineEdit(Dialog)
        self.end_port_txt.setObjectName(u"end_port_txt")
        sizePolicy.setHeightForWidth(self.end_port_txt.sizePolicy().hasHeightForWidth())
        self.end_port_txt.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.end_port_txt)

        self.btn_scan = QPushButton(Dialog)
        self.btn_scan.setObjectName(u"btn_scan")
        sizePolicy.setHeightForWidth(self.btn_scan.sizePolicy().hasHeightForWidth())
        self.btn_scan.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.btn_scan)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.textBrowser = QTextBrowser(Dialog)
        self.textBrowser.setObjectName(u"textBrowser")

        self.verticalLayout_3.addWidget(self.textBrowser)


        self.verticalLayout_2.addLayout(self.verticalLayout_3)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Port Scanner", None))
        self.lbl_ip_address.setText(QCoreApplication.translate("Dialog", u"IP Address", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Ports", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"TO", None))
        self.btn_scan.setText(QCoreApplication.translate("Dialog", u"Scan", None))
    # retranslateUi

