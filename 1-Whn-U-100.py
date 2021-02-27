#Logic:
#ask for the name
#ask for the age
#ask for a random number(int)
#Feduce 100 by their age
#have the current time
#Add the remainder of 100 to the current year
#address them in a sentece and tell them at what age they will be a 100 years old 
#multiply the message by the random number on seperate lines

from datetime import datetime, timedelta
name = input('Please eneter your name: ')
age = int(input('Please eneter your age: '))
number = int(input('Please give me a random number: '))
the100 = 100 - age
time = datetime.now()
time = time.replace(year=time.year+the100)
print(f'Hello {name} you are going to be 100 years old at the year {time}\n'*number)