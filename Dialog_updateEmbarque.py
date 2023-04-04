# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Dialog-updateEmbarque.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_EditarEmbarque(object):
    def setupUi(self, EditarEmbarque):
        EditarEmbarque.setObjectName("EditarEmbarque")
        EditarEmbarque.resize(380, 265)
        self.gridLayoutWidget = QtWidgets.QWidget(EditarEmbarque)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 50, 361, 187))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.idArea = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.idArea.setObjectName("idArea")
        self.verticalLayout_2.addWidget(self.idArea)
        self.embarqueDateArea = QtWidgets.QDateEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.embarqueDateArea.setFont(font)
        self.embarqueDateArea.setObjectName("embarqueDateArea")
        self.verticalLayout_2.addWidget(self.embarqueDateArea)
        self.desembarqueDateArea = QtWidgets.QDateEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.desembarqueDateArea.setFont(font)
        self.desembarqueDateArea.setObjectName("desembarqueDateArea")
        self.verticalLayout_2.addWidget(self.desembarqueDateArea)
        self.idFuncArea = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.idFuncArea.setFont(font)
        self.idFuncArea.setObjectName("idFuncArea")
        self.verticalLayout_2.addWidget(self.idFuncArea)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.textEdit = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayout.addWidget(self.textEdit)
        self.horizontalLayout.setStretch(0, 40)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 2)
        self.clearButton = QtWidgets.QPushButton(EditarEmbarque)
        self.clearButton.setGeometry(QtCore.QRect(150, 245, 80, 23))
        self.clearButton.setObjectName("clearButton")
        self.submitButton = QtWidgets.QPushButton(EditarEmbarque)
        self.submitButton.setGeometry(QtCore.QRect(240, 245, 80, 23))
        self.submitButton.setObjectName("submitButton")
        self.label_5 = QtWidgets.QLabel(EditarEmbarque)
        self.label_5.setGeometry(QtCore.QRect(110, 10, 160, 41))
        self.label_5.setObjectName("label_5")
        self.cancelButton = QtWidgets.QPushButton(EditarEmbarque)
        self.cancelButton.setGeometry(QtCore.QRect(60, 245, 80, 23))
        self.cancelButton.setObjectName("cancelButton")

        self.retranslateUi(EditarEmbarque)
        QtCore.QMetaObject.connectSlotsByName(EditarEmbarque)

    def retranslateUi(self, EditarEmbarque):
        _translate = QtCore.QCoreApplication.translate
        EditarEmbarque.setWindowTitle(_translate("EditarEmbarque", "Dialog"))
        self.label_6.setText(_translate("EditarEmbarque", "Id"))
        self.label.setText(_translate("EditarEmbarque", "Data do Embarque"))
        self.label_2.setText(_translate("EditarEmbarque", "Data do Desembarque"))
        self.label_3.setText(_translate("EditarEmbarque", "Id do Funcionario"))
        self.label_4.setText(_translate("EditarEmbarque", "Comentario"))
        self.clearButton.setText(_translate("EditarEmbarque", "Limpar"))
        self.submitButton.setText(_translate("EditarEmbarque", "Editar"))
        self.label_5.setText(_translate("EditarEmbarque", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Editar Embarque</span></p></body></html>"))
        self.cancelButton.setText(_translate("EditarEmbarque", "Cancelar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EditarEmbarque = QtWidgets.QDialog()
    ui = Ui_EditarEmbarque()
    ui.setupUi(EditarEmbarque)
    EditarEmbarque.show()
    sys.exit(app.exec_())
