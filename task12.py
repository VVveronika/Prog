a = input().split(' ')
n = int(a[0])
m = int(a[1])
massiv = []
x = 0

for i in range(0, n):
    b = input().split(' ')
    t = int(b[0])
    d = int(b[1])
    c = int(b[2])
    massiv.append(abs((t) + (d) + (c)))

massiv.sort(reverse=True)

for j in range(0, m):
    x += massiv[j]

print(x)