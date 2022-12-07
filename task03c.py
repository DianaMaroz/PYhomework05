from tkinter import *


def click(num):
    pass

root = Tk()

label = Label(width=20, text= "Крестики vs Нолики", font=('Arial', 20, 'bold'))
bottons =[Button(width=5, height=3, font=('Arial', 26, 'bold'), bg="green", command=lambda x=i: click(x)) for i in range(9)]
label.grid(row=0, column=0, columnspan=3)
count_botton = 0
for row in range(1, 4):
    for col in range(3):
        bottons[count_botton].grid(row=row, column=col)
        count_botton += 1
root.mainloop()
