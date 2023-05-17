from tkinter import *
import random

def on_key_press(event):
    if event.keysym == "Up":
        canvas.move(user, 0, -10)
    elif event.keysym == "Down":
        canvas.move(user, 0, 10)
    elif event.keysym == "Left":
        canvas.move(user, -10, 0)
    elif event.keysym == "Right":
        canvas.move(user, 10, 0)

def move_bullets():
    bullets_to_remove = []
    for bullet in bullets:
        canvas.move(bullet, bullets[bullet][0], bullets[bullet][1])
        bullet_coords = canvas.coords(bullet)
        if bullet_coords[2] >= canvas.coords(user)[0] and bullet_coords[0] <= canvas.coords(user)[2] and bullet_coords[3] >= canvas.coords(user)[1] and bullet_coords[1] <= canvas.coords(user)[3]:
            user_health.set(user_health.get() - 1)
            if user_health.get() <= 0:
                game_over()
        if bullet_coords[3] >= 400:
            bullets_to_remove.append(bullet)
    for bullet in bullets_to_remove:
        canvas.delete(bullet)
        bullets.pop(bullet)
    root.after(50, move_bullets)

def shoot_bullet():
    x = random.randint(0, 380)
    y = 0
    bullet = canvas.create_rectangle(x, y, x + 20, y + 20, fill="red")
    bullets[bullet] = (0, 5)

def game_over():
    canvas.unbind("<KeyPress>")
    canvas.create_text(200, 200, text="Game Over", font=("Arial", 24), fill="red")

root = Tk()
root.title("Bullet Hell Game")

canvas = Canvas(root, width=400, height=400)
canvas.pack()
canvas.bind("<KeyPress>", on_key_press)
canvas.focus_set()

user = canvas.create_rectangle(180, 350, 220, 390, fill="blue")

bullets = {}

monster_health = IntVar()
monster_health.set(10)

user_health = IntVar()
user_health.set(10)

monster_health_label = Label(root, text="Monster Health:")
monster_health_label.pack()

monster_health_value = Label(root, textvariable=monster_health)
monster_health_value.pack()

user_health_label = Label(root, text="User Health:")
user_health_label.pack()

user_health_value = Label(root, textvariable=user_health)
user_health_value.pack()

attack_button = Button(root, text="Attack", command=shoot_bullet)
attack_button.pack()

heal_button = Button(root, text="Heal", command=None)  # Add your heal function here
heal_button.pack()

surrender_button = Button(root, text="Surrender", command=game_over)
surrender_button.pack()

shoot_bullet()  # Initial bullet

root.after(1000, move_bullets)  # Bullet movement

def generate_bullets():
    shoot_bullet()
    root.after(1000, generate_bullets)  # Bullet generation interval

root.after(1000, generate_bullets)  # Initial bullet generation

root.mainloop()
