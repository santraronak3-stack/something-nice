import tkinter
# Variables
f_color1 = "cyan"
bg_color1 = "grey"; bg_color2 = "cyan"
def main():
    win1 = tkinter.Tk()
    win1.title("Test")
    win1.geometry("500x300")
    win1["bg"] = bg_color1
    s1 = tkinter.Label(win1, text="A Simple eval()-based calculator", bg="grey",
         fg=f_color1,
         font=("Consolas", 10)); s1.pack()
    inp = tkinter.Entry(win1, bg=bg_color2); inp.pack()
    a = tkinter.Label(win1, text="Result: ", bg="grey", font=("Consolas", 10), fg=f_color1); a.pack()
    def calc_engine1():
        try:
            a.config(text="Result: " + str(eval(inp.get(), {"__builtins__": None})), fg=f_color1)
        except Exception as e:
            a.config(text="Result: Type a valid input", fg=f_color1)
    b1 = tkinter.Button(win1, text="Calculate", command=calc_engine1, font=("Consolas", 10), bg=f_color1)
    b1.pack()
    def leaver():
        win1.destroy()
    b2 = tkinter.Button(win1, text="Quit", command=leaver, font=("Consolas", 10), bg=f_color1)
    b2.pack(pady=5)
    win1.mainloop()


main()
