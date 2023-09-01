import graphviz


class Graph():
    def __init__(self, nombreArchivo):
        self.nombreArchivo = nombreArchivo
        self.dot = graphviz.Digraph('structs', filename=f'{self.nombreArchivo}.gv', node_attr={'shape': 'ellipse', 'fontname':'Helvetica'})    

    def add(self, nodoInicio, nodoSiguiente,Amplitud):
        global cambioDeFila
        cambioDeFila = False
        if(nodoSiguiente != None):
            if nodoInicio.getId() == 0:
                self.dot.node("a","Prueba1")
                for i in Amplitud:
                    self.dot.node(str(nodoInicio.getId()), str(nodoInicio.getDato()))#(0,2)
                    self.dot.edge("a",str(nodoInicio.getId()))
                    # self.dot.node(str(nodoSiguiente.getId()), str(nodoSiguiente.getDato()))#(1,3)
                    # self.dot.edge("a",str(nodoSiguiente.getId()))
                    self.dot.node(str(nodoSiguiente.getId()+i), str(nodoSiguiente.getDato()+i))#(2,0)
                    self.dot.edge("a",str(nodoSiguiente.getId()+i))
                cambioDeFila = True

            elif cambioDeFila:
                self.dot.node(str(nodoInicio.getId()), str(nodoInicio.getDato()))
                self.dot.node(str(nodoSiguiente.getId()), str(nodoSiguiente.getDato()))
                self.dot.edge(str(nodoInicio.getId()), str(nodoSiguiente.getId()))

    def generar(self):
       self.dot.render(outfile=f'img/{self.nombreArchivo}.png').replace('\\', '/')
       f'img/{self.nombreArchivo}.png' 