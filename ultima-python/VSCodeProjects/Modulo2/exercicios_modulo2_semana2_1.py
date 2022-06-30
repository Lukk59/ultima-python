'''
1.Crie um programa em Python que gere tabelas para uma aplicação de gerenciamento de tarefas. 
 As tabelas devem compreender as seguintes funcionalidades:
a)As tarefas devem ser divididas em “categorias”;
b)Uma tarefa deve ter nome, data, categoria e status de conclusão (se foi realizada ou não); 
c)As restrições/relacionamentos devem fazer sentido.

R:
'''
import sqlite3

conexao = sqlite3.connect('exercicio1.sqlite3')

cursor = conexao.cursor()

sql = '''
create table categorias(
    id int not null,
    nome varchar(100),
    primary key (id)
);

create table tarefa1(
    id int not null,
    nome varchar(50),
    data varchar(20),
    status varchar(100),
    categorias_id int not null,
    primary key (id),
    foreig key (categorias_id) references categorias(id)
);

create table tarefa2(
    id int not null,
    nome varchar(50),
    data varchar(20),
    status varchar(100),
    categorias_id int not null,
    primary key (id),
    foreig key (categorias_id) references categorias(id)
);

create table tarefa3(
    id int not null,
    nome varchar(50),
    data varchar(20),
    status varchar(100),
    categorias_id int not null,
    primary key (id),
    foreig key (categorias_id) references categorias(id)
);
'''
cursor.execute(sql)
conexao.commit()
conexao.close()