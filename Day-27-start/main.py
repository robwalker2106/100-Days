import tkinter

window = tkinter.Tk()
window.minsize(width=250, height=200)
window.title("Miles to KM Converter")

miles_input = tkinter.Entry(width=10)
miles_input.grid(column=1, row=2)

miles = tkinter.Label(text="Miles")
miles.grid(column=2, row=2)

is_equal_to = tkinter.Label(text="is equal to")
is_equal_to.grid(column=0, row=3)

miles_to_km = tkinter.Label(text="Press Calculate")
miles_to_km.grid(column=1, row=3)

Km = tkinter.Label(text="Km")
Km.grid(column=2, row=3)


def calculate():
    inputted_miles = int(miles_input.get())
    km = (inputted_miles * 8) / 5
    miles_to_km.config(text=km)


calculate = tkinter.Button(text="Calculate", command=calculate)
calculate.grid(column=1, row=4)

window.mainloop()