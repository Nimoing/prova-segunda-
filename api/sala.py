from flask import Flask, Blueprint, request, jsonify
import sqlite3

#especificar rota
sala = Blueprint('sala',__name__)#ele adiciona uma su roda que se chama cliente

def conectar():
    return sqlite3.connect('database/tabela.db')

@sala.route('/<id>', methods=['GET'])
def get_by_id(id):
    sala = {}
    try:
        conn = conectar()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM tb_tabela where id=?",(id,))
        row = cur.fetchone()
      
        sala["id"] = row["id"]
        sala["conta"] = row["conta"]
        sala["ganho"] = row["ganho"]

           
    except Exception as e:
        print(str(e))
        sala = {}

    return jsonify(sala)


@sala.route('/',  methods = ['PUT'])
def update():
    sala = request.get_json()

    try:
        conn = conectar()
        cur = conn.cursor()
        cur.execute("UPDATE tb_tabela SET conta=?, ganho=? WHERE id=?",
                    (sala['conta'], sala['ganho'],  sala['id']) )
        conn.commit()
        resposta = jsonify({'mensagem':'Operacao realizada com sucesso'})

    except Exception as e:
        conn.rollback()
        resposta = jsonify({'erro' : str(e)})
    finally:
        conn.close()

    return resposta



