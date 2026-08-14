CREATE TABLE biblioteca (
    codigo INT NOT NULL,
    descricao VARCHAR(150) NOT NULL,
    endereco VARCHAR(100),
    PRIMARY KEY (codigo)
);

CREATE TABLE associado (
    codigo INT NOT NULL,
    descricao VARCHAR(150) NOT NULL,
    endereco VARCHAR(100),
    PRIMARY KEY (codigo)
);

CREATE TABLE assunto (
    codigo INT NOT NULL,
    descricao VARCHAR(150) NOT NULL,
    endereco VARCHAR(100),
    PRIMARY KEY (codigo)
);

CREATE TABLE autor (
    codigo INT NOT NULL,
    descricao VARCHAR(150) NOT NULL,
    endereco VARCHAR(100),
    PRIMARY KEY (codigo)
);

CREATE TABLE Livro (
    ISBN INT NOT NULL,
    titulo VARCHAR(100),
    B_codigo INT,
    A_matricula INT,
    PRIMARY KEY (ISBN),
    FOREIGN KEY (B_codigo)
        REFERENCES biblioteca(codigo),
    FOREIGN KEY (A_matricula)
        REFERENCES associado(codigo)
);

CREATE TABLE CADASTRA (
    B_codigo INT,
    A_matricula INT,
    FOREIGN KEY (B_codigo)
        REFERENCES biblioteca(codigo),
    FOREIGN KEY (A_matricula)
        REFERENCES associado(codigo)
);

CREATE TABLE ABORDA (
    L_ISBN INT,
    Ass_codigo INT,
    FOREIGN KEY (L_ISBN)
        REFERENCES Livro(ISBN),
    FOREIGN KEY (Ass_codigo)
        REFERENCES assunto(codigo)
);

CREATE TABLE ESCREVE (
    L_ISBN INT,
    Au_cod INT,
    FOREIGN KEY (L_ISBN)
        REFERENCES Livro(ISBN),
    FOREIGN KEY (Au_cod)
        REFERENCES autor(codigo)
);

INSERT INTO biblioteca (codigo, descricao, endereco)
VALUES
(1, 'Biblioteca Central', 'Rua das Flores, 100'),
(2, 'Biblioteca Municipal', 'Av. Brasil, 250'),
(3, 'Biblioteca Universitaria', 'Rua da Universidade, 500');

INSERT INTO associado (codigo, descricao, endereco)
VALUES
(101, 'Joao Guilherme', 'Rua A, 10'),
(102, 'Maria Silva', 'Rua B, 20'),
(103, 'Carlos Souza', 'Rua C, 30');

INSERT INTO assunto (codigo, descricao, endereco)
VALUES
(1, 'Banco de Dados', NULL),
(2, 'Programacao', NULL),
(3, 'Redes de Computadores', NULL);

INSERT INTO autor (codigo, descricao, endereco)
VALUES
(1, 'Machado de Assis', NULL),
(2, 'Clarice Lispector', NULL),
(3, 'George Orwell', NULL);

INSERT INTO Livro (ISBN, titulo, B_codigo, A_matricula)
VALUES
(1001, 'Dom Casmurro', 1, 101),
(1002, 'A Hora da Estrela', 1, 102),
(1003, '1984', 2, 103);



SELECT * FROM biblioteca;

