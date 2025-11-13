# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'window_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QHBoxLayout, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 200)
        self.formLayout = QFormLayout(Form)
        self.formLayout.setObjectName(u"formLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lineEditlogin = QLineEdit(Form)
        self.lineEditlogin.setObjectName(u"lineEditlogin")

        self.verticalLayout.addWidget(self.lineEditlogin)

        self.lineEditpassword = QLineEdit(Form)
        self.lineEditpassword.setObjectName(u"lineEditpassword")
        self.lineEditpassword.setEchoMode(QLineEdit.EchoMode.Password)

        self.verticalLayout.addWidget(self.lineEditpassword)


        self.formLayout.setLayout(0, QFormLayout.ItemRole.FieldRole, self.verticalLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButtonOK = QPushButton(Form)
        self.pushButtonOK.setObjectName(u"pushButtonOK")

        self.horizontalLayout.addWidget(self.pushButtonOK)

        self.pushButtonCancel = QPushButton(Form)
        self.pushButtonCancel.setObjectName(u"pushButtonCancel")

        self.horizontalLayout.addWidget(self.pushButtonCancel)


        self.formLayout.setLayout(2, QFormLayout.ItemRole.FieldRole, self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(10, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.formLayout.setItem(1, QFormLayout.ItemRole.FieldRole, self.verticalSpacer)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u0422\u0435\u0441\u0442\u043e\u0432\u0430\u044f \u0444\u043e\u0440\u043c\u0430", None))
        self.lineEditlogin.setPlaceholderText(QCoreApplication.translate("Form", u"\u0412\u0432\u0435\u0434\u0438 \u0412\u0430\u0448 \u043b\u043e\u0433\u0438\u043d:", None))
        self.lineEditpassword.setPlaceholderText(QCoreApplication.translate("Form", u"\u0412\u0432\u0435\u0435\u0434\u0438\u0442\u0435 \u0412\u0430\u0448 \u043f\u0430\u0440\u043e\u043b\u044c:", None))
        self.pushButtonOK.setText(QCoreApplication.translate("Form", u"OK", None))
        self.pushButtonCancel.setText(QCoreApplication.translate("Form", u"Cancel", None))
    # retranslateUi

