import tkinter as tk
import random

def move_character(event):
    key = event.keysym
    if key == "Up":
        canvas.move(character, 0, -10)
    elif key == "Down":
        canvas.move(character, 0, 10)
    elif key == "Left":
        canvas.move(character, -10, 0)
    elif key == "Right":
        canvas.move(character, 10, 0)

def move_obstacle():
    x, y, _, _ = canvas.coords(obstacle)
    canvas.move(obstacle, 0, 10)

    # 충돌 감지
    if y >= 380 and character_in_collision(x, y):
        game_over()
    else:
        window.after(100, move_obstacle)

def character_in_collision(x, y):
    character_coords = canvas.coords(character)
    character_x1, character_y1, character_x2, character_y2 = character_coords
    return x >= character_x1 and x <= character_x2 and y >= character_y1 and y <= character_y2

def game_over():
    canvas.delete("all")
    canvas.create_text(200, 200, text="게임 오버", font=("Arial", 24), fill="red")

# 윈도우 생성
window = tk.Tk()
window.title("똥 피하기")

# 캔버스 생성
canvas = tk.Canvas(window, width=400, height=400)
canvas.pack()

# 캐릭터 생성
character = canvas.create_rectangle(180, 380, 220, 400, fill="blue")

# 랜덤으로 똥 생성
x_pos = random.randint(50, 350)
obstacle = canvas.create_oval(x_pos, 0, x_pos + 40, 40, fill="brown")

# 키 이벤트 바인딩
window.bind("<Key>", move_character)
window.focus_set()

# 똥 이동 시작
move_obstacle()

# 윈도우 실행
window.mainloop()
