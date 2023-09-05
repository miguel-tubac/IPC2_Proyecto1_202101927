from ListaSimple import ListaSimple
import tkinter as tk
from tkinter import filedialog
from DatosEstudiante import DatosEstudiante
from LecturaDelArchivo import LecturaXML
from ArchivoDeSalida import crear_xml



##-------------------------------------------------------------Selecion del archivo-----------------------------------------------
def seleccionar_archivo():
    root = tk.Tk()
    root.withdraw()  # Ocultar la ventana principal
    
    archivo = filedialog.askopenfilename(initialdir='C:/Users/DELL/Downloads', title='Seleccionar archivo .xml', filetypes=[('Archivos de inventario', '*.xml')])
    return archivo

##-------------------------------------------------------------Menu principal-----------------------------------------------
while True:
    print("""          ---------------------------------------------------------------
                                MENU PRINCIPAL
          ---------------------------------------------------------------

          1. Cargar Archivo
          2. Procesar Archivo
          3. Escribir Archivo de Salida
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
        print("Opcion Carga Archivo, ---Seleccione el Archivo Correcto---")
        archivo_inventario = seleccionar_archivo()
        objLectura = LecturaXML(archivo_inventario)
        #objLectura.getDatos()
        print("----Archivo Ingresado Con Exito!----, Precione *Enter*", end=" ")
        input()
        objLectura.getSenal()

    elif opcionSeleccionada == 2:
        #print("Opcion 2")
        objLectura.getDatos()
        #print("> Realizando Suma de Tuplas")

    elif opcionSeleccionada == 3:
        print("----Calculadno El Archivo de salida 'archivo.xml'----, Precione *Enter para finalizar*", end=" ")
        input()
        crear_xml()
        print("-----Se finalizo & Guardo el archivo de salida 'archivo.xml'-----\n")
    elif opcionSeleccionada == 4:
        #print("Opcion 4")
        DatosEstudiante()
    elif opcionSeleccionada == 5:
        #print("Opcion 5")
        objLectura.creacionDeGraficas()
    elif opcionSeleccionada == 6:
        print("Iniciando el sistema...")
        objLectura.reiniciSistema()  # Llama a la función para reiniciar el sistema
        print("El sistema ha sido reiniciado. Para comprovar buelva a Graficar", end=" ")
        input()
    elif opcionSeleccionada == 7:
        print("Saliendo del programa.")
        break
    else:
        print("Error: Ingrese un número válido.")