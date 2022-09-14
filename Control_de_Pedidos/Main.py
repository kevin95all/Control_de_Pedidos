from TDA import Cola
from Grafica import Grafica
from colorama import Fore
import os
import webbrowser
import datetime


class Main:

    def __init__(self):
        self.salida = False
        self.hora = 0
        self.minuto = 0
        self.hora_final = ''
        self.op = ''
        self.nombre = ''
        self.pizzas = ''
        self.ingredientes = []
        self.pedidos = []
        self.pedidos_consola = Cola()
        self.grafica = Grafica()

    def menu_principal(self):
        while not self.salida:
            print('                                          ')
            print('┌------------ MENU PRINCIPAL ------------┐')
            print('|                                        |')
            print('|          1)   Generar pedido           |')
            print('|          2)   Mostrar pedidos          |')
            print('|          3)   Entregar pedido          |')
            print('|          4)   Mostrar datos            |')
            print('|          5)   Salir                    |')
            print('|                                        |')
            print('└----------------------------------------┘')
            print('                                          ')

            self.op = input('--> Ingrese una opción: ')

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
                print('                    ')
                print('--> Opción no valida')

    def generar_pedido(self):
        hora = datetime.datetime.now()
        self.hora = int(hora.strftime('%H'))
        self.minuto = int(hora.strftime('%M'))
        print('                                      ')
        self.nombre = input('--> Nombre del cliente: ')
        print('                                      ')
        self.pizzas = input('--> Cantidad de pizzas: ')
        for pizza in range(int(self.pizzas)):
            print('             ')
            print('Ingredientes:')
            print('  * 1) Pepperoni')
            print('  * 2) Salchicha')
            print('  * 3) Carne')
            print('  * 4) Queso')
            print('  * 5) Piña')
            print('                                                      ')
            ingrediente = input(f'Ingrediente para la pizza {pizza + 1}: ')
            if ingrediente == '1':
                self.ingredientes.append('Pepperoni')
                self.minuto = self.minuto + 3
                if self.minuto > 60:
                    self.hora = self.hora + 1
                    tiempo_extra = self.minuto - 60
                    self.minuto = tiempo_extra
            elif ingrediente == '2':
                self.ingredientes.append('Salchicha')
                self.minuto = self.minuto + 4
                if self.minuto > 60:
                    self.hora = self.hora + 1
                    tiempo_extra = self.minuto - 60
                    self.minuto = tiempo_extra
            elif ingrediente == '3':
                self.ingredientes.append('Carne')
                self.minuto = self.minuto + 10
                if self.minuto > 60:
                    self.hora = self.hora + 1
                    tiempo_extra = self.minuto - 60
                    self.minuto = tiempo_extra
            elif ingrediente == '4':
                self.ingredientes.append('Queso')
                self.minuto = self.minuto + 5
                if self.minuto > 60:
                    self.hora = self.hora + 1
                    tiempo_extra = self.minuto - 60
                    self.minuto = tiempo_extra
            elif ingrediente == '5':
                self.ingredientes.append('Piña')
                self.minuto = self.minuto + 2
                if self.minuto > 60:
                    self.hora = self.hora + 1
                    tiempo_extra = self.minuto - 60
                    self.minuto = tiempo_extra
            else:
                self.ingredientes.append('Pepperoni')
                self.minuto = self.minuto + 3
                if self.minuto > 60:
                    self.hora = self.hora + 1
                    tiempo_extra = self.minuto - 60
                    self.minuto = tiempo_extra
                print('                         ')
                print('--> Ingrediente no valida')
        self.hora_final = f'{self.hora}:{self.minuto}'

        self.pedidos_consola.agregar(f'Cantidad de pizzas: {self.pizzas}')
        self.pedidos_consola.agregar(f'Tiempo de entrega: {self.hora_final}')
        self.pedidos_consola.agregar(f'Nombre del cliente: {self.nombre}')
        self.pedidos_consola.agregar('<------------------------->')
        self.pedidos.append(f'Nombre_{self.nombre}__Pizzas_{self.pizzas}')

        print('                             ')
        print('--> Pedido generado con exito')

    def mostrar_pedidos(self):
        if self.pedidos_consola.lista_vacia():
            print('                          ')
            print('--> No hay pedidos en cola')
        else:
            print('                               ')
            self.pedidos_consola.mostrar_contenido()
            self.grafica.generar_grafica(self.pedidos)

    def entregar_pedido(self):
        if self.pedidos_consola.lista_vacia():
            print('                          ')
            print('--> No hay pedidos en cola')
        else:
            self.pedidos_consola.quitar()
            self.pedidos_consola.quitar()
            self.pedidos_consola.quitar()
            self.pedidos_consola.quitar()
            self.pedidos.pop(0)
            self.grafica.generar_grafica(self.pedidos)
            print('                    ')
            print('--> Pedido entregado')

    def mostrar_datos(self):
        hora = datetime.datetime.now()
        self.hora = hora.strftime('%d/%m/%Y %H:%M:%S')
        print('                                                              ')
        print('┌------------------------------------------------------------┐')
        print('|                      Práctica 1 - IPC2                     |')
        print('|                                                            |')
        print('|  --> Nombre: Kevin Alexander Lorenzo Lopez                 |')
        print('|  --> Carnet: 201602987                                     |')
        print('|  --> Curso: Introducción a la programación y computación 2 |')
        print('|  --> Sección: A                                            |')
        print('└------------------------------------------------------------┘')

    def salir(self):
        print('                       ')
        print('--> Programa finalizado')
        self.op = ''
        self.salida = True


app = Main()
app.menu_principal()
