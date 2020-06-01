# -*- coding: utf-8 -*- (serve para o interpretador python reconhecer os acentos)
# Comentario de uma linha
print ("Hello World!")


"""
Comentario de
varias linhas
"""

#Operações matemáticas
print (2 + 2) #soma
print (2 - 2) #subtração
print (2 / 2) #divisão
print (2 * 2) #multiplicação
print (2 ** 3) #exponenciação
print (3 % 2) #módulo - resto


#Variáveis
variavel = 47 #int
print(type(variavel)) 
variavel = 47.55 #flaot
print(type(variavel)) 
variavel = "47.55" #str
print(type(variavel))
variavel = '47.55' #str
print(type(variavel))
variavel = True #bool
print(type(variavel))
variavel = [1, 2, 3, "abacaxi", 5.55, True] #list
print(type(variavel))

#Operadores Relacionais
# == igual
# != diferente
# > maior
# < menor
# >= maior ou igual
# <= menor ou igual

#Operadores Lógicos
# and Duas condições sejam verdadeiras
# or Pelo menos uma condição seja verdadeira
# not Inverte o valor

#Estruturas de Condição
# IF - ELSE - ELIF
if 10 < 5:
	print("10 é menor do que 5!")
elif 10 > 5:
	print("10 é maior do que 5!")
else:
	print("São iguais!")

#Estruturas de Repetição
# WHILE
x = 1
while x < 10:
	print (x)
	x += 1
# FOR
lista = [10,11,12,13,14]
for i in lista:
	print (i)
# FOR RANGE
for i in range(5):
	print(i)
for i in range(10,15):
	print(i)
for i in range(10,15,2):
	print(i)

#Strings
#Concatenação
a = "Thiago"
b = "M Monteiro"
c = a + " " + b
print(c)
#Tamanho de uma string
tamanho = len(a)
print(tamanho)
#Impressão
print(a[0])
print(a[0:3])
print(a[3:])
#Função lower (deixa tudo em minúsculo) e upper (deixa tudo em maiúsculo)
a = "THIAGO"
print(a) 
print(a.lower())
a = a.lower()
print(a) 
print(a.upper()) 
#Função strip (remove espaços e caracteres especiais como quebra de linha (\n))
var = "      conteudo\n"
print(var)
print(var.strip())
#Função split (Separa a string e transforma em lista)
var = "Thiago Mânica Monteiro"
print(var)
print(type(var))
print(var.split()) #parâmetro default: " "
print(type(var.split()))
#Função find (busca de substrings)
print(var.find("Monteiro")) #Retorna o índice da primeira ocorrência / -1 se não encontrar
print(var.find("Monasterio"))
#Função replace
var = var.replace("Monteiro", "Monastério")
print(var)

#Funções
def soma(x, y):
	return x + y
s = soma(2, 3)
print(s)

#Manipulação de Arquivos
"""
#Função open

variavel = open(nome, modo)

#nome - nome do arquivo
#modo - r: somente leitura (default)
		w: escrita (caso o arquivo já exista, ele será apagado e um novo arquivo vazio será criado)
		a: leitura e escrita (adiciona o novo conteúdo ao fim do arquivo)
		r+: leitura e escrita
		w+: escrita (o modo w+, assim como o w, também apaga o conteúdo anterior do arquivo)
		a+: leitura e escrita (abre o arquivo para atualização)

#Funções de leitura - read() - readline() - readlines()
read() - lê o arquivo inteiro
readline() - lê uma linha do arquivo
readlines() - lê as linhas do arquivo e armazena em uma lista

#Função de escrita - write()
"""
arquivo = open("arquivoteste.txt", "r")

#conteudo = arquivo.read()
#print(conteudo)

linhas = arquivo.readlines()
for linha in linhas:
	print(linha)
arquivo.close()

#readline lê somente uma linha por vez - é o menos usado
arquivo = open("arquivotestecriado.txt", "w")
arquivo.write("Este arquivo foi criado pelo código\n")
arquivo.close()

#Listas
minha_lista = [1, 2, 2.5, "abacaxi", True, False]
minha_lista_vazia = []
print(minha_lista)
print(minha_lista_vazia)

for item in minha_lista:
	print(item)

#Função len - tamanho da lista
tamanho = len(minha_lista)
print(tamanho)
#Encontrar um elemento na lista
if 2.5 in minha_lista:
	print("Yes!")
#Função append - insere elemento no final da lista
minha_lista.append("limão")
print(minha_lista)
#Função del - remove elemento(s) da lista
del minha_lista[0] #remove o item de índice 0
print(minha_lista)
del minha_lista[3:] #remove do índice 3 até o final
print(minha_lista)
del minha_lista[:] #remove todos os itens da lista, deixando vazia
print(minha_lista)

#Como ordenar listas
minha_lista = [9, 6, 5, 3, 7, 2, 1, 4, 8]
minha_lista2 = ["c", "b", "d", "a", "f", "e"]
print(minha_lista)
print(minha_lista2)
#Método sort - altera a lista original
minha_lista.sort()
minha_lista2.sort()
print(minha_lista)
print(minha_lista2)
#Função sorted - retorna uma lista ordenada, não alterando a original
minha_lista = [9, 6, 5, 3, 7, 2, 1, 4, 8]
print(minha_lista)
lista_ordenada = sorted(minha_lista)
print(lista_ordenada)
print(minha_lista)
#Ordenar de forma decrescente
minha_lista.sort(reverse=True)
print(minha_lista)
#Método reverse - inverte a lista 
minha_lista.reverse()
print(minha_lista)

#Dicionários
"""
Listas de associações compostas por:
-uma chave
-um valor correspondente
dicionário = {'chave': 'valor'}
"""
dicionario = {"Thiago": "30", "Marcelo": "50", "Patrícia": "40"}
print(dicionario)
print(dicionario["Patrícia"])
#Imprime as chaves
for chave in dicionario:
	print(chave)
#Imprime os valores
for chave in dicionario:
	print(dicionario[chave])
#Imprime de forma personalizada
for chave in dicionario:
	print(chave + " - " + dicionario[chave])
#Função items() - converte cada par do dicionário em uma tupla
for i in dicionario.items():
	print(i)
#Método values() - retorna apenas os valores
for valor in dicionario.values():
	print(valor)
#Método keys() - retorna apenas as chaves
for chave in dicionario.keys():
	print(chave)

#Números aleatórios - Random
import random #módulo/lib python que gera números aleatórios
"""
Método randint(&num_inicial, &num_final) - gera um número aleatório de um range escolhido
num_inicial: Primeiro número possível aleatório
num_final: Último número possível aleatório
"""
num = random.randint(0,10)
print(num)

"""
Métudo choice(&lista) - Gera um número aleatório a partir de uma lista pré-definida
"""
minha_lista = [5, 7, 9, 13, 15]
num = random.choice(minha_lista)
print(num)

#Tratamento de exceções
a = 2
b = 0
try:
	print(a/b)
except:
	print("Não é permitido divisão por 0!")
print("Aqui continua a execução normalmente")

"""
Python 2 vs. Python 3
Não muda muita coisa na prática. Python 3 possui melhor performance. Quanto a sintaxe, destaco apenas dois pontos:

1) Comando print( )
Ao executar o print, em Python 3, os parênteses passam a ser obrigatórios:

# Python 2
print "Olá mundo"
# Python 3
print("Olá mundo")


2) Comando input( )
Em Python 2 há duas variações do comando input:

raw_input( ) #strings
input( ) # valores numéricos
Em python 3, deve-se usar apenas input( ) para strings, e para números deve-se combinar com as funções float ou int. Veja:

# Recebendo textos
meu_texto = input("Digite um texto: ")
# Recebendo números
numero_inteiro = int(input("Digite um numero inteiro: "))
numero_decimal = float(input("Digite um numero decimal: "))


O Sublime Text não aceita o comando input(), e você receberá uma mensagem como "EOFError: EOF when reading a line". 
Esse comando só funciona no terminal/cmd. Você pode inserir o valor diretamente na variável, caso use sublime text.
Ou instalar este pacote, para funcionar no Sublime (siga este vídeo):
https://www.youtube.com/watch?v=R5-niid0m8A
"""
#Exercício 1 - Escreva um programa que recebe a idade de um usuário e diga se ele é menor ou maior de idade.
idade = int(input("Digite a sua idade: "))
if idade >= 18:
	print("Você é MAIOR de idade!")
else:
	print("Voce é MENOR de idade!")
#Exercício 2 - Faça um programa que receba duas notas digitadas pelo usuário. 
#Se a nota for maior ou igual a seis, escreva aprovado, senão escreva reprovado. 
nota1 = float(input("Digite a nota da primeira prova: "))
nota2 = float(input("Digite a nota da segunda prova: "))
nota_final = (nota1 + nota2)/2
print(nota_final)

if nota_final >= 6:
	print("Aprovado!")
else:
	print("Reprovado!")
#Exercício 3 - Escreva um programa que resolva uma equação de segundo grau.

"""
-b +- (sqrt(b² - 4ac))/2a
"""

from math import sqrt

a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))

delta = b**2 - 4*a*c
if delta < 0:
	print("Delta negativo!")
else:
	raiz_delta = sqrt(delta)
	x1 = (-b - raiz_delta)/2*a
	x2 = (-b + raiz_delta)/2*a

	print(x1)
	print(x2)
#Exercício 4 - Escreva um programa que ordene uma lista numérica com 3 elementos
lista4 = [5, 3, 2]
print(lista4)
print(sorted(lista4))

#Exercício 5 - Escreva um programa que receba dois números e um sinal, e faça a operação definida pelo sinal

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
sinal = input("Digite o sinal da operação (+, -, /, *, **): ")

if sinal == "+":
	print(num1+num2)
elif sinal == "-":
	print(num1-num2)
elif sinal == "/":
	print(num1/num2)
elif sinal == "*":
	print(num1*num2)
elif sinal == "**":
	print(num1**num2)

#List Comprehension
x = [1, 2, 3, 4, 5]
# y = [valor_a_adicionar laço condição]

y = [i**2 for i in x]
print(x)
print(y)
z = [i for i in x if i%2 == 1]
print(z)

#Função enumerate
lista = ["abacate", "bola", "cachorro"]

for i, nome in enumerate(lista):
	print(i, nome)

#Função map
def dobro(x):
	return x*2

valor = 2
print(dobro(valor))
lista_valores = [1, 2, 3, 4, 5]
print(dobro(lista_valores)) #duplica a lista

valor_dobrado = map(dobro, lista_valores)
valor_dobrado = list(valor_dobrado)
print(valor_dobrado)

#Função reduce
from functools import reduce
def soma(x,y):
	return x+y

lista = [10, 20, 30]

soma = reduce(soma, lista)

print(soma)
