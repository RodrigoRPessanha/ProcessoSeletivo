import datetime
import sqlite3


def conectar():
    conn = sqlite3.connect('mydatabase.db')
    return conn


def createTableFuncionario():
    conn = conectar()
    conn.execute('''CREATE TABLE IF NOT EXISTS FUNCIONARIOS
                (IDFUNCIONARIO INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                NOME TEXT NOT NULL,
                SOBRENOME TEXT NOT NULL,
                DATADENASCIMENTO DATETIME NOT NULL,
                APTOPARAEMBARQUE BOOL NOT NULL);''')
    conn.close()


def createTableEmbarque():
    conn = conectar()
    conn.execute('''CREATE TABLE EMBARQUE
                (ID_EMBARQUE INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                DATA_EMBARQUE DATETIME NOT NULL,
                DATA_DESEMBARQUE DATETIME NOT NULL,
                ID_FUNCIONARIO INT NOT NULL,
                COMENTARIO TEXT);''')
    conn.close()


def dropTable(tabela):
    conn = conectar()
    conn.execute(f'''DROP TABLE {tabela}''')
    conn.close()


def selectAllFuncionarios():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM FUNCIONARIOS')

    resultados = cursor.fetchall()

    registros = []

    for linha in resultados:
        registro = {}
        registro['id'] = linha[0]
        registro['nome'] = linha[1]
        registro['sobrenome'] = linha[2]
        registro['dataNasc'] = linha[3]
        registro['AptoEmbarque'] = linha[4]
        registros.append(registro)

    cursor.close()
    conn.close()

    jsonValores = {}
    jsonValores['valores'] = registros
    return jsonValores


def selectAllEmbarque():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM EMBARQUE')

    resultados = cursor.fetchall()

    registros = []

    for linha in resultados:
        registro = {}
        registro['id'] = linha[0]
        registro['dataEmbarque'] = linha[1]
        registro['dataDesembarque'] = linha[2]
        registro['idFuncionario'] = linha[3]
        registro['comentario'] = linha[4]
        registros.append(registro)

    jsonValores = {}
    jsonValores['valores'] = registros
    cursor.close()
    conn.close()
    return jsonValores


def selectIdFuncionarios():
    conn = sqlite3.connect('mydatabase.db')

    cursor = conn.cursor()
    cursor.execute('SELECT * FROM FUNCIONARIOS')

    resultados = cursor.fetchall()

    registros = []

    for linha in resultados:
        registro = {}
        registro['id'] = linha[0]
        registro['nome'] = linha[1]
        registro['sobrenome'] = linha[2]
        registro['dataDeNascimento'] = linha[3]
        registro['aptoParaEmbarque'] = linha[4]
        registros.append(registro)

    idsBd = []
    for i in range(len(registros)):
        idsBd.append(registros[i]['id'])
    cursor.close()
    conn.close()
    return idsBd


def selectIdEmbarque():
    conn = sqlite3.connect('mydatabase.db')

    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Embarque')

    resultados = cursor.fetchall()

    registros = []

    for linha in resultados:
        registro = {}
        registro['id'] = linha[0]
        registro['dataEmbarque'] = linha[1]
        registro['dataDesembarque'] = linha[2]
        registro['idFuncionario'] = linha[3]
        registro['comentario'] = linha[4]
        registros.append(registro)

    idsBd = []
    for i in range(len(registros)):
        idsBd.append(registros[i]['id'])
    cursor.close()
    conn.close()
    return idsBd


def insertFuncionario(nome, sobrenome, dataDeNascimento, aptoParaEmbarque: bool):
    conn = conectar()
    conn.execute("INSERT INTO FUNCIONARIOS (NOME, SOBRENOME, DATADENASCIMENTO, APTOPARAEMBARQUE) \
                  VALUES (?, ?, ?, ?)", (nome, sobrenome, dataDeNascimento, aptoParaEmbarque))
    conn.commit()
    conn.close()


def insertEmbarque(dataEmbarque: datetime, dataDesembarque: datetime, idTrabalhador: int, comentario: str = None):
    idsBd = selectIdFuncionarios()
    conn = conectar()
    if dataDesembarque > dataEmbarque:
        if int(idTrabalhador) in idsBd:
            conn.execute(f"INSERT INTO EMBARQUE (DATA_EMBARQUE, DATA_DESEMBARQUE, ID_FUNCIONARIO, COMENTARIO) \
                        VALUES  (?, ?, ?, ?)", (dataEmbarque, dataDesembarque, idTrabalhador, comentario))
        else:
            print(f"O id {idTrabalhador} não pertence a nenhum funcionario")
    else:
        print(
            f"A data de embarque do trabalhador com id {idTrabalhador} selecionada é depois da data de desembarque")
    conn.commit()
    conn.close()


def updateFuncionario(id: int, novoNome: str = None, novoSobrenome: str = None, novaDataNascimento: str = None, novaSituacao: bool = None):
    conn = conectar()
    if novoNome:
        conn.execute(
            f'UPDATE FUNCIONARIOS SET NOME = "{novoNome}" WHERE IDFUNCIONARIO = {id}')
    if novoSobrenome:
        conn.execute(
            f'UPDATE FUNCIONARIOS SET SOBRENOME = "{novoSobrenome}" WHERE IDFUNCIONARIO = {id}')
    if novaDataNascimento:
        conn.execute(
            f'UPDATE FUNCIONARIOS SET DATADENASCIMENTO = "{novaDataNascimento}" WHERE IDFUNCIONARIO = {id}')
    if novaSituacao:
        conn.execute(
            f'UPDATE FUNCIONARIOS SET APTOPARAEMBARQUE = "{novaSituacao}" WHERE IDFUNCIONARIO = {id}')
    conn.commit()
    conn.close()


def updateEmbarque(id: int, novaDataEmbarque: datetime = None, novaDataDesembarque: datetime = None, novoId: int = None, novoComentario: str = None):
    conn = conectar()
    if novaDataEmbarque:
        conn.execute(
            f'UPDATE EMBARQUE SET DATA_EMBARQUE = {novaDataEmbarque} WHERE ID_EMBARQUE = {id}')
    if novaDataDesembarque:
        conn.execute(
            f'UPDATE EMBARQUE SET DATA_DESEMBARQUE = {novaDataDesembarque} WHERE ID_EMBARQUE = {id}')
    if novoId:
        conn.execute(
            f'UPDATE EMBARQUE SET ID_FUNCIONARIO = {novoId} WHERE ID_EMBARQUE = {id}')
    if novoComentario:
        conn.execute(
            f'UPDATE EMBARQUE SET COMENTARIO = {novoComentario} WHERE ID_EMBARQUE = {id}')
    conn.commit()
    conn.close()


def deleteFuncionario(id: int):
    conn = conectar()
    if id:
        conn.execute(f'DELETE FROM FUNCIONARIOS WHERE IDFUNCIONARIO = {id}')
    conn.commit()
    conn.close()


def deleteEmbarque(id: int):
    conn = conectar()
    if id:
        conn.execute(f'DELETE FROM EMBARQUE WHERE ID_EMBARQUE = {id}')
    conn.commit()
    conn.close()


def selectNomeEmbarqueDesembarque():
    conn = conectar()
    cursor2 = conn.cursor()

    cursor2.execute(
        'SELECT f.NOME || " " || f.SOBRENOME, em.DATA_EMBARQUE, em.DATA_DESEMBARQUE FROM FUNCIONARIOS f JOIN EMBARQUE em ON f.IDFUNCIONARIO = em.ID_FUNCIONARIO')

    resultados2 = cursor2.fetchall()

    registros2 = []

    for linha2 in resultados2:
        registro2 = {}
        registro2['nome'] = linha2[0]
        registro2['embarque'] = linha2[1]
        registro2['desembarque'] = linha2[2]
        registros2.append(registro2)

    for linha in registros2:
        print(linha)
    cursor2.close()
    conn.close()


def verificarApto(id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(f'SELECT APTOPARAEMBARQUE FROM FUNCIONARIOS WHERE {id}')

    resultado = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    return resultado
