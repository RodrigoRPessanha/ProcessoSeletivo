# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Dialog-telaConsultaCEO.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_telaConsultaCEO(object):
    def setupUi(self, telaConsultaCEO):
        telaConsultaCEO.setObjectName("telaConsultaCEO")
        telaConsultaCEO.resize(600, 319)
        self.resultTable = QtWidgets.QTableWidget(telaConsultaCEO)
        self.resultTable.setGeometry(QtCore.QRect(30, 80, 551, 211))
        self.resultTable.setObjectName("resultTable")
        self.resultTable.setColumnCount(3)
        self.resultTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.resultTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.resultTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.resultTable.setHorizontalHeaderItem(2, item)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(telaConsultaCEO)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(30, 20, 291, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.idArea = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.idArea.setObjectName("idArea")
        self.horizontalLayout.addWidget(self.idArea)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.submitButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.submitButton.setObjectName("submitButton")
        self.horizontalLayout_2.addWidget(self.submitButton)

        self.retranslateUi(telaConsultaCEO)
        QtCore.QMetaObject.connectSlotsByName(telaConsultaCEO)

    def retranslateUi(self, telaConsultaCEO):
        _translate = QtCore.QCoreApplication.translate
        telaConsultaCEO.setWindowTitle(_translate("telaConsultaCEO", "Dialog"))
        item = self.resultTable.horizontalHeaderItem(0)
        item.setText(_translate("telaConsultaCEO", "Nome"))
        item = self.resultTable.horizontalHeaderItem(1)
        item.setText(_translate("telaConsultaCEO", "Embarque"))
        item = self.resultTable.horizontalHeaderItem(2)
        item.setText(_translate("telaConsultaCEO", "Desembarque"))
        self.label.setText(_translate("telaConsultaCEO", "Id Funcionario"))
        self.submitButton.setText(_translate("telaConsultaCEO", "Procurar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    telaConsultaCEO = QtWidgets.QDialog()
    ui = Ui_telaConsultaCEO()
    ui.setupUi(telaConsultaCEO)
    telaConsultaCEO.show()
    sys.exit(app.exec_())