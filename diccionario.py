d1 = {
    "nombre": "Carlos",
    "edad": 45,
    "dni": "Y32987B",
    10: "X"
}

d2 = dict ([
    ('nombre', 'Dulce'),
    ('edad', 25),
    ('dni','T8787R'),
    (2, "activado")

])
print(d1)
print(d2)

#función get
print(d2.get(2))

#función clear, elimina todo el diccionario
d2.clear()
print("función clear", d2)

#función items. Devuelve una lista con los keys y values del diccionario (útil para poder iterar)

valores = d1.items()
print("función items", valores)

for key,val in valores:
    print(str(key) + " - " + str(val))

#función keys. Devuelve una lista con todas las keys del diccionario

keys = d1.keys()
print("función key", keys)

#función values, devuelve una lista con todos los valores del diccionario

valores = d1.values()
print("función values", valores)

#función para agregar, pop(key)

d1.pop(10)
print("función pop(10)", d1)

#función update para añadir más valores a un diccionario

#d3 = {'a': 100, 'b': 5, 'c': 60} -> Otra manera de hacerlo
d1.update({'a':100, 'b': 50, 'c': 60})
print("función update", d1)

#popitem() elimina de manera aleatoria un elemento del diccionario

d1.popitem()
print("función popitem", d1)