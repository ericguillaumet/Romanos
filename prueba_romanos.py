from romano_class import NumeroRomano

continuar = True
quiero = True
valor = ""

while continuar:

    operacion = input("Convertir Entero a Romano: ingrese X\n Converitr Romano a Entero: ingrese Y")

    if operacion == "X":

        valor = input(int("Por favor ingresa un valor numérico: "))

        obj = NumeroRomano(valor)
        print (f"El valor de {obj.valor} es {obj.representacion}")

    elif operacion == "Y":

        valor = input(int("Por favor ingresa un valor romano: "))
        obj = NumeroRomano(valor)
        print (f"El valor de {obj.valor} es {obj.representacion}")
    
    else:
        print("Ingrese X o Y por favor")


    obj = NumeroRomano(valor)
    print (f"El valor de {obj.valor} es {obj.representacion}")

    v = input("Deseas continuar s/n")
    if v == "n":
        continuar = False