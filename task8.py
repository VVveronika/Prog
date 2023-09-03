t = int(input())

numbers = []

for i in range(t):
    numbers.append(int(input()))

for number in numbers:
    b_number = bin(number)
    ones = b_number.count('1')

    if number < 7:
        print(-1)
        continue

    elif ones > 3:
        b_number = b_number[::-1].replace('1', '0', ones - 3)[::-1]

    elif ones == 1:
        b_number = b_number.replace('1000', '111')

    elif ones == 2:
        if b_number[-2:] == '01' or b_number[-2:] == '10':
            b_number = '0b111' + ('0' * (len(b_number) - 6))
        else:
            b_number = b_number[::-1].replace('001', '110', 1)[::-1]
            
    print(int(b_number, 2))
