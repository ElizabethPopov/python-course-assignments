import sys

# Check if the correct number of arguments is provided
if len(sys.argv) < 2 or len(sys.argv) > 3:
    print("----\nError: You must provide only a txt file and optionally one selection (number or color).")
    print("Example: python color_selector_file.py [file] [selection]")
    sys.exit(1)

file_name = sys.argv[1]

# Check if it is a valid text file
if not file_name.endswith('.txt'):
    print("----\nError: The provided file is not a valid text file.")
    sys.exit(1)

# Check if the file exists and is readable
try:
    with open(file_name, 'r') as file:
        content = file.read().splitlines()
        color_list = [color.strip() for color in content if color.strip()]
except FileNotFoundError:
    print(f"----\nError: The file '{file_name}' does not exist.")
    sys.exit(1)

# Check if the file is empty
if not color_list:
    print("----\nError: The file is empty.")
    sys.exit(1)

# Function for checking the selection
def check_selection(selection, color_list):
    selection = selection.strip()

    if selection.lower() == 'x':
        return 'exit'
    
    elif selection.isdigit():
        selection = int(selection)
        if 1 <= selection <= len(color_list):
            return color_list[selection - 1]
        else:
            return 'invalid'
    
    elif selection.lower() in [color.lower() for color in color_list]:
         for color in color_list:
            if color.lower() == selection.lower():
                return color
    else:
        return 'invalid'

# Check if the user provided a selection in command line
if len(sys.argv) == 3:
    selection = sys.argv[2]
    result = check_selection(selection, color_list)

    if result == 'invalid':
        print("----\nInvalid selection. Please select an existing color or a valid number.")
        sys.exit(1)
    
    elif result == 'exit':
        print("Exiting the program.")
        sys.exit(0)
    
    else:
        print(f"----\nYou selected: {result}")
        sys.exit(0)

# If no selection is provided in command line, show menue and prompt for selection
print("----\nHere are the colors in the file:\n----")

for i, color in enumerate(color_list,1):
    print(f"{i}. {color}")

print("----\nType 'x' to exit the program.\n----")

while True:
    selection = input("What color do you want to select? ")
    result = check_selection(selection, color_list)

    if result == 'invalid':
        print("----\nInvalid selection. Please select an existing color or a valid number.")
    
    elif result == 'exit':
        print("Exiting the program.")
        break
    
    else:
        print(f"----\nYou selected: {result}")
        break



