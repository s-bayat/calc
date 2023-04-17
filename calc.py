from tkinter import *

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

# ========================== buttons ==========================
btn_plus = Button(top_third, text="+", width=8, highlightbackground=color)
btn_plus.pack(side=LEFT, padx=5, pady=5)
btn_minus = Button(top_third, text="-", width=8, highlightbackground=color)
btn_minus.pack(side=LEFT, padx=5, pady=5)
btn_mul = Button(top_third, text="*", width=8, highlightbackground=color)
btn_mul.pack(side=LEFT, padx=5, pady=5)
btn_div = Button(top_third, text="/", width=8, highlightbackground=color)
btn_div.pack(side=LEFT, padx=5, pady=5)
# ========================== entries and lables ==========================
label_first_num = Label(top_first, text="Input number 1:", bg=color)
label_first_num.pack(side=LEFT, padx=5, pady=5)
entry_first_num = Entry(top_first)
entry_first_num.pack(side=LEFT)
label_second_num = Label(top_second, text="Input number 2:", bg=color)
label_second_num.pack(side=LEFT, padx=5, pady=5)
entry_second_num = Entry(top_second)
entry_second_num.pack(side=LEFT)

res = Label(top_forth, text="Result", bg=color)
res.pack(side=LEFT, padx=5, pady=5)
res_num = Entry(top_forth)
res_num.pack(side=LEFT)

root.mainloop()
