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
def obter_funcionarios():
    return jsonify(funcionarios)

@app.route('/funcionarios/<int:id>', methods=['GET'])
def obter_funcionario_por_id(id):
    for funcionario in funcionarios:
        if funcionario['id'] == id:
            return jsonify(funcionario)
    return jsonify({'error': 'Funcionário não encontrado'}), 404

@app.route('/funcionarios', methods=['POST'])
def criar_funcionario():
    novo_funcionario = request.get_json()
    novo_id = len(funcionarios) + 1
    novo_funcionario['id'] = novo_id
    funcionarios.append(novo_funcionario)
    return jsonify(novo_funcionario), 201

@app.route('/funcionarios/<int:id>', methods=['PUT'])
def atualizar_funcionario(id):
    for funcionario in funcionarios:
        if funcionario['id'] == id:
            dados_atualizados = request.get_json()
            funcionario.update(dados_atualizados)
            return jsonify(funcionario)
    return jsonify({'error': 'Funcionário não encontrado'}), 404

@app.route('/funcionarios/<int:id>', methods=['DELETE'])
def excluir_funcionario(id):
    for funcionario in funcionarios:
        if funcionario['id'] == id:
            funcionarios.remove(funcionario)
            return jsonify({'message': 'Funcionário excluído com sucesso'})
    return jsonify({'error': 'Funcionário não encontrado'}), 404

if __name__ == '__main__':
    app.run()
