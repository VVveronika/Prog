d = input().split(' ')
a = abs(int(d[0]))
b = abs(int(d[1]))
x = 0

while a != b:
    if b > a:
        b = b - a
        x = x + 1
    else:
        a = a - b
        x = x + 1

print(x)
