from tkinter import *
from functools import *
primer = ''
def count (nameB):
    global primer
    if nameB == '=':
        label.config(text = str(eval(primer)))
    elif nameB == 'C':
        primer = ''
        label.config(text = primer)
    elif nameB == 'DEL':
        primer = primer[:-1]
        label.config(text = primer)
    elif nameB == 'X^2':
        nameB = '**2'
        primer += nameB
        label.config(text = primer)
    else:
        primer += str(nameB)
        label.config(text = primer)

root = Tk()
root.title('Калькулятор')
root.geometry('450x550')
root.resizable(False, False)

label = Label(root, text='0', font=('consolas', 20))
label.pack(expand=True, anchor=NW)

nameButton = ['C', 'DEL', '*', '=', '1', '2', '3', '/', '4', '5', '6', '+', '7', '8', '9', '-', '(', '0', ')', 'X^2']
x = 10
y = 140

for i in nameButton:
    button = Button(root, text = i, font=('consolas', 20), border='0', command = partial(count, i)).place(x = x, y = y)
    x += 117
    if x > 400:
        x = 10
        y += 81

root.mainloop()
