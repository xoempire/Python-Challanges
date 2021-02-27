#logic
#ask the user to choose a mode
#if the mode choosen is not in range of 1, 2, 3 --> the programm would stop and ask the user what are you looking for
#if 1 is choosen --> we would calculate the remainder of the nuber divided by two if not zero then it is odd
#if 2 is choosen we would calculate the remainder of the number divided by 4 if not zero then it is not evenly divideable by 4
#if 3 is choosen we would ask for another number to check the first one by and see if it is evenly divideable by the second number or not
#at each stage we would print out the result in each mode
mode = int(input("""press 1 if you want to see if a number is odd or even\n
press 2 if you want to see if a number is evenly divideable by 4\n
press 3 if you wan to see if a number is divideable by another number 
"""))
while mode in range(1, 4):
    number = int(input('please enter a number to be divided: '))

    if mode == 1:
        if number%2!=0:
            print(f'{number} is odd ')
        else:
            print(f'{number} is even ')
    elif mode == 2:
        if number%4!=0:
            print(f'{number} is not divideable by 4')
        else:
            print(f'{number} is divideable by 4')
    elif mode == 3:
        check = int(input('please enter a number to divide the other number by: '))
        if number%check!=0:
            print(f'{number} is not divideable by {check}')
        else:
            print(f'{number} is divideable by {check}')
else:
    print('what are you looking for?')