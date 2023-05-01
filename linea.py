import tkinter as tk
import numpy as np
import time
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
        if self.x2 - self.x1 > 0:
            # Línea diagonal hacia abajo desde el lado izquierdo
            m = (self.y2 - self.y1) / (self.x2 - self.x1)
            b = self.y1 - m * self.x1
            nuevo_x2 = self.x2 + 1
            nuevo_y2 = m * nuevo_x2 + b
            nuevo_x1 = self.x1 - 1            
            nuevo_y1 = m * nuevo_x1 + b
        else:
            # Línea diagonal hacia arriba desde el lado izquierdo
            m = (self.y1 - self.y2) / (self.x1 - self.x2)
            b = self.y1 - m * self.x1
            nuevo_x2 = self.x2 - 1
            nuevo_y2 = m * nuevo_x2 + b
            nuevo_x1 = self.x1 + 1            
            nuevo_y1 = m * nuevo_x1 + b
        
        self.x1 = nuevo_x1
        self.y1 = nuevo_y1
        self.x2 = nuevo_x2
        self.y2 = nuevo_y2
        # Devolver la matriz actualizada con la línea dibujada
        return self.dibujar()

    def disminuirLongitud(self):
        m = int((self.y2 - self.y1) / (self.x2 - self.x1))
        b = self.y1 - m * self.x1
        nuevo_x2 = self.x2 - 1
        nuevo_y2 = m * nuevo_x2 + b
        nuevo_x1 = self.x1 + 1
        nuevo_y1 = m * nuevo_x1 + b

        self.x1 = nuevo_x1
        self.y1 = nuevo_y1
        self.x2 = nuevo_x2
        self.y2 = nuevo_y2

        # Devolver la matriz actualizada con la línea dibujada
        return self.dibujar()


# Crear ventana y canvas
ventana = tk.Tk()
canvas = tk.Canvas(ventana, width=400, height=400)
canvas.pack()

# Crear instancia de la clase Linea y obtener la matriz de coordenadas
linea = Linea(20, 220, 200, 30)
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
    time.sleep(1) """
    
for i in range(100):
    # Aumentar la longitud de la línea
    coords = linea.disminuirLongitud()

    # Obtener la nueva lista de coordenadas
    coord_list = coords.T.flatten().tolist()

    # Actualizar la línea dibujada en el canvas
    canvas.coords(linea_dibujada, coord_list)

    ventana.update()
    time.sleep(1) 

# Iniciar el loop de la ventana
ventana.mainloop() 