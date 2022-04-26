from tkinter import *

window = Tk()
window.geometry("500x500")
window.title("Calculator")
window.configure(bg="grey")


def hello():
    print("button clicked")


def clear():
    global function






button1 = Button(window, text="ok", command=hello)
button2 = Button(window, text="ok", command=hello)

button1.grid(row=0, column=0)
button2.grid(row=1, column=1)

window.mainloop()
