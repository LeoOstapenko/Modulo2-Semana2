import sqlite3
conexao = sqlite3.connect('atividade_m2s2_2.sqlite3')
cursor = conexao.cursor()

tab_organizador = '''
CREATE TABLE organizador (
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	nome TEXT(100) NOT NULL,
	email TEXT(100),
	cpf TEXT(11) NOT NULL UNIQUE
);
'''
tab_evento = '''
CREATE TABLE evento (
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	titulo TEXT(100) NOT NULL,
	data TEXT(10),
	local TEXT(100),
	organizador_id INTEGER NOT NULL,
		FOREIGN KEY (organizador_id) REFERENCES organizador(id)
);
'''

cursor.execute(tab_organizador)
cursor.execute(tab_evento)

conexao.commit() 
conexao.close()