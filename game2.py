from tkinter import *
import random

def stage1():
    # 사용자가 방향키를 입력받는 함수
    def on_key_press(event):
        # 몬스터의 턴이 아닐 때에만 사용자 이동 가능
        if event.keysym == "Up" and not monster_turn_active():
            canvas.move(user, 0, -10)
        elif event.keysym == "Down" and not monster_turn_active():
            canvas.move(user, 0, 10)
        elif event.keysym == "Left" and not monster_turn_active():
            canvas.move(user, -10, 0)
        elif event.keysym == "Right" and not monster_turn_active():
            canvas.move(user, 10, 0)

    # 몬스터의 턴 여부를 확인하는 함수
    def monster_turn_active():
        return attack_button["state"] == DISABLED  

    # 총알을 발사하는 함수
    def shoot_bullet():
        # x = random.randint(0, 380)  # x 좌표 랜덤 생성
        # y = 0
        # bullet = canvas.create_rectangle(x, y, x + 20, y + 20, fill="red")  # 총알 생성
        # bullets[bullet] = (0, 7.5)  # 총알의 이동 속도 설정
        global x, y, width, height
        x = random.randint(0, 400)  # x 좌표 랜덤 생성
        y = 0
        width = 50  # 기둥 가로 길이 고정
        height = 400  # 기둥 세로 길이 고정
        bullet = canvas.create_rectangle(x, y, x + width, y + height, fill="white")  # 흰색 기둥 생성
        root.after(1000, change_color, bullet)  # 1초 후에 색상 변경
        check_collision(bullet)
        root.after(1500, remove_obstacle, bullet)  # 1.5초 후에 기둥 삭제
        # root.after(1500, shoot_bullet)  # 1.5초 후에 새로운 기둥 생성

    def check_collision(bullet):
        user_coords = canvas.coords(user)
        bullet_coords = canvas.coords(bullet)
        if user_coords[0] < bullet_coords[2] and user_coords[2] > bullet_coords[0] and user_coords[1] < bullet_coords[3] and user_coords[3] > bullet_coords[1]:
            if canvas.itemcget(bullet, "fill") == "red":  # 사각형이 빨간색일 때만 게임 오버 처리
                user_health.set(user_health.get() - 10)  # 유저 체력 감소
                canvas.delete(bullet)  # 충돌한 총알 삭제
                if user_health.get() <= 0:
                    game_over()  # 게임 오버
        else:
            root.after(10, lambda: check_collision(bullet))  # 지연 후 충돌 확인
    
    def change_color(bullet):
        canvas.itemconfig(bullet, fill="red")  # 기둥 색상 변경

    def remove_obstacle(bullet):
        canvas.delete(bullet)

    # 게임 오버 처리 함수
    def game_over():
        canvas.unbind("<KeyPress>")  # 키 입력 이벤트 언바인딩
        if monster_health.get() <= 0:
            canvas.create_text(200, 200, text="Win", font=("Arial", 24), fill="green")  # 몬스터를 처치한 경우
        else:
            canvas.create_text(200, 200, text="Game Over", font=("Arial", 24), fill="red")  # 몬스터에게 패배한 경우

    # 몬스터의 턴 처리 함수
    def monster_turn():
        recover_canvas()
        remove_battleUi()
        # canvas.bind("<KeyPress>", on_key_press)
        shoot_bullets(0)  # 총알 여러 개 발사

    # 몬스터가 총알을 발사하는 함수
    def shoot_bullets(count):
        if count >= 15:  # 총알을 10개 발사하면 종료
            end_monster_turn()
            return

        shoot_bullet()  # 총알 발사
        root.after(1500, lambda: shoot_bullets(count + 1))  # 2초 간격으로 총알 발사

    # 몬스터의 턴 종료 처리 함수
    def end_monster_turn():
        remove_bullets()
        recover_battleUi()
        remove_canvas()

    # 총알 삭제 함수
    def remove_bullets():
        for bullet in bullets.copy():
            canvas.delete(bullet)
            bullets.pop(bullet)

    # 전투 UI 숨기기 함수
    def remove_battleUi():
        surrender_button.pack_forget()
        attack_button.pack_forget()
        heal_button.pack_forget()
        
    def recover_battleUi():
        attack_button.pack()
        heal_button.pack()
        surrender_button.pack()

    # 캔버스 숨기기 함수
    def remove_canvas():
        canvas.pack_forget()

    # 캔버스 복구 함수
    def recover_canvas():
        canvas.pack()

    # 사용자의 공격 처리 함수
    def user_attack():
        monster_health.set(monster_health.get() - 20)  # 몬스터 체력 감소
        if monster_health.get() <= 0:
            game_over()  # 몬스터 체력이 0 이하이면 게임 오버
        else:
            monster_turn()  # 몬스터의 턴으로 넘어감

    # 사용자의 회복 처리 함수
    def user_heal():
        if user_health.get() == 100:
            # 체력이 이미 다 찼을 때
            user_turn()
        else:
            user_health.set(user_health.get() + 10)  # 사용자 체력 증가
            if user_health.get() > 100:
                user_health.set(100)
            monster_turn()  # 몬스터의 턴으로 넘어감

    # 사용자의 항복 처리 함수
    def user_surrender():
        game_over()  # 게임 오버 처리

    # 사용자의 턴 처리 함수
    def user_turn():
        canvas.bind("<KeyPress>", on_key_press)
        attack_button.config(state=NORMAL)
        heal_button.config(state=NORMAL)
        surrender_button.config(state=NORMAL)

    root = Tk()
    root.title("게임이다")
    scw = root.winfo_screenwidth()
    sch = root.winfo_screenheight()
    x = (scw - 800) / 2
    y = (sch - 800) / 2
    root.geometry('%dx%d+%d+%d' % (800, 800, x, y))

    image_label = Label(root)  # 몬스터 이미지를 표시할 Label 위젯 생성
    image_label.pack()

    canvas = Canvas(root, width=400, height=400)
    canvas.pack()
    canvas.bind("<KeyPress>", on_key_press)
    canvas.focus_set()

    user = canvas.create_rectangle(185, 355, 215, 385, fill="blue")

    bullets = {}

    monster_health = IntVar(root)
    monster_health.set(100)

    user_health = IntVar(root)
    user_health.set(100)

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

    remove_canvas()

    def load_image():
        image = PhotoImage(file="1.png", master=root)  # 이미지 파일 경로에 맞게 수정
        image = image.subsample(4)  # 이미지를 1/2로 축소
        image_label.config(image=image)
        image_label.image = image

    load_image()  # 이미지 로드

    user_turn()  # Start the first turn

    root.mainloop()

if __name__ == "__main__":
    stage1()

# game2()
