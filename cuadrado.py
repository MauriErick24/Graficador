import tkinter as tk
import time
class Cuadrado:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def dibujar(self):
        # Calcula la diferencia en x y y
        dx = abs(self.x2 - self.x1)
        dy = abs(self.y2 - self.y1)
        
        # Encuentra el tamaño del lado más corto
        lado = min(dx, dy)
        
        # Encuentra las coordenadas del extremo opuesto del lado más corto
        x2 = self.x1 + lado
        y2 = self.y1 + lado
        
        coords = []
        
        # Linea de x1, y1 a x2, y1 usando el algoritmo simple de línea
        for x in range(self.x1, x2+1):
            coords.append((x, self.y1))
        
        # Linea de x2, y1 a x2, y2 usando el algoritmo simple de línea
        for y in range(self.y1, y2+1):
            coords.append((x2, y))
        
        # Linea de x2, y2 a x1, y2 usando el algoritmo simple de línea
        for x in range(x2, self.x1-1, -1):
            coords.append((x, y2))
        
        # Linea de x1, y2 a x1, y1 usando el algoritmo simple de línea
        for y in range(y2, self.y1-1, -1):
            coords.append((self.x1, y))
            
        # Devuelve las coordenadas resultantes
        return coords


    def aumentar(self):
            self.x1 -= 1
            self.y1 -= 1
            self.x2 += 1
            self.y2 += 1
            return self.dibujar()
            
    def reducir(self):
            dx = abs(self.x2 - self.x1)
            dy = abs(self.y2 - self.y1)
            lado = min(dx, dy)
            if lado <= 2:
                return
            x2 = self.x1 + lado
            y2 = self.y1 + lado
            dx_new = dx - 2
            dy_new = dy - 2
            if dx < dy:
                x2_new = x2 - 2
                y2_new = self.y1 + dy_new
            else:
                x2_new = self.x1 + dx_new
                y2_new = y2 - 2
            self.x1 += 1
            self.y1 += 1
            self.x2 = x2_new
            self.y2 = y2_new
            
            # Reducir el cuadrado en 1 píxel en cada lado
            self.x1 += 1
            self.y1 += 1
            self.x2 -= 1
            self.y2 -= 1
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
            
# Crear un objeto Cuadrado con las coordenadas de dos vértices opuestos
cuadrado = Cuadrado(90, 90, 200, 200)

# Dibujar el cuadrado en una ventana de Tkinter
ventana = tk.Tk()
canvas = tk.Canvas(ventana, width=600, height=600)
canvas.pack()

# Dibujar el primer cuadrado
coords = cuadrado.dibujar()
cuadrado_id = canvas.create_polygon(coords, outline='black', fill='')

for i in range(100):
    # Borrar el cuadrado anterior
    canvas.delete(cuadrado_id)

    # Obtener las nuevas coordenadas del cuadrado
    coords = cuadrado.aumentar()

    # Dibujar el nuevo cuadrado
    cuadrado_id = canvas.create_polygon(coords, outline='black', fill='')

    ventana.update()
    time.sleep(0.1)

ventana.mainloop()