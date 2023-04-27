import math
class circuferencia:
    listaPuntosBorde=[]
    def __init__(self,pxi,pyi,pxf,pyf):
        self.crearCirculoDiametro(pxi,pyi,pxf,pyf)
    def crearCirculoDiametro(self,pxi,pyi,pxf,pyf):
        diametro=math.sqrt(math.pow(pxf-pxi,2)+math.pow(pyf-pyi,2))
        radio = int(diametro/2)
        puntomediox=int((pxf+pxi)/2)
        p0=1-radio
        puntomedioy=int((pyf+pyi)/2)
        xi=0
        yi=radio
        while(xi<=yi):
            self.listaPuntosBorde.append((xi+puntomediox,yi+puntomedioy))
            self.listaPuntosBorde.append((yi+puntomedioy,xi+puntomediox))
            xi=-xi
            self.listaPuntosBorde.append((xi+puntomediox,yi+puntomedioy))
            self.listaPuntosBorde.append((yi+puntomedioy,xi+puntomediox))
            xi=-xi
            yi=-yi
            self.listaPuntosBorde.append((xi+puntomediox,yi+puntomedioy))
            self.listaPuntosBorde.append((yi+puntomedioy,xi+puntomediox))
            xi=-xi
            self.listaPuntosBorde.append((xi+puntomediox,yi+puntomedioy))
            self.listaPuntosBorde.append((yi+puntomedioy,xi+puntomediox))
            xi=-xi
            yi=-yi
            self.listaPuntosBorde.append((xi+puntomediox,yi+puntomedioy))
            self.listaPuntosBorde.append((yi+puntomedioy,xi+puntomediox))
            if(p0<0):
               
                p0=p0+2*xi+2+1
                xi=xi+1
            else:
                p0=p0+2*xi+2+1-(2*yi-2)
                xi=xi+1 
    def getPoints(self):
        return self.listaPuntosBorde
                
nc=circuferencia(0,3,100,100)
print(nc.getPoints())