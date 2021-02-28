#Logic:
#ask the user for a number
#devide the number by all the numbers less than or qual to it
#if the remainder was something other than 0, then it is not a divider for the nmber
#add the dividers to a list
number = int(input('please enter a number: '))
list=[]
for i in range(1, number+1):
    if number%i==0:
        list.append(i)

if list.__len__()>3:
    print(list)
else:
    print(f'{number} has no dividers other than 1 and {number}')

