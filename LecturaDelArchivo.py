import xml.etree.ElementTree as ET
from ListaSimple import ListaSimple
from  Senal import Senal
import copy


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

        # print("_____Lista de senales_____")  la deje para mientras 
        # senalGuardada = listSenales.getInicio()
        # while senalGuardada != None:
        #     print(senalGuardada.getDato().getNombre(),"   :aqui")
        #     senalGuardada = senalGuardada.getSiguiente()

    def getDatos(self):
        for senal in self.raiz.findall('senal'):
            for dato in senal.findall('dato'):
                self.lista_enlazada.insertar(int(dato.text))
        
        global listaBinaria
        listaBinaria = copy.deepcopy(self.lista_enlazada)
        print("> Calculando la matriz binaria.... Precione *Enter*", end=" ")
        input()
        listaBinaria.convertirABinario()
        print("-----Se finalizo & Guardo el Calculo de la Matriz Binaria-----\n")
        
    
    def creacionDeGraficas(self):
        print("> Generando grafica Binaria y Lista_Enlazada.... Precione *Enter*", end=" ")
        input()
        listaBinaria.graficar('Lista_Binaria')  
        self.lista_enlazada.graficar('Lista_Enlazada')
        print("-----Se finalizo & Guardo las graficas Binaria y Lista_Enlazada-----\n")

    def reiniciSistema(self):
        listaBinaria.limpiar_sistema()
        self.lista_enlazada.limpiar_sistema()