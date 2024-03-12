from tkinter import *
import random
import string

root = Tk()
root.geometry("400x280")
root.title("Password Generator")
root.configure(bg='lightgray')  
root.resizable(False,False)

# intro text
title_label = Label(root, text="The strength of password", bg='grey', fg='white')
title_label.grid(row=0, column=0, columnspan=3, padx=20, pady=10)

title = StringVar()
title.set("The strength of password")

def selection():
    selection = choice.get()

choice = IntVar()
R1 = Radiobutton(root, text="POOR", variable=choice, value=1, command=selection, bg='lightgrey')
R1.grid(row=1, column=0, padx=5, pady=5)
R2 = Radiobutton(root, text="AVERAGE", variable=choice, value=2, command=selection, bg='lightgrey')
R2.grid(row=1, column=1, padx=5, pady=5)
R3 = Radiobutton(root, text="ADVANCED", variable=choice, value=3, command=selection, bg='lightgrey')
R3.grid(row=1, column=2, padx=5, pady=5)

# pass length
lenlabel = StringVar()
lenlabel.set("password length")
Label(root, textvariable=lenlabel, bg='lightgrey').grid(row=2, column=0, columnspan=2, padx=10, pady=5)

val = IntVar()
spinlength = Spinbox(root, from_=8, to_=24, textvariable=val, width=13)
spinlength.grid(row=2, column=2, padx=10, pady=5)

def callback():
    generated_password = passgen()
    isum.delete('1.0', END)  # Clear previous content
    isum.insert(END, generated_password)

passgenButton = Button(root, text="Generate password", bd=5, height=2, command=callback)
passgenButton.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

isum = Text(root, height=2, width=len(passgenButton.cget("text")), bg='lightgrey')
isum.grid(row=3, column=2, padx=10, pady=10)

# logic
poor = string.ascii_uppercase + string.ascii_lowercase
average = string.ascii_uppercase + string.ascii_lowercase + string.digits
symbols = """`~!@#$%^&()_-+={[\|:;'''<>,.?/"""
advanced = poor + average + symbols

def passgen():
    if choice.get() == 1:
        return "".join(random.sample(poor, val.get()))
    elif choice.get() == 2:
        return "".join(random.sample(average, val.get()))
    elif choice.get() == 3:
        return "".join(random.sample(advanced, val.get()))

root.mainloop()
