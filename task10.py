n = int(input())

a = list(map(int, input().split(' ')))
b = list(map(int, input().split(' ')))

move = set()
j = n - 1 
i = n - 1
res = 0

while i >= 0 and j >= 0:

    if a[j] == b[i]:
        i -= 1
        j -= 1
    elif b[i] in move:
        move.remove(b[i])
        i -= 1
    else:
        move.add(a[j])
        res += 1
        j -= 1
              
print(res)

