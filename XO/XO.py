from tkinter import * 
from functools import *
a = 1
def ForButton(j):
    global a
    if a % 2 == 1:
        root.children[f'b{j}'].config(text = 'O')
    else:
        root.children[f'b{j}'].config(text = 'X')
    a += 1
    if a == 10:
        root.children['b1'](state = DISABLED)


root = Tk()
root.title('XO')
root.geometry('520x510')
root.resizable('False', 'False')


x = 0
y = 0


for j in range(1,10):
    button = Button(root, name=f'b{j}', text='', width=10, height=4, border='2', font=('consolas', 20), command=partial(ForButton, j))
    button.place(x=x,y=y)
    x+=180
    if x > 530:
        x = 0
        y += 180

root.mainloop()