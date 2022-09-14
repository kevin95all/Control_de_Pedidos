import os


class Grafica:

    def __init__(self):
        self.id = 0
        self.lista = []

    def generar_grafica(self, pedidos):
        self.id = 0
        self.lista = pedidos
        with open('archivos_creados/Grafica.dot', mode='w') as grafica:
            grafica.write('digraph Pedidos{\n')
            for nodo in self.lista:
                if nodo != self.lista[-1]:
                    grafica.write(f'{self.lista[self.id + 1]}' + '->' + f'{self.lista[self.id]};\n')
                else:
                    grafica.write('Fin_de_la_cola->' + f'{self.lista[self.id]};\n')
                self.id = self.id + 1
            grafica.write('}')
        os.system('dot -Tpdf archivos_creados/Grafica.dot -o archivos_creados/Grafica.pdf')
