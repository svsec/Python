#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 19:31:05 2020

@author: adal
"""
# Esse arquivo será destinado a tipos de estruturas de dados :)

# tupla (imutavel de tamanho fixo), utiliza-se parenteses ()

t = (1, 2, 3)
type(t)

print(t)
print(t[1])

aluno = ("adalberto", 8, 12)
print(aluno[0])

# comandos como count e len também funcionam

# Lista (tuplas mutaveis), usa-se colchetes []

lista = [1, 2, 3]

lista.append("Adal")
print(lista[3])
# append para o final da lista
# insert(valor,indice) num lugar especifico
# del para remover um indice da lista
# in para verificar se há determinado elemento na lista

sequencia = list(range(10, -5, -1))


# Dicionario, coleção de pares de chave-valor tamanho fléxivel
# itens são ligados por chaves e não por indeces
# sempre será utilizado chaves {}

curso = {"linguagem": "python", "aluno": "Adalberto", "duração": "8horas"}
print(curso["linguagem"])
print("aluno:", curso['aluno'])
print('duração', curso['duração'])

# keys() retorna as chaves do dicionario

# usando comando for pode-se criar uma iteração de listas ou tuples

for i in lista:
    print(i)

# iteração de dicionario

for key in curso:
    print('KEY:', key, "descrição:", curso[key])

# Funções

# Ex:
def alterar(a, b):
    return a - b

print(alterar(3,5))

# Pode-se passar listas por parametro para a função 

def dobrar(list):
    for i in range(len(list)):
        list[i] = list[i] * 2
lista = [1, 2, 3, 4]
dobrar(lista)

# usamos o len porquê não é passado a quantidade de elementos da lista

# usamos ** para exponencial

# uma funçao pode retornar mais de um valor 

# def baskara (a, b, c):
#     return x1, x2
# a, b = baskara(a, b, c)

# tratamento de exceções
# try:
#    pass //comandos que possam ter problemas 
# except:
#   pass //comando que irão processar se houver algum erro
# finally 
#  pass /// opcional. sempre executará

# manipulação de arquivos

with open("arquivo.txt", "w") as file:
    file.write("sei lá")
    
# w escrever /r ler /a anexar

with open("arquivo.txt", "r") as file:
    dados = file.readlines()
print(dados)

