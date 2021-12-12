numbers = [1, 2, 4, -3]
n = len(numbers)
max_sum = -1e18
current_sum = 0

for i in range(n):
    current_sum += numbers[i]
    if current_sum > max_sum:
        max_sum = current_sum
    if current_sum < 0:
        current_sum = 0

print(max_sum)
