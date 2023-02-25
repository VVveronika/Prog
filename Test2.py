from tkinter import * 
from random import randint


def forB ():
    canvas.delete('all')
    randomNum = randint(1,3)
    if randomNum == 1:
        canvas.create_rectangle(15, 15, 145, 145)
    if randomNum == 2:
        canvas.create_oval(15, 15, 145, 145)
    if randomNum == 3:
        canvas.create_polygon(100, 100, 70, 250, 230, 250)

root = Tk()
root.geometry('500x500')
root.title('App')

canvas = Canvas(root, width=540, height=400)
canvas.pack()

button = Button(root, text = 'Click', width=15, height=8, bg = 'grey', command=forB)
button.pack(side = BOTTOM)

root.mainloop()
