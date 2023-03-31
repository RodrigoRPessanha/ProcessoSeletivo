from flask import Flask, request, jsonify
from EmbarqueTrabalhador import *

app = Flask(__name__)


@app.route('/create/Funcionario/', methods=['POST'])
def createFuncionario():
    data = request.get_json()

    if not data or not 'name' in data or not 'birth_date' in data or not 'aptoEmbarque' in data:
        return jsonify({'message': 'Please provide all required information.'}), 400

    name = data['name']
    last_name = data['last_name']
    birth_date = data['birth_date']
    aptoEmbarque = data['aptoEmbarque']

    insertFuncionario(name, last_name, birth_date, aptoEmbarque)
    return jsonify({'message': 'User created successfully.'}), 201


@app.route('/select/Funcionario/', methods=['GET'])
def getAllFuncionarios():
    listaFuncionarios = selectAllFuncionarios()
    return jsonify(listaFuncionarios), 200


@app.route('/delete/Funcionario/<int:id>', methods=['DELETE'])
def deleteFuncionarioById(id):
    if id in selectIdFuncionarios():
        deleteFuncionario(id)
        return jsonify({'message': 'User deleted successfully.'}), 200
    else:
        return jsonify({'message': 'Error: user does not exist.'}), 404


@app.route('/update/Funcionario/', methods=['POST'])
def updateFuncionarioById():
    data = request.get_json()
    id = data['id']
    if int(id) in selectIdEmbarque():
        name = data['name'] if data['name'] else None
        last_name = data['last_name'] if data['last_name'] else None
        birth_date = data['birth_date'] if data['birth_date'] else None
        aptoEmbarque = data['aptoEmbarque'] if data['aptoEmbarque'] else None
    else:
        return jsonify({'message': 'Error: funcionario does not exist.'}), 404

    updateFuncionario(id, name, last_name, birth_date, aptoEmbarque)
    return jsonify({'message': 'User updated successfully.'}), 200


@app.route('/create/Embarque/', methods=['POST'])
def createEmbarque():
    data = request.get_json()

    if not data or not 'dataEmbarque' in data or not 'dataDesembarque' in data or not 'idFuncionario' in data:
        return jsonify({'message': 'Please provide all required information.'}), 400

    dataEmbarque = data['dataEmbarque']
    dataDesembarque = data['dataDesembarque']
    idFuncionario = data['idFuncionario']
    if not verificarApto(idFuncionario):
        comentario = data['comentario']
    else:
        return jsonify({'message': f'Usuario {idFuncionario} nao esta apto para embarque.'}), 400
    insertEmbarque(dataEmbarque, dataDesembarque, idFuncionario, comentario)
    return jsonify({'message': 'Embarque created successfully.'}), 201


@app.route('/select/Embarque/', methods=['GET'])
def getAllEmbarque():
    listaEmbarques = selectAllEmbarque()
    return jsonify(listaEmbarques), 200


@app.route('/delete/Embarque/<int:id>', methods=['DELETE'])
def deleteEmbarqueById(id):
    if id in selectIdEmbarque():
        deleteEmbarque(id)
        return jsonify({'message': 'Embarque deleted successfully.'}), 200
    else:
        return jsonify({'message': 'Error: embarque does not exist.'}), 404


@app.route('/update/Embarque/', methods=['POST'])
def updateEmbarqueById():

    data = request.get_json()
    id = data['id']
    idFuncionario = data['idFuncionario'] if data['idFuncionario'] else None

    if int(id) in selectIdEmbarque():
        if int(idFuncionario) in selectIdFuncionarios():
            dataEmbarque = data['dataEmbarque'] if data['dataEmbarque'] else None
            dataDesembarque = data['dataDesembarque'] if data['dataDesembarque'] else None
            comentario = data['comentario'] if data['comentario'] else None

            updateEmbarque(id, dataEmbarque, dataDesembarque,
                           idFuncionario, comentario)
        else:
            return jsonify({'message': 'Error: funcionario does not exist.'}), 404
    else:
        return jsonify({'message': 'Error: embarque does not exist.'}), 404

    return jsonify({'message': 'Embarque updated successfully.'}), 200


if __name__ == '__main__':
    app.run()
