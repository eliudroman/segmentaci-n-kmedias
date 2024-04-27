import numpy as np
import random
import math
from skimage import io
import matplotlib.pyplot as plt


def distancia_euclidiana_RGB(z, m):

    return math.sqrt((z[0]-m[0])**2 + (z[1]-m[1])**2 + (z[2]-m[2])**2)


def inicializar_medias_RGB(k):
    
    medias = []

    for punto in range(k):
        R = random.randint(0, 255)
        G = random.randint(0, 255)
        B = random.randint(0, 255)

        medias.append([R,G,B])
    
    return medias


def kmedias(k, imagen, Error):
    
    filas,columnas,_ = imagen.shape

    medias = inicializar_medias_RGB(k)
    #medias = [[255,0,0],[0,255,0],[0,0,255]]
    distancias = []
    
    etiquetas = np.zeros((filas, columnas))
    contador_etiquetas = np.zeros(k)

    suma_z = np.zeros((k, 3))
    suma_error = Error + 1
    sum_distancias_minimas=0

    while(suma_error >= Error):
        etiquetas[:] = 0
        contador_etiquetas[:] = 0
        suma_z[:] = 0
        suma_error = 0
        sum_distancias_minimas=0

        for i in range(filas):
            for j in range(columnas):
                
                for media in medias:
                    distancias.append(distancia_euclidiana_RGB(imagen[i][j], media))

                distancia_minima = min(distancias)
                sum_distancias_minimas+=distancia_minima
                etiqueta = distancias.index(distancia_minima)
                
                etiquetas[i][j] = etiqueta
                contador_etiquetas[etiqueta] +=1

                suma_z[etiqueta] = suma_z[etiqueta] + imagen[i][j]
                
                distancias.clear()

        medias_nuevas = inicializar_medias_RGB(k)

        for i in range(k):
            medias_nuevas[i][0] = (suma_z[i][0]/contador_etiquetas[i])
            medias_nuevas[i][1] = (suma_z[i][1]/contador_etiquetas[i])
            medias_nuevas[i][2] = (suma_z[i][2]/contador_etiquetas[i])

            suma_error += distancia_euclidiana_RGB(medias[i], medias_nuevas[i])

        medias = medias_nuevas


    return medias,etiquetas,sum_distancias_minimas




imagen_prueba = io.imread("images/202277_sat_15.jpg")

 
vectores_cluster, etiquetada = kmedias(3,imagen_prueba,0.5)

plt.imshow(etiquetada)
plt.show()
