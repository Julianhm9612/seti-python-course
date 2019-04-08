colors = {'green', 'blue', 'yellow'}
print(type(colors))
print('red' in colors)
colors.add('violet')
print(colors) # agrega al inicio
colors.remove('blue')
colors.clear()
# del colors # eliminar set
print(colors)