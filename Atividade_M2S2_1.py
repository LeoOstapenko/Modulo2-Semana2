import sqlite3
conexao = sqlite3.connect('atividade_m2s2_1.sqlite3')
cursor = conexao.cursor()

sql = '''
CREATE TABLE categoria (
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	nome TEXT(100) NOT NULL
);
'''
sql2 = '''
CREATE TABLE tarefa (
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	nome TEXT(100) NOT NULL,
	data TEXT(10),
	categoria_id INTEGER NOT NULL,
	status_conclusao TEXT(20) NOT NULL,
		FOREIGN KEY (categoria_id) REFERENCES categoria(id)
);
'''

cursor.execute(sql)
cursor.execute(sql2)

conexao.commit() 
conexao.close()