from tkinter import *

window = Tk()
window.title("Calculator")
window.iconbitmap("D:\Python\Calculator\Calc.ico")

entry = Entry(window, width=30, borderwidth=5, fg="Black", font='14')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

a = 0
b = 0
op = ''


def button_click(number):
    global op
    if op == '=':
        entry.delete(0, END)
        op = ''
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(current) + str(number))


def clear():
    entry.delete(0, END)


def add():
    global a, op
    a = float(entry.get())
    entry.delete(0, END)
    op = '+'


def subtract():
    global a, op
    a = float(entry.get())
    entry.delete(0, END)
    op = '-'


def multiply():
    global a, op
    a = float(entry.get())
    entry.delete(0, END)
    op = '*'


def divide():
    global a, op
    a = float(entry.get())
    entry.delete(0, END)
    op = '/'


def equal():
    global a, b, op
    b = float(entry.get())
    entry.delete(0, END)
    if op == '+':
        entry.insert(0, a + b)
    elif op == '-':
        entry.insert(0, a - b)
    elif op == '*':
        entry.insert(0, a * b)
    elif op == '/':
        entry.insert(0, a / b)
    op = '='


clear = Button(window, text='C', padx=35, pady=20, font='Georgia 14', command=clear).grid(row=1, column=0)
subtract = Button(window, text='-', padx=35, pady=20, font='Georgia 14', command=subtract).grid(row=1, column=3)
multiply = Button(window, text='*', padx=35, pady=20, font='Georgia 14', command=multiply).grid(row=1, column=2)
divide = Button(window, text='/', padx=35, pady=20, font='Georgia 14', command=divide).grid(row=1, column=1)

button_1 = Button(window, text='1', padx=35, pady=20, font='Georgia 14', command=lambda: button_click(1)).grid(row=4,
                                                                                                               column=0)
button_2 = Button(window, text='2', padx=35, pady=20, font='Georgia 14', command=lambda: button_click(2)).grid(row=4,
                                                                                                               column=1)
button_3 = Button(window, text='3', padx=35, pady=20, font='Georgia 14', command=lambda: button_click(3)).grid(row=4,
                                                                                                               column=2)

button_4 = Button(window, text='4', padx=35, pady=20, font='Georgia 14', command=lambda: button_click(4)).grid(row=3,
                                                                                                               column=0)
button_5 = Button(window, text='5', padx=35, pady=20, font='Georgia 14', command=lambda: button_click(5)).grid(row=3,
                                                                                                               column=1)
button_6 = Button(window, text='6', padx=35, pady=20, font='Georgia 14', command=lambda: button_click(6)).grid(row=3,
                                                                                                               column=2)
equals = Button(window, text='=', padx=35, pady=60, font='Georgia 14', command=equal).grid(row=4, column=3, rowspan=2)

button_7 = Button(window, text='7', padx=35, pady=20, font='Georgia 14', command=lambda: button_click(7)).grid(row=2,
                                                                                                               column=0)
button_8 = Button(window, text='8', padx=35, pady=20, font='Georgia 14', command=lambda: button_click(8)).grid(row=2,
                                                                                                               column=1)
button_9 = Button(window, text='9', padx=35, pady=20, font='Georgia 14', command=lambda: button_click(9)).grid(row=2,
                                                                                                               column=2)
add = Button(window, text='+', padx=35, pady=60, font='Georgia 14', command=add).grid(row=2, column=3, rowspan=2)

button_0 = Button(window, text='0', padx=85, pady=20, font='Georgia 14', command=lambda: button_click(0)).grid(row=5,
                                                                                                               column=0,
                                                                                                               columnspan=2)
button_dot = Button(window, text='.', padx=35, pady=20, font='Georgia 14', command=lambda: button_click('.')).grid(
    row=5, column=2)

window.mainloop()
