from tkinter import *

root = Tk()
root.title("My Calculator")
root.configure(bg="white")  # Window background

# Entry box (calculator screen)
e = Entry(root, width=20, borderwidth=8, fg="black", bg="white",
          font=("Arial", 22, "bold"), justify="right")
e.grid(row=0, column=0, columnspan=4, padx=15, pady=20, ipady=15)


def buttonclick(symbol):
    current = e.get()
    e.delete(0, END)
    e.insert(0, current + str(symbol))


def clear():
    e.delete(0, END)


def equal():
    try:
        expression = e.get().replace("×", "*").replace("÷", "/").replace("^", "**")
        result = eval(expression)
        e.delete(0, END)
        e.insert(0, str(result))
    except:
        e.delete(0, END)
        e.insert(0, "Error")


# Common style for buttons
btn_style = {
    "bg": "black",
    "fg": "white",
    "font": ("Arial", 14, "bold"),
    "width": 5,
    "height": 2,
    "relief": "raised",
    "bd": 3
}

# Number & special buttons
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2),
    ("0", 4, 0), (".", 4, 1), ("^", 4, 2)
]

for (text, row, col) in buttons:
    Button(root, text=text, command=lambda t=text: buttonclick(t), **btn_style)\
        .grid(row=row, column=col, padx=5, pady=5)

# Operator buttons (right side)
Button(root, text="÷", command=lambda: buttonclick("÷"), **btn_style)\
    .grid(row=1, column=3, padx=5, pady=5)
Button(root, text="×", command=lambda: buttonclick("×"), **btn_style)\
    .grid(row=2, column=3, padx=5, pady=5)
Button(root, text="−", command=lambda: buttonclick("-"), **btn_style)\
    .grid(row=3, column=3, padx=5, pady=5)
Button(root, text="+", command=lambda: buttonclick("+"), **btn_style)\
    .grid(row=4, column=3, padx=5, pady=5)

# Bottom row: Clear and Equal
Button(root, text="C", command=clear, **btn_style)\
    .grid(row=5, column=0, columnspan=2, sticky="we", padx=5, pady=5)
Button(root, text="=", command=equal, **btn_style)\
    .grid(row=5, column=2, columnspan=2, sticky="we", padx=5, pady=5)

root.mainloop()
