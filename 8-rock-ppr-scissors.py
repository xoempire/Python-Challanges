#logic:
# set 3 options for rock paper and scissors
# ask the user to choose one of the three available options 
# then switch to theother user and ask the other one to choose one of the options
# if both choose the same thing it is a draw
# rock beats scissors
# scissors beat paper 
# paper beats rock
# declare the winner and you can ask them to press 2 if they want to start over
user1=int(input("""User 1's turn\n\n\npress 1 for rock\npress 2 for paper\npress 3 for scissors"""))
user2=int(input("""User 2's turn\n\n\npress 1 for rock\npress 2 for paper\npress 3 for scissors\n\n\n"""))
if user1==user2:
    print("it was a draw")
elif user1==1:
    if user2==2:
        print("user 2 has won")
    elif user2==3:
        print('User 2 has lost')
elif user1==2:
    if user2==1:
        print('User 1 has won')
    elif user2==3:
        print('User 2 has lost')
elif user1==3:
    if user2==2:
        print('User 2 has lost')
    elif user2==1:
        print('User 2 has lost')
if user1==1:
    first="rock"
elif user1==2:
    first="paper"
elif user1==3:
    first="scissors"
else:
    print('who can tell where the road goes!?')
if user2==1:
    second="rock"
elif user2==2:
    second="paper"
elif user2==3:
    second="scissors"
else:
    print('who can tell where the road goes!?')
print(f'User 1 choose {first}')
print(f'User 2 choose {second}')