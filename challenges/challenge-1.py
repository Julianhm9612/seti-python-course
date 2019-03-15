#
# Challenge 1
#
# Write an algorithm that can takes a sentence, reverse each
# word and returns the new sentence
#
# Input 'Hola mundo desde python!'
#

######################## solution 1 #########################

def reverse_word(word):
  return word[::-1]

result = 'Hola mundo desde python!'
result = map(reverse_word, result.split(' '))
result = ' '.join(result)
print(result)

######################## solution 2 #########################

solution_2 = lambda sentence : (' '.join(map(lambda word : word[::-1], sentence.split(' '))))

print(solution_2('Hola mundo desde python!'))

######################## solution 3 #########################

def reverse_sentence(sentence):
  return ' '.join(map(lambda word : word[::-1], sentence.split(' ')))

print(reverse_sentence('Hola mundo desde python!'))

######################## solution 4 #########################

product = reduce((lambda string, word: string + word[::-1] + ' '), 'Hola mundo desde python!'.split(' '), '')

print(product.strip())