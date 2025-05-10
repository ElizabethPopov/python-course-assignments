import random

random_num = random.randint(1, 20)

print("Welcome to the Number Guessing Game!")
print("Type 's' to see the number, or 'x' to exit the game.")

while True:

    user_input = input("Guess a number between 1 and 20: ")

    if user_input.lower() == 'x':
        print("Exiting the game.")
        break

    elif user_input.lower() == 's':
        print(f'The number is {random_num}')
        continue
    
    try:
        user_input = int(user_input)
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 20.")
        continue

    if random_num == int(user_input):
        print("You guessed the number correctly!")
        break

    elif random_num < int(user_input):
        print("The number you guessed is bigger than the actual number. Try again!")

    else:
        print("The number you guessed is smaller than the actual number. Try again!")