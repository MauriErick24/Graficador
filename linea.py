import numpy as np
import tkinter as tk

class Linea:
    def dibujar(self, x1, y1, x2, y2):
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        sx = 1 if x1 < x2 else -1
        sy = 1 if y1 < y2 else -1
        err = dx - dy
        x = x1
        y = y1

        # Matriz para almacenar las coordenadas de cada pixel
        coords = np.zeros((2, dx + dy), dtype=int)
        idx = 0

        while x != x2 or y != y2:
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

    def cambiarLongitud(self, x1, y1, x2, y2):
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        sx = 1 if x1 < x2 else -1
        sy = 1 if y1 < y2 else -1
        err = dx - dy
        x = x1
        y = y1

        # Crear una matriz temporal más grande
        coords_temp = np.zeros((2, 2*(dx + dy)), dtype=int)
        idx = 0

        while x != x2 or y != y2:
            coords_temp[0, idx] = x
            coords_temp[1, idx] = y
            idx += 1

            e2 = 2 * err
            if e2 > -dy:
                err -= dy
                x += sx
            if e2 < dx:
                err += dx
                y += sy

        # Agregar las coordenadas del último pixel
        coords_temp[0, idx] = x
        coords_temp[1, idx] = y
        idx += 1

        # Copiar los valores de la matriz más pequeña en la matriz temporal
        coords = np.zeros((2, idx), dtype=int)
        coords[:, :idx] = coords_temp[:, :idx]

        # Devolver la matriz de coordenadas
        return coords



#matriz de dibujar
linea = Linea()
coordenadasDibujo=linea.dibujar(50,50,100,100)
print(coordenadasDibujo)
#matriz que aumento o disminuye
nuevasCoordenadas = linea.cambiarLongitud(25,25,90,90)
print(nuevasCoordenadas)






#lo de abajo es para probar nomas como se ve en la garfica, funciona
""" 
 #Crear una ventana y un lienzo
ventana = tk.Tk()
canvas = tk.Canvas(ventana, width=300, height=300)
canvas.pack()

# Crear la línea y obtener las coordenadas
linea = Linea()
coords = linea.dibujar(25,25,200,200)
print(coords)

# Dibujar la línea en el lienzo
for i in range(len(coords[0])-1):
    canvas.create_line(coords[0, i], coords[1, i], coords[0, i+1], coords[1, i+1], width=2, fill='black')

# Aumentar la línea y actualizar el dibujo en el lienzo
canvas.delete("all") # Borrar todo lo que hay en el lienzo


coordsAumentado = linea.cambiarLongitud(10, 10, 50, 50)
for i in range(len(coordsAumentado[0])-1):
            canvas.create_line(coordsAumentado[0, i], coordsAumentado[1, i], coordsAumentado[0, i+1], coordsAumentado[1, i+1], width=2, fill='black')
print (coordsAumentado)
 
# Mostrar la ventana
ventana.mainloop() """
