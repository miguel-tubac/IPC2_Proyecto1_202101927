from Nodo import Nodo
from Graph import Graph

##-------------------------------------------------------------Lista enlazada-----------------------------------------------
class ListaSimple():
    id = 0
    def __init__(self):
        self.nodoInicio = None
        self.nodoFinal = None
        self.size = 0
        self.listaDeAmplitudes = None  

    def getInicio(self):
        return self.nodoInicio

    def estaVacia(self):
        return self.nodoInicio == None

    def insertar(self, dato):
        nuevo = Nodo(self.id, dato)
        self.id += 1
        if self.estaVacia():
            self.nodoInicio = nuevo
            self.nodoFinal = nuevo
        else:
            self.nodoFinal.setSiguiente(nuevo)
            self.nodoFinal = nuevo
        self.size += 1

    def imprimir(self):
        tmp = self.nodoInicio
        while tmp != None:
            print(tmp.getDato())
            tmp = tmp.getSiguiente()
#-----aqui intente recorrer la lista y para obtener la amplitud y poder graficar en forma de una tabla

    # def setAmplitudMaxima(self, amplitudmax):
    #     self.listaDeAmplitudes = amplitudmax

    # def getlistaAmplitudMaxima(self):
    #     return self.listaDeAmplitudes
    
    # def graficar(self, nombreArchivo):
    #     graph = Graph(nombreArchivo)
    #     tmp = self.nodoInicio
    #     while tmp != None:
    #         senal = tmp.getDato()
    #         amp = senal.getAmplitudMaxima()  # Obtener la amplitud máxima de la señal
    #         print("Amplitud: ", amp)
    #         graph.add(tmp, tmp.getSiguiente(),"2")
    #         tmp = tmp.getSiguiente()
    #     graph.generar()

    def limpiar_sistema(self):
        self.nodoInicio = None
        self.nodoFinal = None
        self.size = 0
        id = 0

    def graficar(self, nombreArchivo):
        graph = Graph(nombreArchivo)
        tmp = self.nodoInicio
        while tmp != None:
            graph.add(tmp, tmp.getSiguiente())
            tmp = tmp.getSiguiente()
        graph.generar()

    def convertirABinario(self):
        tmp = self.nodoInicio
        while tmp != None:
            if(int(tmp.getDato())>=1):
                tmp.setDato(1)
            tmp = tmp.getSiguiente()