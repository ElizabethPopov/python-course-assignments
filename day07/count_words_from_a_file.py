import sys
from collections import Counter

file = sys.argv[1]
output_file = 'words_and_spaces_counted.txt'

with open(file, 'r') as f:
    content = f.read().lower()
    words = content.split()
    
counts = Counter(words)
items = counts.most_common()  # sorts by frequency in descending order

with open(output_file, 'w') as f:
    for i, (key, value) in enumerate(items):
        line = "{:<15} {}".format(key, value)
        if i < len(items) - 1:
            line += '\n'
        f.write(line)
