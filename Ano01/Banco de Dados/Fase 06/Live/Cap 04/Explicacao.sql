-- BANCO DE DADOS E SGBD --

-- Banco de dados é o local onde armazenamos dados. Podemos chamar de banco de
-- dados arquivos do Microsoft Access, por exemplo. Ou planilhas de excel, ou
-- outras fontes onde podemos salvar dados de forma organizada.

-- Já um SGBD, ou Sistema Gerenciador de Banco de Dados, é um software voltado
-- para gerir dados organizados em objetos que se relacionam e podem ser consultados
-- de forma organizada através de um interface de programação.
-- Ou como a definição mais tradicional do Wikipedia:

-- “Um Sistema de Gerenciamento de Banco de Dados (SGBD) – do inglês Data Base
-- Management System (DBMS) – é o conjunto de programas de computador (softwares)
-- responsáveis pelo gerenciamento de uma base de dados. Seu principal objetivo é
-- retirar da aplicação cliente a responsabilidade de gerenciar o acesso, a
-- manipulação e a organização dos dados. O SGBD disponibiliza uma interface para
-- que seus clientes possam incluir, alterar ou consultar dados previamente armazenados.
-- Em bancos de dados relacionais a interface é constituída pelas APIs (Application
-- Programming Interface) ou drivers do SGBD, que executam comandos na linguagem
-- SQL (Structured Query Language).�?


-- SGBD E SQL (O que é SQL?) --

-- Como a propria definição do Wikipedia, SQL é uma das principais interfaces de
-- comunicação do desenvolvedor com o banco de dados, seja para manipulá-lo ou
-- consultá-lo.


-- CLIENT DE BANCO DE DADOS --

-- É importante definir que um client visual utilizado para acessar os SGBDs não
-- é o Banco em sí. Um client é a ferramenta que se conectará ao SGBD (o banco em
-- sí não tem interface gráfica normalmente), e facilitará o acesso através de recursos
-- visuais e um interface de desenvolvimento mais amigável. 

-- Exemplos de clients são: DBeaver, DataGrip e o próprio Oracle SQL Developer.


-- ESTRUTURAS DENTRO DO BANCO DE DADOS --

-- Um banco de dados é composto principalmente por tabelas que se relacionam ou não.
-- Mas não somente por tabelas. A estrutura mais genérica de um banco é o próprio banco.
-- Um servidor com o SGBD Oracle, pode conter diversos bancos Oracle sendo administrados
-- ao mesmo tempo, seja para aplicações distintas, ambientes diferentes, ou qualquer
-- outro cenário. É importante sabermos qual o banco que vamos acessar dentro de um 
-- host. Uma vez que temos um banco, podemos organizá-lo segregando assuntos através
-- de schemas, e dentros dos schemas teremos as tabelas, views e etc.

-- Banco >> Schema >> Tabelas,Views


-- TIPOS DE DADOS --

-- varchar2
-- char
-- number
-- date
-- long
-- ...


-- SQL (da definição a consulta) --

-- SQL é uma linguagem de definição, manipulação e controle de banco de dados.
-- Representa um conjunto de comandos responsáveis pela definição das tabelas,
-- seleção e atualização dos dados em um SGBD. Temos subdivisões dentro do SQL:

-- DDL (Data Definition Language)
-- DML (Data Manipulation Language)
-- DCL (Data Control Language)
-- DTL (Data Transaction Language)
-- DQL (Data Query Language)

-- DDL >> DML >> DQL

-- DDL --

-- CREATE TABLE
-- ALTER TABLE
-- CONTRAINTS
-- DROP TABLE
-- CASCADE
-- SEQUENCE

-- EXEMPLO --

CREATE TABLE t_sip_departamento(
    cd_departamento NUMBER(3),
    nm_departamento VARCHAR2(30)
);

-- Puxando todas as colunas da tabela t_sip_departamento
SELECT * FROM t_sip_departamento;

-- Apagar tabela t_sip_departamento
DROP TABLE t_sip_departamento;

CREATE TABLE T_SIP_DEPARTAMENTO(
    cd_departamento NUMBER(3)    NOT NULL, -- NOT NULL n�o deixa a coluna vir sem nenhum valor
    nm_departamento VARCHAR2(30)
);

ALTER TABLE T_SIP_DEPARTAMENTO
    ADD CONSTRAINT PK_SIP_DEPTO PRIMARY KEY (cd_departamento);

DROP TABLE T_SIP_DEPARTAMENTO;

-- TABELA DEPARTAMENTO
CREATE TABLE T_SIP_DEPARTAMENTO(
    cd_departamento NUMBER(3)    NOT NULL,
    nm_departamento VARCHAR2(30) NOT NULL,
    CONSTRAINT PK_SIP_DEPTO PRIMARY KEY (cd_departamento)
);

ALTER TABLE T_SIP_DEPARTAMENTO
    ADD CONSTRAINT UN_SIP_DEPTO_NOME
    UNIQUE (nm_departamento);

-- DML
INSERT INTO T_SIP_DEPARTAMENTO VALUES (1, 'mkt');
INSERT INTO T_SIP_DEPARTAMENTO VALUES (2, null);
INSERT INTO T_SIP_DEPARTAMENTO VALUES (2, NULL);
INSERT INTO T_SIP_DEPARTAMENTO (nm_departamento) VALUES ('mkt');
INSERT INTO T_SIP_DEPARTAMENTO VALUES (1, 'mkt');
INSERT INTO T_SIP_DEPARTAMENTO VALUES (2, 'mkt');


SELECT * FROM t_sip_departamento;

CREATE TABLE T_SIP_FUNCIONARIO
  (
    nr_matricula    NUMBER(6)    NOT NULL,
    cd_departamento NUMBER(3)    NOT NULL,
    nm_nome         VARCHAR2(60) NOT NULL,
    dt_nascimento   DATE         NULL,
    dt_admissao     DATE         NULL,
    ds_endereco     VARCHAR2(60) NOT NULL,
    vl_salario      NUMBER(8,2)  NOT NULL
);

INSERT INTO T_SIP_FUNCIONARIO (
    nr_matricula, cd_departamento, nm_nome, ds_endereco, vl_salario)
VALUES (1,1,'A','E',1000);

SELECT * FROM T_SIP_FUNCIONARIO;

ALTER TABLE T_SIP_FUNCIONARIO
    ADD CONSTRAINT FK_DEPTO_FUNC FOREIGN KEY (cd_departamento)
    REFERENCES T_SIP_DEPARTAMENTO (cd_departamento);

DROP TABLE T_SIP_DEPARTAMENTO CASCADE CONSTRAINTS;
DROP TABLE T_SIP_FUNCIONARIO;

-- TABELA FUNCIONARIO
CREATE TABLE T_SIP_FUNCIONARIO
  (
    nr_matricula    NUMBER(6)    NOT NULL,
    cd_departamento NUMBER(3)    NOT NULL,
    nm_nome         VARCHAR2(60) NOT NULL,
    dt_nascimento   DATE         NULL,
    dt_admissao     DATE         NULL,
    ds_endereco     VARCHAR2(60) NOT NULL,
    vl_salario      NUMBER(8,2)  NOT NULL,
    CONSTRAINT FK_DEPTO_FUNC FOREIGN KEY (cd_departamento)
    REFERENCES T_SIP_DEPARTAMENTO (cd_departamento)
);

DROP TABLE T_SIP_DEPARTAMENTO CASCADE CONSTRAINTS;
DROP TABLE T_SIP_FUNCIONARIO  CASCADE CONSTRAINTS;

-- Definindo a sequ�ncia de 1 at� 999
CREATE SEQUENCE SQ_DEPTO
INCREMENT BY 1 START WITH 1
MAXVALUE 999;

-- Dual serve para quando n�o tem uma tabela espec�fica para puxar a informa��o
SELECT SQ_DEPTO.NEXTVAL FROM DUAL; --Pr�ximo valor dispon�vel da sequ�ncia. Toda vez que rodar ele vai puxar um n�mero diferente que n�o pode se repetir
SELECT SQ_DEPTO.CURRVAL FROM DUAL; --

INSERT INTO T_SIP_DEPARTAMENTO VALUES (SQ_DEPTO.NEXTVAL, 'RH');
INSERT INTO T_SIP_DEPARTAMENTO VALUES (SQ_DEPTO.NEXTVAL, 'RH');
INSERT INTO T_SIP_DEPARTAMENTO VALUES (SQ_DEPTO.NEXTVAL, 'MKT');

SELECT * FROM t_sip_departamento;

-- Apagando a coluna de cd_departamento 11 da tabela T_SIP_DEPARTAMENTO
DELETE FROM T_SIP_DEPARTAMENTO WHERE cd_departamento = 11;

DROP TABLE T_SIP_DEPARTAMENTO CASCADE CONSTRAINTS;
DROP TABLE T_SIP_FUNCIONARIO  CASCADE CONSTRAINTS;
DROP SEQUENCE SQ_DEPTO;