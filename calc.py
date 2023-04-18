from tkinter import *
import tkinter.messagebox

# ========================== settings ==========================
root = Tk()
root.title("calculator")
root.geometry("300x600")
root.resizable(height=False, width=False)
color = "gray"
root.configure(bg=color)
# ========================== frames ==========================
top_first = Frame(root, width=400, height=50, bg=color)
top_first.pack(side=TOP)
top_second = Frame(root, width=400, height=50, bg=color)
top_second.pack(side=TOP)
top_third = Frame(root, width=400, height=50, bg=color)
top_third.pack(side=TOP)
top_forth = Frame(root, width=400, height=50, bg=color)
top_forth.pack(side=TOP)


# ========================== functions ==========================
def errormsg(msg):
    if msg == 'error':
        tkinter.messagebox.showerror("Error", "something went wrong")
    elif msg == "division zero error":
        tkinter.messagebox.showerror("Error", "can not divide by zero")


def plus():
    try:
        value = float(num_1.get()) + float(num_2.get())
        res_value.set(value)
    except:
        errormsg("error")


def minus():
    try:
        value = float(num_1.get()) - float(num_2.get())
        res_value.set(value)
    except:
        errormsg("error")


def mul():
    try:
        value = float(num_1.get()) * float(num_2.get())
        res_value.set(value)
    except:
        errormsg("error")


def div():
    if num_2.get() == '0':
        errormsg("division zero error")
    elif num_2.get() != "0":
        try:
            value = float(num_1.get()) / float(num_2.get())
            res_value.set(value)
        except:
            errormsg("error")


# ========================== variables ==========================

num_1 = StringVar()
num_2 = StringVar()
res_value = StringVar()

# ========================== buttons ==========================
btn_plus = Button(top_third, text="+", width=8, highlightbackground=color, command=lambda: plus())
btn_plus.pack(side=LEFT, padx=5, pady=5)
btn_minus = Button(top_third, text="-", width=8, highlightbackground=color, command=lambda: minus())
btn_minus.pack(side=LEFT, padx=5, pady=5)
btn_mul = Button(top_third, text="*", width=8, highlightbackground=color, command=lambda: mul())
btn_mul.pack(side=LEFT, padx=5, pady=5)
btn_div = Button(top_third, text="/", width=8, highlightbackground=color, command=lambda: div())
btn_div.pack(side=LEFT, padx=5, pady=5)
# ========================== entries and labels ==========================
label_first_num = Label(top_first, text="Input number 1:", bg=color)
label_first_num.pack(side=LEFT, padx=5, pady=5)
entry_first_num = Entry(top_first, textvariable=num_1)
entry_first_num.pack(side=LEFT)
label_second_num = Label(top_second, text="Input number 2:", bg=color)
label_second_num.pack(side=LEFT, padx=5, pady=5)
entry_second_num = Entry(top_second, textvariable=num_2)
entry_second_num.pack(side=LEFT)

res = Label(top_forth, text="Result", bg=color)
res.pack(side=LEFT, padx=5, pady=5)
res_num = Entry(top_forth, textvariable=res_value)
res_num.pack(side=LEFT)

root.mainloop()
