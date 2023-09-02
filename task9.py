x, y, a, b, c = map(int, input().split(' '))

p = list(map(int, input().split(' ')))
q = list(map(int, input().split(' ')))
r = list(map(int, input().split(' ')))

for i in p, q, r:
    i.sort(reverse=True)

sweet_apples = p[:x] + q[:y]
sweet_apples.sort()

for i in range(min(c, x + y)):
    if sweet_apples[i] < r[i]:
        sweet_apples[i] = r[i]
    else:
        break

print(sum(sweet_apples))

