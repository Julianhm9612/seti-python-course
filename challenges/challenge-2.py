#
# Challenge 2
#
# Given a set of numbers, return the additive inverse of each.
# Each positive becomes negatives, and the negatives become positives.
#

######################## solution 1 #########################

def invert_numbers(numbers):
  return map(lambda number : number - number * 2 if number > 0 else number + number * -2, numbers)

print(invert_numbers((1, 2, -5)))