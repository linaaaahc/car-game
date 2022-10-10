command = ""

while command.upper() != "QUIT":
    command = input("> ")
    if command.upper() == "HELP":
        print('''Start - to start the car
Stop - stop the car
Quit - to exit''')

    elif command.upper() == "START":
        print("Car started...ready to go! ")
    elif command.upper() == "STOP":
        print("The car has been stopped ")
    elif command.upper() == "QUIT":
        break
