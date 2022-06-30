'''
2.Crie um programa em Python que gere tabelas para uma aplicação de eventos. 
 Elas devem compreender as seguintes funcionalidades:
a)Eventos devem ter título, data e local, além da referência ao organizador;
b)O organizador deve ter nome, email e cpf;
c)As restrições/relacionamentos devem fazer sentido.
R:
'''
import sqlite3

conexao = sqlite3.connect('exercicio2.sqlite3')

cursor = conexao.cursor()

sql = '''
create table organizador(
    id int not null,
    nome varchar(100),
    email varchar(50),
    cpf varchar(11) not null,
    primary key (id)
);

create table eventos(
    organizador_id int not null,
    titulo varchar(50),
    data varchar(20),
    local varchar(100),
    primary key (organizador_id),
    foreig key (organizador_id) references organizador(id)
);
'''
cursor.execute(sql)
conexao.commit()
conexao.close()