import tkinter as tk

def age_Calculator():
    age_inp = dob.get()
    agee = int(age_inp)
    age = 2025 - agee
    btnshow.config(text = f"You are {age} years old.")

app = tk.Tk()
app.geometry("800x350")
app.title("Age Calculator")
app.config(background = "#1af0d7")

lbl = tk.Label(app, text = "Age Calculator", font = ("robort", 50, "bold"), fg = "#1af0d7", bg = "#2f968a")
lbl.pack(fill = "x")

dob = tk.Entry(app, font = ("robort", 30))
dob.pack(pady = 30)

btn = tk.Button(app, text = "Check Age", font = ("robort", 25, "bold"), fg = "#1af0d7", bg = "#2f968a", command = age_Calculator)
btn.pack(ipadx = 30)


btnshow = tk.Label(app, text = "", bg = "#1af0d7", font = ("robort", 20), fg = "#1a544d")
btnshow.pack(pady = 30)


app.mainloop()