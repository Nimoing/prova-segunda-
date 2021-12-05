from flask import Flask, Blueprint, request, jsonify
import sqlite3

#especificar rota
listaconta = Blueprint('listaconta',__name__)#ele adiciona uma su roda que se chama cliente



#conequitar no banco
def conectar():
    return sqlite3.connect('database/data.db')


@listaconta.route('/', methods=['GET'])
def get_all():
    lista = []
    try:
        conn = conectar()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM tb_cliente")

        for i in cur.fetchall():
            listaconta = {}
            listaconta["id"] = i["id"]
            listaconta["nome"] = i["nome"]
            listaconta["email"] = i["email"]
            listaconta["banco"] = i["banco"]
            listaconta["saldo"] = i["saldo"]
            listaconta["tem_conta_nao_paga"] = i["tem_conta_nao_paga"]
            listaconta["quantidade_deve"] = i["quantidade_deve"]
            lista.append(listaconta)
    except Exception as e:
        print(e)
        lista = []

    return jsonify(lista)

