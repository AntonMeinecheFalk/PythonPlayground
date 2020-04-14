from random import randint

isRunning = True

# Function: roleDice(sides)
def getDiceRoll(sides):
    diceRoll = randint(1, sides)
    return diceRoll

while isRunning:

    # Print options
    print("========================")
    print("1) 4 sided die")
    print("2) 6 sided die")
    print("3) 8 sided die")
    print("4) 10 sided die")
    print("5) 12 sided die")
    print("6) 20 sided die")

    # Ask the user, what die to roll

    userPick = input("Pick a option (type the number):")





    # Roll the given die
    if userPick == "1":
        print("your dice rolled: " + str(getDiceRoll(4)))
    elif userPick == "2":
        print("your dice rolled: " + str(getDiceRoll(6)))
    elif userPick == "3":
        print("your dice rolled: " + str(getDiceRoll(8)))
    elif userPick == "4":
        print("your dice rolled: " + str(getDiceRoll(10)))
    elif userPick == "5":
        print("your dice rolled: " + str(getDiceRoll(12)))
    elif userPick == "6":
        print("your dice rolled: " + str(getDiceRoll(20)))
    elif userPick == "7":
        isRunning = False
    else:
        print("please just pick a fucking die, im tired of this shit")
    