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

#Listas e Dicionários
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

