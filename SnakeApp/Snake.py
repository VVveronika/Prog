from tkinter import *
from tkinter import messagebox

def for_closing():
    if messagebox.askokcancel(title = 'Выход', message='Вы хотите закрыть приложение?'):
        root.destroy()

list_for_snake = []
start_num = 30
for i in range(10):
    list_for_snake.append(start_num)
    start_num += 10

def creating_circles():
    for i in list_for_snake:
        canvas.create_oval(i, i, i + 20, i + 20, fill='aquamarine', activefill='red')

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
        canvas.coords(id, x-size_x, y-size_y, x+size_x, y+size_x)

root = Tk()

root.title('Точки')
root.geometry('400x400')
root.resizable(False, False)
root.iconbitmap(default='C:\Prog\SnakeApp\Snake1.jpg')

canvas = Canvas(root, width=390, height=390,  cursor = 'heart')
canvas.pack()

#canvas.create_oval(190, 190, 210, 210, fill='black', activefill='red')
creating_circles()

canvas.bind('<B1-Motion>', move)

root.protocol('WM_DELETE_WINDOW', for_closing)
canvas.focus()
root.mainloop()