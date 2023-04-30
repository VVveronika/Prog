from tkinter import *
from tkinter import messagebox

class Snake_element:
    def __init__(self, x, y, half_width_x, half_width_y = None):
        self.x = x
        self.y = y
        self.half_width_x = half_width_x
        self.half_width_y = half_width_x if half_width_y == None else half_width_y
        #self.draw()

    def draw(self):
        self.id = canvas.create_oval(self.coords(),
                            fill='black',
                            activefill='red')
        
    def coords(self):
        coords = (self.x - self.half_width_x,
                self.y - self.half_width_y,
                self.x + self.half_width_x,
                self.y + self.half_width_y)
        return coords

    def move(self, d_x = 0, d_y = 0):
        self.x = self.x + d_x
        self.y = self.y + d_y
        canvas.coords(self.id, self.coords())    

class Snake:
    def __init__(self, lenght, start_x, start_y):
        x = start_x
        y = start_y
        self.lenght = lenght
        self.body = []
        for i in range(lenght):
            element = Snake_element(x, y, 10)
            self.body.append(element)
            x -= 2 * element.half_width_x

    def draw(self):
         for i in self.body:
            i.draw()

    def move(self, d_x = 0, d_y = 0):
        for i in self.body:
            i.move(d_x, d_y)

def move_right(event):
    b.move(20)

def for_closing():
    if messagebox.askokcancel(title = 'Выход', message='Вы хотите закрыть приложение?'):
        root.destroy()

def size(id):
    (leftX, topY, rightX, bottomY) = canvas.coords(id)
    size_x = (rightX - leftX) / 2
    size_y = (bottomY - topY) / 2
    return size_x, size_y 

def mouse_coords():
    x = canvas.winfo_pointerx() - canvas.winfo_rootx()
    y = canvas.winfo_pointery() - canvas.winfo_rooty()
    return x, y

def move(event):
    id = canvas.find_withtag('current')
    if id != ():
        x, y = mouse_coords()
        size_x, size_y = size(id)
        canvas.coords(id, x-size_x, y-size_y, x+size_x, y+size_y)

root = Tk()

root.title('Точки')
root.geometry('400x400')
root.resizable(False, False)
root.iconbitmap(default='C:\Prog\SnakeApp\Snake1.jpg')

canvas = Canvas(root, width=390, height=390,  cursor = 'heart')
canvas.pack()

canvas.bind('<B1-Motion>', move)

canvas.bind('<Button-1>', move_right)

root.protocol('WM_DELETE_WINDOW', for_closing)

canvas.focus()

b = Snake(10, 200, 200)
b.draw()


root.mainloop()
