# logic:
# asking the user for a string
# a function with the following abilities
# split the word with a space delimiter and add them to a list
# the list woudl be printed out with a reverse order
user_string=input('type in some words: ')
def reverser(stringy):
    listy=[i for i in stringy.split(' ')]
    a= listy[::-1]
    return print(" ".join(a))
reverser(user_string)
