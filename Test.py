import tkinter
def main():
    win1 = tkinter.Tk()
    win1.title("Test")
    win1.geometry("500x300")
    win1["bg"] = "grey"
    s1 = tkinter.Label(win1, text="A Simple eval()-based calculator", bg="grey",
         fg="white",
         font=("Consolas", 10)); s1.pack()
    inp = tkinter.Entry(win1, bg="grey"); inp.pack()
    a = tkinter.Label(win1, text="Result: ", bg="grey", font=("Consolas", 10)); a.pack()
    def test1():
        a.config(text="Result: " + str(eval(inp.get())))
    b1 = tkinter.Button(win1, text="Calculate", command=test1, font=("Consolas", 10))
    b1.pack()
    win1.mainloop()


main()
