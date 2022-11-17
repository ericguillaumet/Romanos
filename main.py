'''
1. Crear una función que pase de entero > 0 y < 4000 a romano.

2. Cualquier otra entrada debe dar error.

Casos de prueba

a) 1994 -> MCMXCIV
b) 4000 -> RomanNumberError("el valor debe ser menor de 4000")
c) "unacadena" -> RomanNumberError("debe ser un entero")
d) 0 -> RomanNumberError("el valor debe ser mayor a cero")
e) -3 -> RomanNumberError("el valor debe ser mayor de cero")
f) 4.5 -> RomanNumberError("Debe ser un entero")
'''

class RomanNumberError(Exception):
    pass

milesimas = {
    1000: "M", 2000: "MM", 3000: "MMM"
}

unidades = {
    1: "I", 2: "II", 3: "III",
    4: "IV", 5: "V", 6: "VI",
    7: "VII", 8: "VIII", 9: "IX"
}

decenas = {
    10: "X", 20: "XX", 30: "XXX",
    40: "XL", 50: "L", 60: "LX",
    70: "LXX", 80: "LXXX", 90: "XC"
}

centenas = {
    100: "C", 200: "CC", 300: "CCC",
    400: "CD", 500: "D", 600: "DC",
    700: "DCC", 800: "DCCC", 900: "CM"
}

print("diccionario unidades ", unidades.get("I"))

def entero_a_romano(num):
    lista = []
    num = str(num)
    if len(num) <4:
        num = "{:0>4s}".format(num)

    lista = list(num)
    for i in range(len(lista)):
        lista[i] = lista[i] + "0" * ((len(lista)-1)-i)

    return lista

print("Funcion en acción", entero_a_romano(336))

for c,v in unidades.items():
    print(str(c) + " - " + str(v))