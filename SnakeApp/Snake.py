from tkinter import *
from tkinter import messagebox

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
        canvas.coords(id, x-size_x, y-size_y, x+size_x, y+size_x)

root = Tk()

root.title('Точки')
root.geometry('400x400')
root.resizable(False, False)
#root.iconbitmap(default='C:\Users\Veronika\OneDrive\Изображения\ForPlay\Snake.jpg')

canvas = Canvas(root, width=390, height=390)
canvas.pack()

canvas.create_oval(190, 190, 210, 210, fill='black', activefill='red')
canvas.create_rectangle(90, 90, 110, 110, fill='black', activefill='red')

canvas.bind('<B1-Motion>', move)

root.protocol('WM_DELETE_WINDOW', for_closing)
root.mainloop()