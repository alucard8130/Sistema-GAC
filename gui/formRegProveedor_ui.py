# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'formRegProveedor.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QTextEdit, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.setWindowModality(Qt.WindowModality.ApplicationModal)
        Dialog.resize(590, 506)
        Dialog.setModal(True)
        self.btnRegistrar = QPushButton(Dialog)
        self.btnRegistrar.setObjectName(u"btnRegistrar")
        self.btnRegistrar.setGeometry(QRect(20, 450, 150, 40))
        font = QFont()
        font.setFamilies([u"Comic Sans MS"])
        font.setPointSize(12)
        self.btnRegistrar.setFont(font)
        self.btnRegistrar.setStyleSheet(u"background-color: rgb(8, 19, 95);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:5px;")
        icon = QIcon()
        icon.addFile(u"../iconos/guardar.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnRegistrar.setIcon(icon)
        self.btnRegistrar.setIconSize(QSize(40, 40))
        self.btnSalir = QPushButton(Dialog)
        self.btnSalir.setObjectName(u"btnSalir")
        self.btnSalir.setGeometry(QRect(420, 450, 150, 40))
        font1 = QFont()
        font1.setFamilies([u"Comic Sans MS"])
        font1.setPointSize(14)
        font1.setBold(False)
        self.btnSalir.setFont(font1)
        self.btnSalir.setStyleSheet(u"background-color: rgb(8, 19, 95);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:5px;")
        icon1 = QIcon()
        icon1.addFile(u"../iconos/salir.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnSalir.setIcon(icon1)
        self.btnSalir.setIconSize(QSize(30, 30))
        self.frame_5 = QFrame(Dialog)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(0, 0, 881, 71))
        self.frame_5.setMaximumSize(QSize(16777215, 16777215))
        self.frame_5.setStyleSheet(u"background-color: rgb(8, 14, 91);")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.label_13 = QLabel(self.frame_5)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(0, 40, 832, 31))
        font2 = QFont()
        font2.setFamilies([u"Comic Sans MS"])
        font2.setPointSize(12)
        font2.setBold(True)
        self.label_13.setFont(font2)
        self.label_13.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(19, 39, 113);\n"
"color: rgb(255, 78, 2);\n"
"color: rgb(216, 224, 236);")
        self.label_13.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(-10, 70, 601, 351))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.txtRFC = QTextEdit(self.frame)
        self.txtRFC.setObjectName(u"txtRFC")
        self.txtRFC.setGeometry(QRect(390, 40, 191, 30))
        self.txtRFC.setStyleSheet(u"border-radius:5px;")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 20, 141, 16))
        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 280, 91, 16))
        self.label_10 = QLabel(self.frame)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(390, 20, 71, 16))
        self.label_12 = QLabel(self.frame)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(280, 190, 71, 16))
        self.txtEmail = QLineEdit(self.frame)
        self.txtEmail.setObjectName(u"txtEmail")
        self.txtEmail.setGeometry(QRect(20, 300, 221, 30))
        self.txtEmail.setStyleSheet(u"border-radius:5px;")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(500, 0, 101, 16))
        font3 = QFont()
        font3.setFamilies([u"Comic Sans MS"])
        font3.setPointSize(7)
        font3.setBold(True)
        font3.setItalic(True)
        self.label_3.setFont(font3)
        self.label_3.setStyleSheet(u"color: rgb(85, 0, 0);")
        self.label_11 = QLabel(self.frame)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(20, 100, 111, 16))
        self.txtBanco = QLineEdit(self.frame)
        self.txtBanco.setObjectName(u"txtBanco")
        self.txtBanco.setGeometry(QRect(280, 210, 151, 30))
        self.txtBanco.setStyleSheet(u"border-radius:5px;")
        self.txtRazon_social = QLineEdit(self.frame)
        self.txtRazon_social.setObjectName(u"txtRazon_social")
        self.txtRazon_social.setGeometry(QRect(20, 40, 321, 30))
        self.txtRazon_social.setStyleSheet(u"border-radius:5px;")
        self.txtNombre_comercial = QLineEdit(self.frame)
        self.txtNombre_comercial.setObjectName(u"txtNombre_comercial")
        self.txtNombre_comercial.setGeometry(QRect(20, 120, 321, 30))
        self.txtNombre_comercial.setStyleSheet(u"border-radius:5px;")
        self.txtDireccion = QLineEdit(self.frame)
        self.txtDireccion.setObjectName(u"txtDireccion")
        self.txtDireccion.setGeometry(QRect(310, 280, 271, 61))
        self.txtDireccion.setStyleSheet(u"border-radius:5px;")
        self.label_15 = QLabel(self.frame)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(310, 260, 101, 16))
        self.label_16 = QLabel(self.frame)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(390, 100, 71, 16))
        self.txtCURP = QTextEdit(self.frame)
        self.txtCURP.setObjectName(u"txtCURP")
        self.txtCURP.setGeometry(QRect(390, 120, 191, 30))
        self.txtCURP.setStyleSheet(u"border-radius:5px;")
        self.cmbServicios = QComboBox(self.frame)
        self.cmbServicios.addItem("")
        self.cmbServicios.setObjectName(u"cmbServicios")
        self.cmbServicios.setGeometry(QRect(20, 210, 231, 30))
        self.cmbServicios.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:5px;")
        self.label_17 = QLabel(self.frame)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(20, 190, 101, 16))
        self.txtTelefono = QLineEdit(self.frame)
        self.txtTelefono.setObjectName(u"txtTelefono")
        self.txtTelefono.setGeometry(QRect(460, 210, 121, 30))
        self.txtTelefono.setStyleSheet(u"border-radius:5px;")
        self.label_19 = QLabel(self.frame)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(460, 190, 71, 16))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle("")
        self.btnRegistrar.setText(QCoreApplication.translate("Dialog", u"Guadar", None))
        self.btnSalir.setText(QCoreApplication.translate("Dialog", u"Salir", None))
        self.label_13.setText(QCoreApplication.translate("Dialog", u" REGISTRO PROVEEDORES", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Razon Social*", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Email*", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", u"RFC*", None))
        self.label_12.setText(QCoreApplication.translate("Dialog", u"Cta Banco*", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"* campos obligatorios", None))
        self.label_11.setText(QCoreApplication.translate("Dialog", u"Nombre Comercial", None))
        self.label_15.setText(QCoreApplication.translate("Dialog", u"Direccion*", None))
        self.label_16.setText(QCoreApplication.translate("Dialog", u"CURP", None))
        self.cmbServicios.setItemText(0, QCoreApplication.translate("Dialog", u"--selecciona una opcion--", None))

        self.label_17.setText(QCoreApplication.translate("Dialog", u"Tipo Servicio*", None))
        self.label_19.setText(QCoreApplication.translate("Dialog", u"Telefono*", None))
    # retranslateUi

