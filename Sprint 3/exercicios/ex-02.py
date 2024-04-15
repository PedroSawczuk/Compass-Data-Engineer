# ---------------- Exercício 6
"""
def encontrar_intersecao_sem_repeticao(lista1, lista2):
    set1 = set(lista1)
    set2 = set(lista2)
    
    intersecao = set1.intersection(set2)
    
    intersecao_lista = list(intersecao)
    
    return intersecao_lista

a = [1, 1, 2, 3, 5, 8, 14, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

intersecao_resultado = encontrar_intersecao_sem_repeticao(a, b)

print(intersecao_resultado)

# ---------------- Exercício 7

numeros = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

num_impares = []

for num in numeros: 
    if num % 2 != 0:
        num_impares.append(num)  

print(num_impares)

# ---------------- Exercício 8

palavras = ['maça', 'arara', 'audio', 'radio', 'radar', 'moto']

def palindromo(palavra):
    return palavra == palavra[::-1]

for palavra in palavras:
    if palindromo(palavra):
        print(f"A palavra: {palavra} é um palíndromo")
    else:
        print(f"A palavra: {palavra} não é um palíndromo")

# ---------------- Exercício 9

primeirosNomes = ['Joao', 'Douglas', 'Lucas', 'José']
sobreNomes = ['Soares', 'Souza', 'Silveira', 'Pedreira']
idades = [19, 28, 25, 31]

for i in range(len(primeirosNomes)):
    print(f"{i} - {primeirosNomes[i]} {sobreNomes[i]} está com {idades[i]} anos")

# ---------------- Exercício 10

def remove_duplicados(lista):
    lista_sem_duplicados = list(set(lista))
    return lista_sem_duplicados

lista_teste = ['abc', 'abc', 'abc', '123', 'abc', '123', '123']
resultado = remove_duplicados(lista_teste)
print(resultado)

# ---------------- Exercício 11

import json

def ler_e_imprimir_json(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            dados = json.load(arquivo)
            print(json.dumps(dados, indent=4))
    except FileNotFoundError:
        print(f"Erro: o arquivo '{nome_arquivo}' não foi encontrado.")
    except json.JSONDecodeError as e:
        print(f"Erro ao fazer o parsing do JSON: {e}")

nome_arquivo_json = 'person.json'
ler_e_imprimir_json(nome_arquivo_json)

# ---------------- Exercício 12

def my_map(lst, f):
    return [f(x) for x in lst]

def potencia(x):
    return x ** 2

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

resultado = my_map(lista, potencia)

print(resultado)

# ---------------- Exercício 13

def ler_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            conteudo = arquivo.read()
            print(conteudo)
    except FileNotFoundError:
        print(f"Erro: o arquivo '{nome_arquivo}' não foi encontrado.")
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")

nome_do_arquivo = 'arquivo_texto.txt'

ler_arquivo(nome_do_arquivo)

# ---------------- Exercício 14

def imprimir_parametros(*args, **kwargs):
    print("Parâmetros não nomeados:")
    for valor in args:
        print(valor)

    print("\nParâmetros nomeados:")
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")

imprimir_parametros(1, 3, 4, 'hello', parametro_nomeado='alguma coisa', x=20)

# ---------------- Exercício 15

class Lampada:
    def __init__(self, ligada=False):
        self.ligada = ligada

    def liga(self):
        self.ligada = True

    def desliga(self):
        self.ligada = False

    def esta_ligada(self):
        return self.ligada

minha_lampada = Lampada()  # Inicialmente a lâmpada está desligada

minha_lampada.liga()

print("A lâmpada está ligada?", minha_lampada.esta_ligada())  # Deve imprimir: True

minha_lampada.desliga()

print("A lâmpada ainda está ligada?", minha_lampada.esta_ligada())  # Deve imprimir: False

# ---------------- Exercício 16

def soma_numeros_em_string(string_numeros):
    numeros = [int(num) for num in string_numeros.split(',') if num.strip().isdigit()]

    soma = sum(numeros)

    print("A soma dos valores é:", soma)

string_numeros = "1,3,4,6,10,76"

soma_numeros_em_string(string_numeros)

# ---------------- Exercício 17

def dividir_lista_em_tres_partes(lista):
    tamanho = len(lista)
    tamanho_parte = tamanho // 3
    parte1 = lista[:tamanho_parte]
    parte2 = lista[tamanho_parte:2*tamanho_parte]
    parte3 = lista[2*tamanho_parte:]
    return parte1, parte2, parte3

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
parte1, parte2, parte3 = dividir_lista_em_tres_partes(lista)
print("Parte 1:", parte1)
print("Parte 2:", parte2)
print("Parte 3:", parte3)

# ---------------- Exercício 18

speed = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53, 'july': 54, 'Aug': 44, 'Sept': 54}

valores_unicos = list(set(speed.values()))

print("Valores únicos:", valores_unicos)


# ---------------- Exercício 19

import random

random_list = random.sample(range(500), 50)

random_list_sorted = sorted(random_list)

valor_minimo = min(random_list_sorted)
valor_maximo = max(random_list_sorted)
soma = sum(random_list_sorted)

tamanho = len(random_list_sorted)
indice_do_ponto

# ---------------- Exercício 20

    a = [1, 0, 2, 3, 5, 8, 13, 21, 34, 55, 89]

    b = a[::-1]
    print(b)

# ---------------- Exercício 21

class Passaro:
    def voar(self):
        print("Voando...")
    
    def emitir_som(self):
        print("Passaro emitindo som...")


class Pato(Passaro):
    def emitir_som(self):
        super().emitir_som()
        print("Quack Quack")


class Pardal(Passaro):
    def emitir_som(self):
        super().emitir_som()
        print("Piu Piu")


# Testando as classes
if __name__ == "__main__":
    pato = Pato()
    print("Pato")
    pato.voar()
    pato.emitir_som()

    print("\nPardal")
    pardal = Pardal()
    pardal.voar()
    pardal.emitir_som()


# ---------------- Exercício 22

class Pessoa:
    def __init__(self, identificador):
        self.id = identificador
        self.__nome = None

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome


# Testando a classe Pessoa
if __name__ == "__main__":
    pessoa = Pessoa(0)
    pessoa.nome = 'Fulano De Tal'
    print(pessoa.nome)

# ---------------- Exercício 23

class Calculo:
    def soma(self, x, y):
        return x + y
    
    def subtracao(self, x, y):
        return x - y


if __name__ == "__main__":
    x = 4
    y = 5
    
    calc = Calculo()
    
    resultado_soma = calc.soma(x, y)
    print(f"Somando: {x}+{y} = {resultado_soma}")
    
    resultado_subtracao = calc.subtracao(x, y)
    print(f"Subtraindo: {x}-{y} = {resultado_subtracao}")


# ---------------- Exercício 24

class Ordenadora:
    def __init__(self, lista_baguncada):
        self.listaBaguncada = lista_baguncada
    
    def ordenacaoCrescente(self):
        self.listaBaguncada.sort()
        return self.listaBaguncada
    
    def ordenacaoDecrescente(self):
        self.listaBaguncada.sort(reverse=True)
        return self.listaBaguncada

if __name__ == "__main__":
    crescente = Ordenadora([3, 4, 2, 1, 5])
    resultado_crescente = crescente.ordenacaoCrescente()
    print(resultado_crescente)  # Saída esperada: [1, 2, 3, 4, 5]
    
    # Objeto 'decrescente' com lista [9,7,6,

# ---------------- Exercício 25

class Aviao:
    def __init__(self, modelo, velocidade_maxima, capacidade):
        self.modelo = modelo
        self.velocidade_maxima = velocidade_maxima
        self.capacidade = capacidade
        self.cor = "Azul"  


lista_avioes = []

aviao1 = Aviao("BOIENG456", "1500 km/h", "400 passageiros")
aviao2 = Aviao("Embraer Praetor 600", "863 km/h", "14 passageiros")
aviao3 = Aviao("Antonov An-2", "258 km/h", "12 passageiros")

lista_avioes.append(aviao1)
lista_avioes.append(aviao2)
lista_avioes.append(aviao3)

for aviao in lista_avioes:
    print(f"O avião de modelo \"{aviao.modelo}\" possui uma velocidade máxima de \"{aviao.velocidade_maxima}\", "
          f"capacidade para \"{aviao.capacidade}\" e é da cor \"{aviao.cor}\".")

"""
