numbers = [68, 43, 67, 87, 44, 25, 80, 38, 55, -10, 12, 51, 36, 97, 64, 52, 0, 87, -46, 70]

minNumber = numbers[0]
maxNumber = numbers[1]

if minNumber > maxNumber:
    minNumber, maxNumber = maxNumber, minNumber

for number in numbers[3:]:
    if number < minNumber:
        minNumber = number
    elif number > maxNumber:
        maxNumber = number

print('min', minNumber, 'max', maxNumber)

