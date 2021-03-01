#Logic:
#asks the user for a word
#split each character of the string
#append all to a list
#we would go through the list twice once from start to end and once from end to start
#if they both have the same characters each time --> the would be equal
#this would mean that the word is a palindrome
#print that the word is a palindrome
word = str(input('Please give me a word: '))
def split(wordy):
    return [i for i in wordy]
tisk=list(split(word))
if tisk[::-1] ==tisk[::]:
    print(f'{word} is a palindrome')
else:
        print(f'{word} is not a palindrome')