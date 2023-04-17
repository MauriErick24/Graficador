import numpy
import cv2
from PySide6.QtWidgets import QApplication
from PySide6.QtWidgets import QFrame, QColorDialog
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QColor
class circuferencia(QFrame):
    puntoRadiox=0
    puntoRadioy=0
    
    matrizCircuferencia=[[]]
    def __init__(self, parent=None, defaultColor=Qt.GlobalColor.white):
        super(circuferencia, self).__init__(parent)
        self.setStyleSheet("border-color: rgba(0,0,0,0);")
        self._color=QColor()
        self.setFixedSize(20,20)
        self._defaultColor = QColor(defaultColor)
        self.setFrameStyle(1)
    def crearCircuferencia(self,radio,color):
        
        tamanodimen=radio*2+10
        puntomediox=radio+5
        puntomedioy=radio+5
        self.matrizCircuferencia=numpy.ones((tamanodimen,tamanodimen,3),numpy.uint8)*255
        
        
        
        p0=1-radio
        x=0
        y=radio
        color.reverse()
        while(x<y):
           self.matrizCircuferencia[x+puntomediox][y-puntomedioy]=color
           self.matrizCircuferencia[y+puntomediox][x-puntomedioy]=color
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
          
           if(p0<0):
               
               p0=p0+2*x+2+1
               x=x+1
           else:
               p0=p0+2*x+2+1-(2*y-2)
               x=x+1 
               y=y-1
               
               
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

nc.crearCircuferencia(200,valorRGB)
nc.mostar()
exit()
app.exec()