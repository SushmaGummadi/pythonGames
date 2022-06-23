from tkinter import *

def click(event):
    text = event.widget.cget("text")
    print(text)
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            value = eval(screen.get())


        scvalue.set(value)
        screen.update()
         
    elif text == "C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()

root = Tk()

root.geometry("445x700")
root.title("Calculator By Sushma")
#root.wm_iconbitmap("1.ico")

scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar = scvalue, font="lucida 30 bold")
screen.pack(fill=X, ipadx=8, pady=10, padx=10)

f = Frame(root, bg="pink")
b = Button(f, text="9", padx=16, pady=2, font="lucida 25 bold")
b.pack(side = LEFT, padx = 15, pady = 2)
b.bind("<Button-1>", click)

b = Button(f, text="8", padx=16, pady=2, font="lucida 25 bold")
b.pack(side = LEFT, padx = 15, pady = 2)
b.bind("<Button-1>", click)

b = Button(f, text="7", padx=16, pady=8, font="lucida 25 bold")
b.pack(side = LEFT, padx = 15, pady = 6)
b.bind("<Button-1>", click)
f.pack()

f = Frame(root, bg="pink")
b = Button(f, text="6", padx=16, pady=8, font="lucida 25 bold")
b.pack(side = LEFT, padx = 15, pady = 6)
b.bind("<Button-1>", click)

b = Button(f, text="5", padx=16, pady=8, font="lucida 25 bold")
b.pack(side = LEFT, padx = 15, pady = 6)
b.bind("<Button-1>", click)

b = Button(f, text="4", padx=16, pady=8, font="lucida 25 bold")
b.pack(side = LEFT, padx = 15, pady = 6)
b.bind("<Button-1>", click)
f.pack()

f = Frame(root, bg="pink")
b = Button(f, text="3", padx=16, pady=8, font="lucida 25 bold")
b.pack(side = LEFT, padx = 15, pady = 6)
b.bind("<Button-1>", click)

b = Button(f, text="2", padx=16, pady=8, font="lucida 25 bold")
b.pack(side = LEFT, padx = 15, pady = 6)
b.bind("<Button-1>", click)

b = Button(f, text="1", padx=16, pady=8, font="lucida 25 bold")
b.pack(side = LEFT, padx = 15, pady = 6)
b.bind("<Button-1>", click)
f.pack()

f = Frame(root, bg="pink")
b = Button(f, text="0", padx=17, pady=8, font="lucida 25 bold")
b.pack(side = LEFT, padx = 15, pady = 6)
b.bind("<Button-1>", click)

b = Button(f, text="=", padx=17, pady=8, font="lucida 25 bold")
b.pack(side = LEFT, padx = 15, pady = 6)
b.bind("<Button-1>", click)

b = Button(f, text="-", padx=17, pady=8, font="lucida 25 bold")
b.pack(side = LEFT, padx = 15, pady = 6)
b.bind("<Button-1>", click)
f.pack()

f = Frame(root, bg="pink")
b = Button(f, text="+", padx=18, pady=8, font="lucida 25 bold")
b.pack(side = LEFT, padx = 15, pady = 6)
b.bind("<Button-1>", click)

b = Button(f, text="/", padx=18, pady=8, font="lucida 25 bold")
b.pack(side = LEFT, padx = 15, pady = 6)
b.bind("<Button-1>", click)

b = Button(f, text="*", padx=18, pady=8, font="lucida 25 bold")
b.pack(side = LEFT, padx = 15, pady = 6)
b.bind("<Button-1>", click)
f.pack()

f = Frame(root, bg="pink")
b = Button(f, text="%", padx=15, pady=8, font="lucida 25 bold")
b.pack(side = LEFT, padx = 15, pady = 6)
b.bind("<Button-1>", click)

b = Button(f, text=".", padx=15, pady=18, font="lucida 25 bold")
b.pack(side = LEFT, padx = 15, pady = 6)
b.bind("<Button-1>", click)

b = Button(f, text="C", padx=15, pady=8, font="lucida 25 bold")
b.pack(side = LEFT, padx = 15, pady = 6)
b.bind("<Button-1>", click)
f.pack()

root.mainloop()



































