#This code is for inbuilt car button
while True:
    command= input("> ").lower()
    if command == "start":
        print("car started")
    elif command == "stop":
        print("car stopped")
    elif command == "help":
        print("""
    welcome to help @bishop
    start: To start the car
    stop: To stop the car
    quit:To quit the car
        """)
    elif command == "quit":
        break
    else:
        print("I don't understand the command")
print("This program is written by @bishop")

