#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 18:21:42 2020

@author: adal
"""
import numpy as np
import pandas as pandinha

# Lendo o arquivo de extensão csv
# Foi necessario usar o caminho para o arquivo
# pode-se usar mais parâmetros para identificar o padrão de letras
# tipo de variavel será DataFrame
test = pandinha.read_csv("/home/adal/IC (Python)/titanic/test.csv")
train = pandinha.read_csv("/home/adal/IC (Python)/titanic/train.csv")

# para acessar uma ou mais colunas usamos o nome da coluna como indice
# dentro do head podemos especificar quantas linhas iremos querer usar
test["Name"].head(2)
test.Name.head(2)
# ambas retornaram mesmo resultado

# ou mais de uma coluna
test[["Name", "Pclass"]].head(3)


# função loc servirá para pegarmos linhas e colunas especificas pelo INDICE!
test.loc[1:2]

# podemos acrescentar uma ou mais colunas e linhas especificas
test.loc[[1, 2, 7], ['Name', 'Pclass']]

# função loc só trabalha com valores numero para selecionar as linhas e colunas
test.iloc[2:6, 1:4]

# função sort_values() esta que ordena as colunas passadas mas não alterara os dados
test.sort_values("Name")

# porém se adicionarmos o parametro inplace = True a tabela será alterada
test.sort_values("PassengerId", inplace = True)

# filter é uma função equivalente para selecionar colunas especificas
test.filter(itens = ["Name", "Pclass"]).head()

# É possivel realizar operações logicas ("==" igual) (& E) ( | OU) também
train[train.Survived == 1].head
# usando a função isin podemos substituir o operador OU




