import logging
logging.basicConfig(filename = 'CarTestRun.log',level=logging.DEBUG,format = '%(name)s %(asctime)s %(levelname)s %(message)s')

car_is_running = False
print("Initializing the car game")
while True:
    print("""
start - To start the car
stop  - To stop the car
quit  - To quit the game
        """)
    command = input(">> ").lower()
    logging.info(f"The value entered by user is {command}")
    if command == 'start':
        if car_is_running :
            print("The car is already running!!!")
            car_is_running = True
        else :
            print("The car is starting now...")
            car_is_running = True
    elif command == 'quit' :
        print("Game is quitting now!!")
        break
    elif command == 'stop':
        if car_is_running :
            print("The car is stopping now...")
            car_is_running = False
        else :
            print("The car is already stopped!!!")
            car_is_running = False
    else :
        print("Sorry, I don't understand the command!!!")