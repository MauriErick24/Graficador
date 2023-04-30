
import numpy as np
class Linea:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def dibujar(self):
        dx = abs(self.x2 - self.x1)
        dy = abs(self.y2 - self.y1)
        sx = 1 if self.x1 < self.x2 else -1
        sy = 1 if self.y1 < self.y2 else -1
        err = dx - dy
        x = self.x1
        y = self.y1

        # Matriz para almacenar las coordenadas de cada pixel
        coords = np.zeros((2, dx + dy), dtype=int)
        idx = 0

        while x != self.x2 or y != self.y2:
            coords[0, idx] = x
            coords[1, idx] = y
            idx += 1

            e2 = 2 * err
            if e2 > -dy:
                err -= dy
                x += sx
            if e2 < dx:
                err += dx
                y += sy

        # Agregar las coordenadas del último pixel
        coords[0, idx] = x
        coords[1, idx] = y
        idx += 1

        # Devolver la matriz de coordenadas
        return coords[:, :idx]

    def aumentaLongitud(self):
        # Aumentar la longitud de la línea en 1 píxel en ambos extremos
        if self.x1 < self.x2:
            self.x1 -= 1
            self.x2 += 1
        else:
            self.x1 += 1
            self.x2 -= 1

        if self.y1 < self.y2:
            self.y1 -= 1
            self.y2 += 1
        else:
            self.y1 += 1
            self.y2 -= 1

        # Actualizar los atributos con las nuevas coordenadas de los extremos de la línea
        self.x1 = max(0, self.x1)
        self.y1 = max(0, self.y1)
        self.x2 = max(0, self.x2)
        self.y2 = max(0, self.y2)

        # Actualizar la matriz de coordenadas con las nuevas coordenadas de la línea
        return self.dibujar()

    def disminuirLongitud(self):
        # Disminuir la longitud de la línea en 1 píxel en ambos extremos
        if self.x1 < self.x2:
            self.x1 += 1
            self.x2 -= 1
        else:
            self.x1 -= 1
            self.x2 += 1

        if self.y1 < self.y2:
            self.y1 += 1
            self.y2 -= 1
        else:
            self.y1 -= 1
            self.y2 += 1

        # Actualizar los atributos con las nuevas coordenadas de los extremos de la línea
        self.x1 = max(0, self.x1)
        self.y1 = max(0, self.y1)
        self.x2 = max(0, self.x2)
        self.y2 = max(0, self.y2)

        # Actualizar la matriz de coordenadas con las nuevas coordenadas de la línea
        return self.dibujar()

#matriz de dibujar
linea = Linea(50,20,145,100)
coordenadasDibujo=linea.dibujar()
print(coordenadasDibujo)

 #matriz que aumenta el tamanio cada que se llama al metodo aumentarLongitud()
""" print("Coordenadas modificadas para aumentar la longitud")
nuevasCoordenadas = linea.aumentaLongitud()
print(nuevasCoordenadas)
nuevasCoordenadas = linea.aumentaLongitud()
print(nuevasCoordenadas) """ 

#matriz que reduce el tamanio cada que se llama al metodo disminuirLongitud()
print("Coordenadas modificadas para disminuir la longitud")
nuevasCoordenadas = linea.disminuirLongitud()
print(nuevasCoordenadas)
nuevasCoordenadas = linea.disminuirLongitud()
print(nuevasCoordenadas)



