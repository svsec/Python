#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 22:04:09 2020

@author: adal
"""

import cv2 as cv

# função de retorno do mouse
def marcar(event, x, y, flags, param):
    # se houver click no botão esquerdo do mouse
    if event == cv.EVENT_LBUTTONDOWN:
        # MARCA ONDE FOI O CLICKcoordenas(x, y)
        l_pontos.append((x, y))
        print(f"coordenadas {x} e {y}")
        x_len = 3
        cv.line(image, (x+x_len, y+x_len), (x-x_len, y-x_len), (0, 250, 0), 1)
        cv.line(image, (x+x_len, y-x_len), (x-x_len, y+x_len), (0, 250, 0), 1)
        cv.imshow("image", image)



l_pontos = [] # lista dos pontos marcados na figura 
dicionario = {"img": 1, "pontos": l_pontos}  
# Dicionario com a chave referente a imagem, e o valor da chave com a lista 
image = cv.imread("imagem.jpg")  # leitura da imagem
cv.namedWindow("image")  # nomeando a janela
cv.setMouseCallback("image", marcar)  # retorna os eventos do mouse na janela


# fazendo um laço para manter a tela aberta até que seja apertado a tecla 'c'
while True:
    cv.imshow("image", image)
    key = cv.waitKey(0) & 0xFF
    # esperar pelo 'q'
    if key == ord("c"):
        break

print("saindoooo")
cv.destroyAllWindows()
