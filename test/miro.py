from tkinter import *

# 미로 맵
maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 0, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

# 캔버스 크기 및 셀 크기
canvas_width = 400
canvas_height = 400
cell_size = canvas_width // len(maze[0])

def draw_maze(canvas):
    canvas.delete("all")
    for y in range(len(maze)):
        for x in range(len(maze[y])):
            if maze[y][x] == 1:  # 벽
                canvas.create_rectangle(x * cell_size, y * cell_size, (x + 1) * cell_size, (y + 1) * cell_size, fill="black")
            else:  # 길
                canvas.create_rectangle(x * cell_size, y * cell_size, (x + 1) * cell_size, (y + 1) * cell_size, fill="white")

def on_key_press(event):
    x, y = get_user_position()
    if event.keysym == "Up" and y > 0 and maze[y-1][x] == 0:
        move_user(x, y-1)
    elif event.keysym == "Down" and y < len(maze) - 1 and maze[y+1][x] == 0:
        move_user(x, y+1)
    elif event.keysym == "Left" and x > 0 and maze[y][x-1] == 0:
        move_user(x-1, y)
    elif event.keysym == "Right" and x < len(maze[y]) - 1 and maze[y][x+1] == 0:
        move_user(x+1, y)

def get_user_position():
    for y in range(len(maze)):
        for x in range(len(maze[y])):
            if maze[y][x] == 2:  # 사용자 위치
                return x, y

def move_user(x, y):
    current_x, current_y = get_user_position()
    maze[current_y][current_x] = 0  # 이전 위치를 길로 변경
    maze[y][x] = 2  # 새로운 위치에 사용자 표시
    draw_maze(canvas)

    # 목표 지점 도달 시 게임 종료
    if x == len(maze[0]) - 2 and y == len(maze) - 2:
        game_over()
def game_over():
    canvas.unbind("<KeyPress>")
    canvas.create_text(canvas_width // 2, canvas_height // 2, text="Goal Reached!", font=("Arial", 24), fill="red")

root = Tk()
root.title("Maze Game")

canvas = Canvas(root, width=canvas_width, height=canvas_height)
canvas.pack()
canvas.bind("<KeyPress>", on_key_press)
canvas.focus_set()

draw_maze(canvas)
move_user(1, 1) # 사용자 초기 위치

root.mainloop()
