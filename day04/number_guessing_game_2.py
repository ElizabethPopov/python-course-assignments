import random

random_num = random.randint(1, 20)

while True:

    user_input = input("Guess a number between 1 and 20, or use 'x' to exit: ")

    if user_input.lower() == 'x':
        print("Exiting the game.")
        break

    if random_num == int(user_input):
        print("You guessed the number correctly!")
        break

    elif random_num < int(user_input):
        print("The number you guessed is bigger than the actual number. Try again!")

    else:
        print("The number you guessed is smaller than the actual number. Try again!")