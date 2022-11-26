def wordCompare(word: str, answer: str):
    position = 0
    result = ''
    for letter in answer:
        result += letterCompare(word, answer, letter, position)
        position += 1
    return result

def letterCompare(word: str, answer: str, letter: str, position: int):

    count = word.count(letter)

    if count == 0:
        return '-'

    letterIsSame = letter == word[position]
    lc = letterCheck(word, answer, letter)

    if count == 1:
        if letterIsSame:
            return '!'
        if lc:
            return '-'
        else:
            return '+'
    else:
        if not letterIsSame:
            if lc:
                return '-'
            else:
                return '+'
        else:
            if lc:
                return '!'
            return '*'

def letterCheck(word: str, answer: str, letter: str):
    for index in range(len(word)):
        if word[index] == letter and letter != answer[index]:
            return False
    return True
    
word = input('Загадайте слово: ')
wordCount = len(word)
tryes = 10 
word = word.upper()

print('\n' * 20)
print(f'Вам нужно угадать слово из {wordCount} букв.')
print('\'!\' - буква на своем месте.')
print('\'+\' - буква есть в слове, но в другом месте.')
print('\'-\' - буквы нет в слове.')
print('\'*\' - буква стоит на месте, но в слове есть еще такая же буква.')
print('Удачи!')

for i in range(tryes):
    
    cnt = ''
    while True:
        answer = input(f'Осталось {tryes - i} попыток. Введите слово{cnt}: ')
        if wordCount != len(answer):
            cnt = f' из {wordCount} букв'
        else:
            break
    
    answer = answer.upper()
    res = wordCompare(word, answer)
    print(answer, res, sep = '\n')

    if word == answer:
        print('Вы угадали!')
        break
    else:
        print('Вы не угадали, попробуйте еще раз.')
else:
    print(f'Вы не угадали за {tryes} попыток:(')
    print(f'Было загадано слово: {word}.')
