class Heroe:
    nombre = ""
    poder = ""
    apodo = ""

    #self es el valor inicial que se indica para atributos y funciones que pertenecen a la misma clase
    #Se le llama constructor
    def __init__(self, nombre, poder, apodo): #función que inicializa la clase Heroe
        self.nombre = nombre
        self.poder = poder
        self.apodo = apodo

    def saludar(self):
        print("Hola como estás" + self.nombre)

    def datos_heroe(self):
        return f"Heroe: {self.nombre}, poder {self.poder}, apodo: {self.apodo} "

    #__str__ método mágico que devuelve una cadena representación de atributos del objeto

    def __str__(self) -> str:
        return f"Heroe: {self.nombre}, poder {self.poder}, apodo: {self.apodo} "

    #__repr__ método mágico para representar una cadena de devolución final

    def __repr__(self) -> str:
        return f"Heroe: {self.nombre}, poder {self.poder}, apodo: {self.apodo} "


spiderman = Heroe("Peter Parker", "super fuerza", "Spiderman") #spiderman es objeto/instancia de la clase Heroe
spiderman
"""
spiderman.nombre = "Peter Parker"
spiderman.poder = "Super fuerza"
spiderman.apodo = "Spiderman"
"""

ironman = Heroe("Tony Stark", "Millonario", "Hombre de acero")
print(spiderman)
"""
ironman.nombre = "Tony Stark"
ironman.poder = "Millonario"
ironman.apodo = "Hombre de acero"
"""

print(spiderman.nombre)
print(ironman.nombre)