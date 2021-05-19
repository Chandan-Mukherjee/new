# Truthy value / Falsy Value

# 0 , 0.0 and blank string are falsy


# Write a program that will ask for your name and will stop only if it matches. (VVI)

# augmented operator: i +=1

import sys
import random


def name():
    your_real_name = 'Chandan'
    user_provided_name = input("Enter your name pls: ")
    if user_provided_name.lower() == your_real_name.lower():
        print('name matched.')
        sys.exit()
    else:
        print('Name did not match')


def sum_calculator():
    num = int(input("Enter the number: "))
    sum = (num * (num + 1)) / 2
    print('Sum is: ', sum)


# print(sum(list(range(101))))

def guessing_game():
    org = random.randint(1, 20)
    count = 0
    print("Hello, whats's your name?")
    name = input('>>>')
    print('well,', name, ',I am thinking of a number between 1 and 20.Take a guess.')
    while True:
        if count < 6:
            guess = int(input('Take a guess.\n>>>'))
            if guess > org:
                print('your guess is too high.')
                count += 1
            elif guess < org:
                print('your guess is too low.')
                count += 1
            else:
                count += 1
                print('Good job,', name, ',You guessed my number in ', count, 'guesses.')
                break
        else:
            print('Sorry!!!, you are out of guesses.')
            break


# print(list('hello'))