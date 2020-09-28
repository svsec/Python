#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 12:43:46 2020

@author: adal
"""
# Primeiros comandos para a leitura de imagens
# Será usado a ferramenta OepnCV (Open source computer vision)/biblioteca
# Pode-se alterar valor de pixel


# Leitura de uma imagem que necessariamente precisa estar no diretorio do
# projeto
# Usa-se a função cv2.imread()

import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

# carregar uma foto (com cor em preto e branco)
# Segundo argumento é um flag que especifica a maneira que a imagem deve ser
# lida
# cv.IMREAD_COLOR carrega uma foto colorida e qualquer transparencia sera
# negligenciada (1)
# cv.IMREAD_GRAYSCALE (0)
# cv.IMREAD_UNCHARGED carrega a imagem como tal, incluindo o canal alfa (-1)
# obs: PODE-SE passar apenas os numeros
img = cv.imread('imagem.jpg')

# mostrar a imagem usa-se cv2.imshow

cv.imshow('image', img)
# key é uma função que esta ligada ao teclado. O argumento passado a ela é o
# tempo em milesimos de segundo.
# esta especifica o que ocorrera no teclado, se voce apertar qualquer tecla
# dentro do tempo o programa continuará,
# mas se for passado o valor "0" ele esperara indefinidamente, mas tambem pode
# ser usado para detectar teclas especificas.

k = cv.waitKey(0) & 0xFF

# destroi toda janela que foi criada antes
# cv2.destroyallwindows()
# para destruir uma janela especifica usa a função cv2.destroyWindow, passando
# o nome exato da janela


# salvar uma imagem
# primeiro argumento é o nome do arquivo, e depois a imagem que quer salvar
# cv2.imwrite('messigray.png', img)

# EXEMPLO
if k == 27:  # espera pelo botão esc
    cv.destroyAllWindows()
elif k == ord('s'):  # espera pelo pela tecla 's' para salvar e sair
    cv.imwrite('gray.png', img)
    cv.destroyAllWindows()   # ou pode-se usar cv2.destroyWindow('image')

# Espaços de cores, são como as cores são armazenadas
# os mais populares são: BGR(padrão), CMYK (ciano,magenta,amarelo e preto)
# e HSV (matriz,saturação, valor)
# acessar e modificar os valores de pixel
# pode-se acessar o valor dos pixel pelos seus parametros de coluna e linha
# uma imagem BGR retorna um matriz de valores azul(0), verde(1) e vermelho(2).
# para uma imagem em cinza apenas retorna a intensidade.
# exemplo :

px = img[100][100]
print(px)

# acessando apenas o pixel azul
azul = img.item(100, 100, 0)   # //ERROR: perguntar ao professor
print(azul)

# é possivel modificar os valores dos pixels

img[100, 100] = 255
print(img[100][100])

# este metodo é usado para regiões especificas
# o metodo mais rapido seria pela array.item
# img.item(10, 10)

# e para modificar seria array.itemset
img.itemset((10, 10, 0), 100)

# array.shape retorna o numero de linha colunas e se colorida os canais
altura, largura, canais = img.shape
