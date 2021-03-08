is_started = False

while True:
    choice = input('>')
    if choice == 'help' or choice == 'HELP':
        print("start - to start the car")
        print("stop - to stop the car")
        print("quit - to exit")
    elif not is_started and (choice == 'start' or choice == 'START'):
        print("Car started...Ready to go!")
        is_started = True
    elif is_started and (choice == 'start' or choice == 'START'):
        print("Car is already started")
    elif is_started and (choice == 'stop' or choice == 'STOP'):
        print("Car stopped.")
        is_started = False
    elif not is_started and (choice == 'stop' or choice == 'STOP'):
        print("Car is already stopped")
    elif choice == 'quit' or choice == 'QUIT':
        break
    else:
        print("I don't understand that")
