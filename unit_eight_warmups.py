import tkinter

root = tkinter.Tk()
root.title("Temperature Converter")

f_value = tkinter.StringVar()

c_value = tkinter.StringVar()

celsius = tkinter.Label(root, text="degrees C:")
celsius.grid(row=2, column=1)

fahrenheit = tkinter.Label(root, text="degrees F:")
fahrenheit.grid(row=1, column=1)

fahrenheit_two = tkinter.Entry(root, textvariable=f_value)
fahrenheit_two.grid(row=1, column=2)

root.mainloop()
