# you will get three chances to guess

import random

secret_number = random.randint(0, 10)
print(f'Secret number is {secret_number}')
guess_count = 0

guess_limit = 3

while guess_count < guess_limit:
    guess_count += 1
    guessed_number = int(input("Enter the number you guessed between 0 to 10: \n"))
    if guessed_number == secret_number:
        print(f'\nCongratulations, you won the game in {guess_count} guesses')
        break
    else:
        print('\nSorry the number did not match, guess again.')
else:
    print('\nSorry, you are out of guesses !!!\n Try again next time')
