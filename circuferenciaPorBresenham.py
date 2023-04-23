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
    esDoble=False
    def __init__(self, parent=None, defaultColor=Qt.GlobalColor.white):
        super(circuferencia, self).__init__(parent)
        self.setStyleSheet("border-color: rgba(0,0,0,0);")
        self._color=QColor()
        self.setFixedSize(20,20)
        self._defaultColor = QColor(defaultColor)
        self.setFrameStyle(1)
    def crearCircuferencia(self,radio,color, intercambiar, simple):
        self.colorBorde=color
        tamanodimen=radio*2+10
        puntomediox=radio+5
        puntomedioy=radio+5
        self.matrizCircuferencia=numpy.ones((tamanodimen,tamanodimen,3),numpy.uint8)*255
        vInt=False
        color.reverse()
        
        vecesCap=1;
        tamanoPx=4;
        if(simple):tamanoPx=1
        
        for kl in range(0,tamanoPx,3):
            print(kl)
            p0=1-radio-kl
            xi=0-kl
            yi=radio-kl
            while(xi<=yi):
                if(vInt or intercambiar):
                    tam=0
                
                
                    
                    self.matrizCircuferencia[xi+puntomediox][yi-puntomedioy]=color
                    self.matrizCircuferencia[yi+puntomediox][xi-puntomedioy]=color
                    if(vecesCap>0):
                        self.inicioy=yi-puntomedioy+10
                        self.iniciox=yi-puntomedioy+10
                        self.finy=yi+puntomedioy
                        self.finx=yi+puntomedioy
                    xi=-xi
                    self.matrizCircuferencia[xi+puntomediox][yi-puntomedioy]=color
                    self.matrizCircuferencia[yi+puntomediox][xi-puntomedioy]=color
                
                
                    xi=-xi
                    yi=-yi
                    self.matrizCircuferencia[xi+puntomediox][yi-puntomedioy]=color
                    self.matrizCircuferencia[yi+puntomediox][xi-puntomedioy]=color
                
                    xi=-xi
                    self.matrizCircuferencia[xi+puntomediox][yi-puntomedioy]=color
                    self.matrizCircuferencia[yi+puntomediox][xi-puntomedioy]=color
                
                    xi=-xi
                    yi=-yi
                
                    vInt=False
                    tam+=1;
                else:
                    vInt=True
                if(p0<0):
               
                    p0=p0+2*xi+2+1
                    xi=xi+1
                else:
                    p0=p0+2*xi+2+1-(2*yi-2)
                    xi=xi+1 
                    yi=yi-1
                vecesCap-=1
        if(not(simple)):
            self.pintarBorde()
            self.esDoble=True
               
    def pintarBorde(self):# imprementacion de 4 vecinos no llega a ser util muchas llamadas y no termina
        puntoMedio= int(len(self.matrizCircuferencia)/2)
        #colorFondo=self.matrizCircuferencia[puntoMedio][puntoMedio]
        copiaMatriz=self.matrizCircuferencia
        
        self.pintarPixelDA(puntoMedio,self.iniciox+1,self.colorBorde,self.colorFondo,copiaMatriz)
        self.pintarPixelAD(puntoMedio+1,self.iniciox+1,self.colorBorde,self.colorFondo,copiaMatriz)
        self.pintarPixelIA(puntoMedio,self.finx-1,self.colorBorde,self.colorFondo,copiaMatriz)
        self.pintarPixelAI(puntoMedio+1,self.finx-1,self.colorBorde,self.colorFondo,copiaMatriz)
        
        
        
        
    def pintarPixelIA(self,posx, posy, colorPix, colorFon,matriz):
        max=len(matriz)-1#implementacion defectura muchas llamadas recursivas
        if(posx>0 and posx<max and posy>0 and posy<max  ):
            colorPixelActual=matriz [posx][posy]
            if((numpy.array_equal(colorFon,colorPixelActual))):
                self.pintarPixelIA(posx-1,posy,colorPix,colorFon,matriz)
                matriz[posx][posy]=colorPix;
                self.pintarPixelIA(posx,posy-1,colorPix,colorFon,matriz)
    def pintarPixelAI(self,posx, posy, colorPix, colorFon,matriz):
        max=len(matriz)-1#implementacion defectura muchas llamadas recursivas
        if(posx>0 and posx<max and posy>0 and posy<max  ):
            colorPixelActual=matriz [posx][posy]
            if((numpy.array_equal(colorFon,colorPixelActual))):
                self.pintarPixelAI(posx+1,posy,colorPix,colorFon,matriz)
                matriz[posx][posy]=colorPix;
                self.pintarPixelAI(posx,posy-1,colorPix,colorFon,matriz)
                    
    def pintarPixelDA(self,posx, posy, colorPix, colorFon,matriz):
        max=len(matriz)-1#implementacion defectura muchas llamadas recursivas
        if(posx>0 and posx<max and posy>0 and posy<max  ):
            colorPixelActual=matriz [posx][posy]
            if((numpy.array_equal(colorFon,colorPixelActual))):
                self.pintarPixelDA(posx-1,posy,colorPix,colorFon,matriz)
                matriz[posx][posy]=colorPix;
                self.pintarPixelDA(posx,posy+1,colorPix,colorFon,matriz)
    def pintarPixelAD(self,posx, posy, colorPix, colorFon,matriz):
        max=len(matriz)-1#implementacion defectura muchas llamadas recursivas
        if(posx>0 and posx<max and posy>0 and posy<max  ):
            colorPixelActual=matriz [posx][posy]
            if((numpy.array_equal(colorFon,colorPixelActual))):
                self.pintarPixelAD(posx+1,posy,colorPix,colorFon,matriz)
                matriz[posx][posy]=colorPix;
                self.pintarPixelAD(posx,posy+1,colorPix,colorFon,matriz)
                
            
                
            
                      
    def pintarScanLine(self,colorPintar):
        #print("inicio",self.iniciox,self.inicioy)
        #print("fin",self.finx,self.finy)
        
        puntosnegros=0
        if(self.esDoble): puntosnegros=3
        matrizPintar=self.matrizCircuferencia
        tamano=len(matrizPintar)
        for xi in range(tamano):
            pintarlinea=False;
            pintarBool=True
            for yi in range(tamano):
                if(not(xi-self.iniciox<=puntosnegros )and self.finx-xi>puntosnegros):
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
                        matrizPintar[xi][yi]=colorPintar
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

nc.crearCircuferencia(100,valorRGB,True,False)
nc.pintarScanLine([200,100,100])# por el formato el orden de color es BGR
#nc.pintarBorde()


nc.mostar()
exit()
app.exec()