import numpy as np
import tkinter as tk

class Triangulo:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def dibujar(self):
        dx = abs(self.x2 - self.x1)
        dy = abs(self.y2 - self.y1)
        lado = int((dx ** 2 + dy ** 2) ** 0.5)
        altura = int(lado * (3 ** 0.5) / 2)
        x3 = self.x1 + int(lado / 2)
        y3 = self.y1 + altura
        
        # Obtener las coordenadas de los puntos intermedios
        puntos1_x, puntos1_y = self.linea_simple(self.x1, self.y1, self.x2, self.y2)
        puntos2_x, puntos2_y = self.linea_simple(self.x2, self.y2, x3, y3)
        puntos3_x, puntos3_y = self.linea_simple(x3, y3, self.x1, self.y1)

        coords = [(puntos1_x[i], puntos1_y[i]) for i in range(len(puntos1_x))]
        coords += [(puntos2_x[i], puntos2_y[i]) for i in range(len(puntos2_x))]
        coords += [(puntos3_x[i], puntos3_y[i]) for i in range(len(puntos3_x))]
        
        return coords
    
    def linea_simple(self, x1, y1, x2, y2):
        # Implementación del algoritmo de línea simple
        puntos_x = []
        puntos_y = []
        if x1 == x2:
            # Línea vertical
            if y1 > y2:
                y1, y2 = y2, y1
            for y in range(y1, y2 + 1):
                puntos_x.append(x1)
                puntos_y.append(y)
        elif y1 == y2:
            # Línea horizontal
            if x1 > x2:
                x1, x2 = x2, x1
            for x in range(x1, x2 + 1):
                puntos_x.append(x)
                puntos_y.append(y1)
        else:
            # Línea con pendiente
            m = (y2 - y1) / (x2 - x1)
            if abs(m) <= 1:
                if x1 > x2:
                    x1, x2 = x2, x1
                    y1, y2 = y2, y1
                y = y1
                for x in range(x1, x2 + 1):
                    puntos_x.append(x)
                    puntos_y.append(int(y))
                    y += m
            else:
                if y1 > y2:
                    x1, x2 = x2, x1
                    y1, y2 = y2, y1
                x = x1
                for y in range(y1, y2 + 1):
                    puntos_x.append(int(x))
                    puntos_y.append(y)
                    x += 1 / m

        return puntos_x, puntos_y

    
    def aumentar(self):
        self.x1 -= 1
        self.y1 -= 1
        self.x2 += 1
        self.y2 += 1

    def reducir(self):
        self.x1 += 1
        self.y1 += 1
        self.x2 -= 1
        self.y2 -= 1

#Los puntos para usar create_polygon no se pasa en matricez
# Crear un objeto Triangulo con las coordenadas de dos vértices opuestos
# triangulo = Triangulo(90, 90, 200, 200)

# # Obtener las coordenadas del triángulo equilátero
# coords = triangulo.dibujar()
# print(coords)
# print("Triangulo aumentado")
# # Aumentar el tamaño del triángulo y se vuelve a dibujar
# triangulo.aumentar()
# coords = triangulo.dibujar()
# print(coords)

# #Reducir el tamaño del triangulo y volver a dibujar
# print("Triangulo reducido")
# triangulo.reducir()
# coords = triangulo.dibujar()
# print(coords)

# # Dibujar el triángulo en una ventana de Tkinter
# ventana = tk.Tk()
# canvas = tk.Canvas(ventana, width=300, height=300)
# canvas.pack()
# canvas.create_polygon(coords, outline='black', fill='')
# ventana.mainloop()