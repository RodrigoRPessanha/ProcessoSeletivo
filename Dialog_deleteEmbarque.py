# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Dialog-deleteEmbarque.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_RemoverEmbarque(object):
    def setupUi(self, RemoverEmbarque):
        RemoverEmbarque.setObjectName("RemoverEmbarque")
        RemoverEmbarque.resize(380, 150)
        self.clearButton = QtWidgets.QPushButton(RemoverEmbarque)
        self.clearButton.setGeometry(QtCore.QRect(150, 120, 80, 23))
        self.clearButton.setObjectName("clearButton")
        self.label_5 = QtWidgets.QLabel(RemoverEmbarque)
        self.label_5.setGeometry(QtCore.QRect(95, 10, 190, 41))
        self.label_5.setObjectName("label_5")
        self.submitButton = QtWidgets.QPushButton(RemoverEmbarque)
        self.submitButton.setGeometry(QtCore.QRect(240, 120, 80, 23))
        self.submitButton.setObjectName("submitButton")
        self.cancelButton = QtWidgets.QPushButton(RemoverEmbarque)
        self.cancelButton.setGeometry(QtCore.QRect(60, 120, 80, 23))
        self.cancelButton.setObjectName("cancelButton")
        self.gridLayoutWidget = QtWidgets.QWidget(RemoverEmbarque)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 60, 359, 51))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_4.addWidget(self.label_6)
        self.horizontalLayout_3.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.idArea = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.idArea.setFont(font)
        self.idArea.setObjectName("idArea")
        self.verticalLayout_5.addWidget(self.idArea)
        self.horizontalLayout_3.addLayout(self.verticalLayout_5)
        self.horizontalLayout_3.setStretch(0, 2)
        self.horizontalLayout_3.setStretch(1, 3)
        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)

        self.retranslateUi(RemoverEmbarque)
        QtCore.QMetaObject.connectSlotsByName(RemoverEmbarque)

    def retranslateUi(self, RemoverEmbarque):
        _translate = QtCore.QCoreApplication.translate
        RemoverEmbarque.setWindowTitle(_translate("RemoverEmbarque", "Dialog"))
        self.clearButton.setText(_translate("RemoverEmbarque", "Limpar"))
        self.label_5.setText(_translate("RemoverEmbarque", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Remover Embarque</span></p></body></html>"))
        self.submitButton.setText(_translate("RemoverEmbarque", "Remover"))
        self.cancelButton.setText(_translate("RemoverEmbarque", "Cancelar"))
        self.label_6.setText(_translate("RemoverEmbarque", "Id do Embarque"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RemoverEmbarque = QtWidgets.QDialog()
    ui = Ui_RemoverEmbarque()
    ui.setupUi(RemoverEmbarque)
    RemoverEmbarque.show()
    sys.exit(app.exec_())