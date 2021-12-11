def min_max(array, start, end):
    # only 1 element in the array
    if start == end:
        return (array[start], array[end])

    # 2 elments in the array
    elif end - start == 1:
        min_number = min(array[start], array[end])
        max_number = max(array[start], array[end])
        return (min_number, max_number)

    # more than 2 elements in the array
    else:
        middle = int(start + end) / 2
        min_num1, max_num1 = min_max(array, start, middle)
        min_num2, max_num2 = min_max(array, middle + 1, end)
    
    return (min(min_num1, min_num2), max(max_num1, max_num2))

numbers = [1, 2, 4, 5, 6, 3]
start = 0
end = len(numbers) - 1
min_number, max_number = min_max(numbers, start, end)

assert min_number == 1
assert max_number == 6

print('min', min_number, 'max', max_number)

    
