# logic:
# a function generates fibonacci sequence (a specific amount of times)
# the user would be asked to give us the number of times that it wants the function to generate fibonacci numbers
# if the number was 0 --> the result would be nothing
# if the number was 1 the result would be 1
# if the number was 2 the result would be 1,1
# if the result was bigger than 2 the result would be the addition of two previous elements till the number which the user have given us
# the numbers would be added to a list
# the list would be presented to the user
def fibon():
    numb=int(input('how many fibonaccies? '))
    nacci=[]
    if numb == 0:
        print("")
    elif numb ==1:
        nacci.append(1)
    elif numb ==2:
        nacci.extend([1, 1])
    elif numb > 2:
        nacci=[1, 1]
        i = 1
        while i < (numb -1):
            nacci.append(nacci[i]+nacci[i-1])
            i+=1
    return print(nacci)
fibon()





