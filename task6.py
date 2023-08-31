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

floor = set()

for rect in rectangles:

    for y in range(rect.y1, rect.y2):
        
        for x in range(rect.x1, rect.x2):
            key = x * 2001 + y
            floor.add(key)

print(len(floor))