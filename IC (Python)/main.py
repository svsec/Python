@author: Adalberto
"""

import cv2 as cv
import os  #funções para interarir com SO
import json  #biblioteca para ler e guardar arquivos json

arquivo_base = "bufalo"  # pasta com imagens
l_pontos = []  # lista pontos

Dados = {"versão": 1.0, "resolucao":(800, 600), "imagens": []}
# dicionario com {versão, resolução padrão das imagens, e uma lista de dicionarios de imagens com pontos}

# função para interação com imagem
def marcar(event, x, y, flags, param):
    # se houver click no botão esquerdo do mouse
    if event == cv2.EVENT_LBUTTONDOWN:
        # MARCA ONDE FOI O CLICKcoordenas(x, y)
        l_pontos.append((x, y))
        print(f"coordenadas {x} e {y}")
        x_len = 5
        cv2.line(image, (x+x_len, y+x_len), (x-x_len, y-x_len), (0, 250, 0), 2)
        cv2.line(image, (x+x_len, y-x_len), (x-x_len, y+x_len), (0, 250, 0), 2)
        cv2.imshow("image", image)


cv2.namedWindow("image")  # nomeando a janela
cv2.setMouseCallback("image", marcar)  # retorna os eventos do mouse na janela 

# cria uma lista apenas com as imagens dentro da pasta
f_list = os.listdir(arquivo_base)  # função retorna lista de arquivos da pasta
clean_f_list = [f for f in f_list if f[-3:] == 'jpg'] 
# está filtrando a lista para conter somente imagens

for i in clean_f_list:

	print("Imagem: ", i)
	#  Le e padroniza a imagem
	original_img = cv.imread(os.path.join(folder, i))
	image = cv.resize(original_img,Dados["resolução"])
	
	#  mostrando imagen e destacando pontos
	while True:
		cv.imshow("image", image)
		key = cv.waitKey(500) & 0xFF
		#  vai esperar 3 pontos caso não seja clicado, é só apertar tecla 'c' para fechar
		if key == ord("c") or len(l_pontos) > 2:
			break;

	# adiciona a imagem e os pontos a lista de dicionarios no dicionario principal "Dados"
	Dados["imagens"].append({"i": i, "pts": l_pontos.copy()})
	# Pode-se perceber que passamos apenas uma copia da lista dos pontos porque ele sera esvaziado abaixo
	l_pontos = []

#  criamos um arquivos para adicionar a ele nosso dicionario principal "Dados"
arquivo = open("Dados.txt", "w") 
arquivo.write(json.dumps(Dados, indent=3))
#  a biblioteca json é usado para transformar facilmente objetos no caso um dicionario em strings
#  biblioteca json é muito padrão em diversas linguagens para fazer esse armajenamento de dados ou mesmo leitura mais facilmente
#  e para maior facilidade, o mesmo tem mesma sintaxe que um dicionario

print("saindooooo")
cv.destroyAllWindows()