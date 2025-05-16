numbers = [1203, 1256, 312456, 98]

for digit in range(10):
    count = 0
    for number in numbers:
        count += str(number).count(str(digit))
    print(digit, count)
