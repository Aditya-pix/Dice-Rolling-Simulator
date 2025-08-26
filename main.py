import random
from colorama import Fore, Back, Style,init

init(autoreset=True)
print("\nDice Rolling Game\n")

dice_faces = {
    1: ["-------",
        "|     |",
        "|  o  |",
        "|     |",
        "-------"],
    2: ["-------",
        "|o    |",
        "|     |",
        "|    o|",
        "-------"],
    3: ["-------",
        "|o    |",
        "|  o  |",
        "|    o|",
        "-------"],
    4: ["-------",
        "|o   o|",
        "|     |",
        "|o   o|",
        "-------"],
    5: ["-------",
        "|o   o|",
        "|  o  |",
        "|o   o|",
        "-------"],
    6: ["-------",
        "|o   o|",
        "|o   o|",
        "|o   o|",
        "-------"]
}
colors=[Fore.RED,Fore.BLACK,Fore.BLUE,Fore.GREEN,Fore.YELLOW,Fore.CYAN,Fore.MAGENTA,Fore.WHITE]
x=input("press 'Y' to roll and 'Any Key' to exit: ").upper()

while x=='Y':
    num= random.randint(1,6)
    color=random.choice(colors)
    print(color + "\n".join(dice_faces[num]))  

    x = input(
    "Press " 
    + Fore.GREEN + Style.BRIGHT+ "Y" + Style.RESET_ALL 
    + " to roll again and " 
    + Fore.RED +  Style.BRIGHT + "Any Key" + Style.RESET_ALL 
    + " to exit: "
    ).upper()

print( Fore.GREEN + Style.BRIGHT +"\nThank You For Playing !!!\n")
    
