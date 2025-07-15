import tkinter as tk

app = tk.Tk()
app.geometry("700x400")
app.title("My First Desktop Application")
app.config(background = "#4bdb1a")

# font = (font_family, font_size, font_style)

lbl = tk.Label(app, text = "Hellow world", font = ("robort", 40, "bold"), fg = "#4bdb1a", bg = "#1c5708")
lbl.pack(fill = "x", side = "top", pady = 24, padx = 20, ipady = 20)


ent = tk.Entry(app, font = ("robort", 30, "italic"), fg = "#4bdb1a", bg = "#1c5708")
ent.pack()


btn = tk.Button(app, text = "Submit", font = ("robort", 24, "bold"), fg = "#4bdb1a", bg = "#1c5708")
btn.pack(pady = 20, ipadx = 30)

app.mainloop()


# wegigts

# 3 methods
    # 1) pack() -----> center
    # 2) grid()
    # 3) place()