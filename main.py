from DatosEstudiante import DatosEstudiante

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
        print("Opcion 1")
    elif opcionSeleccionada == 2:
        print("Opcion 2")
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