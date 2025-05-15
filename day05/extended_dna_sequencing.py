seq_input = input("Enter a DNA sequence: ")

seq_input = seq_input.upper().split('X') 

seq_input = filter(lambda x: x != '', seq_input)

print(sorted(list(seq_input), key = len, reverse = True))