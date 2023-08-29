a = list(map(int, input().split(' ')))
b = list(map(int, input().split(' ')))
c = list(map(int, input().split(' ')))
d = list(map(int, input().split(' ')))

massiv = [a, b, c, d]
m = []

for i in massiv:
    m.append([0] * ((i[2] - i[0]) * (i[3] - i[1])))

print(m)

