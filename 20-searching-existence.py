# logic:
# accepts a list as the entry 
# if it is not sorted the list woudl be sorted (a list of numbers)
# then it would accept a number from the user and look for the number in the list
# if the nuber eas in the list it would return true and if not it would return false
listy=[i for i in range (1,50)]
number=input('enter a number to see if it exists or not?! ')
if number in listy:
    print('True')
else:
    print(False)



