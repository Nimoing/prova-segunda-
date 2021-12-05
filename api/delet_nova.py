from flask import Flask, Blueprint, request, jsonify
import sqlite3

#especificar rota
deletnova = Blueprint('deletnova',__name__)#ele adiciona uma su roda que se chama cliente


def conectar():
    return sqlite3.connect('database/data.db')


@deletnova.route('/',  methods = ['PUT'])
def update():
    deletnova = request.get_json()

    try:
        conn = conectar()
        cur = conn.cursor()
        cur.execute("UPDATE tb_cliente SET nome=?, email=?, banco=?, saldo=?, tem_conta_nao_paga=?, quantidade_deve=? WHERE id=?",
                    (deletnova['nome'], deletnova['email'], deletnova['banco'], deletnova['saldo'], deletnova['tem_conta_nao_paga'], deletnova['quantidade_deve'],  deletnova['id']) )
        conn.commit()
        resposta = jsonify({'mensagem':'Operacao realizada com sucesso'})

    except Exception as e:
        conn.rollback()
        resposta = jsonify({'erro' : str(e)})
    finally:
        conn.close()

    return resposta


@deletnova.route('/<id>',  methods = ['DELETE'])
def delete(id):
    print(id)
    try:
        conn = conectar()
        cur = conn.cursor()
        cur.execute("DELETE FROM tb_cliente WHERE id=?",(id,))
        conn.commit()
        resposta = jsonify({'mensagem':'Registro apagado com sucesso'})

    except Exception as e:
        conn.rollback()
        resposta = jsonify({'erro' : str(e)})
    finally:
        conn.close()

    return resposta

    
