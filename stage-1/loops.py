fruits = ['apple', 'banana', 'grapes', 'pineapple']

for fruit in fruits:
    if(fruit != 'grapes'):
        print(fruit)
        continue
    else:
        break

print('\n')

for number in range(1, 8):
    print(number)

print('\n')

for letter in 'Hello!':
    print(letter)

print('\n')

count = 4

while count <= 10:
    print(count)
    count = count + 1