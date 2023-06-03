from tkinter import *
import subprocess

def open_file1():
    subprocess.Popen(["python", "1.py"])

root = Tk()

button2 = Button(root, text="Open 1.py", command=open_file1)
button2.pack()

root.mainloop()
