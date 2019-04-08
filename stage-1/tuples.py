x = (1, 2, 3)
print(type(x))
print(dir(x))

z = (1) # si solo tiene un elemento no es considerado una tupla
print(z)
print(type(z))

monts = ('Enero', 'Febrero')

y = tuple((1, 2 , 3))
print(y)
print(y[2])

del y # eliminar tuple

locations = {
    (35.213555, 39.44555): 'tokio',
    (3.213555, 9.44555): 'New york'
}

