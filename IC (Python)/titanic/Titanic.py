#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct

@author: adal
"""

import numpy as np
import pandas as pandinha
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
# função que faz a divisão para encontrar a divisão para treino e validação
# (ou teste)
# from sklearn.model_selection import Kfold


# Arquivo dedicado à aprendizagem de Machine Learning(ML)

# Este problema faz uma alusão ao acidente ocorrido com o navio Titanic onde
# diversas pessoas morreram, porém houve alguns sobreviventes, este algoritmo
# e centrado em tentar descobrir o maior numero de pessoas, que sobreviveram


# Puxando as tabelas com informações a serem averiguadas
teste = pandinha.read_csv("/home/adal/IC (Python)/titanic/test.csv")
treino = pandinha.read_csv("/home/adal/IC (Python)/titanic/train.csv")


Floresta = RandomForestClassifier(n_estimators=150, n_jobs=(-1),
                                  random_state=(0))
# Metodo Random Florest
# n_estimators é o numero de arvores
# random_state é a mesma coisa que np.random_seed(0) para tirar a aleatoriedade
# (semente)
# função .fillna() transformará todos valores nulos ou que estão faltando
# em algum paramentro passado
teste = teste.fillna(-1)
treino = treino.fillna(-1)

# Partindo dos dados, ele diz que mulheres sempre sobrevivem, mas se fizermos
# uma alusão historica ao filme "Titanic" os primeiros a serem salvos são
# mulheres e crianças
# Adicionei o parametro "Pclass" já que pode ser que a classe em que o
# passageiro se encontrava o tivesse ajudado a se regastado também

# Lista com parametros a serem levados em consideração para fazer a previsão
parametros = ["sexo", "Age", "Pclass"]


# Nosso modelo só trabalha com numeros, logo é preciso transformar essa coluna
# em algo relativo ( 1 para homens e 0 para mulheres)
def binario(sexo):
    if sexo == "male":
        return 1
    else:
        return 0


# criando uma nova instancia de coluna e adicionando-a a tabela de treino
# e teste para padronizar
# função .map() pega função passada e aplica linha a linha na tabela
treino["sexo"] = treino["Sex"].map(binario)
teste["sexo"] = treino["Sex"].map(binario)

# Modelo trabalha com variaveis de entrada X que sera treinado, e y o que será
# previsto
X = treino[parametros]
y = treino["Survived"]

# .fit é a função usada para treinar o modelo para chegar em uma previsão
Floresta.fit(X, y)
X_prev = teste[parametros]

# função .predict() usada para fazer a previção em cima das variaveis passadas
pre = Floresta.predict(X_prev)
# É retornado uma array, logo com a função series, criamos uma serie que de
# "PassengerID" e a previsão "Survived"
previsao = pandinha.Series(pre, index=teste["PassengerId"], name="Survived")
previsao.to_csv("ta_indo", header=True)


# fase de validação

# X_treino, X_val, y_treino, y_val = train_test_split(X, y, test_size=0.5)
# Floresta.fit(X_treino, y_treino)
# prev_val = Floresta.predict(X_val)
# np.mean(y_val == prev_val) é função para encontrar a relação entre a
# validação e o treino

# validação cruzada
# divide dados em blocos
