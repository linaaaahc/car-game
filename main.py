command = ""
while True:
    command = input("> ").upper()
    if command == "HELP":
        print('''Start - to start the car
Stop - stop the car
Quit - to exit''')
    elif command == "START":
        print("Car started...ready to go! ")
    elif command == "STOP":
        print("The car has been stopped ")
    elif command == "QUIT":
        break
    else:
        print("Sorry, I don't understand what you mean by that ")

