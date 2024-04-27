import numpy as np
import random

def kmedias(k, imagen, Error):
    
    medias = []

    for punto in range(k):
        R = random.randint(0, 255)
        G = random.randint(0, 255)
        B = random.randint(0, 255)

        medias.append([R,G,B])
    
    print(medias)


kmedias(3,0.5)