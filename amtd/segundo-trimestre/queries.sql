-- =========================================================
-- MODELO FÍSICO - CONCESSIONÁRIA
-- =========================================================


-- =========================================================
-- 1. CRIAÇÃO DAS TABELAS
-- =========================================================

CREATE TABLE concessionaria (
    cnpj INTEGER PRIMARY KEY,
    endereco VARCHAR(100),
    razao_social VARCHAR(100)
);


CREATE TABLE acessorio (
    codigo INTEGER PRIMARY KEY,
    descricao VARCHAR(100)
);


CREATE TABLE oficina_mecanica (
    cnpj INTEGER PRIMARY KEY,
    nome VARCHAR(100)
);


CREATE TABLE carro (
    chassi INTEGER PRIMARY KEY,
    ano INTEGER,
    preco INTEGER,
    fabricante VARCHAR(100),
    modelo VARCHAR(100),
    cnpj_concessionaria INTEGER,

    FOREIGN KEY (cnpj_concessionaria)
        REFERENCES concessionaria(cnpj)
);


CREATE TABLE cliente (
    cpf INTEGER PRIMARY KEY,
    sexo VARCHAR(100),
    nome VARCHAR(100),
    chassi_carro INTEGER,

    FOREIGN KEY (chassi_carro)
        REFERENCES carro(chassi)
);


-- =========================================================
-- 2. TABELA DO RELACIONAMENTO CADASTRA
--    CONCESSIONARIA N:N CLIENTE
-- =========================================================

CREATE TABLE cadastra (
    cnpj_concessionaria INTEGER,
    cpf_cliente INTEGER,

    PRIMARY KEY (cnpj_concessionaria, cpf_cliente),

    FOREIGN KEY (cnpj_concessionaria)
        REFERENCES concessionaria(cnpj),

    FOREIGN KEY (cpf_cliente)
        REFERENCES cliente(cpf)
);


-- =========================================================
-- 3. TABELA DO RELACIONAMENTO POSSUI
--    CARRO N:N ACESSORIO
-- =========================================================

CREATE TABLE carro_acessorio (
    chassi_carro INTEGER,
    codigo_acessorio INTEGER,

    PRIMARY KEY (chassi_carro, codigo_acessorio),

    FOREIGN KEY (chassi_carro)
        REFERENCES carro(chassi),

    FOREIGN KEY (codigo_acessorio)
        REFERENCES acessorio(codigo)
);


-- =========================================================
-- 4. TABELA DO RELACIONAMENTO É_MANTIDO_POR
--    CARRO N:N OFICINA_MECANICA
-- =========================================================

CREATE TABLE manutencao (
    chassi_carro INTEGER,
    cnpj_oficina INTEGER,

    PRIMARY KEY (chassi_carro, cnpj_oficina),

    FOREIGN KEY (chassi_carro)
        REFERENCES carro(chassi),

    FOREIGN KEY (cnpj_oficina)
        REFERENCES oficina_mecanica(cnpj)
);


-- =========================================================
-- 5. INSERTS - CONCESSIONARIAS
-- =========================================================

INSERT INTO concessionaria
VALUES
(1001, 'Rua Brasil, 100', 'Concessionaria Sul'),
(1002, 'Rua Flores, 200', 'Concessionaria Norte');


-- =========================================================
-- 6. INSERTS - ACESSORIOS
-- =========================================================

INSERT INTO acessorio
VALUES
(1, 'Ar condicionado'),
(2, 'Bancos de couro'),
(3, 'Camera de re');


-- =========================================================
-- 7. INSERTS - OFICINAS
-- =========================================================

INSERT INTO oficina_mecanica
VALUES
(2001, 'Oficina Central'),
(2002, 'Oficina Sul');


-- =========================================================
-- 8. INSERTS - CARROS
-- =========================================================

INSERT INTO carro
VALUES
(5001, 2024, 85000, 'Toyota', 'Corolla', 1001),
(5002, 2023, 72000, 'Honda', 'Civic', 1001),
(5003, 2025, 95000, 'Volkswagen', 'Jetta', 1002);


-- =========================================================
-- 9. INSERTS - CLIENTES
-- =========================================================

INSERT INTO cliente
VALUES
(1111, 'Masculino', 'Joao', 5001),
(2222, 'Feminino', 'Maria', 5002),
(3333, 'Masculino', 'Carlos', NULL);


-- =========================================================
-- 10. INSERTS - CADASTRA
-- =========================================================

INSERT INTO cadastra
VALUES
(1001, 1111),
(1001, 2222),
(1002, 3333);


-- =========================================================
-- 11. INSERTS - CARRO_ACESSORIO
-- =========================================================

INSERT INTO carro_acessorio
VALUES
(5001, 1),
(5001, 2),
(5002, 1),
(5003, 3);


-- =========================================================
-- 12. INSERTS - MANUTENCAO
-- =========================================================

INSERT INTO manutencao
VALUES
(5001, 2001),
(5001, 2002),
(5002, 2001),
(5003, 2002);


-- =========================================================
-- 13. SELECTS
-- =========================================================

SELECT * FROM concessionaria;

SELECT * FROM cliente;

SELECT * FROM carro;

SELECT * FROM acessorio;

SELECT * FROM oficina_mecanica;

SELECT * FROM cadastra;

SELECT * FROM carro_acessorio;

SELECT * FROM manutencao;