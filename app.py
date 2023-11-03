from flask import Flask, jsonify, request

app = Flask(__name__)

funcionarios = [
    {
        'id': 1,
        'nome': 'Murilo',
        'sobrenome': 'Munari',
        'cargo': 'Gerente'
    },

    {
        'id': 2,
        'nome': 'Claudio',
        'sobrenome': 'Miranda',
        'cargo': 'Auxiliar',
    },
    {
        'id': 3,
        'nome': 'Rodinei',
        'sobrenome': 'Pereira',
        'cargo': 'CEO',
    },
]


@app.route('/funcionarios', methods=['GET'])
def obeter_funcionarios():
    return jsonify(funcionarios)


@app.route('/funcionarios/<int:id>', methods=['GET'])
def obter_funcionarios_por_id(id):
    for funcionario in funcionario:
        if funcionario.get('id') == id:
            return jsonify(funcionarios)


app.run()