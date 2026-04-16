import tkinter as tk

root = tk.Tk()
root.title("Calculator")
root.geometry("320x500")
root.configure(bg="#1e1e1e")
root.resizable(False, False)

expression = "" 

display = tk.Entry(
    root,
    font=("Arial", 28),
    background="#1e1e1e",
    fg="White",
    borderwidth=0,
    justify="right"
)
display.pack(fill="both",padx=10,pady=20,ipady=20)

def update():
    display.delete(0,tk.END)
    display.insert(0, expression)

def press(value):
    global expression

    if value == "=":
        try:
            expression = str(eval(expression))
        except:
            expression = "ERROR"
    elif value == "C":
        expression = ""
    else:
        expression  += value
    
    update()

buttons = [
    ["C","(",")", "/"],
    ["7", "8", "9", "*"],
    ["4","5","6","-"],
    ["1","2","3","+"],
    ["0",".","="]
]
btn_bg = "#2d2d2d"
btn_fg = "white"
op_bg = "#ff9500"

for row in buttons:
    frame = tk.Frame(root,bg="#1e1e1e")
    frame.pack(expand=True, fill="both", padx=5, pady=5)

    for btn in row:
        color = op_bg if btn in "+-*/=" else btn_bg

        b = tk.Button(
            frame,
            text=btn,
            font=("Arial", 16),
            bg = color,
            fg=btn_fg,
            borderwidth=0,
            command=lambda x=btn:press(x)
        )
        b.pack(side="left", expand=True, fill="both", padx=5, pady=5)

def key(event):
    k = event.char

    if k in "0123456789+-*/().":
        press(k)
    elif event.keysym == "Return":
        press("=")
    elif event.keysym == "Backspace":
        global expression
        expression = expression[:-1]
        update()
root.bind("<Key>", key)

root.mainloop()