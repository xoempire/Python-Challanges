# logic:
# a function which each time that it is called would generate a random password with custome difficulty
# we woudl have 3 lists one for numbers one for alphabetical characters and one for special characters
# a random numbetr would be generated integer
# the user woudl be asked about the difficulty of the password and the number of characters that it wants the password to have
import random
listy=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 
'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
"1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "!", "@", "#", "$", "&", "*", "?"]
diff=int(input('for a normal password press 1\nfor a hard password press 2\nfor a super password press 3\n'))
if diff ==1:
    number =random.randint(8,15)
elif diff ==2:
    number =random.randint(10,18)
elif diff ==3:
    number =random.randint(18,40)
print(number)
passw=''.join(random.sample(listy, number))
print(f'Hi sir, your password has {number} characters and is\n{passw}')
