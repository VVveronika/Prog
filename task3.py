n = int(input())

sequence = list(map(float, input().split(' ')))
sequence.sort(reverse=True)

if sequence[n//2 - 1] > sequence[n//2]:
    print('Yes')
else:
    print('No')


