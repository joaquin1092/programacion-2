from PIL import Image
import numpy as np
imagen = Image.open("perro.jpg")

pixels = np.array(imagen)
alto, ancho, canales = pixels.shape

salida = np.zeros_like(pixels)

kernel = np.ones((5, 5), dtype=np.float32) / 25

margen = 2  

for canal in range(3):
    for i in range(margen, alto - margen):
        for j in range(margen, ancho - margen):
            region = pixels[i - margen:i + margen + 1, j - margen:j + margen + 1, canal]
            valor = np.sum(region * kernel)
            salida[i, j, canal] = int(valor)

imagen_desenfocada = Image.fromarray(salida)

imagen.show(title="Original")
imagen_desenfocada.show(title="Desenfocada")
