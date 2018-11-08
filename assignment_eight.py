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


answer = tkinter.Entry(root, textvariable=real_answer)
answer.grid(row=2, column=0)

Enter = tkinter.Button(root, text="Enter")
Enter.grid(row=7, column=5)

clear = tkinter.Button(root, text="Clear")
clear.grid(row=7, column=6)

plus = tkinter.Button(root, text="+")
plus.grid(row=6, column=6)

minus = tkinter.Button(root, text="-")
minus.grid(row=5, column=6)

multiply = tkinter.Button(root, text="*")
multiply.grid(row=4, column=6)

squared = tkinter.Button(root, text="xˆ2")
squared.grid(row=3, column=6)

square_root = tkinter.Button(root, text="√")
square_root.grid(row=2, column=6)

one = tkinter.Button(root, text="1", command=one_)
one.grid(row=3, column=1)

two = tkinter.Button(root, text="2")
two.grid(row=3, column=2)

three = tkinter.Button(root, text="3")
three.grid(row=3, column=3)

four = tkinter.Button(root, text="4")
four.grid(row=4, column=1)

five = tkinter.Button(root, text="5")
five.grid(row=4, column=2)

six = tkinter.Button(root, text="6")
six.grid(row=4, column=3)

seven = tkinter.Button(root, text="7")
seven.grid(row=5, column=1)

eight = tkinter.Button(root, text="8")
eight.grid(row=5, column=2)

nine = tkinter.Button(root, text="9")
nine.grid(row=5, column=3)

zero = tkinter.Button(root, text="0")
zero.grid(row=6, column=2)

root.mainloop()
