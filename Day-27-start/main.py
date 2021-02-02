import tkinter

window = tkinter.Tk()
window.title("My First TK program")
window.minsize(width=500, height=300)


my_label = tkinter.Label(text='First label')
my_label.pack()

window.mainloop()
