"""-------------------------------------------------------------------------------------------------
Este archivo contiene lo necesario para analizar el grupo de pixeles y determinar un k optimo

Contiene una función que imprime los pixeles de la imagen en un espacio tridimensional, de
esta manera el analista puede observar grupos probables y definir un rango.

Contiene una función que ejecuta k medias un numero N de veces de acuerdo al rango de k definido
por el analista y determina cuál de los k dentro del rango produce el menor resultado de distancias
entre los pixeles y los centroides
-------------------------------------------------------------------------------------------------"""
import cv2
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from kmedias import kmedias

def grafica_pixeles3d(ruta_img):

    imagen = cv2.imread(ruta_img)
    #imagen = imagen.astype(float) / 255.0
    
    alto, ancho, _ = imagen.shape

    pixeles = [] #Lista para almacenar los diccionarios de píxeles
    colores=[] #Lista para almacenar las tuplas para los colores

    #Recorrido de imagen
    for i in range(alto):
        for j in range(ancho):
            r, g, b = imagen[i, j]
            pixeles.append({'R': r, 'G': g, 'B': b}) #Se guarda el vector de características como diccionario
            colores.append((r/255,g/255,b/255)) #Se guarda una tupla con el color

    #Se crea el DataFrame a partir de la lista de diccionarios
    df = pd.DataFrame(pixeles)

    #Creación de la gráfica
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(df['R'], df['G'], df['B'], c=colores, s=5, cmap='viridis')
    ax.set_xlabel('Rojo')
    ax.set_ylabel('Verde')
    ax.set_zlabel('Azul')
    plt.show()

def koptimo(imagen,kinf,ksup,deltaT):
    distancias=[]
    for k in range(kinf,ksup+1):
        distanciak,_=kmedias(k,imagen,deltaT)
        distancias.append(distanciak)
        print(f"Distancia minima para D_min({k})={distanciak}\n")
    indice_min=distancias.index(min(distancias))
    indice_min=indice_min-(ksup-kinf+1)+ksup

    return indice_min





