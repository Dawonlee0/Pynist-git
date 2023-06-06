from tkinter import *
import random
import subprocess

def stage3():
    # main 파일 실행 함수
    def open_main():
        subprocess.Popen(["python", "main.py"])
        root.destroy()  # Tkinter 창 닫기

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

    def create_wall():
        global rx, ry, rwidth, rheight, wall

        position = random.randint(1, 4)
        if position == 1: #위쪽 벽 생성
            rx = 0
            ry = 0
            rwidth = 400
            rheight = -400

        elif position == 2: #왼쪽 벽 생성
            rx = 0
            ry = 0
            rwidth = -400
            rheight = 400

        elif position == 3: #아래쪽 벽 생성
            rx = 0
            ry = 405
            rwidth = 400
            rheight = 400

        elif position == 4: #오른쪽 벽 생성
            rx = 405
            ry = 0
            rwidth = 400
            rheight = 400
        wall = canvas.create_rectangle(rx, ry, rx + rwidth, ry + rheight, fill="red")

        move_wall(position)
        

    def move_wall(position):

        for repetition in range(1000, 2499, 100):
            root.after(repetition, move1, position)
            

        for repetition in range(2500, 3999, 100):
            root.after(repetition, move2, position)
            


    def move1(position):
        global wall_coords, wall

        if position == 1:
            canvas.move(wall, 0, 20)
            damage_()

        elif position == 2:
            canvas.move(wall, 20, 0)
            damage_()

        elif position == 3:
            canvas.move(wall, 0, -20)
            damage_()

        elif position == 4:
            canvas.move(wall, -20, 0)
            damage_()

        wall_coords = canvas.coords(wall)
        

    def move2(position):
        global wall_coords, wall

        if position == 1:
            canvas.move(wall, 0, -20)
            damage_()

        elif position == 2:
            canvas.move(wall, -20, 0)
            damage_()

        elif position == 3:
            canvas.move(wall, 0, 20)
            damage_()

        elif position == 4:
            canvas.move(wall, 20, 0)
            damage_()

        

        

    def damage_():
        rxm = canvas.coords(wall)[0]
        rym = canvas.coords(wall)[1]
        rxwm = canvas.coords(wall)[2]
        ryhm = canvas.coords(wall)[3]
        if canvas.coords(user)[2] >= rxm and canvas.coords(user)[0] <= rxwm and canvas.coords(user)[3] >= rym and canvas.coords(user)[1] <= ryhm:
            user_health.set(user_health.get() - 1)
            if user_health.get() <= 0:
                game_over()

    def remove_wall(wall):
        canvas.delete(wall)

    # 게임 오버 처리 함수
    def game_over():
        canvas.unbind("<KeyPress>")  # 키 입력 이벤트 언바인딩
        if monster_health.get() <= 0:
            canvase = Canvas(root, width=400, height=400)
            canvase.pack()
            canvase.create_text(200, 200, text="Win", font=("Arial", 24), fill="green")  # 몬스터를 처치한 경우
            button1 = Button(root, text="메인화면", command=open_main)
            button1.pack()
        else:
            canvase = Canvas(root, width=400, height=400)
            canvase.pack()
            canvase.create_text(200, 200, text="Game Over", font=("Arial", 24), fill="red")
            button1 = Button(root, text="메인화면", command=open_main)
            button1.pack()


    # 몬스터의 턴 처리 함수
    def monster_turn():
        recover_canvas()
        remove_battleUi()
        # canvas.bind("<KeyPress>", on_key_press)
        count_walls(0)

    # 몬스터의 턴 종료 처리 함수
    def end_monster_turn():
        recover_battleUi()
        remove_canvas()
        remove_wall(wall)

    def count_walls(count):
        if user_health.get() <= 0:
            count = 5
        if count >= 4:
            end_monster_turn()
            if count == 5:
                remove_battleUi()
            return
        
            

        create_wall()
        root.after(4500, lambda: count_walls(count + 1))

    # 전투 UI 숨기기 함수
    def remove_battleUi():
        attack_button.pack_forget()
        heal_button.pack_forget()

    def recover_battleUi():
        attack_button.pack()
        heal_button.pack()

    # 캔버스 숨기기 함수
    def remove_canvas():
        canvas.pack_forget()

    # 캔버스 복구 함수
    def recover_canvas():
        canvas.pack()

    # 사용자의 공격 처리 함수
    def user_attack():
        monster_health.set(monster_health.get() - 90)  # 몬스터 체력 감소
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


    # 사용자의 턴 처리 함수
    def user_turn():
        canvas.bind("<KeyPress>", on_key_press)
        attack_button.config(state=NORMAL)
        heal_button.config(state=NORMAL)

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
    stage3()