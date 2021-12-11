s = ['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd']

print('before', s)

start = 0
end = len(s) - 1
while start < end:
    s[start], s[end] = s[end], s[start]
    start += 1
    end -= 1

assert ''.join(s) == 'dlroW olleH'

print('after', s)
