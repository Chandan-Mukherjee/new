import sys


def start():
    print('Car started...Ready to go!')


def stop():
    print('Car stopped.')


def quit():
    sys.exit()


def main_function():
    Car_running = False
    while True:
        user_input = input('>')

        if user_input.lower() == 'help':
            print('Start - to start the car')
            print('Stop - to stop the car')
            print('quit - to exit')
        elif user_input.lower() == 'start':
            if not Car_running:
                start()
                Car_running = True
            else:
                print('Car is already started.')
        elif user_input.lower() == 'stop':
            if Car_running:
                stop()
                Car_running = False
            else:
                print('Car is already stopped.')
        elif user_input.lower() == 'quit':
            quit()
        else:
            print("I don't understand that...")


main_function()
