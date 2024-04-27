from koptimo import grafica_pixeles3d, koptimo
from kmedias import kmedias, colorear_secciones

import matplotlib.pyplot as plt
from skimage import io

print('Algoritmo de Kmedias para la segmentación de Imagenes RGB')

rutas_imagenes = []
rutas_imagenes.append('images/202277_sat_05.jpg')
rutas_imagenes.append('images/202277_sat_06.jpg')
rutas_imagenes.append('images/202277_sat_14.jpg')
rutas_imagenes.append('images/202277_sat_15.jpg')


for ruta in rutas_imagenes:

    imagen = io.imread(ruta)
    k = koptimo(imagen, 2, 4, 0.5)

    _,etiquetada,_ = kmedias(k,imagen,0.5)
    imagen_coloreada = colorear_secciones(imagen,etiquetada,k)

    fig, axs = plt.subplots(1, 2, figsize=(10, 4))  # 1 fila y 2 columnas para las imágenes
    axs[0].imshow(imagen)
    axs[0].set_title('Imagen Original')

    axs[1].imshow(imagen_coloreada)
    axs[1].set_title(f'Imagen Segmentada, k = {k}')

    plt.tight_layout()
    plt.show()

