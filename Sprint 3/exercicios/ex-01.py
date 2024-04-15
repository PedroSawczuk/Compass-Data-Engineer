# ---------------- Exercício 1
"""
nome = str(input('Digite seu nome: '))
idade = int(input('Sua idade: '))

ano_nascimento = 2024 - idade
ano_100_anos = ano_nascimento + 100

print(f'{nome} terá 100 anos em {ano_100_anos}!')

# ---------------- Exercício 2

numeros = []

for i in range(1, 4):
    num = int(input(f"Digite o {i}º número: "))  
    numeros.append(num)

for num in numeros:
    if num % 2 == 0:
        print(f"Par: {num}")
    else:
        print(f"Ímpar: {num}")

# ---------------- Exercício 3

numeros = list(range(21))

num_pares = []

for num in range(21): 
    if num % 2 == 0:
        num_pares.append(num)  

print(num_pares)

# ---------------- Exercício 4

def num_primo(n):
    
    if n <= 1:
        return False 
    for i in range(2, int(n**0.5) + 1):  
        if n % i == 0:
            return False  
    return True
  
print("Números primos entre 1 e 100:")
for num in range(1, 101):
    if num_primo(num):
        print(num, end=", ")  

# ---------------- Exercício 5

dia = 22
mes = 10
ano = 2022

print(f'{dia}/{mes}/{ano}')
"""

