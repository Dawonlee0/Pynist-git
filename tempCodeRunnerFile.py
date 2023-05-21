from tkinter import *
import random

def on_key_press(event):
    global player_x, player_y
    if event.keysym == "Up":
        player_y -= 10
    elif event.keysym == "Down":
        player_y += 10
    elif event.keysym == "Left":
        player_x -= 10
    elif event.keysym == "Right":
        player_x += 10
    canvas.coords(player, player_x, player_y)

def move_obstacles():
    global obstacle_x, obstacle_y
    canvas.move(obstacle, -5, 0)
    obstacle_x -= 5
    if obstacle_x + obstacle_width < 0:
        obstacle_x = canvas_width
        obstacle_y = random.randint(50, canvas_height - 50 - obstacle_height)
        canvas.coords(obstacle, obstacle_x, obstacle_y)
    if check_collision():
        game_over()
    else:
        root.after(20, move_obstacles)

def check_collision():
    player_coords = canvas.coords(player)
    obstacle_coords = canvas.coords(obstacle)
    if player_coords[2] >= obstacle_coords[0] and player_coords[0] <= obstacle_coords[2] and \
            player_coords[3] >= obstacle_coords[1] and player_coords[1] <= obstacle_coords[3]:
        return True
    return False

def collect_item():
    global score
    player_coords = canvas.coords(player)
    item_coords = canvas.coords(item)
    if player_coords[2] >= item_coords[0] and player_coords[0] <= item_coords[2] and \
            player_coords[3] >= item_coords[1] and player_coords[1] <= item_coords[3]:
        score += 1
        score_label.config(text="Score: {}".format(score))
        item_x = canvas_width
        item_y = random.randint(50, canvas_height - 50 - item_size)
        canvas.coords(item, item_x, item_y)

def game_over():
    canvas.unbind("<KeyPress>")
    canvas.create_text(canvas_width / 2, canvas_height / 2, text="Game Over", font=("Arial", 24), fill="red")

root = Tk()
root.title("Undertale-like Game")

canvas_width = 400
canvas_height = 300
canvas = Canvas(root, width=canvas_width, height=canvas_height)
canvas.pack()
canvas.bind("<KeyPress>", on_key_press)
canvas.focus_set()

player_width = 20
player_height = 20
player_x = 50
player_y = canvas_height / 2 - player_height / 2
player = canvas.create_rectangle(player_x, player_y, player_x + player_width, player_y + player_height, fill="blue")

obstacle_width = 40
obstacle_height = 20
obstacle_x = canvas_width
obstacle_y = random.randint(50, canvas_height - 50 - obstacle_height)
obstacle = canvas.create_rectangle(obstacle_x, obstacle_y, obstacle_x + obstacle_width, obstacle_y + obstacle_height, fill="red")

item_size = 10
item_x = canvas_width
item_y = random.randint(50, canvas_height -50 - item_size)
item = canvas.create_rectangle(item_x, item_y, item_x + item_size, item_y + item_size, fill="green")

score = 0
score_label = Label(root, text="Score: 0")
score_label.pack()

root.after(1000, move_obstacles)
root.after(1000, collect_item)

root.mainloop()
