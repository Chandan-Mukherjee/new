import sys

name = input('Hi there, what is your name? ')
print(f'Hello {name}, it is nice to meet you.')


def age_in_seconds():
    age_in_year = int(input('Please enter your age in years: '))
    age_in_second = age_in_year * 365 * 24 * 60 * 60
    print(f'Your age in seconds is: {age_in_second}')


def age_in_years():
    age_in_second = int(input('Please enter your age in seconds: '))
    age_in_year = age_in_second / 365 / 24 / 60 / 60
    print(f'Your age in years is: {age_in_year}')


def consent_2():
    while True:
        consent = input('Would you like to play again? press y to say yes and n to say no: ')
        if consent == 'y':
            return True
        elif consent == 'n':
            print(f'Bye {name}, hope to see you again.')
            sys.exit()
        else:
            print('please select y or n')


while True:
    option = int(input(
        'Please enter 1 to know your age in seconds, enter 2 to know your age in years, enter 3 to exit the game.'))
    if option == 1:
        age_in_seconds()
        consent_2()
    elif option == 2:
        age_in_years()
        consent_2()
    elif option == 3:
        print(f'Bye {name}, hope to see you again.')
        break
    else:
        print('Please select correct option.')
