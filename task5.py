size = list(map(int, input().split(' ')))
a = size[0]
b = size[1]

a += a % 2
b += b % 2

print(a * b // 4)