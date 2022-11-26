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

for i in range(tryes):
    
    while True:
        answer = input(f'Осталось {tryes - i} попыток. Введите слово из {wordCount} букв: ')
        if wordCount == len(answer):
            break
    
    answer = answer.upper()
    res = wordCompare(word, answer)
    print(answer, res, sep = '\n')

    if word == answer:
        print('Вы угадали!')
        break
else:
    print(f'Вы не угадали за {tryes} попыток:(')
