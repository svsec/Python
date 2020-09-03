#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 18:36:57 2020

@author: adal
"""
# Este arquivo será destinado a noçoẽs basicas de python :)
x = 5

y = 5.2

curso = 'python'

print(x+y)


birth = 08.12
idade = 19
nome = 'Adal'

aluno = nome + str(idade) + str(birth)

print(len(aluno))


print(aluno[2])

aluno.replace('adal', 'Cris')

print(aluno)

aluno.split('a')
print(aluno)


print(aluno.find('8'))

print(aluno, x+5)

# importante
# necessario fazer casting toda vez antes do input

N1 = int(input("N1:"))
N2 = int(input("N2:"))

media = (N1 + N2)/2

if media > 6:
    print("flwww")
elif media == 6:
    print("flwww")
else:
    print('vai ficar lindo')

nota = float(input("digite uma nota:"))

if nota < 0 or nota > 10:
    print("nota invalida lindo")
    print("flwww")

x = 0

while x < 10:
    print(x)
    x = x + 1

for y in range(0, 10):
    print(y)

# for valor in variavel
# range (inicio, fim , intervalo)
for z in range(5, 0, -1):
    print(z)
