x = 10
y = 1
color = 'blue'
first_name = 'Julian'
last_name = 'Henao'

# < > <= <= ==

if x < 30:
    print('X is less than 30')
else:
    print('X is greater than 30')

if color == 'red':
    print('The color is red')
else:
    print('Any color')

if color == 'yellow':
    print('The color is yellow')
elif color == 'blue':
    print('The color is blue')
else:
    print('Any color')

if first_name == 'Julian':
    if last_name == 'Henao':
        print('Tu eres Julian Henao')
    else:
        print('Tu no eres Julian Henao')

# and, or, not

if x > 2 and x < 100:
    print('x is greater than 2 and less than 100')

if x < 2 or x > 100:
    print('x is less than 2 or greater than 100')

if not(x == y):
    print('x is not equal y')