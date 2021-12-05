from flask import Flask, Blueprint, request, jsonify
import sqlite3
from api.salarioxgasto import deleta #importa3

#especificar rota
info = Blueprint('info',__name__)#ele adiciona uma su roda que se chama cliente

info.register_blueprint(deleta,url_prefix='/deleta/')

def conectar():
    return sqlite3.connect('database/info.db')



@info.route('/', methods=['GET'])
def get_all():
    lista = []
    try:
        conn = conectar()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM tb_info")

        for i in cur.fetchall():
            info = {}
            info["id"] = i["id"]
            info["cpf"] = i["cpf"]
            info["rg"] = i["rg"]
            info["cep"] = i["cep"]
            lista.append(info)
    except Exception as e:
        print(e)
        lista = []

    return jsonify(lista)

@info.route('/<id>', methods=['GET'])
def get_by_id(id):
    info = {}
    try:
        conn = conectar()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM tb_info  where id=?",(id,))
        
        row = cur.fetchone()
      
        info["id"] = row["id"]
        info["cpf"] = row["cpf"]
        info["rg"] = row["rg"]
        info["cep"] = row["cep"]
   
    except Exception as e:
        print(str(e))
        info = {}

    return jsonify(info)


@info.route('/',  methods = ['POST'])
def add():
    info = request.get_json()
    try:
        conn = conectar()
        cur = conn.cursor()
        cur.execute("INSERT INTO tb_info (cpf, rg, cep) VALUES (?, ?, ?)",
                    (info['cpf'], info['rg'], info['cep']) )
        conn.commit()
        resposta = jsonify(
            {
                'mensagem':'Operacao realizada com sucesso',
                'id' : cur.lastrowid
            }
        )
    except Exception as e:
        conn.rollback()
        resposta = jsonify({'erro' : str(e)})
    finally:
        conn.close()
    return resposta
 


