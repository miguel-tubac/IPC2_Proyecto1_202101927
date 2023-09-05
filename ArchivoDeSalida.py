import xml.etree.ElementTree as ET
import xml.dom.minidom

def crear_xml():
    # Crear el elemento raíz
    root = ET.Element("senalesReducidas")

    # Crear la etiqueta senal
    senal = ET.SubElement(root, "senal")
    senal.set("nombre", "Prueba 1")
    senal.set("A", "4")

    # Crear grupos
    for g in range(1, 4):
        grupo = ET.SubElement(senal, "grupo")
        grupo.set("g", str(g))

        # Crear tiempos
        tiempos = ET.SubElement(grupo, "tiempos")
        if g == 1:
            tiempos.text = "1,3"
        elif g == 2:
            tiempos.text = "2,5"
        elif g == 3:
            tiempos.text = "4"

        # Crear datosGrupo
        datosGrupo = ET.SubElement(grupo, "datosGrupo")
        for a in range(1, 5):
            dato = ET.SubElement(datosGrupo, "dato")
            dato.set("A", str(a))
            if g == 1:
                if a == 1:
                    dato.text = "5"
                elif a == 2:
                    dato.text = "7"
                elif a == 3:
                    dato.text = "0"
                elif a == 4:
                    dato.text = "6"
            elif g == 2:
                if a == 1:
                    dato.text = "0"
                elif a == 2:
                    dato.text = "0"
                elif a == 3:
                    dato.text = "9"
                elif a == 4:
                    dato.text = "4"
            elif g == 3:
                if a == 1:
                    dato.text = "1"
                elif a == 2:
                    dato.text = "0"
                elif a == 3:
                    dato.text = "1"
                elif a == 4:
                    dato.text = "5"

    # Crear un objeto ElementTree
    tree = ET.ElementTree(root)

    # Crear una cadena XML con formato
    xml_str = xml.dom.minidom.parseString(ET.tostring(root)).toprettyxml()

    # Escribir la cadena en un archivo XML
    with open("archivo.xml", "w") as xml_file:
        xml_file.write(xml_str)

