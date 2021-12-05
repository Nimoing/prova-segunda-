import sqlite3

try:
    conn = sqlite3.connect('database/info.db')#ele cria na ´pasta em bloco de testo
    conn.execute('drop table if exists tb_info')
    #aqui ele cria a tabela com seus tipos sendo id nome entre outros
    conn.execute('''
        CREATE TABLE tb_info (
            id INTEGER PRIMARY KEY NOT NULL,
            cep TEXT NOT NULL,
            cpf TEXT NOT NULL,
            rg TEXT NOT NULL
            );
    ''')
    #serve para criar na ordem que foi informado em cima
    conn.execute(
        '''
        INSERT INTO `tb_info` (`id`,`cep`,`cpf`,`rg`)
        VALUES
            (1,"68960-971","203.024.927-04","12.205.903-7"),
            (2,"29240-987","824.373.977-79","39.294.642-7"),
            (3,"29190-362","670.101.057-15","14.905.150-5"),
            (4,"68980-970","297.691.067-71","38.722.013-6"),
            (5,"79910-970","767.210.677-57","24.374.606-4"),
            (6,"68371-274","135.036.527-01","46.904.152-3"),
            (7,"95773-970","441.478.077-20","15.664.158-6"),
            (8,"59870-970","220.842.857-98","25.581.920-1"),
            (9,"53690-970","774.794.087-49","25.599.126-5"),
            (10,"76862-970","655.929.987-24","25.185.280-5");
        '''
    )
    conn.commit()
    print("Operacao realizada com sucesso!")
except:
    print("ERRO")
finally:
    conn.close()
