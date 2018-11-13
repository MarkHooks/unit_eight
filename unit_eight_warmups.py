import tkinter

root = tkinter.Tk()
root.title("Temperature Converter")


def f_to_c():
    value = int(f_value.get())
    c = 5/9 * (value - 32)
    c_value.set(str(c))


f_value = tkinter.StringVar()

c_value = tkinter.StringVar()

f_value.set("0")

celsius = tkinter.Label(root, text="degrees C:")
celsius.grid(row=2, column=1)

fahrenheit = tkinter.Label(root, text="degrees F:")
fahrenheit.grid(row=1, column=1)

fahrenheit_two = tkinter.Entry(root, textvariable=f_value)
fahrenheit_two.grid(row=1, column=2)

celsius_two = tkinter.Label(root, textvariable=c_value)
celsius_two.grid(row=2, column=2, sticky="W")

convert = tkinter.Button(root, text="convert", command=f_to_c)
convert.grid(row=3, column=1, columnspan=2)

root.mainloop()
