from tkinter import *
from tkinter import messagebox

def for_closing():
    if messagebox.askokcancel(title = 'Выход', message='Вы хотите закрыть приложение?'):
        root.destroy()

root = Tk()

root.title('Точки')
root.geometry('400x400')
root.resizable(False, False)

canvas = Canvas(root, width=390, height=390)
canvas.pack()

circle = canvas.create_oval(190, 190, 210, 210, fill='black', activefill='red')

#button = tk.Button(window, text="Закрыть", command=window.destroy)
root.protocol('WM_DELETE_WINDOW', for_closing)
root.mainloop()