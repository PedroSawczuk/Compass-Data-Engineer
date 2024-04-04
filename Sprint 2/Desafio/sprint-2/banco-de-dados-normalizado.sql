CREATE TABLE dim_cliente (
    idCliente INT PRIMARY KEY,
    nomeCliente VARCHAR(100),
    cidadeCliente VARCHAR(40),
    estadoCliente VARCHAR(40),
    paisCliente VARCHAR(40),
    sexoCliente SMALLINT
);

CREATE TABLE dim_carro (
    idCarro INT PRIMARY KEY,
    marcaCarro VARCHAR(80),
    modeloCarro VARCHAR(80),
    anoCarro INT,
    tipoCombustivel VARCHAR(20)
);

CREATE TABLE dim_locacao (
    idLocacao INT PRIMARY KEY,
    dataLocacao TIMESTAMP,
    dataEntrega DATE,
    qtdDiaria INT,
    vlrDiaria DECIMAL(18, 2)
);

CREATE TABLE fato_locacao (
    idLocacao INT,
    idCliente INT,
    idCarro INT,
    dataLocacao TIMESTAMP,
    dataEntrega DATE,
    qtdDiaria INT,
    vlrDiaria DECIMAL(18, 2),
    PRIMARY KEY (idLocacao),
    FOREIGN KEY (idCliente) REFERENCES dim_cliente(idCliente),
    FOREIGN KEY (idCarro) REFERENCES dim_carro(idCarro),
    FOREIGN KEY (idLocacao) REFERENCES dim_locacao(idLocacao)
);

INSERT INTO dim_cliente (idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente, sexoCliente)
VALUES
(2, 'Cliente dois', 'São Paulo', 'São Paulo', 'Brasil', 0),
(3, 'Cliente três', 'Rio de Janeiro', 'Rio de Janeiro', 'Brasil', 1),
(4, 'Cliente quatro', 'Rio de Janeiro', 'Rio de Janeiro', 'Brasil', 1),
(5, 'Cliente cinco', 'Manaus', 'Amazonas', 'Brasil', 0),
(6, 'Cliente seis', 'Belo Horizonte', 'Minas Gerais', 'Brasil', 1),
(10, 'Cliente dez', 'Rio Branco', 'Acre', 'Brasil', 0),
(20, 'Cliente vinte', 'Macapá', 'Amapá', 'Brasil', 0),
(22, 'Cliente vinte e dois', 'Porto Alegre', 'Rio Grande do Sul', 'Brasil', 0),
(23, 'Cliente vinte e três', 'Eusébio', 'Ceará', 'Brasil', 0),
(26, 'Cliente vinte e seis', 'Campo Grande', 'Mato Grosso do Sul', 'Brasil', 1);

INSERT INTO dim_carro (idCarro, marcaCarro, modeloCarro, anoCarro, tipoCombustivel)
VALUES
(98, 'Fiat', 'Fiat Uno', 2000, 'Gasolina'),
(99, 'Fiat', 'Fiat Palio', 2010, 'Gasolina'),
(3, 'VW', 'Fusca 78', 1978, 'Gasolina'),
(1, 'Toyota', 'Corolla XEI', 2023, 'Flex'),
(7, 'Fiat', 'Fiat 147', 1996, 'Gasolina'),
(2, 'Nissan', 'Versa', 2019, 'Etanol'),
(4, 'Nissan', 'Versa', 2020, 'Etanol'),
(5, 'Nissan', 'Frontier', 2022, 'Diesel'),
(13, 'MarcaX', 'ModeloX', 2024, 'Gasolina');

INSERT INTO dim_locacao (idLocacao, dataLocacao, dataEntrega, qtdDiaria, vlrDiaria)
VALUES
(1, '2015-01-10 10:00:00', '2015-01-12', 5, 100.00),
(2, '2015-02-10 12:00:00', '2015-02-12', 5, 100.00),
(3, '2015-02-13 12:00:00', '2015-02-15', 2, 150.00),
(4, '2015-02-15 13:00:00', '2015-02-20', 5, 150.00),
(5, '2017-01-02 18:00:00', '2017-01-12', 10, 250.00),
(7, '2018-04-01 11:00:00', '2018-04-11', 10, 50.00),
(8, '2022-05-01 08:00:00', '2022-05-21', 20, 150.00),
(9, '2022-09-01 08:00:00', '2022-09-21', 20, 150.00),
(10, '2023-01-02 18:00:00', '2023-01-12', 10, 880.00),
(11, '2023-01-25 08:00:00', '2023-01-30', 5, 600.00);
