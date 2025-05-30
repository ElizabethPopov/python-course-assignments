import random

random_num = random.randint(1, 20)
debug_mode = False

print("Welcome to the Number Guessing Game!")
print("Type 's' to see the number, 'x' to exit the game, or 'd' for debug mode.")

while True:

    if debug_mode:
        print(f"DEBUG MODE: The random number is {random_num}")

    user_input = input("Guess a number between 1 and 20: ")

    if user_input.lower() == 'x':
        print("Exiting the game.")
        break

    elif user_input.lower() == 's':
        print(f'The number is {random_num}')
        continue
    
    elif user_input.lower() == 'd':
        debug_mode = not debug_mode 
        print(f"Debug mode is now {'ON' if debug_mode else 'OFF'}")
        continue

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