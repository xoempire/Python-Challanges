# logic:
# a random 4 digit number woudl be generated by the program
# the user woudl be asked to guss the numberif the number matches the number generated by the program the game would stop and the user woudl win
# mean while if the user gusses a number which is in the number that we generated by in a wrong place the user would get a cowif the user gusses a number which has the correct value and the correct place she woudl get a bullonce the user gets 4 bulls she woudl win the game
# the number of times that the user has made a guss would be counted and printd at the end of the gamealso at any time if the user types in exit the game woudl end
import random
number = str(random.sample(range(10), 4))
print(number)
def checekr(number, guss):
    global cowbull
    cowbull=[0,0]
    for i  in range(len(number)):
        if guss[i]==number[i]:
            cowbull[1]+=1
        else:
            cowbull[0]+=1
            return print(cowbull)
    print(f'as of this moment you have {cowbull[0]} cows and {cowbull[1]} bulls. keep on trying')
palying=True
gusses=0
# print(f'a 4 digit numebr is generated by the computer\nfor each correct digit that you guss(with the wrong positioning) you woudl get a cow\nfor each number that you guss with the right value and position yu woudl get a bull\nonce you get 4 bulls you woudl be declared the winner of the game and it woudl end\nat any point in the game if you type "exit" the game woudl stop and you woudl be retured to the terminal')
while palying:
    guss=input('guss the number if you may: ')
    if guss=='exit':
        print('Goodbye!')
        break
    cowbullcounter= checekr(number, guss)
    gusses+=1
    if cowbull[1]==4:
        print('Mis felicitaciones, you just won the fane with {gusses} number of gusses')
        break
    else:
        print('somehting aint right. try again')


