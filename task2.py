a, b = int(input()), int(input())
x = 0
while a != b:
    if b > a:
        b = b - a
        x = x + 1
    else:
        a = a - b
        x = x + 1
print(x)
