from tkinter import *
from tkinter import messagebox

class Snake_element:
    def __init__(self, x, y, width_x, width_y = None):
        self.id = None
        self.x = x
        self.y = y
        self.width_x = width_x
        self.width_y = width_x if width_y == None else width_y

    def draw(self):
        if self.id == None:
            self.id = canvas.create_oval(self.coords(),
                            fill='black',
                            activefill='red')
        else:
            canvas.coords(self.id, self.coords())    
        
    def coords(self):
        coords = (self.x - self.width_x / 2,
                self.y - self.width_y / 2,
                self.x + self.width_x / 2,
                self.y + self.width_y / 2)
        return coords

    def move(self, d_x = 0, d_y = 0):
        self.x = self.x + d_x
        self.y = self.y + d_y
        self.draw()

class Snake:
    def __init__(self, lenght, start_x, start_y):
        self.width_x = 20
        self.width_y = 20
        self.d_x = self.width_x
        self.d_y = 0
        x = start_x
        y = start_y
        self.lenght = lenght
        self.body = []
        for i in range(lenght):
            element = Snake_element(x, y, self.width_x, self.width_y)
            self.body.append(element)
            x -= element.width_x

    def move(self):
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i - 1].x
            self.body[i].y = self.body[i - 1].y
            self.body[i].draw()    
        self.body[0].x = self.body[0].x + self.d_x
        self.body[0].y = self.body[0].y + self.d_y
        self.body[0].draw()
        
def key_pressed(event):
    key = event.keysym
    if key == 'Up':
        b.d_x = 0
        b.d_y = -b.width_y
    if key == 'Down':
        b.d_x = 0
        b.d_y = b.width_y
    if key == 'Left':
        b.d_x = -b.width_x
        b.d_y = 0
    if key == 'Right':
        b.d_x = b.width_x
        b.d_y = 0

def for_closing():
    if messagebox.askokcancel(title = 'Выход', message='Вы хотите закрыть приложение?'):
        root.destroy()

def main():
    b.move()
    root.after(1000, main)

root = Tk()

root.title('Питон')
root.geometry('400x400')
root.resizable(False, False)
#root.iconbitmap(default='C:\Prog\SnakeApp\Snake1.jpg')

canvas = Canvas(root, width=390, height=390,  cursor = 'heart')
canvas.pack()

root.bind('<Key>', key_pressed)

root.protocol('WM_DELETE_WINDOW', for_closing)

canvas.focus()

b = Snake(10, 200, 200)

main()

root.mainloop()
