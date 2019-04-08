myString = unicode('hello world!', 'utf-8')
expresion = 'Hey!'

# Mostrar que se puede hacer con el string
print(dir(myString))

print('{} {}'.format(expresion, myString))
print('Hey! {0}'.format(myString))
# print(expresion, myString, sep=' ')
# print(f'Hey! {myString}') # Otra manera de concatenar python >= 3.6

print(myString.upper())
print(myString.lower())
print(myString.swapcase())
print(myString.capitalize())
print(myString.replace('hello', 'bye'))
print(myString.count('l'))
print(myString.startswith('l'))
print(myString.endswith('!'))
print(myString.split()) # Separa por espacio
print(myString.split(' '))
print(myString.find('o'))
print(len(myString))
print(myString.index('e'))
print(myString.isnumeric()) # Funciona siempre y cuando es unicode
print(myString.isalpha()) # Solo que contenga letras del alfabeto
print(myString[4]) # Mostrar caracter en n posicion
