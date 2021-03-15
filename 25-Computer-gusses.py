# logic:
# the user woudl have a number in her mind
# the program wudl try to guss it by giving it a number
# the user would give the program instructions wheather the nmber is higher or lower
# the program would guss different numbers based on the user input
# the number of gusses done by the program would be logged by the program and it woudl be presented to the user at the end of the programonce the program gusses the number the program woudl end
# the user has 3 input options --> +  -    =
# the user woudl also be asked to give us the range for the program to guss among
import sys
s=int(input('what is the first number for your range? '))
e=int(input('what is the last number for your range? '))
nomlist=[i for i in range(s,e)]
lst_itm=nomlist[int(len(nomlist)-1)]
frst_itm=nomlist[0]
middle=nomlist[int((lst_itm - frst_itm)/2)]
scnd_qua=nomlist[int((lst_itm + middle)/2)]
frst_qua=nomlist[int((middle + frst_itm)/2)]
def user():
    global user_input
    user_input=input("""if the number is higher than what the program has gussed press '+'\nif the number is lower than what the programm has gussed press '-'\nif the number is exactly right press '='\n """)
    return print(user)
computer_guss=middle
print(computer_guss)
user()
gusses=0
if user_input=="=":
        print('The computer in da house! ')
        gusses+=1
        exit()
else:
    while user_input!="=":
        if user_input=="=":
            print('The computer in da house! ')
            gusses+=1
            exit()
        elif user_input=='+' or user=="-":
            if user_input=="+":
                computer_guss2=scnd_qua
                print(computer_guss2)
                gusses+=1
                user()
                if user_input=="=":
                    print('The computer in da house! ')
                    exit()
                else:
                    while user_input!="=":
                        if user_input=="+":
                            while user_input!="=":
                                for i in range(scnd_qua, lst_itm):
                                    print(i)
                                    gusses+=1
                                    user()
                                    if user_input=="=":
                                        print('The computer in da house! ')
                                        exit()
                        elif user_input=="-":
                            while user_input!="=":
                                for i in range(scnd_qua, middle):
                                    print(i)
                                    gusses+=1
                                    user()
                                    if user_input=="=":
                                        print('The computer in da house! ')
                                        exit()
            elif user_input=="-":
                computer_guss=frst_qua
                print(computer_guss)
                gusses+=1
                user()
                if user=="=":
                    print('The computer in da house! ')
                    exit()
                else:
                    while user_input!="=":
                        if user_input=="+":
                            while user_input!="=":
                                for i in range(frst_qua, middle):
                                    print(i)
                                    gusses+=1
                                    user()
                                    if user_input=="=":
                                        print('The computer in da house! ')
                                        
                        elif user_input=="-":
                            while user_input!="=":
                                for i in range(frst_itm, frst_qua):
                                    print(i)
                                    gusses+=1
                                    user()
                                    if user_input=="=":
                                        print('The computer in da house! ')
                                        exit()







