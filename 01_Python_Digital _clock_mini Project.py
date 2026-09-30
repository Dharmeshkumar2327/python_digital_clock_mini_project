import tkinter as tk
from time import strftime


root = tk.Tk()
root.title("Digital Clock")
root.geometry("700x350")
root.configure(bg="#101010")


def update_clock():
    time = strftime("%I:%M:%S %p")
    date = strftime("%A, %d %B %Y")

    time_label.config(text=time)
    date_label.config(text=date)

    root.after(1000, update_clock)


title_label = tk.Label(
    root,
    text="DIGITAL CLOCK",
    font=("Segoe UI", 20, "bold"),
    fg="white",
    bg="#101010"
)
title_label.pack(pady=(40, 10))


time_label = tk.Label(
    root,
    font=("Segoe UI", 60, "bold"),
    fg="#00FFCC",
    bg="#101010"
)
time_label.pack()


date_label = tk.Label(
    root,
    font=("Segoe UI", 18),
    fg="white",
    bg="#101010"
)
date_label.pack(pady=10)


update_clock()

root.mainloop()