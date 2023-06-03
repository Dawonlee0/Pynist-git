from tkinter import *
import random

def generate_obstacle():
    global x, y, width, height
    x = random.randint(0, 400)  # x 좌표 랜덤 생성
    y = 0
    width = 50  # 기둥 가로 길이 고정
    height = 400  # 기둥 세로 길이 고정
    obstacle = canvas.create_rectangle(x, y, x + width, y + height, fill="white")  # 흰색 기둥 생성
    root.after(1000, change_color, obstacle)  # 1초 후에 색상 변경
    root.after(1500, remove_obstacle, obstacle)  # 1.5초 후에 기둥 삭제
    root.after(1500, generate_obstacle)  # 1.5초 후에 새로운 기둥 생성

def change_color(obstacle):
    canvas.itemconfig(obstacle, fill="red")  # 기둥 색상 변경
    if canvas.coords(user)[2] >= x and canvas.coords(user)[0] <= x + width and canvas.coords(user)[3] >= y and canvas.coords(user)[1] <= y + height:
        if canvas.itemcget(obstacle, "fill") == "red":  # 사각형이 빨간색일 때만 게임 오버 처리
            game_over()

def remove_obstacle(obstacle):
    canvas.delete(obstacle)

def game_over():
    canvas.unbind("<KeyPress>")
    canvas.create_text(200, 200, text="Game Over", font=("Arial", 24), fill="red")

root = Tk()
root.title("Game")
canvas = Canvas(root, width=400, height=400)
canvas.pack()
user = canvas.create_rectangle(185, 355, 215, 385, fill="blue")
generate_obstacle()
root.mainloop()
