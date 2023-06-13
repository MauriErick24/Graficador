import tkinter as tk
from tkinter import ttk
from tkinter import *


class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.canvas1=tk.Canvas(self.ventana1, width=700, height=500, background="black")
        self.canvas1.grid(column=0, row=0)
        archi1=tk.PhotoImage(file="AV. KENNEDY (1).png")
        self.canvas1.create_image(30, 100, image=archi1, anchor="nw")
        
        #self.canvas1 = Canvas(width=400, height=300, bg='white')
        self.canvas1.pack(expand=YES, fill=BOTH,)
        self.canvas1.create_line(100, 100, 80, 500)
        self.canvas1.create_line(100, 500, 80, 100)
        self.ventana1.mainloop()
    def presion_mouse(self, evento):
        self.canvas1.create_oval(evento.x-5,evento.y-5,evento.x+5,evento.y+5, fill="red")
        print(evento)
       

aplicacion1=Aplicacion()



