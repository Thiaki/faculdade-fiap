CREATE TABLE TAB_COLABORADOR_FASE6_CAP8 (
    CODIGO_COLABORADOR NUMBER,
    NOME VARCHAR2(255),
    EMAIL VARCHAR2(255),
    SALARIO NUMBER(10, 2),
    DATA_CONTRATACAO DATE
);

ALTER TABLE TAB_COLABORADOR_FASE6_CAP8
ADD PRIMARY KEY (CODIGO_COLABORADOR);


INSERT INTO TAB_COLABORADOR_FASE6_CAP8 (CODIGO_COLABORADOR, NOME, EMAIL, SALARIO, DATA_CONTRATACAO)
    VALUES (SQ_COLABORADOR.NEXTVAL, 'Eduardo', 'eduardo@gmail.com', 1500, TO_DATE('10/10/2010', 'DD/MM/YYYY'));
    
SELECT * FROM TAB_COLABORADOR_FASE6_CAP8;
SELECT * FROM TAB_COLABORADOR_FASE6_CAP8 WHERE CODIGO_COLABORADOR = 2;

UPDATE TAB_COLABORADOR_FASE6_CAP8 SET NOME = 'Luiz' WHERE CODIGO_COLABORADOR = 1;

DELETE FROM TAB_COLABORADOR_FASE6_CAP8 WHERE CODIGO_COLABORADOR = 1;

