import sys

if len(sys.argv) != 2:  
    print("You should provide a txt file.")
    sys.exit(1)

file_name = sys.argv[1]

print("Type 'x' to exit the program.")

with open(file_name, 'r') as file:
    content = file.read()
    color_list = content.splitlines()

if not color_list:
        print("The file is empty.")
        sys.exit(1)

print("Here are the colors in the file:")

for i, color in enumerate(color_list):
    print(f"{i+1}. {color_list[i]}")

while True:

    selection = input("What color do you want to select? ")

    if selection.isdigit():
        try:
            selection = int(selection)
            if 1 <= selection <= len(color_list):
                print(f"You selected: {color_list[selection - 1]}")
            else:
                print("Invalid selection. Please select a number from the list.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    else:
        selection = selection.lower()
        if selection in [color.lower() for color in color_list]:
            print(f"You selected: {selection}")
        
        elif selection == 'x':
            print("Exiting the program.")
            break

        else:
            print("Invalid selection. Please select a color from the list.")



