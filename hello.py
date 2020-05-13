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
variavel = [1,2,3] #list
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
