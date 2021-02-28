#Logic:
#among two lists get the ones that are in both lists
#no duplicates 
#print out the new list
list_1=[1, 234, 21342345, 2435, 345324, 3245234, 13453245, 13452345, 13452345, 222, 222, 234534, 234653456, 11, 2, 3, 4, 5]
list_2=[1, 21342345, 2345234, 444, 23423, 2222, 2345345, 5532134, 23134123, 123123, 111, 1, 343, 234, 2222, 22, 45345, 222, 44254, 345324, 23452364, 23452364, 234652356]
new_list=list(set(list_1).intersection(list_2))
print(new_list)
