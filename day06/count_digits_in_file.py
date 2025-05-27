import re

numbers_file = 'numbers.txt'

with open(numbers_file, 'r') as file:
    content = file.read()

numbers = re.findall(r'\d', content)

with open('report.txt', 'w') as digit_count:
    for i, digit in enumerate(range(10)):
        count = numbers.count(str(digit))
        if i < 9:
            digit_count.write(f'{digit} {count}\n')
        else:
            digit_count.write(f'{digit} {count}')