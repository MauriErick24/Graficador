import tkinter as tk
from tkinter import *
from tkinter.colorchooser import askcolor
import linea
import triangulo
import circulo
import cuadrado

class PaintApp:
    global canvas 
    global x1, y1, x2, y2
    global flag
    global painting
    global master
    global line
    global triangle
    global selection 
    global circle 
    global square
    global fill_color


    def __init__(self, master):
        self.master = master
        master.title("Paint App")
        self.flag = 0
        self.painting = 0
        self.line = 0
        self.selection = 0
        self.triangle = 0
        self.circle = 0
        self.square = 0
        self.fill_color = ''
        self.figure = 0
   

        # Frame para botones
        self.button_frame = tk.Frame(master)
        self.button_frame.pack(side="top", fill="x", padx=10, pady=10)

        # Botones para herramientas de dibujo
        # self.line_button = tk.Button(self.button_frame, text="Línea", command=self.draw_line)
        # self.line_button.pack(side="left", padx=5)
        self.line_button = tk.Button(self.button_frame, text="Línea",command=self.button_click_line)
        self.line_button.pack(side="left", padx=5)
  
        # Botón para borrar pantalla
       
        
        # self.clear_button = tk.Button(self.button_frame, text="Borrar Pantalla", command=self.button_stop)
        # self.clear_button.pack(side="left", padx=5)

        # Botones para ajustar el color de la línea
        self.color_label = tk.Label(self.button_frame, text="Color de línea:")
        self.color_label.pack(side="left", padx=5)
       
   

        # Botones para ajustar el grosor y la segmentación de la línea
        self.width_label = tk.Label(self.button_frame, text="Grosor de línea:")
        self.width_label.pack(side="left", padx=5)
        self.width_scale = tk.Scale(self.button_frame, from_=1, to=10, orient="horizontal")
        self.width_scale.pack(side="left", padx=5)
        self.segment_label = tk.Label(self.button_frame, text="Segmentación de línea:")
        self.segment_label.pack(side="left", padx=5)
        self.segment_scale = tk.Scale(self.button_frame, from_=1, to=2, orient="horizontal")
        self.segment_scale.pack(side="left", padx=5)

        # Lienzo para dibujar
        self.canvas = tk.Canvas(master, width=800, height=480, bg="white")
        self.canvas.pack(side="bottom", fill="both", expand=True, padx=10, pady=10)
        master.bind("<Key>", self.key_press)
     
        
 ############################ Linea ##############################################   
    def button_click_line(self):
         self.figure = 1
         self.fill_color = ''
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
        self.pointLines = self.line.dibujar()
        coord_list = [[  self.pointLines[0][i],   self.pointLines[1][i]] for i in range(len(  self.pointLines[0]))]
        if self.segment_scale.get() > 1:
            self.linea_dibujada = self.canvas.create_line(coord_list, width=self.width_scale.get(), dash=(1, 6))
        else:
            self.linea_dibujada = self.canvas.create_line(coord_list, width=self.width_scale.get())
        # for i in range(len(pointLines[0])):
        #     print("Coordenadas x, y: ({}, {})".format(pointLines[0][i], pointLines[1][i]))
        #     cordx = pointLines[0][i]
        #     cordy = pointLines[1][i]
        #     self.canvas.create_rectangle(cordx, cordy, cordx+1, cordy+1, fill="black")
#############################################################################################

 ############################ Triangulo ##############################################   
root = tk.Tk()
app = PaintApp(root)
root.mainloop()