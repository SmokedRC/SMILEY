import sys
import random
from tkinter import *
import tkinter as tk

root = tk.Tk()
root.title("Feedback Machine")
root.config(bg="skyblue")

left_frame = tk.Frame(root, bg="grey")
left_frame.grid(row=0, column=1, padx=10, pady=10, sticky=tk.N+S+E+W)

left_middle_frame = tk.Frame(root, bg="grey")
left_middle_frame.grid(row=0, column=2, padx=10, pady=10, sticky=tk.N+S+E+W)

middle_frame = tk.Frame(root, bg="grey")
middle_frame.grid(row=0, column=3, padx=10, pady=10, sticky=tk.N+S+E+W)

right_middle_frame = tk.Frame(root, bg="grey")
right_middle_frame.grid(row=0, column=4, padx=10, pady=10, sticky=tk.N+S+E+W)

right_frame = tk.Frame(root, bg="grey")
right_frame.grid(row=0, column=5, padx=10, pady=10, sticky=tk.N+S+E+W)

root.columnconfigure(0, weight=1)
root.columnconfigure(6, weight=1)
root.rowconfigure(0, weight=1)

image_excellent = PhotoImage(file="download.png")
image_okay = PhotoImage(file="straight.png")
image_bad = PhotoImage(file="sad.png")

def RegisterResponseExcellent():
    print("Glad to hear it was excellent")

def RegisterResponseOkay():
    print("Thanks for the repsonse")

def RegisterResponseBad():
    print("Sorry to hear it was bad")

button_excellent = tk.Button(left_frame, text="Excellent", image=image_excellent, command=RegisterResponseExcellent)
button_excellent.pack(fill=tk.BOTH, expand=True)

button_straight = tk.Button(middle_frame, text="Okay", image=image_okay, command=RegisterResponseOkay)
button_straight.pack(fill=tk.BOTH, expand=True)

button_bad = tk.Button(right_frame, text="Bad", image=image_bad , command=RegisterResponseBad)
button_bad.pack(fill=tk.BOTH, expand=True)

root.mainloop()