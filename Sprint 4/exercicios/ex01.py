############ EX 01
"""
é_par = lambda x: x % 2 == 0

with open('arq.txt', 'r') as arquivo:
    números = [int(linha.strip()) for linha in arquivo]

números_pares = filter(é_par, números)

números_pares_ordenados = sorted(números_pares, reverse=True)

cinco_maiores_números_pares = números_pares_ordenados[:5]

soma_dos_maiores_números_pares = sum(cinco_maiores_números_pares)

print("Os 5 maiores números pares em ordem decrescente:")
print(cinco_maiores_números_pares)
print("A soma destes valores é:", soma_dos_maiores_números_pares)

############ EX 02

conta_vogais = lambda frase: len(list(filter(lambda letra: letra.lower() in 'aeiou', frase)))

frase_teste = "Sou estagiário da Compass"
print("Número de vogais na frase:", conta_vogais(frase_teste))

############ EX 03

from functools import reduce

def calcula_saldo(lancamentos) -> float:
    calcular_saldo_lancamento = lambda lancamento: lancamento[0] if lancamento[1] == 'C' else -lancamento[0]
    saldos = map(calcular_saldo_lancamento, lancamentos)
    saldo_final = reduce(lambda x, y: x + y, saldos)
    return saldo_final

lancamentos = [
    (200,'D'),
    (300,'C'),
    (100,'C')
]

print("Saldo final:", calcula_saldo(lancamentos))

############ EX 04

def calcular_valor_maximo(operadores, operandos) -> float:
    aplicar_operacao = lambda op, opd: eval(str(opd[0]) + op + str(opd[1]))
    resultados = map(aplicar_operacao, operadores, operandos)
    maximo = max(resultados)
    return maximo

operadores = ['+','-','*','/','+']
operandos = [(3,6), (-7,4.9), (8,-8), (10,2), (8,4)]

print("Maior valor obtido:", calcular_valor_maximo(operadores, operandos))

############ EX 05

import csv

def processar_notas(arquivo):
    with open(arquivo, 'r', newline='') as file:
        reader = csv.reader(file)
        next(reader)  
        
        for linha in reader:
            nome = linha[0]
            notas = list(map(int, linha[1:]))
            tres_maiores_notas = sorted(notas, reverse=True)[:3]
            media = round(sum(tres_maiores_notas) / 3, 2)
            print(f"Nome: {nome} Notas: {tres_maiores_notas} Média: {media}")

processar_notas('estudantes.csv')

############ EX 06

def maiores_que_media(conteudo: dict) -> list:
    media = sum(conteudo.values()) / len(conteudo)
    produtos_acima_da_media = [(produto, preco) for produto, preco in conteudo.items() if preco > media]
    produtos_acima_da_media_ordenados = sorted(produtos_acima_da_media, key=lambda x: x[1])
    return produtos_acima_da_media_ordenados

lista = {
    "arroz": 4.99,
    "feijão": 3.49,
    "macarrão": 2.99,
    "leite": 3.29,
    "pão": 1.99
}

print(maiores_que_media(lista))

############ EX 07

def pares(n: int):
    if n % 2 == 1:
        n -= 1

    for i in range(2, n + 1, 2):
        yield i

gerador = pares(10)

for valor in gerador:
    print(valor)
"""
