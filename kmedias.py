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

    while(suma_error >= Error):
        etiquetas[:] = 0
        contador_etiquetas[:] = 0
        suma_z[:] = 0
        suma_error = 0

        for i in range(filas):
            for j in range(columnas):
                
                for media in medias:
                    distancias.append(distancia_euclidiana_RGB(imagen[i][j], media))

                distancia_minima = min(distancias)
                etiqueta = distancias.index(distancia_minima)
                
                etiquetas[i][j] = etiqueta
                contador_etiquetas[etiqueta] +=1

                suma_z[etiqueta] = suma_z[etiqueta] + imagen[i][j]
                
                distancias.clear()

        medias_nuevas = inicializar_medias_RGB(k)

        for i in range(k):

            if(contador_etiquetas[i] != 0):
                medias_nuevas[i][0] = (suma_z[i][0]/contador_etiquetas[i])
                medias_nuevas[i][1] = (suma_z[i][1]/contador_etiquetas[i])
                medias_nuevas[i][2] = (suma_z[i][2]/contador_etiquetas[i])
            
            else:
                medias_nuevas[i][0] = random.randint(0, 255)
                medias_nuevas[i][1] = random.randint(0, 255)
                medias_nuevas[i][2] = random.randint(0, 255)

            suma_error += distancia_euclidiana_RGB(medias[i], medias_nuevas[i])

        medias = medias_nuevas


    return medias,etiquetas


def colorear_secciones(imagen_rgb, imagen_etiquetas, num_etiquetas):

    filas, columnas, _ = imagen_rgb.shape

    imagen_coloreada = np.zeros((filas, columnas,3))

    colores_promedio = []

    for etiqueta in range(num_etiquetas):
        indices_etiqueta = np.where(imagen_etiquetas == etiqueta)
        colores_etiqueta = imagen_rgb[indices_etiqueta]

        color_promedio_etiqueta = np.round(np.mean(colores_etiqueta, axis=0)).astype(int)
        colores_promedio.append(color_promedio_etiqueta)


    for i in range(filas):
        for j in range(columnas):

            imagen_coloreada[i][j][0] = int(colores_promedio[int(imagen_etiquetas[i][j])][0])
            imagen_coloreada[i][j][1] = int(colores_promedio[int(imagen_etiquetas[i][j])][1])
            imagen_coloreada[i][j][2] = int(colores_promedio[int(imagen_etiquetas[i][j])][2])

    return imagen_coloreada/255



'''

#-------------------------------------------------------------
imagen_prueba = io.imread("images/202277_sat_15.jpg")

vectores_cluster, etiquetada = kmedias(3,imagen_prueba,0.5)

imagen_coloreada = colorear_secciones(imagen_prueba,etiquetada,3)
plt.imshow(imagen_coloreada)
plt.show()

'''