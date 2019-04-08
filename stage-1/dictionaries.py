product = {
    'name': 'book',
    'quantity': 3,
    'price': 4.99
}

person = {
    'first_name': 'Julian',
    'last_name': 'Henao'
}

print(type(product))
print(dir(product))
print(person.keys())
print(person.items())
person.clear()
# del person
print(person)

products = [
    {'name': 'book', 'price': 12},
    {'name': 'pen', 'price': 5}
]
print(products)