# logic:
# a function which would accept a number
#the number would be tried agains all the positive numbers less than itself excpet 0 wo see if it is a prime number
#the result would be returned 
def prime(number):
    divi=[ i for i in range(1,number) if number%i==0]
    if number==1:
        return print('the number is not prime')
    if divi.__len__()>2:
        print('the number is not prime')
    else:
        print("the number is prime")
prime(1381)