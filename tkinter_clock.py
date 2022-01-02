from tkinter import *

root = Tk()
root.configure(background='white')
root.title("clock by daniild")
root.geometry("600x400")


def update(my_lab):
    my_lab.config(text=f"new text")


my_label = Label(root, text="Old text")
my_label.pack(pady=20)
my_label.after(5000, lambda: update(my_label))

root.mainloop()
