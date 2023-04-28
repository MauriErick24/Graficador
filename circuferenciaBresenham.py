import math
import cv2
import numpy
class circuferencia:
    listaPuntosBorde=[]
    def __init__(self,pxi,pyi,pxf,pyf,grosor,separado):
        self.crearCirculoDiametro(pxi,pyi,pxf,pyf,grosor,separado)
    def crearCirculoDiametro(self,pxi,pyi,pxf,pyf,grosor,separado):
        falck=True
        diametro=math.sqrt(math.pow(pxf-pxi,2)+math.pow(pyf-pyi,2))
        radio = int(diametro/2)
        puntomediox=int((pxf+pxi)/2)
        p0=1-radio
        puntomedioy=int((pyf+pyi)/2)
        xi=0
        yi=radio
        contador=separado
        while(xi<=yi):
            if(contador==separado):
                print(xi,yi)
                self.listaPuntosBorde.append((xi+puntomediox,yi+puntomedioy))
                self.listaPuntosBorde.append((yi+puntomediox,xi+puntomedioy))
                xi=-xi
                self.listaPuntosBorde.append((xi+puntomediox,yi+puntomedioy))
                self.listaPuntosBorde.append((yi+puntomediox,xi+puntomedioy))
                xi=-xi
                yi=-yi
                self.listaPuntosBorde.append((xi+puntomediox,yi+puntomedioy))
                self.listaPuntosBorde.append((yi+puntomediox,xi+puntomedioy))
                xi=-xi
                self.listaPuntosBorde.append((xi+puntomediox,yi+puntomedioy))
                self.listaPuntosBorde.append((yi+puntomediox,xi+puntomedioy))
                xi=-xi
                yi=-yi
                self.listaPuntosBorde.append((xi+puntomediox,yi+puntomedioy))
                self.listaPuntosBorde.append((yi+puntomediox,xi+puntomedioy))
                contador=1
            else:
                contador+=1;
                
            if(p0<0):
               
                p0=p0+2*xi+2+1
                xi=xi+1
            else:
                p0=p0+2*xi+2+1-(2*yi-2)
                xi=xi+1
                yi=yi-1
            if(falck):
                print(self.listaPuntosBorde) 
                print(puntomediox,puntomedioy,radio)
                falck=False
    def getPoints(self):
        return self.listaPuntosBorde
    def pintar(self,tam):
        color=[0,0,0]
        tam=tam+10
        matrizCircula=numpy.ones((tam,tam,3),numpy.uint8)*255
        
        for pl in self.listaPuntosBorde:
            x,y=pl
            print(x,y)
            matrizCircula[x][y]=color
            
        cv2.imshow('imgCircuferencia',matrizCircula)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    
                
nc=circuferencia(100,50,100,100,1,1)
print()
#print(nc.getPoints())
nc.pintar(200)