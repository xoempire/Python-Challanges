# logic:
# a function which wold get a list as entry
# creates a duplicate of teh list without the coppy using set
# a function which would get a list as entry 
# creates a duplicate of the list and removes all the duplicates
a=[1, 1, 3, 5, 6, 7, 22, 22, 77, 88]
ini_lengh=a.__len__()
def dup_set(liist):
    b=set(liist)
    print(f'initial lengh={ini_lengh}')
    lst_lengh=b.__len__()
    print(f'initial lengh={lst_lengh}')
    return print(b)
dup_set(a)
print('\n\n\n')

def for_dup(a):
    b=a
    for i in b:
        if b.count(i)>1:
            b.remove(i)
    lst2_lengh=b.__len__()
    print(f'initial lengh={ini_lengh}')
    print(f'initial lengh={lst2_lengh}')
    return print(b)
for_dup(a)