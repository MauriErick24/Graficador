import numpy
import cv2
from PySide6.QtWidgets import QApplication
from PySide6.QtWidgets import QFrame, QColorDialog
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QColor
class circuferencia(QFrame):
    iniciox=0;
    inicioy=0;
    finx=0;
    finy=0;
    puntoRadiox=0
    puntoRadioy=0
    colorFondo=[255,255,255]
    colorBorde=[]
    matrizCircuferencia=[[]]
    def __init__(self, parent=None, defaultColor=Qt.GlobalColor.white):
        super(circuferencia, self).__init__(parent)
        self.setStyleSheet("border-color: rgba(0,0,0,0);")
        self._color=QColor()
        self.setFixedSize(20,20)
        self._defaultColor = QColor(defaultColor)
        self.setFrameStyle(1)
    def crearCircuferencia(self,radio,color, intercambiar):
        self.colorBorde=color
        tamanodimen=radio*2+10
        puntomediox=radio+5
        puntomedioy=radio+5
        self.matrizCircuferencia=numpy.ones((tamanodimen,tamanodimen,3),numpy.uint8)*255
        vInt=False
        
        vecesCap=1;
        p0=1-radio
        x=0
        y=radio
        color.reverse()
        while(x<=y):
            if(vInt or intercambiar):
                self.matrizCircuferencia[x+puntomediox][y-puntomedioy]=color
                self.matrizCircuferencia[y+puntomediox][x-puntomedioy]=color
                if(vecesCap>0):
                    self.inicioy=y-puntomedioy+10
                    self.iniciox=y-puntomedioy+10
                    self.finy=y+puntomedioy
                    self.finx=y+puntomedioy
                x=-x
                self.matrizCircuferencia[x+puntomediox][y-puntomedioy]=color
                self.matrizCircuferencia[y+puntomediox][x-puntomedioy]=color
                
                
                x=-x
                y=-y
                self.matrizCircuferencia[x+puntomediox][y-puntomedioy]=color
                self.matrizCircuferencia[y+puntomediox][x-puntomedioy]=color
                
                x=-x
                self.matrizCircuferencia[x+puntomediox][y-puntomedioy]=color
                self.matrizCircuferencia[y+puntomediox][x-puntomedioy]=color
                
                x=-x
                y=-y
                
                vInt=False
            else:
                vInt=True
            if(p0<0):
               
                p0=p0+2*x+2+1
                x=x+1
            else:
                p0=p0+2*x+2+1-(2*y-2)
                x=x+1 
                y=y-1
            vecesCap-=1
            
               
    def pintar(self,color):# imprementacion de 4 vecinos no llega a ser util muchas llamadas y no termina
        puntoMedio= int(len(self.matrizCircuferencia)/2)
        #colorFondo=self.matrizCircuferencia[puntoMedio][puntoMedio]
        copiaMatriz=self.matrizCircuferencia;
        
        self.pintarPixel(puntoMedio,puntoMedio,color,self.colorFondo,copiaMatriz)

        
        
    def pintarPixel(self,posx, posy, colorPix, colorFon,matriz):
        max=len(matriz)-1#implementacion defectura muchas llamadas recursivas
        if(posx>0 and posx<max and posy>0 and posy<max  ):
            colorPixelActual=matriz [posx][posy]
           
            
            #if(numpy.array_equal(colorPixelActual,colorPix)):return
            #if(numpy.array_equal(colorFon,colorPixelActual)):
            matriz[posx][posy]=colorPix;
            self.pintarPixel(posx+1,posy,colorPix,colorFon,matriz)
            self.pintarPixel(posx,posy+1,colorPix,colorFon,matriz)
            self.pintarPixel(posx-1,posy,colorPix,colorFon,matriz)
            self.pintarPixel(posx,posy-1,colorPix,colorFon,matriz)
                
            
                      
    def pintarScanLine(self):
        print("inicio",self.iniciox,self.inicioy)
        print("fin",self.finx,self.finy)
        
        puntosnegros=0
        matrizPintar=self.matrizCircuferencia
        tamano=len(matrizPintar)
        for xi in range(tamano):
            pintarlinea=False;
            pintarBool=True
            for yi in range(tamano):
                if(self.iniciox!=xi and self.finx!=xi  ):
                    if(numpy.array_equal(matrizPintar[xi][yi],self.colorBorde)):
                        if(pintarBool):
                            #este parte busca donde inicia el pintado y donde acaba, solo sirve para figuras regulares, y no va funcionar para otro tipo de figura 
                             
                            if(not(pintarlinea)):
                                if(not(numpy.array_equal(matrizPintar[xi][yi+1],self.colorBorde))):pintarlinea=True
                            else:    
                                if(not(numpy.array_equal(matrizPintar[xi][yi-1],self.colorBorde))):
                                    pintarlinea=False
                                    pintarBool=False
                        
                    elif(pintarlinea ):
                        matrizPintar[xi][yi]=[10,200,100]
        #primera solucion para poner 2 ejes de ejecutar muy inefiente 
        '''
        for yi in range(tamano):
            pintarlinea=False;
            for xi in range(tamano):
                if(self.inicioy!=yi and self.finy!=yi  ):
                    if(numpy.array_equal(matrizPintar[xi][yi],self.colorBorde)):
                        pintarlinea=not(pintarlinea)
                    elif(pintarlinea and pintarBool):
                        matrizPintar[xi][yi]=[10,200,100]
           '''     
                
        
    def mostar(self):
        cv2.imshow('imgCircuferencia',self.matrizCircuferencia)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    def selecionarColor(self):
        color = QColorDialog.getColor(self._color)
        return [color.red(),color.green(),color.blue()]
        
    def getMatriz(self):
        return self.matrizCircuferencia
    def setMatriz(self,nMatriz):
        self.matrizCircuferencia=nMatriz
        


app = QApplication([])

nc=circuferencia()


valorRGB=nc.selecionarColor()

nc.crearCircuferencia(200,valorRGB,True)
nc.pintarScanLine()
#nc.pintar([100,200,10])


nc.mostar()
exit()
app.exec()