from flask import Flask, Blueprint, request, jsonify
import sqlite3

#especificar rota
salarioxgasto = Blueprint('salarioxgasto',__name__)#ele adiciona uma su roda que se chama cliente

def conectar():
    return sqlite3.connect('database/tabela.db')

@salarioxgasto.route('/<id>', methods=['GET'])
def get_by_id(id):
    salarioxgasto = {}
    try:
        conn = conectar()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM tb_tabela where id=?",(id,))
        row = cur.fetchone()
      
        salarioxgasto["id"] = row["id"]
        salarioxgasto["conta"] = row["conta"]
        salarioxgasto["ganho"] = row["ganho"]

           
    except Exception as e:
        print(str(e))
        salarioxgasto = {}

    return jsonify(salarioxgasto)


@salarioxgasto.route('/',  methods = ['PUT'])
def update():
    salarioxgasto = request.get_json()

    try:
        conn = conectar()
        cur = conn.cursor()
        cur.execute("UPDATE tb_tabela SET conta=?, ganho=? WHERE id=?",
                    (salarioxgasto['conta'], salarioxgasto['ganho'],  salarioxgasto['id']) )
        conn.commit()
        resposta = jsonify({'mensagem':'Operacao realizada com sucesso'})

    except Exception as e:
        conn.rollback()
        resposta = jsonify({'erro' : str(e)})
    finally:
        conn.close()

    return resposta



