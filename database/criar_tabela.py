import sqlite3

try:
    conn = sqlite3.connect('database/data.db')#ele cria na ´pasta em bloco de testo
    conn.execute('drop table if exists tb_cliente')
    #aqui ele cria a tabela com seus tipos sendo id nome entre outros
    conn.execute('''
        CREATE TABLE tb_cliente (
            id INTEGER PRIMARY KEY NOT NULL,
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            banco TEXT NOT NULL,
            saldo TEXT NOT NULL,
            tem_conta_nao_paga  TEXT NOT NULL,
            quantidade_deve TEXT NOT NULL
        );
    ''')
    #serve para criar na ordem que foi informado em cima
    conn.execute(
        '''
        INSERT INTO `tb_cliente` (`id`,`nome`,`email`,`banco`,saldo,tem_conta_nao_paga,quantidade_deve)
        VALUES
            (1,"Jessamine Mccormick","aenean.massa@hotmail.com","Banco do Brasil","R$ 1.500,00","Sim","R$ 2.000,00"),
            (2,"Whoopi Morrow","mauris@icloud.com","Caixa Econômica Federal","R$ 100","nao","R$ 0,00"),
            (3,"Jackson Warner","dis@aol.couk","Bradesco","R$ 10.562,00","Sim","R$ 5.000,00"),
            (4,"Lev Whitley","fermentum.vel@outlook.net","Banco Safra","R$ 13.513,00","Sim","R$ 11.234,00"),
            (5,"Bryar James","dolor@outlook.couk","Votoraantim","R$ 23.546,00","nao","R$ 0,00"),
            (6,"Jescie Cruz","ut.dolor.dapibus@icloud.edu","Credit Suisse","R$ 64.634.156,00,","nao","R$ 0,00"),
            (7,"Lacey Madden","pretium.aliquet@yahoo.ca","Banco do Nordeste do Brasil","R$ 52.114.145,00","Sim","R$ 20.453.789,00"),
            (8,"Bethany Bonner","ac.turpis@google.com","BMG","R$ 1,00","nao","R$ 0,00"),
            (9,"Sawyer Garcia","odio.vel.est@hotmail.com","Banco Volksvagem","R$ 132.154.486,00","nao","R$ 0,00"),
            (10,"Regina Gilmore","ante.vivamus.non@outlook.org","Banco Cooperativo Sicredi","R$ 1.000.000.000,00","Sim","R$ 1,00");
        '''
    )
    conn.commit()
    print("Operacao realizada com sucesso!")
except:
    print("ERRO")
finally:
    conn.close()
