from tkinter import *
import subprocess

# main 파일 실행 함수
def open_file2():
    subprocess.Popen(["python", "main.py"])
    root.destroy()  # Tkinter 창 닫기

root1 = Tk()

button1 = Button(root, text="Open main.py", command=open_file2)
button1.pack()

root1.mainloop()
