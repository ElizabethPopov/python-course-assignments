import sys

if len(sys.argv) != 2:  
    print("You should provide a single sequence composed of letters.")
    sys.exit(1)

seq_input = sys.argv[1]

seq_input = seq_input.upper().split('X') 

seq_input = filter(lambda x: x != '', seq_input)

print(sorted(list(seq_input), key = len, reverse = True))