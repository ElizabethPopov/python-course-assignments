import random

random_num = random.randint(1, 20)

while True:

    user_input = input("Guess a number between 1 and 20: ")
    
    try:
        user_guess = int(user_input)
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 20.")
        continue

    if random_num == user_guess:
        print("You guessed the number correctly!")
        break

    elif random_num < user_guess:
        print("The number you guessed is bigger than the actual number. Try again!")

    else:
        print("The number you guessed is smaller than the actual number. Try again!")


    