import sqlite3

try:
    conn = sqlite3.connect('database/tabela.db')#ele cria na ´pasta em bloco de testo
    conn.execute('drop table if exists tb_tabela')
    #aqui ele cria a tabela com seus tipos sendo id nome entre outros
    conn.execute('''
        CREATE TABLE tb_tabela (
            id INTEGER PRIMARY KEY NOT NULL,
            conta TEXT NOT NULL,
            ganho TEXT NOT NULL
            );
    ''')
    #serve para criar na ordem que foi informado em cima
    conn.execute(
        '''
        INSERT INTO `tb_tabela` (`id`,`conta`,`ganho`)
        VALUES
            (1,3000,2500),
            (2,2500,3000),
            (3,1500,2000),
            (4,4000,3500),
            (5,6000,5500),
            (6,5000,4800),
            (7,4500,5000),
            (8,3500,4000),
            (9,1000,1500),
            (10,2500,4000);
        '''
    )
    conn.commit()
    print("Operacao realizada com sucesso!")
except:
    print("ERRO")
finally:
    conn.close()
