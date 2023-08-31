class Rectangle():

    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2


rectangles = []

for i in range(4):
    c = map(int, input().split(' '))
    rect = Rectangle(*c)
    rectangles.append(rect)

min_x = min(min(rect.x1, rect.x2) for rect in rectangles)
min_y = min(min(rect.y1, rect.y2) for rect in rectangles)

for rect in rectangles:
    rect.x1 -= min_x
    rect.y1 -= min_y
    rect.x2 -= min_x
    rect.y2 -= min_y

max_x = list(max(rect.x1, rect.x2) for rect in rectangles)
max_y = list(max(rect.y1, rect.y2) for rect in rectangles)

floor = list(list(0 for x in range(max(max_x))) for j in range(max(max_y)))

space = 0

for rect in rectangles:

    for y in range(rect.y1, rect.y2):
        
        for x in range(rect.x1, rect.x2):
            if floor[y][x] == 0:
                space += 1            
                floor[y][x] = 1

print(space)