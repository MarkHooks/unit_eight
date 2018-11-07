import tkinter

root = tkinter.Tk()
root.title("Temperature Converter")

celsius = tkinter.Label(root, text="degrees C:")
celsius.grid(row=10, column=1)

fahrenheit = tkinter.Label(root, text="degrees F:")
fahrenheit.grid(row=1, column=1)

fahrenheit_two = tkinter.Entry(root)
fahrenheit_two.grid(row=1, column=2)

root.mainloop()
