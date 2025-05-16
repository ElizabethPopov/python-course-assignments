seq_input = input("Enter a DNA sequence: ")

seq_input = seq_input.upper()

seq_lst = []
seq = ''

for letter in seq_input:
    if letter in 'ATCG':
        seq += letter
    else:
        if seq:
            seq_lst.append(seq)
            seq = ''

# capture the last sequence if it exists
if seq:
    seq_lst.append(seq)

print(sorted(list(seq_lst), key = len, reverse = True))