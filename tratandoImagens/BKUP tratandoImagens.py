# -*- coding: utf-8 -*-

import cv2
import os

# CARREGAR IMAGEM
image = cv2.imread("2011-01-19-07-49-38.pgm")
# cv2.imshow("original", image)
# cv2.waitKey(0)

# CORTAR IMAGENS
# print image.shape
(h, w) = image.shape[:2]

occupied_thresh = 0.65
free_thresh = 0.196

xi = 0
yi = 0
xf = 200
yf = 200
ix = 0
iy = 0
label = (0, 0)
imagem_db = bool(0)

while ix < image.shape[0] and iy < image.shape[1]:

    for b in range(image.shape[1] / yf):
        for a in range(image.shape[0] / xf):
            # CORTAR A IMAGEM
            cropped = image[xi+ix:xf+ix, yi+iy:yf+iy]
            # cv2.imshow("cropped", cropped)
            # cv2.waitKey(0)

            # TESTAR SE A IMAGEM POSSUI DADOS OCC E NÃO OCC
            label = (b, a)

            print ("Imagem {} só possui dados 'unknown'".format(label))
            # SALVAR IMAGEM CORTADA EM UMA NOVA PASTA DO DATASET
            num_imagem = 0
            if imagem_db == bool(0):
                imagem_db = bool(0)
                #os.makedirs('/home/au16/codigosTeste/tratandoImagens/db/'+str(label))
                #os.chdir("/home/au16/codigosTeste/tratandoImagens/db/"+str(label))
                #cv2.imwrite(str(num_imagem)+".pgm", cropped)
                # print cropped.shape
                num_imagem = num_imagem + 1
            ix = ix + xf
        iy = iy + yf
        ix = 0



'''
    If negate is false, p = (255 - x) / 255.0.
    This means that black (0) now has the highest value (1.0)
    and white (255) has the lowest (0.0)
    If p > occupied_thresh, output the value 100 to indicate the cell is occupied.
    If p < free_thresh, output the value 0 to indicate the cell is free.
'''

# ROTACIONAR IMAGEM