import os


class Grafica:

    def __init__(self):
        self.pedidos = []  # -----> Contiene la lista de todos los pedidos
        self.pedido = []  # -----> [nombre, cantidad, ingredientes[], tiempo]
        self.lista_nombres = []  # -----> Guarda una lista con los nombres
        self.nombre = ''  # -----> Guarda el nombre de cada cliente
        self.cantidad = 0  # -----> Guarda la cantidad de panes por cliente
        self.ingredientes = []  # -----> Guarda la lista de ingredientes por cliente
        self.tiempo = ''  # -----> Guarda el tiempo de cada pedido
        self.nodo = ''  # -----> Contendra la estructura de cada nodo

    def generar_grafica(self, pedidos):
        self.pedidos = pedidos
        self.pedido = []  # -----> Limpia las variables para graficar de nuevo
        self.lista_nombres = []  # ----->            |
        self.nombre = ''  # ----->                   |
        self.cantidad = 0  # ----->                  |
        self.ingredientes = []  # ----->             |
        self.tiempo = ''  # ----->                   v
        self.nodo = ''  # ----->            Lo mismo hasta aqui

        for pedido in range(len(self.pedidos)):  # -----> Va creando cada nodo con tablas
            self.pedido = self.pedidos[pedido]
            self.nombre = self.pedido[0]
            self.cantidad = self.pedido[1]
            self.ingredientes = self.pedido[2]
            self.tiempo = self.pedido[3]
            self.lista_nombres.append(self.nombre)
            self.nodo += f'{self.nombre} [shape=none, margin=0, label=<\n'
            self.nodo += '<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="2" CELLPADDING="7">\n'
            self.nodo += f'<TR><TD>Nombre</TD><TD>{self.nombre}</TD></TR>\n'
            self.nodo += f'<TR><TD>Cantidad</TD><TD>{self.cantidad}</TD></TR>\n'
            self.nodo += f'<TR><TD>Ingredientes</TD><TD>{self.ingredientes}</TD></TR>\n'
            self.nodo += f'<TR><TD>Tiempo</TD><TD>{self.tiempo}</TD></TR>\n'
            self.nodo += '</TABLE>>];\n'
            self.nodo += '\n'

        for nombre in range(len(self.lista_nombres)):  # -----> Va ordenando los nodos
            if self.lista_nombres[nombre] == self.lista_nombres[-1]:
                self.nodo += f'Fin_Pedidos->{self.lista_nombres[nombre]}\n'
            else:
                self.nodo += f'{self.lista_nombres[nombre+1]}->{self.lista_nombres[nombre]}\n'

        with open('archivos_creados/Comandos.dot', mode='w') as grafo:  # -----> Genera el grafo
            grafo.write('digraph Pedidos {\n')
            grafo.write(self.nodo)
            grafo.write('}')
        os.system('dot -Tpdf archivos_creados/Comandos.dot -o archivos_creados/Pedidos.pdf')

    def generar_grafica_vacia(self):  # -----> Genera un grafo sin pedidos
        self.nodo = 'Sin_Pedidos\n'

        with open('archivos_creados/Comandos.dot', mode='w') as grafo:
            grafo.write('digraph Pedidos {\n')
            grafo.write(self.nodo)
            grafo.write('}')
        os.system('dot -Tpdf archivos_creados/Comandos.dot -o archivos_creados/Pedidos.pdf')
