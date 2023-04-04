from principal import Ui_TelaPrincipal
from Dialog_cadastroFunc import Ui_CadastrarFuncionario
from Dialog_cadastroEmbarque import Ui_CadastrarEmbarque
from Dialog_updateFunc import Ui_EditarFuncionario
from Dialog_updateEmbarque import Ui_EditarEmbarque
from Dialog_deleteFunc import Ui_RemoverFuncionario
from Dialog_deleteEmbarque import Ui_RemoverEmbarque
from Dialog_telaConsultaCEO import Ui_telaConsultaCEO
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtPrintSupport import *
from PyQt5.Qt import Qt
import os
import sys
import requests
import app


class TelaPrincipal(QMainWindow):
    def __init__(self, *args, **argvs):
        super(TelaPrincipal, self).__init__(*args, **argvs)
        self.ui = Ui_TelaPrincipal()
        self.ui.setupUi(self)
        self.ui.addFuncButton.clicked.connect(self.cadastrarFuncionario)
        self.ui.updateFuncButton.clicked.connect(self.editarFuncionario)
        self.ui.deleteFuncButton.clicked.connect(self.removerFuncionario)
        self.ui.addEmbarqueButton.clicked.connect(self.cadastrarEmbarque)
        self.ui.updateEmbarqueButton.clicked.connect(self.editarEmbarque)
        self.ui.deleteEmbarqueButton.clicked.connect(self.removerEmbarque)
        self.ui.selectAllEmbarqueButton.clicked.connect(self.listar)

    def cadastrarFuncionario(self):
        cadastrarFunc = CadastrarFuncionario()
        cadastrarFunc.exec_()

    def editarFuncionario(self):
        editarFunc = EditarFuncionario()
        editarFunc.exec_()

    def removerFuncionario(self):
        removerFunc = RemoverFuncionario()
        removerFunc.exec_()

    def cadastrarEmbarque(self):
        editarEmbarque = CadastrarEmbarque()
        editarEmbarque.exec_()

    def editarEmbarque(self):
        editarEmbarque = EditarEmbarque()
        editarEmbarque.exec_()

    def removerEmbarque(self):
        removerEmbarque = RemoverEmbarque()
        removerEmbarque.exec_()

    def listar(self):
        listar = listaCEO()
        listar.exec_()


class CadastrarFuncionario(QDialog):
    def __init__(self, *args, **argvs):
        super(CadastrarFuncionario, self).__init__(*args, **argvs)
        self.ui = Ui_CadastrarFuncionario()
        self.ui.setupUi(self)
        self.ui.submitButton.clicked.connect(self.cadastrar)

    def cadastrar(self):
        nome = self.ui.firstNameArea.text()
        sobrenome = self.ui.lastNameArea.text()
        apto = self.ui.aptoCheckBox.isChecked()
        dataDeNascimento = self.ui.birthdayArea.date().toString('yyyy-MM-dd')
        url = 'http://127.0.0.1:5000/create/Funcionario/'
        data = {
            'name': nome,
            'last_name': sobrenome,
            'birth_date': dataDeNascimento,
            'aptoEmbarque': apto,
        }
        response = requests.post(url, json=data)
        if response.status_code == 201:
            QMessageBox.information(
                self, "Funcionário criado com sucesso", "O funcionário foi criado com sucesso.")
        else:
            QMessageBox.warning(
                self, "Erro", "Ocorreu um erro ao criar o funcionário.")


class EditarFuncionario(QDialog):
    def __init__(self, *args, **argvs):
        super(EditarFuncionario, self).__init__(*args, **argvs)
        self.ui = Ui_EditarFuncionario()
        self.ui.setupUi(self)
        self.ui.submitButton.clicked.connect(self.editar)

    def editar(self):
        idArea = self.ui.idArea.text()
        nome = self.ui.firstNameArea.text()
        sobrenome = self.ui.lastNameArea.text()
        apto = self.ui.aptoCheckBox.isChecked()
        dataDeNascimento = self.ui.birthdayArea.date().toString('yyyy-MM-dd')
        url = 'http://127.0.0.1:5000/update/Funcionario/'
        data = {
            'id': idArea,
            'name': nome,
            'last_name': sobrenome,
            'birth_date': dataDeNascimento,
            'aptoEmbarque': apto,
        }
        response = requests.post(url, json=data)
        if response.status_code == 200:
            QMessageBox.information(
                self, "Funcionário editado com sucesso", "O funcionário foi editado com sucesso.")
        else:
            QMessageBox.warning(
                self, "Erro", "Ocorreu um erro ao editar o funcionário.")


class RemoverFuncionario(QDialog):
    def __init__(self, *args, **argvs):
        super(RemoverFuncionario, self).__init__(*args, **argvs)
        self.ui = Ui_RemoverFuncionario()
        self.ui.setupUi(self)
        self.ui.submitButton.clicked.connect(self.editar)

    def editar(self):
        idArea = self.ui.idArea.text()
        url = f'http://127.0.0.1:5000/delete/Funcionario/{idArea}'
        response = requests.delete(url)
        response.content
        if response.status_code == 200:
            QMessageBox.information(
                self, "Funcionário deletado com sucesso", "O funcionário foi deletado com sucesso.")
        else:
            QMessageBox.warning(
                self, "Erro", "Ocorreu um erro ao deletar o funcionário.")


class CadastrarEmbarque(QDialog):
    def __init__(self, *args, **argvs):
        super(CadastrarEmbarque, self).__init__(*args, **argvs)
        self.ui = Ui_CadastrarEmbarque()
        self.ui.setupUi(self)
        self.ui.submitButton.clicked.connect(self.cadastrar)

    def cadastrar(self):
        embarqueDate = self.ui.embarqueDateArea.date().toString('yyyy-MM-dd')
        desembarqueDate = self.ui.desembarqueDateArea.date().toString('yyyy-MM-dd')
        idFunc = self.ui.idFuncArea.text()
        comentario = self.ui.commentArea.toPlainText()
        if not comentario:
            comentario = ""
        url = 'http://127.0.0.1:5000/create/Embarque/'
        data = {
            'dataEmbarque': embarqueDate,
            'dataDesembarque': desembarqueDate,
            'idFuncionario': idFunc,
            'comentario': comentario
        }
        response = requests.post(url, json=data)
        print(response.content)
        if response.status_code == 201:
            QMessageBox.information(
                self, "Embarque criado com sucesso", "O embarque foi criado com sucesso.")
        else:
            QMessageBox.warning(
                self, "Erro", "Ocorreu um erro ao criar o embarque.")


class EditarEmbarque(QDialog):
    def __init__(self, *args, **argvs):
        super(EditarEmbarque, self).__init__(*args, **argvs)
        self.ui = Ui_EditarEmbarque()
        self.ui.setupUi(self)
        self.ui.submitButton.clicked.connect(self.editar)

    def editar(self):
        idArea = self.ui.idArea.text()
        dataEmbarque = self.ui.embarqueDateArea.date().toString('yyyy-MM-dd')
        dataDesembarque = self.ui.desembarqueDateArea.date().toString('yyyy-MM-dd')
        idFuncionario = self.ui.idFuncArea.text()
        comentario = self.ui.textEdit.toPlainText()
        print("coment", comentario)
        url = 'http://127.0.0.1:5000/update/Embarque/'
        data = {
            'id': idArea,
            'dataEmbarque': dataEmbarque,
            'dataDesembarque': dataDesembarque,
            'idFuncionario': idFuncionario,
            'comentario': comentario
        }
        print("data: ", data)
        response = requests.post(url, json=data)
        print(response.content)
        if response.status_code == 200:
            QMessageBox.information(
                self, "Embarque editado com sucesso", "O embarque foi editado com sucesso.")
        else:
            QMessageBox.warning(
                self, "Erro", "Ocorreu um erro ao editar o embarque.")


class RemoverEmbarque(QDialog):
    def __init__(self, *args, **argvs):
        super(RemoverEmbarque, self).__init__(*args, **argvs)
        self.ui = Ui_RemoverEmbarque()
        self.ui.setupUi(self)
        self.ui.submitButton.clicked.connect(self.remover)

    def remover(self):
        idArea = self.ui.idArea.text()
        url = f'http://127.0.0.1:5000/delete/Embarque/{idArea}'
        response = requests.delete(url)
        response.content
        if response.status_code == 200:
            QMessageBox.information(
                self, "Embarque deletado com sucesso", "O embarque foi deletado com sucesso.")
        else:
            QMessageBox.warning(
                self, "Erro", "Ocorreu um erro ao deletar o embarque.")


class listaCEO(QDialog):
    def __init__(self, *args, **argsv):
        super(listaCEO, self).__init__(*args, **argsv)
        self.ui = Ui_telaConsultaCEO()
        self.ui.setupUi(self)
        self.ui.submitButton.clicked.connect(self.listar)

    def listar(self):
        url = 'http://127.0.0.1:5000/select/dadosCEO/'
        response = requests.get(url)
        listaEmbarques = response.json()
        self.ui.resultTable.setRowCount(0)
        lista = [tuple(i.values()) for i in listaEmbarques]
        for linha, dados in enumerate(lista):
            self.ui.resultTable.insertRow(linha)
            for coluna, dados in enumerate(tuple(reversed(dados))):
                self.ui.resultTable.setItem(
                    linha, coluna, QTableWidgetItem(str(dados)))


app = QtWidgets.QApplication(sys.argv)
window = TelaPrincipal()
window.show()
sys.exit(app.exec_())
