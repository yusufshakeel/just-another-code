def sum_of_subarray(array):
    n = len(array)
    max_sum = -1e18

    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += array[j]
            if current_sum > max_sum:
                max_sum = current_sum

    return max_sum


numbers = [1, 2, 4, -3]
print(sum_of_subarray(numbers))
