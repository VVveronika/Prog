n = int(input())

sequence = list(map(float, input().split(' ')))
sequence.sort()

answer = 'Yes'
a = 0

for i in range(n // 2 + 1, n):

    if sequence[i] <= sequence[a] or sequence[i] <= sequence[a + 1]:
        answer = 'No'
        break

    a += 1

print(answer)

