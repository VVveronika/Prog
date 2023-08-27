n = int(input())
words = []

for i in range(n):
    int(input())
    words.append(input())
    
for word in words:
    test_completed = False
    word_len = len(word)

    for j in range(1, word_len):

        for i in range(0, j):
            i_2 = j + i

            if i_2 == word_len or word[i] > word[i_2]:
                break
            elif (word[i] == word[i_2] and i == j - 1 and word_len > j * 2) or (word[i] < word[i_2]):
                    print('Yes')
                    test_completed = True
                    break

        if test_completed: 
            break
        
    else:
        print('No')

        