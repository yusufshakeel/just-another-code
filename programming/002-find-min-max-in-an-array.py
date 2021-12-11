numbers = [68, 43, 67, 87, 44, 25, 80, 38, 55, -10, 12, 51, 36, 97, 64, 52, 0, 87, -46, 70]

min_number = numbers[0]
max_number = numbers[1]

if min_number > max_number:
    min_number, max_number = max_number, min_number

for number in numbers[3:]:
    if number < min_number:
        min_number = number
    elif number > max_number:
        max_number = number

assert min_number == -46
assert max_number == 97

print('min', min_number, 'max', max_number)

