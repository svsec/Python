#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 23:46:45 2020

@author: adal
"""
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

# Procedimentos um pouco mais avançados

# Dimensionamento
# |cv.resize()
# |cv.INTER_AREA (interpolação)
# |cv.INTER_CUBIC ou cv.INTER_LINEAR (interpolação)

# Rotação
# |cv.getRotationMatrix2D

# Transformação afim //pesquisar mais a fundo
# Transformação de Perspectiva *IMPORTANTE*
# |cv.getPerspectiveTransform
# |cv.warpPerspective

# Gradientes da Imagem
# | Sobel
# | Scharr
# | Laplacian
