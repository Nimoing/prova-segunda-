from flask import Flask, Blueprint, request, jsonify
import sqlite3

#especificar rota
salario = Blueprint('salario',__name__)#ele adiciona uma su roda que se chama cliente



#conequitar no banco
def conectar():
    return sqlite3.connect('database/tabela_sala.db')


    
@salario.route('/<id>', methods=['GET'])
def get_by_id(id):
    salario = {}
    try:
        conn = conectar()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM tb_tabela where id=?",(id,))
        row = cur.fetchone()
      
        salario["id"] = row["id"]
        salario["conta"] = row["conta"]
        salario["ganho"] = row["ganho"]
      
    except Exception as e:
        print(str(e))
        salario = {}

    return jsonify(salario)


@salario.route('/',  methods = ['PUT'])
def update():
    salario = request.get_json()

    try:
        conn = conectar()
        cur = conn.cursor()
        cur.execute("UPDATE tb_tabela SET conta=?, ganho=? WHERE id=?",
                    (salario['conta'], salario['ganho'], salario['id']) )
        conn.commit()
        resposta = jsonify({'mensagem':'Operacao realizada com sucesso'})

    except Exception as e:
        conn.rollback()
        resposta = jsonify({'erro' : str(e)})
    finally:
        conn.close()

    return resposta






