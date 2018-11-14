# mark hooks 11/13/18

# this program is to create a calculator using tkinter


import tkinter

root = tkinter.Tk()
root.title("Calculator")
root.config(bg="tomato2")
real_answer = tkinter.StringVar()


def one_():
    """
    this is to get the number 1
    :return:none
    """
    number = real_answer.get()
    new_number = number + "1"
    real_answer.set(new_number)


def two_():
    """
    this is to get the number 2
    :return:none
    """
    number = real_answer.get()
    new_number = number + "2"
    real_answer.set(new_number)


def three_():
    """
    this is to get the number 3
    :return:none
    """
    number = real_answer.get()
    new_number = number + "3"
    real_answer.set(new_number)


def four_():
    """
    this is to get the number 4
    :return:none
    """
    number = real_answer.get()
    new_number = number + "4"
    real_answer.set(new_number)


def five_():
    """
    this is to get the number 5
    :return:none
    """
    number = real_answer.get()
    new_number = number + "5"
    real_answer.set(new_number)


def six_():
    """
    this is to get the number 1
    :return:none
    """
    number = real_answer.get()
    new_number = number + "6"
    real_answer.set(new_number)


def seven_():
    """
    this is to get the number 7
    :return:none
    """
    number = real_answer.get()
    new_number = number + "7"
    real_answer.set(new_number)


def eight_():
    """
    this is to get the number 8
    :return:none
    """
    number = real_answer.get()
    new_number = number + "8"
    real_answer.set(new_number)


def nine_():
    """
    this is to get the number 9
    :return:none
    """
    number = real_answer.get()
    new_number = number + "9"
    real_answer.set(new_number)


def zero_():
    """
    this is to get the number 0
    :return:none
    """
    number = real_answer.get()
    new_number = number + "0"
    real_answer.set(new_number)


def clear_():
    """
    this is to clear the answer
    :return:none
    """
    real_answer.set("")


def plus_():
    """
    this is to get the + function
    :return:none
    """
    number = real_answer.get()
    new_number = number + "+"
    real_answer.set(new_number)


def minus_():
    """
    this is to get the - function
    :return:none
    """
    number = real_answer.get()
    new_number = number + "-"
    real_answer.set(new_number)


def divide_():
    """
    this is to get the / function
    :return:none
    """
    number = real_answer.get()
    new_number = number + "/"
    real_answer.set(new_number)


def squareroot():
    """
    this is to get the √ function
    :return:none
    """
    number = float(real_answer.get())
    new_number = number ** .5
    real_answer.set(str(new_number))


def multiply_():
    """
    this is to get the * function
    :return:none
    """
    number = real_answer.get()
    new_number = number + "*"
    real_answer.set(new_number)


def square():
    """
    this is to get the Xˆ2 function
    :return:none
    """
    number = float(real_answer.get())
    new_number = number ** 2
    real_answer.set(str(new_number))


def enter():
    """
    this is to get the calculator to work
    :return: none
    """
    equation = real_answer.get()
    new = eval(equation)
    real_answer.set(new)


# everything below is to create the calculator

answer = tkinter.Entry(root, textvariable=real_answer, bg="tomato2")
answer.grid(row=2, column=0, columnspan=4)

Enter = tkinter.Button(root, text="Enter", command=enter, fg="tomato", activeforeground="green")
Enter.grid(row=7, column=0, columnspan=2, sticky="W,E", ipadx=6, ipady=2)

clear = tkinter.Button(root, text="Clear", command=clear_, fg="tomato", activeforeground="green")
clear.grid(row=7, column=1, columnspan=2, ipadx=6, ipady=2, sticky="E")

plus = tkinter.Button(root, text="+", command=plus_, fg="tomato", activeforeground="green")
plus.grid(row=6, column=3, sticky="N,E,S,W", ipady=2)

divide = tkinter.Button(root, text="/", command=divide_, fg="tomato", activeforeground="green")
divide.grid(row=6, column=2, sticky="N,E,S,W", ipady=2)

minus = tkinter.Button(root, text="-", command=minus_, fg="tomato", activeforeground="green")
minus.grid(row=5, column=3, sticky="N,E,S,W", ipady=2)

multiply = tkinter.Button(root, text="*", command=multiply_, fg="tomato", activeforeground="green")
multiply.grid(row=4, column=3, sticky="N,E,S,W", ipady=2)

squared = tkinter.Button(root, text="xˆ2", command=square, fg="tomato", activeforeground="green")
squared.grid(row=3, column=3, sticky="N,E,S,W", ipady=2)

square_root = tkinter.Button(root, text="√", command=squareroot, fg="tomato", activeforeground="green")
square_root.grid(row=7, column=3, sticky="N,E,S,W")

one = tkinter.Button(root, text="1", command=one_, fg="tomato", activeforeground="green")
one.grid(row=3, column=0, sticky="N,E,S,W", ipady=2)

two = tkinter.Button(root, text="2", command=two_, fg="tomato", activeforeground="green")
two.grid(row=3, column=1, sticky="N,E,S,W", ipady=2)

three = tkinter.Button(root, text="3", command=three_, fg="tomato", activeforeground="green")
three.grid(row=3, column=2, sticky="N,E,S,W", ipady=2)

four = tkinter.Button(root, text="4", command=four_, fg="tomato", activeforeground="green")
four.grid(row=4, column=0, sticky="N,E,S,W", ipady=2)

five = tkinter.Button(root, text="5", command=five_, fg="tomato", activeforeground="green")
five.grid(row=4, column=1, sticky="N,E,S,W", ipady=2)

six = tkinter.Button(root, text="6", command=six_, fg="tomato", activeforeground="green")
six.grid(row=4, column=2, sticky="N,E,S,W", ipady=2)

seven = tkinter.Button(root, text="7", command=seven_, fg="tomato", activeforeground="green")
seven.grid(row=5, column=0, sticky="N,E,S,W", ipady=2)

eight = tkinter.Button(root, text="8", command=eight_, fg="tomato", activeforeground="green")
eight.grid(row=5, column=1, sticky="N,E,S,W", ipady=2)

nine = tkinter.Button(root, text="9", command=nine_, fg="tomato", activeforeground="green")
nine.grid(row=5, column=2, sticky="N,E,S,W", ipady=2)

zero = tkinter.Button(root, text="0", command=zero_, fg="tomato", activeforeground="green")
zero.grid(row=6, column=0, ipadx=18, columnspan=2, sticky="N,E,S,W", ipady=2)

root.mainloop()
