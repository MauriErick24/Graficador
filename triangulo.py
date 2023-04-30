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

        total_puntos = lado + 1
        residuo = total_puntos % 3
        puntos_por_lado = total_puntos // 3
        
        puntos1_x = np.linspace(self.x1, self.x2, num=puntos_por_lado+residuo, dtype=int)
        puntos1_y = np.linspace(self.y1, self.y2, num=puntos_por_lado+residuo, dtype=int)

        puntos2_x = np.linspace(self.x2, x3, num=puntos_por_lado, dtype=int)
        puntos2_y = np.linspace(self.y2, y3, num=puntos_por_lado, dtype=int)

        puntos3_x = np.linspace(x3, self.x1, num=puntos_por_lado, dtype=int)
        puntos3_y = np.linspace(y3, self.y1, num=puntos_por_lado, dtype=int)

        coords = [(puntos1_x[i], puntos1_y[i]) for i in range(len(puntos1_x))]
        coords += [(puntos2_x[i], puntos2_y[i]) for i in range(len(puntos2_x))]
        coords += [(puntos3_x[i], puntos3_y[i]) for i in range(len(puntos3_x))]
        
        return coords

    
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

#Los puntos para usar create_polygon no se pasa en matricez, no pudo usar la linea
# Crear un objeto Triangulo con las coordenadas de dos vértices opuestos
triangulo = Triangulo(90, 90, 200, 100)

# Obtener las coordenadas del triángulo equilátero
coords = triangulo.dibujar()
print(coords)
print("Triangulo aumentado")
# Aumentar el tamaño del triángulo y se vuelve a dibujar
triangulo.aumentar()
coords = triangulo.dibujar()
print(coords)

#Reducir el tamaño del triangulo y volver a dibujar
print("Triangulo reducido")
triangulo.reducir()
coords = triangulo.dibujar()
print(coords)

# Dibujar el triángulo en una ventana de Tkinter
ventana = tk.Tk()
canvas = tk.Canvas(ventana, width=300, height=300)
canvas.pack()
canvas.create_polygon(coords, outline='black', fill='')
ventana.mainloop()

