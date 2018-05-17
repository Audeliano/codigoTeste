# -*- coding: utf-8 -*-

'''
    If negate is false, p = (255 - x) / 255.0.
    This means that black (0) now has the highest value (1.0)
    and white (255) has the lowest (0.0)
    If p > occupied_thresh, output the value 100 to indicate the cell is occupied.
    If p < free_thresh, output the value 0 to indicate the cell is free.
'''

import cv2
import os

def augDataset():

    # CARREGAR IMAGEM
    image = cv2.imread("2011-01-19-07-49-38.pgm")
    # cv2.imshow("original", image)
    # cv2.waitKey(0)

    occupied_thresh = 0.65
    free_thresh = 0.196

    xi = 0
    yi = 0
    xf = 200
    yf = 200
    ix = 0
    iy = 0
    label = (0,0)
    imagem_db = bool(0)


    while ix < image.shape[0] and iy < image.shape[1]:
        # LAÇO PARA SEPARAR IMAGENS DE 200x200
        for b in range(image.shape[1] / yf):
            for a in range(image.shape[0] / xf):
                # LAÇO PARA PERCORRER PIXEL POR PIXEL DE CADA IMAGEM 200x200
                for k in range(yf):
                    for j in range(xf):
                        # LÊ O VALOR DO PIXEL E ANALISA SE POSSUI CÉLULA OCC OU NÃO OCC
                        (dado_pixel, canal2, canal3) = image[xi + ix + j, yi + iy + k]
                        dado_occ = (255 - dado_pixel) / 255.0
                        if dado_occ > occupied_thresh or dado_occ < free_thresh:
                            imagem_db = bool(1)

                            # CORTAR A IMAGEM
                            cropped = image[xi + ix:xf + ix, yi + iy:yf + iy]
                            cv2.imshow("cropped", cropped)
                            break
                label = (b, a)
                if imagem_db == bool(0):
                    print ("Imagem {} só possui dados 'unknown'".format(label))

                # SALVAR IMAGEM CORTADA EM UMA NOVA PASTA DO DATASET
                num_imagem = 0
                if imagem_db == bool(1):
                    imagem_db = bool(0)
                    os.makedirs('/home/au16/codigosTeste/tratandoImagens/db/'+str(label))
                    os.chdir("/home/au16/codigosTeste/tratandoImagens/db/"+str(label))
                    cv2.imwrite(str(num_imagem)+".pgm", cropped)

                    # ROTACIONAR IMAGEM
                    (h, w) = cropped.shape[:2]
                    centro = (w/2, h/2)
                    fator_de_rotacao = 10
                    r = 1
                    while r < 360 / fator_de_rotacao:
                    #for r in range(360 / fator_de_rotacao):
                        num_rot = (r * fator_de_rotacao)
                        M = cv2.getRotationMatrix2D(centro, r * fator_de_rotacao, 1.0)
                        rotated = cv2.warpAffine(cropped, M, (h, w))
                        cv2.imshow("rotated", rotated)
                        os.chdir("/home/au16/codigosTeste/tratandoImagens/db/" + str(label))
                        cv2.imwrite(str(num_rot) + ".pgm", rotated)
                        r = r + 1

                    num_imagem = num_imagem + 1

                ix = ix + xf
            iy = iy + yf
            ix = 0

augDataset()
