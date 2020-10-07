# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 22:30:51 2020

@author: adalberto.teixeira
"""

# Arquivo dedicado à aprendizagem de Machine Learning(ML)

# Este problema faz uma alusão ao acidente ocorrido com o navio Titanic onde
# diversas pessoas morreram, porém houve alguns sobreviventes, este algoritmo
# e centrado em tentar descobrir o maior numero de pessoas, que sobreviveram


import numpy as np
import pandas as pandinha
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.model_selection import RepeatedKFold


# Puxando as tabelas com informações a serem averiguadas
treino = pandinha.read_csv("C:/Users/adalberto.teixeira/Desktop/IC/train.csv")
teste = pandinha.read_csv("C:/Users/adalberto.teixeira/Desktop/IC/test.csv")

# Partindo dos dados, ele diz que mulheres sempre sobrevivem, mas se fizermos
# uma alusão historica ao filme "Titanic" os primeiros a serem salvos são
# mulheres e crianças
# Adicionei o parametro "Pclass" já que pode ser que a classe em que o
# passageiro se encontrava o tivesse ajudado a se regastado também


# alo = treino.groupby("Sex")[["Survived"]].mean()
# plt.plot(alo)
# alo2 = treino.groupby("Pclass")[["Survived"]].mean()
# plt.scatter(alo2)
treino.groupby("SibSp")[["Survived"]].mean()
treino.groupby("Fare")[["Survived"]].mean()
treino.pivot_table("Survived", index="Sex", columns="Pclass")
descricao = treino.describe()

teste = teste.fillna(-1)
treino = treino.fillna(-1)
# função .fillna() transformará todos valores nulos ou que estão faltando
# em algum paramentro passado

Floresta = RandomForestClassifier(n_estimators=150, n_jobs=(1),
                                  random_state=(0))
# Metodo Random Florest
# n_estimators é o numero de arvores
# random_state é a mesma coisa que np.random_seed(0) para tirar a aleatoriedade
# (semente)


# Nosso modelo só trabalha com numeros.
# transformaremos essa coluna em binarios ( 1 para homens e 0 para mulheres)
def binario(sexo):
    if sexo == "male":
        return 1
    else:
        return 0


# transformaremos essa coluna em  ( 1 para "Q", 0 para "S" e 2 para "C")
def numerico(embarque):
    if embarque == "Q":
        return 1
    elif embarque == "S":
        return 0
    else:
        return 2


# criando uma nova instancia de coluna e adicionando-a a tabela de treino
# e teste para padronizar
# função.map() pega função passada e aplica linha a linha na tabela ao criar
# nova coluna
treino["sexo"] = treino["Sex"].map(binario)
teste["sexo"] = treino["Sex"].map(binario)
treino["embarque"] = treino["Embarked"].map(numerico)
teste["embarque"] = treino["Embarked"].map(numerico)

# Lista com parametros a serem levados em consideração para fazer a previsão
parametros = ["sexo", "Age", "Pclass", "Parch", "Fare"]

# Modelo trabalha com variaveis de entrada X que sera treinado, e y o que será
# previsto
X = treino[parametros]
y = treino["Survived"]


# Validação cruzada

resultados = []
# Lista de resultados onde será calculada a acuracia
X_treino, X_val, y_treino, y_val = train_test_split(X, y, test_size=0.6)
# função train_test_split é usada para dividir nossos dados de maneira padroni-
# zada, assim como foi passado 60% para teste e 40% para treino


KFold = RepeatedKFold(n_splits=2, n_repeats=10, random_state=10)
# função que faz a divisão para encontrar a divisão para treino e validação
# (ou teste) para poder encontrar acuracia do modelo, além de repetir essas
# divições

# laço dedicado para nos dizer aleatoriamente quais linhas devemos usar do
# treino e da validação
for linhas_treino, linhas_val in KFold.split(X):
    X_treino = X.iloc[linhas_treino]
    X_val = X.iloc[linhas_val]
    y_treino = y.iloc[linhas_treino]
    y_val = y.iloc[linhas_val]
    Floresta.fit(X_treino, y_treino)
# funçao.fit é a função usada para treinar o modelo para chegar em uma previsão
    valid = Floresta.predict(X_val)
# função .predict() usada para fazer a previção em cima das variaveis passadas
    acuracia = np.mean(y_val == valid)
    resultados.append(acuracia)

print("Acuracia: ", np.mean(resultados))

# Teste

# .fit é a função usada para treinar o modelo para chegar em uma previsão
Floresta.fit(X, y)

X_prev = teste[parametros]
pre = Floresta.predict(X_prev)
# É retornado uma array, logo com a função series, criamos uma serie que de
# "PassengerID" e a previsão "Survived"
previsao = pandinha.Series(pre, index=teste["PassengerId"], name="Survived")
previsao.to_csv("previsao", header=True)
