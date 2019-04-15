def hello(param_name = 'World'):
    print('Hello '+ param_name +'!')

hello('Julian')
hello()

def sum(param_number_one, param_number_two):
    return param_number_one + param_number_two

print(sum(4, 7))
print(sum(4, sum(3, 1)))

add = lambda number_one, number_two : number_one + number_two

print(add(2, 10))