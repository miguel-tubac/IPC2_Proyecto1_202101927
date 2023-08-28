import tkinter as tk
from tkinter import filedialog
from DatosEstudiante import DatosEstudiante
from Graph import Graph
from Nodo import Nodo
import xml.etree.ElementTree as ET
import copy

##-------------------------------------------------------------Selecion del archivo-----------------------------------------------
def seleccionar_archivo():
    root = tk.Tk()
    root.withdraw()  # Ocultar la ventana principal
    
    archivo = filedialog.askopenfilename(initialdir='C:/Users/DELL/Downloads', title='Seleccionar archivo .xml', filetypes=[('Archivos de inventario', '*.xml')])
    return archivo

##-------------------------------------------------------------Lista enlazada-----------------------------------------------
class ListaSimple():
    id = 0
    def __init__(self):
        self.nodoInicio = None
        self.nodoFinal = None
        self.size = 0

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

    # def agregarInicio(self, dato):
    #     nuevo = Nodo(self.id, dato)
    #     self.id += 1
    #     if self.estaVacia():
    #         self.nodoInicio = nuevo
    #         self.nodoFinal = nuevo
    #     else:
    #         nuevo.setSiguiente(self.nodoInicio)
    #         self.nodoInicio = nuevo
    #     self.size += 1

    def imprimir(self):
        tmp = self.nodoInicio
        while tmp != None:
            print(tmp.getDato())
            tmp = tmp.getSiguiente()

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
    
    # def crearMatrizReducida(self, tiempoMaximoA):
    #     datosenal = self.nodoInicio
    #     iteradorSenal = 
    #     while 
    #         while datosenal != None:
    #             print(datosenal.dato," ID: ",datosenal.id, "Teimpo: ",tiempoMaximoA)
    #             datosenal = datosenal.getSiguiente()

##----------------------------------------Clase Pila para almacenar la informacion---------------------------------------------------
# class Pila(ListaSimple): #uso de herencia

#     def push(self, dato):
#         ListaSimple.insertar(self, dato)
    
#     def imprimir(self):
#         ListaSimple.imprimir(self)

#     def graficar(self, nombreArchivo):
#         ListaSimple.graficar(self, nombreArchivo)

#     def convertirABinario(self):
#         ListaSimple.convertirABinario(self)

##----------------------------------------------Funcion para almacenar la informacion-----------------------------------------------
class LecturaXML():
    def __init__(self, path):
        self.raiz = ET.parse(path).getroot()
        self.lista_enlazada = ListaSimple()

    def getSenal(self):
        listSenales = ListaSimple()
        for senal in self.raiz.findall('senal'):
           nombreSenal = senal.get('nombre')
           tiempoMaximo = senal.get('t')
           amplitudMaxima = senal.get('A') 
           tmpSenal = Senal(nombreSenal, tiempoMaximo, amplitudMaxima)


        print("_____Lista de senales_____")
        senalGuardada = listSenales.getInicio()
        while senalGuardada != None:
            print(senalGuardada.getDato().getNombre())
            senalGuardada = senalGuardada.getSiguiente()

    # def crearMatrizReducida(self):
    #     datosenal = self.nodoInicio
    #     iteradorSenal = 
    #     while 
    #         while datosenal != None:
    #             print(datosenal.dato," ID: ",datosenal.id, "Teimpo: ",tiempoMaximoA)
    #             datosenal = datosenal.getSiguiente()

    def getDatos(self):
        for senal in self.raiz.findall('senal'):
            for dato in senal.findall('dato'):
                self.lista_enlazada.insertar(int(dato.text))

        listaBinaria = copy.deepcopy(self.lista_enlazada)
        listaBinaria.convertirABinario()
        
        listaBinaria.graficar('listaBinaria')
        print("> Calculando la matriz binaria.... Precione *Enter*", end=" ")
        input()
        self.lista_enlazada.graficar('Lista_Enlazada')

        # aqui bamos a recorrer para comparar y comprimir la matriz 
        tmp = None
        for senal in self.raiz.findall('senal'):
            for dato in senal.findall('dato'):
                if int(self.senal.findall('t')) > 0:
                    tmp = True

        # lista_Reducida = copy.deepcopy(self.lista_enlazada)
        # lista_Reducida.crearMatrizReducida()


##----------------------------------------------Clase Amplitud de senal-----------------------------------------------
class Amplitud:
    def __init__(self, amplitud, dato=0):
        self.amplitud = amplitud
        self.dato = dato

    def getAmplitud(self):
        return self.amplitud
    
    def getDato(self):
        return self.dato
    
    def print(self):
        print(self.amplitud, self.dato)


##----------------------------------------------Funcion para almacenar las senales-----------------------------------------------
class Senal:
    def __init__(self, nombre, tiempoMaximo, amplitudMaxima):
        self.nombre = nombre
        self.tiempoMaximo = tiempoMaximo
        self.amplitudMaxima = amplitudMaxima
        self.tiempos = ListaSimple()
        self.crearListaTiempo()
        self.imprimir()
        

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
        print("_____Tiempos para senal:", self.getNombre() ,"_____")
        tmpTiempo = self.tiempos.getInicio()
        while tmpTiempo != None:
            print(tmpTiempo.getDato().getTiempo())
            tmpTiempo = tmpTiempo.getSiguiente()

##----------------------------------------------Clase tiempo-----------------------------------------------
class Tiempo:
    def __init__(self, tiempo, amplitud):
        self.tiempo = tiempo
        self.amplitud = amplitud
        self.listaAmplitudes = ListaSimple()
        self.llenarListadoAmplitudes()
        self.imprimir()


    def getTiempo(self):
        return self.tiempo
    
    def getAmplitud(self):
        return self.amplitud
    
    def llenarListadoAmplitudes(self):
        for i in range(1, int(self.amplitud)+1):
            tmpAmplitud = Amplitud(i)
            self.listaAmplitudes.insertar(tmpAmplitud)

    def imprimir(self):
        print("_____Amplitudes para tiempo:", self.getTiempo() ,"_____")
        objAmplitud = self.listaAmplitudes.getInicio()
        while objAmplitud != None:
            print(objAmplitud.getDato().getAmplitud())
            objAmplitud = objAmplitud.getSiguiente()



##-------------------------------------------------------------Menu principal-----------------------------------------------
while True:
    print("""          ---------------------------------------------------------------
                                MENU PRINCIPAL
          ---------------------------------------------------------------

          1. Cargar Archivo
          2. Procesar Archivo
          3. Escrivir Archivo de Salida
          4. Mostrar Datos del Estudiante
          5. Generar Grafica
          6. Iniciar Sistema
          7. Salir

          Ingrese una Opcion: """, end=" ")
    try:
        opcionSeleccionada = int(input())
    except ValueError:
        print("Error: Ingrese un número válido.")
        continue

    if opcionSeleccionada == 1:
        print("Opcion Carga Archivo, Seleccione el Archivo Correcto")
        archivo_inventario = seleccionar_archivo()
        objLectura = LecturaXML(archivo_inventario)
        #objLectura.getDatos()
        print("----Archivo Ingresado Con Exito!----, Precione *Enter*", end=" ")
        input()
        objLectura.getSenal()

    elif opcionSeleccionada == 2:
        print("Opcion 2")
        objLectura.getDatos()
        #print("> Realizando Suma de Tuplas")

    elif opcionSeleccionada == 3:
        print("Opcion 3")
    elif opcionSeleccionada == 4:
        print("Opcion 4")
        DatosEstudiante()
    elif opcionSeleccionada == 5:
        print("Opcion 5")
    elif opcionSeleccionada == 6:
        print("Opcion 6")
    elif opcionSeleccionada == 7:
        print("Saliendo del programa.")
        break

