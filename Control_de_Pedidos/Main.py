from TDA import Cola
from Grafica import Grafica
from colorama import Fore
import os
import webbrowser
import datetime


class Main:

    def __init__(self):
        self.op = ''  # -----> Variable para controlar las opciones
        self.salida = False  # -----> Variable para finalizar el programa
        self.fecha = ''  # -----> Contendra la fecha y hora actual
        self.hora_p = 0  # -----> Controla las horas para el pedido
        self.hora_c = []  # -----> Controla las horas para la cola
        self.minuto_p = 0  # -----> Controla los minutos para el pedido
        self.minuto_c = []  # -----> Controla los minutos para la cola
        self.tiempo_pedido = ''  # -----> Muestra el tiempo del pedido
        self.tiempo_cola = [0, 0]  # -----> Muestra el tiempo del pedido en cola
        self.ingredientes = []  # -----> Lista de ingredientes seleccionados
        self.pedido = []  # -----> Contendra toda la información de 1 pedido
        self.pedidos = []  # -----> Es una lista de todos los pedidos
        self.pedidos_consola = Cola()  # -----> Lista de pedidos para mostrar en consola
        self.grafica = Grafica()  # -----> Es un objeto encargado de graficar

    def menu_principal(self):
        while not self.salida:
            print('                                                     ')
            print(Fore.GREEN+'┌------------ MENU PRINCIPAL ------------┐')
            print(Fore.GREEN+'|                                        |')
            print(Fore.GREEN+'|          1)   Generar pedido           |')
            print(Fore.GREEN+'|          2)   Mostrar pedidos          |')
            print(Fore.GREEN+'|          3)   Entregar pedido          |')
            print(Fore.GREEN+'|          4)   Mostrar datos            |')
            print(Fore.GREEN+'|          5)   Salir                    |')
            print(Fore.GREEN+'|                                        |')
            print(Fore.GREEN+'└----------------------------------------┘')
            print('                                                     ')

            self.op = input(Fore.CYAN+'--> Ingrese una opción: ')

            if self.op == '1':
                self.generar_pedido()
            elif self.op == '2':
                self.mostrar_pedidos()
            elif self.op == '3':
                self.entregar_pedido()
            elif self.op == '4':
                self.mostrar_datos()
            elif self.op == '5':
                self.salir()
            else:
                print('                             ')
                print(Fore.RED+'--> Opción no valida')

    def generar_pedido(self):
        print('                                           ')
        nombre = input(Fore.CYAN+'--> Nombre del cliente: ')
        print('                                         ')
        panes = input(Fore.CYAN+'--> Cantidad de panes: ')
        for pan in range(int(panes)):
            print('                                      ')
            print(Fore.YELLOW+'-----> Ingredientes <-----')
            print(Fore.GREEN+'  * 1) Salchicha')
            print(Fore.GREEN+'  * 2) Chorizo')
            print(Fore.GREEN+'  * 3) Salami')
            print(Fore.GREEN+'  * 4) Longaniza')
            print(Fore.GREEN+'  * 5) Costilla')
            print('                                                            ')
            ingrediente = input(Fore.CYAN+f'Ingrediente para el pan {pan + 1}: ')
            if ingrediente == '1':
                self.ingredientes.append('Salchicha')
                self.minuto_p = self.minuto_p + 2
                if self.minuto_p > 60:
                    self.hora_p = self.hora_p + 1
                    tiempo_extra = self.minuto_p - 60
                    self.minuto_p = tiempo_extra
            elif ingrediente == '2':
                self.ingredientes.append('Chorizo')
                self.minuto_p = self.minuto_p + 3
                if self.minuto_p > 60:
                    self.hora_p = self.hora_p + 1
                    tiempo_extra = self.minuto_p - 60
                    self.minuto_p = tiempo_extra
            elif ingrediente == '3':
                self.ingredientes.append('Salami')
                self.minuto_p = self.minuto_p + 1.5
                if self.minuto_p > 60:
                    self.hora_p = self.hora_p + 1
                    tiempo_extra = self.minuto_p - 60
                    self.minuto_p = tiempo_extra
            elif ingrediente == '4':
                self.ingredientes.append('Longaniza')
                self.minuto_p = self.minuto_p + 4
                if self.minuto_p > 60:
                    self.hora_p = self.hora_p + 1
                    tiempo_extra = self.minuto_p - 60
                    self.minuto_p = tiempo_extra
            elif ingrediente == '5':
                self.ingredientes.append('Costilla')
                self.minuto_p = self.minuto_p + 6
                if self.minuto_p > 60:
                    self.hora_p = self.hora_p + 1
                    tiempo_extra = self.minuto_p - 60
                    self.minuto_p = tiempo_extra
            else:
                self.ingredientes.append('Salchicha')
                self.minuto_p = self.minuto_p + 2
                if self.minuto_p > 60:
                    self.hora_p = self.hora_p + 1
                    tiempo_extra = self.minuto_p - 60
                    self.minuto_p = tiempo_extra
                print('                                  ')
                print(Fore.RED+'--> Ingrediente no valido')

        self.tiempo_pedido = f'{self.hora_p}:{self.minuto_p}'  # -----> Tiempo del pedido
        self.tiempo_cola[0] = self.tiempo_cola[0] + self.hora_p  # -----> Horas de espera
        self.tiempo_cola[1] = self.tiempo_cola[1] + self.minuto_p  # -----> Minutos de espera
        self.hora_c.append(self.hora_p)
        self.minuto_c.append(self.minuto_p)

        self.pedido.append(nombre)
        self.pedido.append(panes)
        self.pedido.append(self.ingredientes)
        self.pedido.append(self.tiempo_pedido)

        self.pedidos_consola.agregar(f'Tiempo de preparación: {self.tiempo_pedido}')
        self.pedidos_consola.agregar(f'Ingredientes: {self.ingredientes}')
        self.pedidos_consola.agregar(f'Cantidad de panes: {panes}')
        self.pedidos_consola.agregar(f'Nombre del cliente: {nombre}')
        self.pedidos_consola.agregar(' ')

        self.pedidos.append(self.pedido)
        self.pedido = []
        self.ingredientes = []
        self.hora_p = 0
        self.minuto_p = 0
        print('                                        ')
        print(Fore.GREEN+'--> Pedido generado con exito')

    def mostrar_pedidos(self):
        if not self.pedidos:  # -----> Si la lista de pedidos esta vacia entonces...
            print('                                   ')
            print(Fore.RED+'--> No hay pedidos en cola')

            self.grafica.generar_grafica_vacia()  # -----> Crea una grafo sin pedidos

            direccion = 'file:///' + os.getcwd() + '/' + 'archivos_creados/Pedidos.pdf'
            webbrowser.open_new(direccion)  # -----> Manda a abrir el pdf con el grafo
        else:
            print('                                             ')
            print(Fore.CYAN+'--------> Pedidos en Cola <--------')
            self.pedidos_consola.mostrar_contenido()  # -----> Muestra la cola en consola
            print('                                                                          ')
            print(Fore.YELLOW+f'Tiempo de espera: {self.tiempo_cola[0]}:{self.tiempo_cola[1]}')

            self.grafica.generar_grafica(self.pedidos)  # -----> Crea un grafo con los pedidos

            direccion = 'file:///' + os.getcwd() + '/' + 'archivos_creados/Pedidos.pdf'
            webbrowser.open_new(direccion)  # -----> Manda a abrir el pedf con el grafo

    def entregar_pedido(self):
        if not self.pedidos:  # -----> Si la lista de pedidos esta vacia entonces...
            print('                                   ')
            print(Fore.RED+'--> No hay pedidos en cola')
        else:
            self.pedidos_consola.quitar()
            self.pedidos_consola.quitar()
            self.pedidos_consola.quitar()
            self.pedidos_consola.quitar()
            self.pedidos_consola.quitar()
            self.pedidos.pop(0)
            hora = self.hora_c.pop(0)
            minutos = self.minuto_c.pop(0)
            self.tiempo_cola[0] = self.tiempo_cola[0] - hora
            self.tiempo_cola[1] = self.tiempo_cola[1] - minutos
            print('                               ')
            print(Fore.GREEN+'--> Pedido entregado')

    def mostrar_datos(self):
        hora = datetime.datetime.now()  # -----> Obtiene la fecha y hora actual del sistema
        self.fecha = hora.strftime('%d/%m/%Y %H:%M:%S')
        print('                         ')
        print(Fore.YELLOW+f'{self.fecha}')
        print(Fore.YELLOW+'┌------------------------------------------------------------┐')
        print(Fore.YELLOW+'|                      Práctica 1 - IPC2                     |')
        print(Fore.YELLOW+'|                                                            |')
        print(Fore.YELLOW+'|  --> Nombre: Kevin Alexander Lorenzo Lopez                 |')
        print(Fore.YELLOW+'|  --> Carnet: 201602987                                     |')
        print(Fore.YELLOW+'|  --> Curso: Introducción a la programación y computación 2 |')
        print(Fore.YELLOW+'|  --> Sección: B                                            |')
        print(Fore.YELLOW+'└------------------------------------------------------------┘')

    def salir(self):
        print('                                ')
        print(Fore.RED+'--> Programa finalizado')
        self.op = ''
        self.salida = True


app = Main()
app.menu_principal()
