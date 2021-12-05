from flask import Flask, Blueprint, request, jsonify
import sqlite3

#especificar rota
conta = Blueprint('conta',__name__)#ele adiciona uma su roda que se chama cliente

def conectar():
    return sqlite3.connect('database/data.db')

@conta.route('/<id>', methods=['GET'])
def get_by_id(id):
    conta = {}
    try:
        conn = conectar()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM tb_cliente where id=?",(id,))
        row = cur.fetchone()
      
        conta["id"] = row["id"]
        conta["nome"] = row["nome"]
        conta["email"] = row["email"]
        conta["banco"] = row["banco"]
        conta["saldo"] = row["saldo"]
        conta["tem_conta_nao_paga"] = row["tem_conta_nao_paga"]
        conta["quantidade_deve"] = row["quantidade_deve"]
           
    except Exception as e:
        print(str(e))
        conta = {}

    return jsonify(conta)

@conta.route('/',  methods = ['POST'])
def add():
    conta = request.get_json()
    try:
        conn = conectar()
        cur = conn.cursor()
        cur.execute("INSERT INTO tb_cliente (nome, email, banco, saldo, tem_conta_nao_paga , quantidade_deve) VALUES (?, ?, ?,?, ?, ?)",
                    (conta['nome'], conta['email'], conta['banco'],conta['saldo'], conta['tem_conta_nao_paga'], conta['quantidade_deve']) )
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
 
