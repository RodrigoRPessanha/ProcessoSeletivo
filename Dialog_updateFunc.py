# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Dialog-updateFunc.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_EditarFuncionario(object):
    def setupUi(self, EditarFuncionario):
        EditarFuncionario.setObjectName("EditarFuncionario")
        EditarFuncionario.resize(381, 249)
        self.gridLayoutWidget = QtWidgets.QWidget(EditarFuncionario)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 60, 359, 151))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_4.addWidget(self.label_9)
        self.aptoCheckBox = QtWidgets.QCheckBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.aptoCheckBox.setFont(font)
        self.aptoCheckBox.setObjectName("aptoCheckBox")
        self.horizontalLayout_4.addWidget(self.aptoCheckBox)
        self.horizontalLayout_4.setStretch(0, 40)
        self.horizontalLayout_4.setStretch(1, 57)
        self.gridLayout.addLayout(self.horizontalLayout_4, 1, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_4.addWidget(self.label_6)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_4.addWidget(self.label_7)
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_4.addWidget(self.label_8)
        self.horizontalLayout_3.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.idArea = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.idArea.setObjectName("idArea")
        self.verticalLayout_5.addWidget(self.idArea)
        self.firstNameArea = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.firstNameArea.setFont(font)
        self.firstNameArea.setObjectName("firstNameArea")
        self.verticalLayout_5.addWidget(self.firstNameArea)
        self.lastNameArea = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lastNameArea.setFont(font)
        self.lastNameArea.setObjectName("lastNameArea")
        self.verticalLayout_5.addWidget(self.lastNameArea)
        self.birthdayArea = QtWidgets.QDateEdit(self.gridLayoutWidget)
        self.birthdayArea.setObjectName("birthdayArea")
        self.verticalLayout_5.addWidget(self.birthdayArea)
        self.horizontalLayout_3.addLayout(self.verticalLayout_5)
        self.horizontalLayout_3.setStretch(0, 2)
        self.horizontalLayout_3.setStretch(1, 3)
        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(EditarFuncionario)
        self.label_5.setGeometry(QtCore.QRect(100, 10, 180, 41))
        self.label_5.setObjectName("label_5")
        self.submitButton = QtWidgets.QPushButton(EditarFuncionario)
        self.submitButton.setGeometry(QtCore.QRect(240, 220, 80, 23))
        self.submitButton.setObjectName("submitButton")
        self.cancelButton = QtWidgets.QPushButton(EditarFuncionario)
        self.cancelButton.setGeometry(QtCore.QRect(60, 220, 80, 23))
        self.cancelButton.setObjectName("cancelButton")
        self.clearButton = QtWidgets.QPushButton(EditarFuncionario)
        self.clearButton.setGeometry(QtCore.QRect(150, 220, 80, 23))
        self.clearButton.setObjectName("clearButton")

        self.retranslateUi(EditarFuncionario)
        self.cancelButton.clicked.connect(EditarFuncionario.close) # type: ignore
        self.clearButton.clicked.connect(self.firstNameArea.clear) # type: ignore
        self.clearButton.clicked.connect(self.lastNameArea.clear) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(EditarFuncionario)

    def retranslateUi(self, EditarFuncionario):
        _translate = QtCore.QCoreApplication.translate
        EditarFuncionario.setWindowTitle(_translate("EditarFuncionario", "Dialog"))
        self.label_9.setText(_translate("EditarFuncionario", "<html><head/><body><p><span style=\" font-size:10pt;\">Apto para Embarque</span></p></body></html>"))
        self.aptoCheckBox.setText(_translate("EditarFuncionario", "Apto"))
        self.label.setText(_translate("EditarFuncionario", "Id"))
        self.label_6.setText(_translate("EditarFuncionario", "Nome"))
        self.label_7.setText(_translate("EditarFuncionario", "<html><head/><body><p><span style=\" font-size:10pt;\">Sobrenome</span></p></body></html>"))
        self.label_8.setText(_translate("EditarFuncionario", "<html><head/><body><p><span style=\" font-size:10pt;\">Data de nascimento</span></p></body></html>"))
        self.label_5.setText(_translate("EditarFuncionario", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Editar Funcionario</span></p></body></html>"))
        self.submitButton.setText(_translate("EditarFuncionario", "Editar"))
        self.cancelButton.setText(_translate("EditarFuncionario", "Cancelar"))
        self.clearButton.setText(_translate("EditarFuncionario", "Limpar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EditarFuncionario = QtWidgets.QDialog()
    ui = Ui_EditarFuncionario()
    ui.setupUi(EditarFuncionario)
    EditarFuncionario.show()
    sys.exit(app.exec_())
