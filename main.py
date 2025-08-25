import random

print("\nDice Rolling Game\n")
x=input("press 'Y' to roll and 'Any Key' to exit: ")
while x=='y':
    num= random.randint(1,6)
    if num==1:
        print("-------")
        print("|     |")
        print("|  o  |")
        print("|     |")
        print("-------")
    elif num==2:
        print("-------")
        print("|o    |")
        print("|     |")
        print("|    o|")
        print("-------")
    elif num==3:
        print("-------")
        print("|o    |")
        print("|  o  |")
        print("|    o|")
        print("-------")
    elif num==4:
        print("-------")
        print("|o   o|")
        print("|     |")
        print("|o   o|")
        print("-------")
    elif num==5:
        print("-------")
        print("|o   o|")
        print("|  o  |")
        print("|o   o|")
        print("-------")
    elif num==6:
        print("-------")
        print("|o   o|")
        print("|o   o|")
        print("|o   o|")
        print("-------")
    
    x=input("press 'Y' to roll again and 'Any Key' to exit: ")

print("\nThank You For Playing !!!\n")
    
