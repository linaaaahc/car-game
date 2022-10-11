command = ""
started = False
while True:
    command = input("> ").upper()
    if command == "HELP":
        print('''Start - to start the car
Stop - stop the car
Quit - to exit''')
    elif command == "START":
        if started:
            print("Car is already started ")
        else:
            started = True
            print("Car started...ready to go! ")
    elif command == "STOP":
        if not started:
            print("Car is already stopped")
        else:
            started = False
            print("The car is stopped ")

    elif command == "QUIT":
        break
    else:
        print("Sorry, I don't understand what you mean by that ")

