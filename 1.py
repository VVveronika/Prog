'''
Дан словарь со значениями констант {'pi': 3.14, 'e': 2.71, 'fi': 1.62}. Выведите на экран значения констант, которые превышают число 2.5
'''
d = {'pi': 3.14, 'e': 2.71, 'fi': 1.62}
for i in d:
    if d[i] > 2.5:
        print(f'{i}: {d[i]}')