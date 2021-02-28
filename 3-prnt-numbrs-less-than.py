#Logic:
#create a new empty list
#go through a list and find the elements that are less than 5
#add the previously found elments to a new list
list=[1,3,5,1,6,234,456,23,23,3,1,4352,2,1,4,5,6234,345,2435,432,2345,12345,23]
number = int(input('Please enter a number: '))
new_list=[]
for i in list:
    if i < number:
        new_list.append(i)
print(new_list)
    