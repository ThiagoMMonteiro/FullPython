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

