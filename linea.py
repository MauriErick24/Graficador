import tkinter as tk
import numpy as np
import time
import math
class Linea:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.angulo = 0


    def dibujar(self):
        dx = abs(self.x2 - self.x1)
        dy = abs(self.y2 - self.y1)
        sx = 1 if self.x1 < self.x2 else -1
        sy = 1 if self.y1 < self.y2 else -1
        err = dx - dy
        x = self.x1
        y = self.y1

        # Lista para almacenar las coordenadas de cada pixel
        coords = []

        while True:
            coords.append([x, y])

            # Si llegamos al final de la línea, salir del loop
            if x == self.x2 and y == self.y2:
                break

            # Calcular el error fraccional
            e2 = err * 2
            if e2 > -dy:
                err -= dy
                x += sx
            if e2 < dx:
                err += dx
                y += sy

        # Devolver la matriz de coordenadas
        return np.array(coords).T

    def aumentarLongitud(self):
        # Verificar la pendiente de la línea
        if self.x2 == self.x1:
            m = 0
        else:
            m = (self.y2 - self.y1) / (self.x2 - self.x1)

        # Verificar la dirección de la línea
        if self.x1 < self.x2:
            # Línea diagonal hacia arriba a la derecha
            if m < 0 and self.y1 > self.y2:
                nuevo_x2 = self.x2 + 1
                nuevo_y2 = self.y2 - 1
                nuevo_x1 = self.x1 - 1
                nuevo_y1 = self.y1 + 1
            # Línea diagonal hacia abajo a la derecha
            else:
                nuevo_x2 = self.x2 + 1
                nuevo_y2 = int(round(self.y2 + m))
                nuevo_x1 = self.x1 - 1
                nuevo_y1 = int(round(self.y1 - m))
        else:
            # Línea diagonal hacia abajo a la izquierda
            if m > 0 and self.y1 < self.y2:
                nuevo_x2 = self.x2 - 1
                nuevo_y2 = self.y2 + 1
                nuevo_x1 = self.x1 + 1
                nuevo_y1 = self.y1 - 1
            # Línea diagonal hacia arriba a la izquierda
            else:
                nuevo_x2 = self.x2 - 1
                nuevo_y2 = int(round(self.y2 - m))
                nuevo_x1 = self.x1 + 1
                nuevo_y1 = int(round(self.y1 + m))

        # Actualizar los puntos de la línea
        self.x1 = nuevo_x1
        self.y1 = nuevo_y1
        self.x2 = nuevo_x2
        self.y2 = nuevo_y2

        # Devolver la matriz actualizada con la línea dibujada
        return self.dibujar()

    def disminuirLongitud(self):
        # Verificar la pendiente de la línea
        if self.x2 == self.x1:
            m = 0
        else:
            m = (self.y2 - self.y1) / (self.x2 - self.x1)

        # Verificar la dirección de la línea
        if self.x1 < self.x2:
            # Línea diagonal hacia arriba a la derecha
            if m < 0 and self.y1 > self.y2:
                nuevo_x2 = self.x2 - 1
                nuevo_y2 = self.y2 + 1
                nuevo_x1 = self.x1 + 1
                nuevo_y1 = self.y1 - 1
            # Línea diagonal hacia abajo a la derecha
            else:
                nuevo_x2 = self.x2 - 1
                nuevo_y2 = int(round(self.y2 - m))
                nuevo_x1 = self.x1 + 1
                nuevo_y1 = int(round(self.y1 + m))
        else:
            # Línea diagonal hacia abajo a la izquierda
            if m > 0 and self.y1 < self.y2:
                nuevo_x2 = self.x2 + 1
                nuevo_y2 = self.y2 - 1
                nuevo_x1 = self.x1 - 1
                nuevo_y1 = self.y1 + 1
            # Línea diagonal hacia arriba a la izquierda
            else:
                nuevo_x2 = self.x2 + 1
                nuevo_y2 = int(round(self.y2 + m))
                nuevo_x1 = self.x1 - 1
                nuevo_y1 = int(round(self.y1 - m))

        # Actualizar los puntos de la línea
        self.x1 = nuevo_x1
        self.y1 = nuevo_y1
        self.x2 = nuevo_x2
        self.y2 = nuevo_y2

        # Devolver la matriz actualizada con la línea dibujada
        return self.dibujar()

    def rotar(self):
        # Calcular el punto medio de la línea
        cx = (self.x1 + self.x2) / 2
        cy = (self.y1 + self.y2) / 2

        # Calcular las coordenadas de los extremos de la línea rotada
        dx1 = self.x1 - cx
        dy1 = self.y1 - cy
        dx2 = self.x2 - cx
        dy2 = self.y2 - cy
        angulo_rad = math.radians(self.angulo)
        coseno = math.cos(angulo_rad)
        seno = math.sin(angulo_rad)
        nuevo_dx1 = dx1 * coseno - dy1 * seno
        nuevo_dy1 = dx1 * seno + dy1 * coseno
        nuevo_dx2 = dx2 * coseno - dy2 * seno
        nuevo_dy2 = dx2 * seno + dy2 * coseno

        # Actualizar los puntos de la línea
        self.x1 = int(round(cx + nuevo_dx1))
        self.y1 = int(round(cy + nuevo_dy1))
        self.x2 = int(round(cx + nuevo_dx2))
        self.y2 = int(round(cy + nuevo_dy2))

        # Actualizar el ángulo de rotación
        self.angulo += 3

        # Devolver la matriz actualizada con la línea dibujada
        return self.dibujar()



    def moverDerecha(self):
        self.x1 += 3
        self.x2 += 3
        return self.dibujar()

    def moverIzquierda(self):
        self.x1 -= 3
        self.x2 -= 3
        return self.dibujar()

    def moverAbajo(self):
        self.y1 += 3
        self.y2 += 3
        return self.dibujar()

    def moverArriba(self):
        self.y1 -= 3
        self.y2 -= 3
        return self.dibujar()






# Crear ventana y canvas
ventana = tk.Tk()
canvas = tk.Canvas(ventana, width=400, height=400)
canvas.pack()

# Crear instancia de la clase Linea y obtener la matriz de coordenadas
linea = Linea(50, 20, 200, 150)
coords = linea.dibujar()
print(coords)

# Crear una lista de pares de coordenadas a partir de la matriz
coord_list = [[coords[0][i], coords[1][i]] for i in range(len(coords[0]))]

# Dibujar la línea en el canvas
linea_dibujada = canvas.create_line(coord_list, width=3)

""" for i in range(100):
    # Aumentar la longitud de la línea
    coords = linea.aumentarLongitud()

    # Obtener la nueva lista de coordenadas
    coord_list = coords.T.flatten().tolist()

    # Actualizar la línea dibujada en el canvas
    canvas.coords(linea_dibujada, coord_list)

    ventana.update()
    time.sleep(1)
     """
""" for i in range(100):
    # Aumentar la longitud de la línea
    coords = linea.disminuirLongitud()

    # Obtener la nueva lista de coordenadas
    coord_list = coords.T.flatten().tolist()

    # Actualizar la línea dibujada en el canvas
    canvas.coords(linea_dibujada, coord_list)

    ventana.update()
    time.sleep(1)  """
    
""" for i in range(100):
    # Aumentar la longitud de la línea
    coords = linea.rotar()

    # Obtener la nueva lista de coordenadas
    coord_list = coords.T.flatten().tolist()

    # Actualizar la línea dibujada en el canvas
    canvas.coords(linea_dibujada, coord_list)

    ventana.update()
    time.sleep(1)  """
    
for i in range(30):
    # Aumentar la longitud de la línea
    coords = linea.rotar()

    # Obtener la nueva lista de coordenadas
    coord_list = coords.T.flatten().tolist()

    # Actualizar la línea dibujada en el canvas
    canvas.coords(linea_dibujada, coord_list)

    ventana.update()
    time.sleep(1) 

# Iniciar el loop de la ventana
ventana.mainloop() 