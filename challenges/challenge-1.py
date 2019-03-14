#
# Challenge 1
#
# Write an algorithm that can take a sentence and reverse each
# word and return the new sentence
#

######################## solution 1 #########################

def reverseWord(word):
  return word[::-1]

result = 'Hola mundo!'
result = map(reverseWord, result.split(' '))
result = ' '.join(result)
print(result)

######################## solution 2 #########################

print(' '.join(map(lambda string : string[::-1], 'Hola mundo!'.split(' '))))

######################## solution 3 #########################

def reverseSentence(sentence):
  return ' '.join(map(lambda string : string[::-1], sentence.split(' ')))

print(reverseSentence('Hola mundo!'))