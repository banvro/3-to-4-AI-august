import tkinter as tk 


app = tk.Tk()
app.geometry("700x600")
app.config(background = "green")

lbl = tk.Label(app, text = "Username : ", font = ("robort", 30, "bold"))
lbl.grid(row = 1, column = 1)

ent = tk.Entry(app, font = ("robort", 30))
ent.grid(row = 100, column = 100)


app.mainloop()