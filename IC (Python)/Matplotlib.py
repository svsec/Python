#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 20:17:07 2020

@author: adal
"""
import numpy as np
import cv2
from matplotlib import pyplot as plt


def mostrar(img):
    # A renderização de imagens do matplotlib é contraria ao do python ou seja
    # é preciso inverter as cores
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # AQUI estamos invertendo os
# padroes azuis e vermelhos enquanto os verdes se matem

    plt.imshow(img)
    plt.show()
    
def main():
    # importar imagens com matplotlib
    img = cv2.imread('imagem.jpg')
    
    mostrar(img)
    
# é possivel fazer recortes na imagem atribuindo as coordenadas exatas em uma 
# variavel
# a biblioteca cv sempre usa-se o eixo y primeiro e é positivo indo de cima para
# baixo
    recorte = img[200 : 400, 200 : 400]
    plt.imshow(recorte)
    plt.show()
    
    

   
    
main()
