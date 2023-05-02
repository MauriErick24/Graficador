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
        
        self.square_button = tk.Button(self.button_frame, text="Cuadrado", command=self.button_click_square)
        self.square_button.pack(side="left", padx=5)
        self.circle_button = tk.Button(self.button_frame, text="Círculo", command=self.button_click_circle)
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
    def button_click_triangle(self):
         self.figure = 2
         self.fill_color = ''
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
        if self.segment_scale.get() > 1:
         self.triangulo_dibujado = self.canvas.create_polygon(points, outline='black', fill=self.fill_color,  width=self.width_scale.get(), dash=(1,6))
        else:
            self.triangulo_dibujado = self.canvas.create_polygon(points, outline='black', fill=self.fill_color,  width=self.width_scale.get()) 
        #self.canvas.create_line(points, width=self.width_scale.get())
#############################################################################################

############################ Circulo ##############################################   
    def button_click_circle(self):
         self.figure = 4
         self.fill_color = ''
         self.canvas.bind("<Button-1>", self.canvas_click_circulo)

    def canvas_click_circulo(self, event):
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
            self.draw_circle()

    def draw_circle(self):
        self.painting = 1
       
        if self.segment_scale.get() > 1:
            self.circle = circulo.Circuferencia(self.x1,self.y1,self.x2,self.y2, self.width_scale.get(),10)
            points = self.circle.getPoints()
            self.canvas.create_polygon(points, outline='black', fill=self.fill_color, width=self.width_scale.get(), dash=(1,1))
        #self.canvas.create_line(points, width=self.width_scale.get())
        else:
            self.circle = circulo.Circuferencia(self.x1,self.y1,self.x2,self.y2, self.width_scale.get(),self.width_scale.get())
            points = self.circle.getPoints()
            self.canvas.create_polygon(points, outline='black', fill=self.fill_color, width=self.width_scale.get())
#############################################################################################
        pass
 
############################ Cuadrado ##############################################   
    def button_click_square(self):
         self.figure = 3
         self.fill_color = ''
         self.canvas.bind("<Button-1>", self.canvas_click_square)

    def canvas_click_square(self, event):
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
            self.draw_square()

    def draw_square(self):
        self.painting = 1
        self.square = cuadrado.Cuadrado(self.x1,self.y1,self.x2,self.y2)
        points = self.square.dibujar()
        if self.segment_scale.get() > 1:
         self.cuadrado_dibujado=self.canvas.create_polygon(points, outline='black', fill=self.fill_color,  width=self.width_scale.get(), dash=(1,6))
        else:
          self.cuadrado_dibujado=self.canvas.create_polygon(points, outline='black', fill=self.fill_color,  width=self.width_scale.get())

#############################################################################################
 
 
    # def draw_square(self):
    #     pass

    # def draw_circle(self):
    #     pass

    # def draw_triangle(self):
    #     pass

    def draw_curve(self):
        pass

    def clear_canvas(self):
        self.painting = 0
        self.canvas.delete("all")

    def choose_color(self):
        get_fill_color = askcolor()[1]
        self.fill_color = get_fill_color
        #self.canvas.itemconfig(self.current_shape, fill=self.fill_color)
        pass


############## detener listener #############################
    def button_stop(self):
        self.canvas.bind("<Button-1>", self.draw_stop)
        pass
    
    def draw_stop(self,event):
        pass
###############################################################



    def key_press(self,event):
         if(self.painting == 1):
            if(self.figure==1):
                if event.keysym == 'r':
                    print("Se ha presionado la tecla '{}'".format(event.char))
                    pointLines = self.line.rotar()
                    coord_list = pointLines.T.flatten().tolist()
            
                    if self.segment_scale.get() > 1:
                        self.linea_dibujada = self.canvas.create_line(coord_list, width=self.width_scale.get(), dash=(1, 6))
                    else:
                     self.linea_dibujada = self.canvas.create_line(coord_list, width=self.width_scale.get())
                    self.canvas.update()
                elif event.keysym == 'q':
                    print("Se ha presionado la tecla '{}'".format(event.keysym))
                    pointLines = self.line.aumentarLongitud()
                    coord_list = pointLines.T.flatten().tolist()
                    if self.segment_scale.get() > 1:
                        self.linea_dibujada = self.canvas.create_line(coord_list, width=self.width_scale.get(), dash=(1, 6))
                    else:
                     self.linea_dibujada = self.canvas.create_line(coord_list, width=self.width_scale.get())
                    self.canvas.update()
                elif event.keysym == 'w':
                    print("Se ha presionado la tecla '{}'".format(event.keysym))
                    pointLines = self.line.disminuirLongitud()
                    coord_list = pointLines.T.flatten().tolist()
                    if self.segment_scale.get() > 1:
                        self.linea_dibujada = self.canvas.create_line(coord_list, width=self.width_scale.get(), dash=(1, 6))
                    else:
                     self.linea_dibujada = self.canvas.create_line(coord_list, width=self.width_scale.get())
                    self.canvas.update()
                elif event.keysym == 'Up':
                    print("Se ha presionado la tecla '{}'".format(event.keysym))
                    pointLines = self.line.moverArriba()
                    coord_list = pointLines.T.flatten().tolist()
                    if self.segment_scale.get() > 1:
                        self.linea_dibujada = self.canvas.create_line(coord_list, width=self.width_scale.get(), dash=(1, 6))
                    else:
                     self.linea_dibujada = self.canvas.create_line(coord_list, width=self.width_scale.get())
                    self.canvas.update()
                elif event.keysym == 'Down':
                    print("Se ha presionado la tecla '{}'".format(event.keysym))
                    pointLines = self.line.moverAbajo()
                    coord_list = pointLines.T.flatten().tolist()
                    if self.segment_scale.get() > 1:
                        self.linea_dibujada = self.canvas.create_line(coord_list, width=self.width_scale.get(), dash=(1, 6))
                    else:
                     self.linea_dibujada = self.canvas.create_line(coord_list, width=self.width_scale.get())
                    self.canvas.update()
                elif event.keysym == 'Left':
                    print("Se ha presionado la tecla '{}'".format(event.keysym))
                    pointLines = self.line.moverIzquierda()
                    coord_list = pointLines.T.flatten().tolist()
                    if self.segment_scale.get() > 1:
                        self.linea_dibujada = self.canvas.create_line(coord_list, width=self.width_scale.get(), dash=(1, 6))
                    else:
                     self.linea_dibujada = self.canvas.create_line(coord_list, width=self.width_scale.get())
                    self.canvas.update()
                elif event.keysym == 'Right':
                    print("Se ha presionado la tecla '{}'".format(event.keysym))
                    pointLines = self.line.moverDerecha()
                    coord_list = pointLines.T.flatten().tolist()
                    if self.segment_scale.get() > 1:
                        self.linea_dibujada = self.canvas.create_line(coord_list, width=self.width_scale.get(), dash=(1, 6))
                    else:
                     self.linea_dibujada = self.canvas.create_line(coord_list, width=self.width_scale.get())
                    self.canvas.update()
            elif(self.figure==2):
                if event.keysym == 'q':
                    print("Se ha presionado la tecla '{}'".format(event.keysym))
                    self.canvas.delete(self.triangulo_dibujado)
                    self.triangle.aumentar()
                    points = self.triangle.dibujar()
                    if self.segment_scale.get() > 1:
                     self.triangulo_dibujado = self.canvas.create_polygon(points, outline='black', fill=self.fill_color,  width=self.width_scale.get(), dash=(1,6))
                    else:
                        self.triangulo_dibujado = self.canvas.create_polygon(points, outline='black', fill=self.fill_color,  width=self.width_scale.get()) 
                    self.canvas.update()  
                elif event.keysym == 'w':
                    print("Se ha presionado la tecla '{}'".format(event.keysym))
                    self.canvas.delete(self.triangulo_dibujado)
                    self.triangle.reducir()
                    points = self.triangle.dibujar()
                    if self.segment_scale.get() > 1:
                     self.triangulo_dibujado = self.canvas.create_polygon(points, outline='black', fill=self.fill_color,  width=self.width_scale.get(), dash=(1,6))
                    else:
                        self.triangulo_dibujado = self.canvas.create_polygon(points, outline='black', fill=self.fill_color,  width=self.width_scale.get()) 
                    self.canvas.update()   
                elif event.keysym == 'Up':
                    print("Se ha presionado la tecla '{}'".format(event.keysym))
                    self.canvas.delete(self.triangulo_dibujado)
                    self.triangle.moverArriba()
                    points = self.triangle.dibujar()
                    if self.segment_scale.get() > 1:
                     self.triangulo_dibujado = self.canvas.create_polygon(points, outline='black', fill=self.fill_color,  width=self.width_scale.get(), dash=(1,6))
                    else:
                        self.triangulo_dibujado = self.canvas.create_polygon(points, outline='black', fill=self.fill_color,  width=self.width_scale.get()) 
                    self.canvas.update()   
                elif event.keysym == 'Down':
                    print("Se ha presionado la tecla '{}'".format(event.keysym))
                    self.canvas.delete(self.triangulo_dibujado)
                    self.triangle.moverAbajo()
                    points = self.triangle.dibujar()
                    if self.segment_scale.get() > 1:
                      self.triangulo_dibujado = self.canvas.create_polygon(points, outline='black', fill=self.fill_color,  width=self.width_scale.get(), dash=(1,6))
                    else:
                        self.triangulo_dibujado = self.canvas.create_polygon(points, outline='black', fill=self.fill_color,  width=self.width_scale.get()) 
                    self.canvas.update()   
                elif event.keysym == 'Left':
                    print("Se ha presionado la tecla '{}'".format(event.keysym))
                    self.canvas.delete(self.triangulo_dibujado)
                    self.triangle.moverIzquierda()
                    points = self.triangle.dibujar()
                    if self.segment_scale.get() > 1:
                     self.triangulo_dibujado = self.canvas.create_polygon(points, outline='black', fill=self.fill_color,  width=self.width_scale.get(), dash=(1,6))
                    else:
                        self.triangulo_dibujado = self.canvas.create_polygon(points, outline='black', fill=self.fill_color,  width=self.width_scale.get()) 
                    self.canvas.update()   
                elif event.keysym == 'Right':
                    print("Se ha presionado la tecla '{}'".format(event.keysym))
                    self.canvas.delete(self.triangulo_dibujado)
                    self.triangle.moverDerecha()
                    points = self.triangle.dibujar()
                    if self.segment_scale.get() > 1:
                     self.triangulo_dibujado = self.canvas.create_polygon(points, outline='black', fill=self.fill_color,  width=self.width_scale.get(), dash=(1,6))
                    else:
                        self.triangulo_dibujado = self.canvas.create_polygon(points, outline='black', fill=self.fill_color,  width=self.width_scale.get()) 
                    self.canvas.update()
            elif(self.figure==3):
                if event.keysym == 'q':
                    print("Se ha presionado la tecla '{}'".format(event.keysym))
                    self.canvas.delete(self.cuadrado_dibujado)
                    self.square.aumentar()
                    points = self.square.dibujar()
                    if self.segment_scale.get() > 1:
                     self.cuadrado_dibujado=self.canvas.create_polygon(points, outline='black', fill=self.fill_color,  width=self.width_scale.get(), dash=(1,6))
                    else:
                        self.cuadrado_dibujado=self.canvas.create_polygon(points, outline='black', fill=self.fill_color,  width=self.width_scale.get())
                    self.canvas.update()
                elif event.keysym == 'w':
                    print("Se ha presionado la tecla '{}'".format(event.keysym))
                    self.canvas.delete(self.cuadrado_dibujado)
                    self.square.reducir()
                    points = self.square.dibujar()
                    if self.segment_scale.get() > 1:
                     self.cuadrado_dibujado=self.canvas.create_polygon(points, outline='black', fill=self.fill_color,  width=self.width_scale.get(), dash=(1,6))
                    else:
                        self.cuadrado_dibujado=self.canvas.create_polygon(points, outline='black', fill=self.fill_color,  width=self.width_scale.get())
                    self.canvas.update()
                elif event.keysym == 'Up':
                    print("Se ha presionado la tecla '{}'".format(event.keysym))
                    self.canvas.delete(self.cuadrado_dibujado)
                    self.square.moverArriba()
                    points = self.square.dibujar()
                    if self.segment_scale.get() > 1:
                     self.cuadrado_dibujado=self.canvas.create_polygon(points, outline='black', fill=self.fill_color,  width=self.width_scale.get(), dash=(1,6))
                    else:
                        self.cuadrado_dibujado=self.canvas.create_polygon(points, outline='black', fill=self.fill_color,  width=self.width_scale.get())
                    self.canvas.update()
                elif event.keysym == 'Down':
                    print("Se ha presionado la tecla '{}'".format(event.keysym))
                    self.canvas.delete(self.cuadrado_dibujado)
                    self.square.moverAbajo()
                    points = self.square.dibujar()
                    if self.segment_scale.get() > 1:
                     self.cuadrado_dibujado=self.canvas.create_polygon(points, outline='black', fill=self.fill_color,  width=self.width_scale.get(), dash=(1,6))
                    else:
                        self.cuadrado_dibujado=self.canvas.create_polygon(points, outline='black', fill=self.fill_color,  width=self.width_scale.get())
                    self.canvas.update()
                elif event.keysym == 'Left':
                    print("Se ha presionado la tecla '{}'".format(event.keysym))
                    self.canvas.delete(self.cuadrado_dibujado)
                    self.square.moverIzquierda()
                    points = self.square.dibujar()
                    if self.segment_scale.get() > 1:
                     self.cuadrado_dibujado=self.canvas.create_polygon(points, outline='black', fill=self.fill_color,  width=self.width_scale.get(), dash=(1,6))
                    else:
                        self.cuadrado_dibujado=self.canvas.create_polygon(points, outline='black', fill=self.fill_color,  width=self.width_scale.get())
                    self.canvas.update()
                elif event.keysym == 'Right':
                    print("Se ha presionado la tecla '{}'".format(event.keysym))
                    self.canvas.delete(self.cuadrado_dibujado)
                    self.square.moverDerecha()
                    points = self.square.dibujar()
                    if self.segment_scale.get() > 1:
                     self.cuadrado_dibujado=self.canvas.create_polygon(points, outline='black', fill=self.fill_color,  width=self.width_scale.get(), dash=(1,6))
                    else:
                        self.cuadrado_dibujado=self.canvas.create_polygon(points, outline='black', fill=self.fill_color,  width=self.width_scale.get())
                    self.canvas.update() 

                     
    """ def key_press_square(self,event):
        if(self.painting == 1):
            print("Se ha presionado la tecla '{}'".format(event.keysym))
            self.canvas.delete(self.cuadrado_dibujado)
            self.square.aumentar()
            points = self.square.dibujar()
            self.cuadrado_dibujado = self.canvas.create_polygon(points, outline='black', fill=self.fill_color, width=self.width_scale.get()) """
    def key_press_square_up(self,event):
        if(self.painting == 1):
            print("Se ha presionado la tecla '{}'".format(event.keysym))
            self.canvas.delete(self.cuadrado_dibujado)
            self.square.moverArriba()
            points = self.square.dibujar()
            self.cuadrado_dibujado = self.canvas.create_polygon(points, outline='black', fill=self.fill_color, width=self.width_scale.get())
root = tk.Tk()
app = PaintApp(root)
root.mainloop()