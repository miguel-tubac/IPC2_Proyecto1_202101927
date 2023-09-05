from ListaSimple import ListaSimple
from Tiempo import Tiempo

##----------------------------------------------Funcion para almacenar las senales-----------------------------------------------
class Senal:
    def __init__(self, nombre, tiempoMaximo, amplitudMaxima):
        self.nombre = nombre
        self.tiempoMaximo = tiempoMaximo
        self.amplitudMaxima = amplitudMaxima
        self.tiempos = ListaSimple()
        self.crearListaTiempo()
        #self.imprimir()
        

    def getNombre(self):
        return self.nombre
    
    def getTiempoMaximo(self):
        return int(self.tiempoMaximo)
    
    def getAmplitudMaxima(self):
        return self.amplitudMaxima
    
    def crearListaTiempo(self):
        for i in range(1, int(self.tiempoMaximo)+1):
            objTiempo = Tiempo(i, self.amplitudMaxima)
            self.tiempos.insertar(objTiempo)

    def imprimir(self):
        print("_____Tiempos para senal:","nombre= ", self.getNombre(),"t = ",self.getTiempoMaximo() ,"A = ",self.getAmplitudMaxima(),"_____")
        tmpTiempo = self.tiempos.getInicio()
        while tmpTiempo != None:
            print(tmpTiempo.getDato().getTiempo())
            tmpTiempo = tmpTiempo.getSiguiente()