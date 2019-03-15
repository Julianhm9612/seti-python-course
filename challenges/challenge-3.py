#
# Challenge 3
#
# Make a program that filters a list of strings and returns a list with only your friends name in it.
# If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours! Otherwise,
# you can be sure he's not...
#
# Input ['Juan', 'Camilo', 'Mateo', 'Luis']
#

######################## solution 1 #########################

def friend(friends):
    return list(filter(lambda f : len(f) == 4, friends))

######################## solution 2 #########################

def friendLen(f):
    if len(f) == 4:
        return f

def friend(friends):
    return list(filter(friendLen, friends))

######################## solution 3 #########################

def friend(friends):
    return [f for f in friends if len(f) == 4]