from tkinter import *
import random

def game2():
    def on_key_press(event):
                    if event.keysym == "Up" and not monster_turn_active():
                     canvas.move(user, 0, -10)
                    elif event.keysym == "Down" and not monster_turn_active():
                        canvas.move(user, 0, 10)
                    elif event.keysym == "Left" and not monster_turn_active():
                        canvas.move(user, -10, 0)
                    elif event.keysym == "Right" and not monster_turn_active():
                        canvas.move(user, 10, 0)

    def monster_turn_active():
        return attack_button["state"] == DISABLED

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
        if monster_health.get() <= 0:
            canvas.create_text(200, 200, text="Win", font=("Arial", 24), fill="green")
        else:
            canvas.create_text(200, 200, text="Game Over", font=("Arial", 24), fill="red")

    def monster_turn():
        remove_battleUi()
        # canvas.bind("<KeyPress>", on_key_press)
        shoot_bullets(0)  # 총알 여러 개 발사

    def shoot_bullets(count):
        if count >= 10:  # !!!!!총알을 10개 발사하면 종료
            end_monster_turn()
            return

        shoot_bullet()
        root.after(2000, lambda: shoot_bullets(count + 1))  # 2초 간격으로 총알 발사

    def end_monster_turn():
        remove_bullets()
        recover_battleUi()
        remove_canvas()

    def remove_bullets():
        for bullet in bullets.copy():
            canvas.delete(bullet)
            bullets.pop(bullet)

    def remove_battleUi():
        surrender_button.pack_forget()
        attack_button.pack_forget()
        heal_button.pack_forget()

    def recover_battleUi():
        attack_button.pack()
        heal_button.pack()
        surrender_button.pack()

    def remove_canvas():
        canvas.pack_forget()
        user.pack_forget()
    
    def user_attack():
        monster_health.set(monster_health.get() - 1)
        if monster_health.get() <= 0:
            game_over()
        else:
            monster_turn()

    def user_heal():
        user_health.set(user_health.get() + 1)
        monster_turn()

    def user_surrender():
        game_over()

    def user_turn():
        canvas.bind("<KeyPress>", on_key_press)
        attack_button.config(state=NORMAL)
        heal_button.config(state=NORMAL)
        surrender_button.config(state=NORMAL)

    root = Tk()
    root.title("게임이다")
    scw = root.winfo_screenwidth()
    sch = root.winfo_screenheight()
    x = (scw - 800)/2
    y = (sch - 800)/2
    root.geometry('%dx%d+%d+%d' % (800, 800, x, y))

    image_label = Label(root)  # 몬스터 이미지를 표시할 Label 위젯 생성
    image_label.pack()

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

    attack_button = Button(root, text="Attack", command=user_attack, state=DISABLED)
    attack_button.pack()

    heal_button = Button(root, text="Heal", command=user_heal, state=DISABLED)
    heal_button.pack()

    surrender_button = Button(root, text="Surrender", command=user_surrender, state=DISABLED)
    surrender_button.pack()

    def load_image():
        image = PhotoImage(file="1.png")  # 이미지 파일 경로에 맞게 수정
        image = image.subsample(4)  # 이미지를 1/2로 축소
        image_label.config(image=image)
        image_label.image = image

    load_image()  # 이미지 로드

    root.after(1000, move_bullets)  # Bullet movement

    user_turn()  # Start the first turn

    root.mainloop()

if __name__ == "__main__":
    game2()

# game2()