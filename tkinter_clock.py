from tkinter import *
import time

root = Tk()
root.configure(background='white')
root.title("clock by daniild")
root.geometry("600x400")


def clock():
    hour = time.strftime('%H')
    minute = time.strftime('%M')
    second = time.strftime('%S')
    am_pm = time.strftime('%p')
    day = time.strftime('%A')
    time_zone = time.strftime('%Z')

    my_label.config(text=f"{hour} : {minute} : {second} - {am_pm}")
    my_label.after(1000, clock)
    my_label2.config(text=f"{day} for {time_zone}")


def update(my_lab):
    my_lab.config(text=f"new text")


my_label = Label(root, text="", font=("Helvetica", 48), foreground='green', background="black")
my_label.pack(pady=20)

my_label2 = Label(root, text='', font=("Helvetica", 16), background="white", foreground='black')
my_label2.pack(pady=10)

clock()
root.mainloop()
