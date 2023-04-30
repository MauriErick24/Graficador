import tkinter as tk
from tkinter import *
import linea
import triangulo

class PaintApp:
    global canvas 
    global x1, y1, x2, y2
    global flag
    global painting
    global master
    global line
    global triangle
    global selection 

    def __init__(self, master):
        self.master = master
        master.title("Paint App")
        self.flag = 0
        self.painting = 0
        self.line = 0
        self.selection = 0
        self.triangle = 0
        # Frame para botones
        self.button_frame = tk.Frame(master)
        self.button_frame.pack(side="top", fill="x", padx=10, pady=10)

        # Botones para herramientas de dibujo
        # self.line_button = tk.Button(self.button_frame, text="Línea", command=self.draw_line)
        # self.line_button.pack(side="left", padx=5)
        self.line_button = tk.Button(self.button_frame, text="Línea",command=self.button_click_line)
        self.line_button.pack(side="left", padx=5)
        
        self.square_button = tk.Button(self.button_frame, text="Cuadrado", command=self.draw_square)
        self.square_button.pack(side="left", padx=5)
        self.circle_button = tk.Button(self.button_frame, text="Círculo", command=self.draw_circle)
        self.circle_button.pack(side="left", padx=5)
        self.triangle_button = tk.Button(self.button_frame, text="Triángulo", command=self.button_click_triangle)
        self.triangle_button.pack(side="left", padx=5)
        self.curve_button = tk.Button(self.button_frame, text="Puntero", command=self.button_stop)
        self.curve_button.pack(side="left", padx=5)

        # Botón para borrar pantalla
        self.clear_button = tk.Button(self.button_frame, text="Borrar Pantalla", command=self.clear_canvas)
        self.clear_button.pack(side="left", padx=5)
        # self.clear_button = tk.Button(self.button_frame, text="Borrar Pantalla", command=self.button_stop)
        # self.clear_button.pack(side="left", padx=5)

        # Botones para ajustar el color de la línea
        self.color_label = tk.Label(self.button_frame, text="Color de línea:")
        self.color_label.pack(side="left", padx=5)
        self.color_button = tk.Button(self.button_frame, text="Seleccionar Color", command=self.choose_color)
        self.color_button.pack(side="left", padx=5)

        # Botones para ajustar el grosor y la segmentación de la línea
        self.width_label = tk.Label(self.button_frame, text="Grosor de línea:")
        self.width_label.pack(side="left", padx=5)
        self.width_scale = tk.Scale(self.button_frame, from_=1, to=10, orient="horizontal")
        self.width_scale.pack(side="left", padx=5)
        self.segment_label = tk.Label(self.button_frame, text="Segmentación de línea:")
        self.segment_label.pack(side="left", padx=5)
        self.segment_scale = tk.Scale(self.button_frame, from_=1, to=10, orient="horizontal")
        self.segment_scale.pack(side="left", padx=5)

        # Lienzo para dibujar
        self.canvas = tk.Canvas(master, width=800, height=480, bg="white")
        self.canvas.pack(side="bottom", fill="both", expand=True, padx=10, pady=10)
        master.bind("<s>", self.key_press_line)
        master.bind("<t>", self.key_press_triangle)

 ############################ Linea ##############################################   
    def button_click_line(self):
         self.canvas.bind("<Button-1>", self.canvas_click_line)

    def canvas_click_line(self, event):
       if(self.flag == 0):
            self.x1 = event.x
            self.y1 = event.y
            print("Coordenadas 1 del clic: ({}, {})".format(self.x1, self.y1))
            self.flag = 1
       elif(self.flag == 1):   
            self.x2 = event.x
            self.y2 = event.y
            print("Coordenadas 2 del clic: ({}, {})".format(self.x2, self.y2))
            self.flag = 0
            self.draw_line()

    def draw_line(self):
        self.painting = 1
        self.line = linea.Linea(self.x1,self.y1,self.x2,self.y2)
        pointLines = self.line.dibujar()
        for i in range(len(pointLines[0])):
            print("Coordenadas x, y: ({}, {})".format(pointLines[0][i], pointLines[1][i]))
            cordx = pointLines[0][i]
            cordy = pointLines[1][i]
            self.canvas.create_rectangle(cordx, cordy, cordx+1, cordy+1, fill="black")
#############################################################################################

 ############################ Triangulo ##############################################   
    def button_click_triangle(self):
         self.canvas.bind("<Button-1>", self.canvas_click_triangle)

    def canvas_click_triangle(self, event):
       if(self.flag == 0):
            self.x1 = event.x
            self.y1 = event.y
            print("Coordenadas 1 del clic: ({}, {})".format(self.x1, self.y1))
            self.flag = 1
       elif(self.flag == 1):   
            self.x2 = event.x
            self.y2 = event.y
            print("Coordenadas 2 del clic: ({}, {})".format(self.x2, self.y2))
            self.flag = 0
            self.draw_triangle()

    def draw_triangle(self):
        self.painting = 1
        self.triangle = triangulo.Triangulo(self.x1,self.y1,self.x2,self.y2)
        points = self.triangle.dibujar()
        self.canvas.create_polygon(points, outline='black', fill='')

#############################################################################################


        pass
    def draw_square(self):
        pass

    def draw_circle(self):
        pass

    # def draw_triangle(self):
    #     pass

    def draw_curve(self):
        pass

    def clear_canvas(self):
        self.painting = 0
        self.canvas.delete("all")
        pass

    def choose_color(self):
        pass


############## detener listener #############################
    def button_stop(self):
        self.canvas.bind("<Button-1>", self.draw_stop)
        pass
    
    def draw_stop(self,event):
        pass
###############################################################



    def key_press_line(self,event):
        if(self.painting == 1):
            print("Se ha presionado la tecla '{}'".format(event.keysym))
            pointLines = self.line.cambiarLongitud()
        for i in range(len(pointLines[0])):
            cordx = pointLines[0][i]
            cordy = pointLines[1][i]
            self.canvas.create_rectangle(cordx, cordy, cordx+1, cordy+1, fill="black")

    def key_press_triangle(self,event):
        if(self.painting == 1):
            print("Se ha presionado la tecla '{}'".format(event.keysym))
            pointLines = self.triangle.aumentar()
            pointLines = self.triangle.dibujar()
            self.canvas.create_polygon(pointLines, outline='black', fill='')
            
        



root = tk.Tk()
app = PaintApp(root)
root.mainloop()