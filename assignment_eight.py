import tkinter

root = tkinter.Tk()
root.title("Calculator")

# title = tkinter.Label(root, text="Calculator")
# title.grid(row=1, column=1)
real_answer = tkinter.StringVar()


def one_():
    number = real_answer.get()
    new_number = number + "1"
    real_answer.set(new_number)


def two_():
    number = real_answer.get()
    new_number = number + "2"
    real_answer.set(new_number)


def three_():
    number = real_answer.get()
    new_number = number + "3"
    real_answer.set(new_number)


def four_():
    number = real_answer.get()
    new_number = number + "4"
    real_answer.set(new_number)


def five_():
    number = real_answer.get()
    new_number = number + "5"
    real_answer.set(new_number)


def six_():
    number = real_answer.get()
    new_number = number + "6"
    real_answer.set(new_number)


def seven_():
    number = real_answer.get()
    new_numebr = number + "7"
    real_answer.set(new_numebr)


def eight_():
    number = real_answer.get()
    new_number = number + "8"
    real_answer.set(new_number)


def nine_():
    number = real_answer.get()
    new_number = number + "9"
    real_answer.set(new_number)


def zero_():
    number = real_answer.get()
    new_number = number + "0"
    real_answer.set(new_number)


def clear_():
    real_answer.set("")


def plus_():
    number = real_answer.get()
    new_number = number + "+"
    real_answer.set(new_number)


def minus_():
    number = real_answer.get()
    new_number = number + "-"
    real_answer.set(new_number)


def squareroot():
    number = float(real_answer.get())
    new_number = number**.5
    real_answer.set(str(new_number))


def multiply_():
    number = real_answer.get()
    new_number = number + "*"
    real_answer.set(new_number)


def enter():
    equation = real_answer.get()
    new = eval(equation)
    real_answer.set(new)


answer = tkinter.Entry(root, textvariable=real_answer)
answer.grid(row=2, column=0)

Enter = tkinter.Button(root, text="Enter", command=enter)
Enter.grid(row=7, column=5)

clear = tkinter.Button(root, text="Clear", command=clear_)
clear.grid(row=7, column=6)

plus = tkinter.Button(root, text="+", command=plus_)
plus.grid(row=6, column=6)

minus = tkinter.Button(root, text="-", command=minus_)
minus.grid(row=5, column=6)

multiply = tkinter.Button(root, text="*", command=multiply_)
multiply.grid(row=4, column=6)

squared = tkinter.Button(root, text="xˆ2")
squared.grid(row=3, column=6)

square_root = tkinter.Button(root, text="√", command=squareroot)
square_root.grid(row=2, column=6)

one = tkinter.Button(root, text="1", command=one_)
one.grid(row=3, column=1, sticky="W")

two = tkinter.Button(root, text="2", command=two_)
two.grid(row=3, column=2)

three = tkinter.Button(root, text="3", command=three_)
three.grid(row=3, column=3)

four = tkinter.Button(root, text="4", command=four_)
four.grid(row=4, column=1)

five = tkinter.Button(root, text="5", command=five_)
five.grid(row=4, column=2)

six = tkinter.Button(root, text="6", command=six_)
six.grid(row=4, column=3)

seven = tkinter.Button(root, text="7", command=seven_)
seven.grid(row=5, column=1)

eight = tkinter.Button(root, text="8", command=eight_)
eight.grid(row=5, column=2)

nine = tkinter.Button(root, text="9", command=nine_)
nine.grid(row=5, column=3)

zero = tkinter.Button(root, text="0", command=zero_)
zero.grid(row=6, column=2)

root.mainloop()
