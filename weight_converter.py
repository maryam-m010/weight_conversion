from tkinter import *
root = Tk()
root.title("weight calculator")

def from_kg():
    gram = float(c.get()) * 1000
    pound = float(c.get()) * 2.20462
    ounce = float(c.get()) * 35.274

    table1.delete("1.0", END)
    table1.insert(END, gram)

    table2.delete("1.0", END)
    table2.insert(END, pound)

    table3.delete("1.0", END)
    table3.insert(END, ounce)

a = Label(root, text = "Enter the Weight in kg: ")
c = StringVar()
b = Entry(root, textvariable = c)

button = Button(root, text = "Convert", command = from_kg)
button.grid(row = 0, column = 2)

a.grid(row = 0, column = 0)
b.grid(row = 0, column = 1)

d = Label(root, text = "Grams")
e = Label(root, text = "Pounds")
f = Label(root, text = "Ounces")

d.grid(row = 1, column = 0)
e.grid(row = 1, column = 1)
f.grid(row = 1, column = 2)

table1 = Text(root, height = 1, width = 20)
table2 = Text(root, height = 1, width = 20)
table3 = Text(root, height = 1, width = 20)

table1.grid(row = 2, column = 0)
table2.grid(row = 2, column = 1)
table3.grid(row = 2, column = 2)

root.mainloop()
