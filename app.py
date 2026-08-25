from flask import Flask, jsonify, request

app = Flask(__name__)

jogos = [
    {
        "id": 1,
        "titulo": "super mario world",
        "genero": "Sandbox",
        "plataforma": "mega drive",
        "ano": 1969
    },
    {
        "id": 2,
        "titulo": "sonic 3",
        "genero": "Plataforma",
        "plataforma": "Megadrive",
        "ano": 1987
    },
    {
        "id": 3,
        "titulo": "fifa 25",
        "genero": "Esporte",
        "plataforma": "playstation 5",
        "ano": 2015
    },
    {
        "id": 4,
        "titulo": "Free fire",
        "genero": "Battle Royale",
        "plataforma": "Multiplataforma",
        "ano": 2017
    },
    {
        "id": 5,
        "titulo": "The Legend of Zelda",
        "genero": "Aventura",
        "plataforma": "Nintendo Switch",
        "ano": 2017
    }
]


def buscar_jogo_por_id(game_id):
    for jogo in jogos:
        if jogo["id"] == game_id:
            return jogo
    return None


@app.route('/api/jogos', methods=['GET'])
def listar_jogos():
    return jsonify(jogos), 200


@app.route('/api/jogos/<int:game_id>', methods=['GET'])
def consultar_jogo(game_id):
    jogo = buscar_jogo_por_id(game_id)

    if jogo is None:
        return jsonify({"erro": "Jogo não encontrado"}), 404

    return jsonify(jogo), 200


@app.route('/api/jogos', methods=['POST'])
def cadastrar_jogo():
    data = request.get_json()

    if not data:
        return jsonify({"erro": "Todos os campos são obrigatórios"}), 400

    novo_id = max((jogo["id"] for jogo in jogos), default=0) + 1

    novo_jogo = {
        "id": novo_id,
        "titulo": data["titulo"],
        "genero": data["genero"],
        "plataforma": data["plataforma"],
        "ano": data["ano"]
    }

    jogos.append(novo_jogo)
    return jsonify(novo_jogo), 201


@app.route('/api/jogos/<int:game_id>', methods=['PUT'])
def atualizar_jogo(game_id):
    jogo = buscar_jogo_por_id(game_id)

    if jogo is None:
        return jsonify({"erro": "Jogo não encontrado"}), 404

    data = request.get_json()

    if not data:
        return jsonify({"erro": "Todos os campos são obrigatórios"}), 400

    for campo in ["titulo", "genero", "plataforma", "ano"]:
        if campo in data:
            jogo[campo] = data[campo]

    return jsonify(jogo), 200


@app.route('/api/jogos/<int:game_id>', methods=['DELETE'])
def excluir_jogo(game_id):
    jogo = buscar_jogo_por_id(game_id)

    if jogo is None:
        return jsonify({"erro": "Jogo não encontrado"}), 404

    jogos.remove(jogo)
    return jsonify({"mensagem": "Jogo excluído com sucesso"}), 200


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
