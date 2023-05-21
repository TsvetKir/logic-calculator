from tkinter import *
from tkinter import ttk
from itertools import product

def input(symbol):
    entry.insert(END, symbol)

def clear():
    entry.delete(0,END)

def clear_back():
    entry.delete(entry.index(END) - 1)

def sort(table, col, reverse):
    # получаем все значения столбцов в виде отдельного списка
    l = [(table.set(k, col), k) for k in table.get_children("")]
    # сортируем список
    l.sort(reverse=reverse)
    # переупорядочиваем значения в отсортированном порядке
    for index,  (_, k) in enumerate(l):
        table.move(k, "", index)
    # в следующий раз выполняем сортировку в обратном порядке
    table.heading(col, command=lambda: sort(table, col, not reverse))

def search(string, variables):
    s = list(string)
    for item in s:
        if item == "x" or item == "y" or item == "z" or item == "w" or item == "k":
            variables.add(item)
    variables = sorted(list(variables))
    if "w" or "k" in variables:
        if "w" and "k" in variables:
            for i in [1,0]:
                item = variables[i]
                variables.remove(item)
                variables.append(item)
        else:
            item = variables[0]
            variables.remove(item)
            variables.append(item)
    return variables

def calculate():
    string = entry.get()
    string = string.replace("¬", "not").replace("∧","and").replace("∨","or").replace("≡","==").replace("→", "<=")
    variables = set([])
    variables = search(string, variables)
    values = list(product([0, 1], repeat=len(variables)))
    list_table_rows =[]
    for cascade in values:
        string_new = string
        table_row =[]
        for item in range(len(variables)):
            string_new = string_new.replace(str(variables[item]), str(cascade[item]))
            table_row.append(cascade[item])
        table_row.append(bool(eval(string_new)))
        list_table_rows.append(table_row)
    output(variables, list_table_rows)

def output(variables, list_table_rows):
    columns = []
    for i in variables:
        columns.append(i)
    columns.append("F")
    table = ttk.Treeview(columns=columns, show="headings")
    table.pack()
    table.place(x=25, y=325, width=350)
    for i in columns:
        txt = str(i)
        table.column(str(i), anchor=CENTER, width=58)
        table.heading(str(i), text=txt, command=lambda: sort(table, len(columns)-1, False))
    for row in list_table_rows:
        table.insert("", END, values=row)

window = Tk()
window.title('Калькулятор')
window.geometry('400x600+500+100')
window.config(background="#8E8E8E")
entry = Entry(window, width=26, font=('', 20), justify=RIGHT)
entry.place(x=25, y=50)
entry.focus()

btn1 = Button(window, text='x', command=lambda: input('x '))
btn1.place(x=25, y=100, width=50, height=50)
btn2 = Button(window, text='y', command=lambda: input('y '))
btn2.place(x=100, y=100, width=50, height=50)
btn3 = Button(window, text='z', command=lambda: input('z '))
btn3.place(x=175, y=100, width=50, height=50)
btn4 = Button(window, text='w', command=lambda: input('w '))
btn4.place(x=250, y=100, width=50, height=50)
btn5 = Button(window, text='k', command=lambda: input('k '))
btn5.place(x=325, y=100, width=50, height=50)
btn6 = Button(window, text='¬', command=lambda: input('¬ '))
btn6.place(x=25, y=175, width=50, height=50)
btn7 = Button(window, text='∧', command=lambda: input('∧ '))
btn7.place(x=100, y=175, width=50, height=50)
btn8 = Button(window, text="∨", command=lambda: input('∨ '))
btn8.place(x=175, y=175, width=50, height=50)
btn9 = Button(window, text="→", command=lambda: input('→ '))
btn9.place(x=250, y=175, width=50, height=50)
btn10 = Button(window, text="≡", command=lambda: input('≡ '))
btn10.place(x=325, y=175, width=50, height=50)
btn11 = Button(window, text='(', command=lambda: input('('))
btn11.place(x=25, y=250, width=50, height=50)
btn12 = Button(window, text=")", command=lambda: input(') '))
btn12.place(x=100, y=250, width=50, height=50)
btn13 = Button(window, text="AС", command=clear)
btn13.place(x=175, y=250, width=50, height=50)
btn14 = Button(window, text="CE", command=clear_back)
btn14.place(x=250, y=250, width=50, height=50)
btn15 = Button(window, text="=", command=calculate)
btn15.place(x=325, y=250, width=50, height=50)

window.mainloop()
