import sys
import codecs

if len(sys.argv) != 2:  
    print("You should provide a txt file.")
    sys.exit(1)

input_file = sys.argv[1]

with open(input_file, 'r') as fl:
    file_content = fl.read()

rot13 = codecs.encode(file_content, "rot13")

with open(input_file, 'w') as file:
    file.write(rot13)

print(f"File {input_file} has been encoded with ROT13.")
print("The original content was:")
print(file_content)



