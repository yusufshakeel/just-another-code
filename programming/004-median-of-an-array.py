def find_median(array):
    size = len(array)
    middle = int(size / 2)
    if size % 2 == 0:
        return (array[middle - 1] + array[middle]) / 2.0
    else:
        return array[middle]


def partition(array, start, end):
    pivot = array[start]
    low = start + 1
    high = end

    while True:
        while low <= high and array[high] >= pivot:
            high = high - 1

        while low <= high and array[low] <= pivot:
            low = low + 1

        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break

    array[start], array[high] = array[high], array[start]
    return high


def quick_sort(array, start, end):
    if start >= end:
        return

    pivot = partition(array, start, end)
    quick_sort(array, start, pivot - 1)
    quick_sort(array, pivot + 1, end)


input1 = [1, 3, 2, 0, 10, 7, 4, 8, 9, 6, 5]
input2 = [47, 32, 51, 19, 99, 38]

quick_sort(input1, 0, len(input1) - 1)
quick_sort(input2, 0, len(input2) - 1)

median1 = find_median(input1)
median2 = find_median(input2)

assert median1 == 5
assert median2 == 42.5

print('sorted', input1, 'median', median1)
print('sorted', input2, 'median', median2)
