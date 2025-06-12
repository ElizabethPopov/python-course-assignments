import sys

def return_sequence_from_input(seq_input):
    '''Returns a sequence from the input string, filtering out non-DNA characters.'''
    seq = ''
    seq_lst = []
    for letter in seq_input.upper():
        if letter in 'ATCG':
            seq += letter
        else:
            if seq:
                seq_lst.append(seq)
                seq = ''
    if seq:
        seq_lst.append(seq)
    
    return seq_lst

def sort_sequences(seq_lst):
    '''Sorts a list of sequences by length in descending order.'''
    return sorted(seq_lst, key=len, reverse=True)

def main():
    '''Main function to execute the sequence processing.'''
    if len(sys.argv) != 2:
        print("Usage: python your_script.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]

    try:
        with open(filename, 'r') as f:
            seq_input = f.read()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)

    seq_lst = return_sequence_from_input(seq_input)
    sorted_seq_lst = sort_sequences(seq_lst)
    print(sorted_seq_lst)

if __name__ == "__main__":
    main()
