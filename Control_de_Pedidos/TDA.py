from Nodo import Nodo
from colorama import Fore


class Cola:

    def __init__(self):
        self.ini = None  # -----> Nodo inicial

    def lista_vacia(self):
        if self.ini is None:  # -----> Si self.ini = None entonces...
            return True  # -----> La lista esta vacia
        else:
            return False  # -----> La lista no esta vacia

    def agregar(self, dato):
        nodo_auxiliar = Nodo(dato)  # -----> nodo_auxiliar es un objeto de la clase Nodo
        nodo_auxiliar.siguiente = self.ini  # -----> El apuntador de nodo_auxiliar --> ini
        self.ini = nodo_auxiliar  # -----> El nodo_auxiliar se coloca al principio de la lista

    def quitar(self):
        if self.lista_vacia():
            print('                       ')
            print(Fore.RED+'--> Cola vacia')
        elif self.ini.siguiente is None:
            self.ini = None
        else:
            nodo_anterior = self.ini
            nodo_actual = self.ini
            while nodo_actual.siguiente is not None:
                nodo_anterior = nodo_actual
                nodo_actual = nodo_actual.siguiente
            nodo_anterior.siguiente = None

    def mostrar_contenido(self):
        nodo_auxiliar = self.ini
        while nodo_auxiliar.siguiente is not None:
            print(nodo_auxiliar.dato)
            nodo_auxiliar = nodo_auxiliar.siguiente
        print(nodo_auxiliar.dato)
