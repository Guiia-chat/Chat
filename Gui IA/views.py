
from testefask import app
from flask import render_template, request, jsonify
from fine_tuning import gerar_resposta

@app.route('/')
@app.route('/GUIIA')
def GUIIA():
    return render_template('chatbot.html')

@app.route('/buscar', methods=['POST'])
def buscar():
    data = request.get_json()
    pergunta = data.get('pergunta')

    if not pergunta:
        return jsonify({'resposta': 'Pergunta vazia'})

    resposta = gerar_resposta(pergunta)
    return jsonify({'resposta': resposta})

