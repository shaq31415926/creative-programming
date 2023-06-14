import tkinter as tk

# code to create the gui window
m = tk.Tk(className="My First Calculator")
# code to change the colour
m.configure(background='orange')
# code to change the size
m.geometry("410x280")

# code to create entry box
equation = tk.StringVar()
expression_field = tk.Entry(m, textvariable=equation, font="arial 16")
expression_field.grid(columnspan=4, ipadx=110)

# creating buttons
expression = ""

def press(value):
    global expression

    expression = expression + str(value)

    equation.set(expression)

button1 = tk.Button(m,
                    text=' 1 ',
                    command=lambda: press(1),
                    height=1,
                    width=7,
                    foreground="pink",
                    background="red",
                    )
button1.grid(row=2, column=0)

button2 = tk.Button(m,
                    text=' 2 ',
                    command=lambda: press(2),
                    height=1,
                    width=7
                    )
button2.grid(row=2, column=1)

button3 = tk.Button(m,
                    text=' 3 ',
                    command=lambda: press(3),
                    height=1,
                    width=7
                    )
button3.grid(row=2, column=2)

button4 = tk.Button(m,
                    text=' 4 ',
                    command=lambda: press(4),
                    height=1,
                    width=7)
button4.grid(row=3, column=0)

button5 = tk.Button(m,
                    text=' 5 ',
                    command=lambda: press(5),
                    height=1,
                    width=7)
button5.grid(row=3, column=1)

button6 = tk.Button(m,
                    text=' 6 ',
                    command=lambda: press(6),
                    height=1,
                    width=7)
button6.grid(row=3, column=2)

button7 = tk.Button(m,
                    text=' 7 ',
                    command=lambda: press(7),
                    height=1,
                    width=7)
button7.grid(row=4, column=0)

button8 = tk.Button(m,
                    text=' 8 ',
                    command=lambda: press(8),
                    height=1,
                    width=7)
button8.grid(row=4, column=1)

button9 = tk.Button(m,
                    text=' 9 ',
                    command=lambda: press(9),
                    height=1,
                    width=7)
button9.grid(row=4, column=2)

button0 = tk.Button(m,
                    text=' 0 ',
                    command=lambda: press(0),
                    height=1,
                    width=7)
button0.grid(row=5, column=0)

# let's create some operators

plus = tk.Button(m,
                 text=' + ',
                 command=lambda: press("+"),
                 height=1,
                 width=7)
plus.grid(row=2, column=3)

minus = tk.Button(m,
                  text=' - ',
                  command=lambda: press("-"),
                  height=1,
                  width=7)
minus.grid(row=3, column=3)

multiply = tk.Button(m,
                     text=' x ',
                     command=lambda: press("*"),
                     height=1,
                     width=7)
multiply.grid(row=4, column=3)

divide = tk.Button(m,
                   text=' ÷ ',
                   command=lambda: press("/"),
                   height=1,
                   width=7)
divide.grid(row=5, column=3)

# we can also create a decimal point
decimal = tk.Button(m,
                   text='.',
                   command=lambda: press('.'),
                   height=1,
                   width=7)
decimal.grid(row=6, column=0)

# we can also create brackets
bracket1 = tk.Button(m,
                   text=' ( ',
                   command=lambda: press('('),
                   height=1,
                   width=7)
bracket1.grid(row=5, column=1)

bracket2 = tk.Button(m,
                   text=' ) ',
                   command=lambda: press(')'),
                   height=1,
                   width=7)
bracket2.grid(row=5, column=2)

comma = tk.Button(m,
                   text=' , ',
                   command=lambda: press(','),
                   height=1,
                   width=7)
comma.grid(row=6, column=1)

def press_equal():
    global expression

    total = str(eval(expression))

    equation.set(total)


equal = tk.Button(m,
                   text=' = ',
                   command=press_equal,
                   height=1,
                   width=7)
equal.grid(row=6, column=2)

def clear():
    global expression
    expression = ""
    equation.set(0)

clear = tk.Button(m,
                   text=' C ',
                   command=clear,
                   height=1,
                   width=7)
clear.grid(row=6, column=3)



# code to run the window
m.mainloop()
