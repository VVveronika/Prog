(x1_1, y1_1, x2_1, y2_1) = tuple(list(map(int, input().split(' '))))
(x1_2, y1_2, x2_2, y2_2) = tuple(list(map(int, input().split(' '))))
(x1_3, y1_3, x2_3, y2_3) = tuple(list(map(int, input().split(' '))))
(x1_4, y1_4, x2_4, y2_4) = tuple(list(map(int, input().split(' '))))

min_x = min(x1_1, x1_2, x1_3, x1_4)
max_x = max(x2_1, x2_2, x2_3, x2_4)
min_y = min(y1_1, y1_2, y1_3, y1_4)
max_y = max(y2_1, y2_2, y2_3, y2_4)

space = 0

for y in range(min_y, max_y + 1):

    for x in range(min_x, max_x + 1):

        if x1_1 <= x < x2_1 and y1_1 <= y < y2_1\
            or x1_2 <= x < x2_2 and y1_2 <= y < y2_2\
            or x1_3 <= x < x2_3 and y1_3 <= y < y2_3\
            or x1_4 <= x < x2_4 and y1_4 <= y < y2_4:
            space += 1

print(space)