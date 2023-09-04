n, m = map(int, input().split(' '))

summs = []
cakes = []
coefficients = [[1, 1, 1], [1, 1, -1], [1, -1, 1], [1, -1, -1],\
            [-1, 1, 1], [-1, 1, -1], [-1, -1, -1], [-1, -1, 1]]    

for i in range(n):
    cakes.append(list(map(int, input().split(' '))))
    
for coefficient in coefficients:

    variant = []
    for cake in cakes:
        variant.append(cake[0] * coefficient[0] + cake[1] * coefficient[1] + cake[2] * coefficient[2])
    
    variant.sort(reverse=True)
    summ = sum(variant[:m])
    summs.append(summ)

print(max(summs))
