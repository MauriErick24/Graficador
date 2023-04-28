import math
import cv2
import numpy
class circuferencia:
    listaPuntosBorde=[]
    listaPuntosRelleno=[]
    matrizCircuferencia=[[]]
    grosor=0
    tamMax=0
    separacion=0
    finx=0
    iniciox=0
    def __init__(self,pxi,pyi,pxf,pyf,grosor,separado):
        self.crearCirculoDiametro(pxi,pyi,pxf,pyf,grosor,separado)
    def crearCirculoDiametro(self,pxi,pyi,pxf,pyf,groso,separado):
        self.grosor=groso
        self.separacion=separado
        self.tamMax=max(pxi,pyi,pxf,pyf);
        falck=True
        diametro=math.sqrt(math.pow(pxf-pxi,2)+math.pow(pyf-pyi,2))
        radio = int(diametro/2)
        puntomediox=int((pxf+pxi)/2)
        p0=1-radio
        puntomedioy=int((pyf+pyi)/2)
        xi=0
        yi=radio
        contador=separado
        self.iniciox=puntomediox-radio
        self.finx=puntomediox+radio
        while(xi<=yi):
            if(contador==separado):
                
                for tlm in range(groso):
                    self.listaPuntosBorde.append((xi+puntomediox,yi+puntomedioy-tlm))
                    self.listaPuntosBorde.append((yi+puntomediox-tlm,xi+puntomedioy))
                xi=-xi
                for tlm in range(groso):
                    self.listaPuntosBorde.append((xi+puntomediox,yi+puntomedioy-tlm))
                    self.listaPuntosBorde.append((yi+puntomediox-tlm,xi+puntomedioy))
                xi=-xi
                yi=-yi
                for tlm in range(groso):
                    self.listaPuntosBorde.append((xi+puntomediox,yi+puntomedioy+tlm))
                    self.listaPuntosBorde.append((yi+puntomediox+tlm,xi+puntomedioy))
                xi=-xi
                for tlm in range(groso):
                    self.listaPuntosBorde.append((xi+puntomediox,yi+puntomedioy+tlm))
                    self.listaPuntosBorde.append((yi+puntomediox+tlm,xi+puntomedioy))
                xi=-xi
                yi=-yi
                
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
            
    def getPoints(self):
        return self.listaPuntosBorde
    def pintarScanLine(self):
        #print("inicio",self.iniciox,self.inicioy)
        #print("fin",self.finx,self.finy)
        self.crearMatriz() 
        puntosnegros=self.grosor-1
        matrizPintar=self.matrizCircuferencia
        tamano=len(matrizPintar)
        for xi in range(tamano):
            pintarlinea=False;
            pintarBool=True
            colorBorde=[0,0,0]
            for yi in range(tamano):
                if(not(xi-self.iniciox<=puntosnegros )and self.finx-xi>puntosnegros):
                    if(numpy.array_equal(matrizPintar[xi][yi],colorBorde)):
                        if(pintarBool):
                            #este parte busca donde inicia el pintado y donde acaba, solo sirve para figuras regulares, y no va funcionar para otro tipo de figura 
                             
                            if(not(pintarlinea)):
                                if(not(numpy.array_equal(matrizPintar[xi][yi+1],colorBorde))):pintarlinea=True
                            else:    
                                if(not(numpy.array_equal(matrizPintar[xi][yi-1],colorBorde))):
                                    pintarlinea=False
                                    pintarBool=False
                        
                    elif(pintarlinea ):
                        self.listaPuntosRelleno.append((xi,yi))
        #mostar 
    def pintar(self):
        self.crearMatriz() 
        cv2.imshow('imgCircuferencia',self.matrizCircuferencia)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    def crearMatriz(self):
        tam=self.tamMax
        tam=tam+10
        self.matrizCircuferencia=numpy.ones((tam,tam,3),numpy.uint8)*255
        
        color=[0,0,0]# hay poner color primeramente 
        for pl in self.listaPuntosBorde:
            x,y=pl
            #print(x,y)
            self.matrizCircuferencia[x][y]=color
        color=[0,200,0]# el color despues de scanline
        for pl in self.listaPuntosRelleno:
            x,y=pl
        
            self.matrizCircuferencia[x][y]=color
    
                
nc=circuferencia(100,50,100,250,7,4)
print()
#print(nc.getPoints())
nc.pintar()
nc.pintarScanLine();
nc.pintar()
