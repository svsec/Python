#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 19:31:05 2020

@author: adal
"""


# Esse arquivo será destinado a tipos de estruturas de dados :)
import numpy as np
import matplotlib.pyplot as plt

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


# após uma função deixar duas linhas em branco por favor
print(alterar(3, 5))


# Pode-se passar listas por parametro para a função
def dobrar(list):
    for i in range(len(list)):
        list[i] = list[i] * 2


lista = [1, 2, 3, 4]
dobrar(lista)

# usamos o lenporquê não é passado a quantidade de elementos da lista

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

# função list comprehension
# pode usar funçôes ou exercutar comandos em determinada lista

# [função(i) for i in lista]

# Numpy biblioteca numerica, permite a resolução de problemas matématicos e
# cientificos


vet = np.array([1, 2, 3, 4])
print(vet)

matriz = np.array([[1, 2], [1, 2]])
print(matriz)

#  funçoes auxiliares
#  matriz.shape / matriz.size / matriz.ndim
#  np.eye() cria matrizes identidades
#  np.zeros/ np.ones

# função arange serve para criar vetores ordenados com certo padrão

oi = np.arange(100, dtype=int)
oii = np.arange(0, 100, 2)
oii = np.arange(50, 0, -1, dtype=float)

# funão numpy.random.randint(inicio = 0, fim, tamanho)

vetorale = np.random.randint(0, 50, 4)
matrizale = np.random.randint(0, 100, (3, 3))


# numpy mais rapido que listas

# Plotagem a partir do matplolib

x = np.array([1, 3, 3, 4])
y = np.array([1, 3, 2, 6])

# funcoes como .plot / .scatter / .bar para diferentes graficos

plt.plot(x, y)
plt.show()

z = np.array([1, 3, 3, 4])
a = np.array([1, 1.5, 2.5, 5])
a2 = np.array([2, 3, 5, 7])

plt.plot(z, a)
plt.plot(a, a2)

plt.savefig('grafico.png')
