field = []
for i in range(3):
    z = []
    for j in range(3):
        z.append('   ')
    field.append(z)

for i in range(9):
    symbol = ' x ' if i % 2 == 0 else ' o '
    num = int(input(f'Введите номер клетки для {symbol}: '))
    num -= 1
    x = num % 3 
    y = num // 3
    field[y][x] = symbol
    print('-' * 13, x, y)
    for j in field:
        print('!', *j, '!', sep=('!'))

    

