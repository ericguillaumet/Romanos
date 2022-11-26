#Clase: molde de estructura de código que se puede reutilizar
#Self: indica función o variable que se atribuye a la clase persona.
#Self: referencia a las variables y funciones de la misma clase

import datetime

class Persona():
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.fecha = datetime.datetime.now()

    #métodos mágicos

    def __str__(self): #mostrar los datos de un objeto en string
        return f"Nombre: {self.nombre}, Email: {self.email}, Fecha: {self.fecha}"

    def __repr__(self): #mostrar la representación de un objeto en string
        return f"Nombre: {self.nombre}, Email: {self.email}, Fecha: {self.fecha}"

    def __add__(self, otro): #sumar objetos
        #return f"Nombre: {self.nombre}, Email: {self.email}, Fecha: {self.fecha} Objeto de afuera: {otro.valor}"
        return f"la suma es: {10 + otro.valor}"

class Segundo:
    def __init__(self, valor):
        self.valor = valor     

class Comida:
    def __init__(self):
        self.valor = 1991   

jose = Persona("Jose", "jose@email.com")
#print(str(datetime.datetime.now()))
#print(repr(datetime.datetime.now()))
saludar = Persona("Eric", "eguillaumet@protonmail.com")
segundo = Segundo(1998)
comida = Comida()

sumar = saludar + comida

print(sumar)