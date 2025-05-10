import random
import sys  

random_num = random.randint(1, 20)

user_input = int(input("Guess a number between 1 and 20: "))

guess = True

while not guess:

    if random_num < user_input:
        print("The number you guessed is bigger than the actual number. Try again!")
        user_input = int(input("Guess a number between 1 and 20: "))

    else:
        print("The number you guessed is smaller than the actual number. Try again!")
        user_input = int(input("Guess a number between 1 and 20: "))

if random_num == user_input:
    print("You guessed the number correctly!")
    sys.exit()

    