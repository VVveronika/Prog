n = int(input())
m = input().split(' ')

for i in (1, n, 2):
    if m[i] == m[i+1] or m[i] == m[i-1]:
        print('No')
    else:
        print('Yes')