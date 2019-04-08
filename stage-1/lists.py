demo_list = [1, 'hello', 1.34, True, [1, 2, 3]]
colors = ['green', 'red', 'blue', 'red']

print(type(colors))
print(dir(colors))
print(len(colors))
print(colors[1])
print(colors[-2])
print('green' in colors) # preguntar si green esta en la lista
print('violet' in colors) # preguntar si violet esta en la lista
colors[1] = 'yellow'
colors.append('violet') # sirve solo para agregar un elemento
colors.extend(('blue', 'black')) # sirve apra agregar multiples elementos
colors.insert(1, 'violet') # insertar en un indice
colors.insert(len(colors), 'violet') # insertar al final
colors.pop() # quitar el ultimo elemento
colors.remove('green') # quitar un elemento en especifico
colors.pop(1) # eliminar un indice
colors.clear() # limpiar la lista
colors.sort(reverse=True)
print(colors.index('red')) # mostrar indice
print(colors.count('red')) # contar cuantas veces existe un elemento
print(colors)

# numbers_list = list((1, 2, 3, 4, 5))
# print(type(numbers_list))

# numbers_range = list(range(1, 101))
# print(numbers_range)