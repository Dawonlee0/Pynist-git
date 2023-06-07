from tkinter import *
import random
import subprocess

def stage2():
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

    def generate_obstacle():
        global rx, ry, rwidth, rheight
        rx = random.randint(0, 350)  # x 좌표 랜덤 생성
        ry = 0
        rwidth = 50  # 기둥 가로 길이 고정
        rheight = 400  # 기둥 세로 길이 고정
        obstacle = canvas.create_rectangle(rx, ry, rx + rwidth, ry + rheight, fill="white")  # 흰색 기둥 생성
        root.after(1000, change_color, obstacle)# 1초 후에 색상 변경
        root.after(1100, damage_, obstacle)
        root.after(1200, damage_, obstacle)
        root.after(1200, damage_, obstacle)
        root.after(1300, damage_, obstacle)
        root.after(1400, damage_, obstacle)
        root.after(1500, damage_, obstacle)
        root.after(1600, damage_, obstacle)
        root.after(1700, damage_, obstacle)
        root.after(1800, damage_, obstacle)
        root.after(1900, damage_, obstacle)
        root.after(2000, remove_obstacle, obstacle)  # 1.5초 후에 기둥 삭제

    def generate_obstacle1():
        global rx1, ry1
        rx1 = random.randint(0, 350)  # x 좌표 랜덤 생성
        ry1 = 0
        obstacle = canvas.create_rectangle(rx1, ry1, rx1 + rwidth, ry1 + rheight, fill="white")  # 흰색 기둥 생성
        root.after(1000, change_color, obstacle)# 1초 후에 색상 변경
        root.after(1100, damage_1, obstacle)
        root.after(1200, damage_1, obstacle)
        root.after(1200, damage_1, obstacle)
        root.after(1300, damage_1, obstacle)
        root.after(1400, damage_1, obstacle)
        root.after(1500, damage_1, obstacle)
        root.after(1600, damage_1, obstacle)
        root.after(1700, damage_1, obstacle)
        root.after(1800, damage_1, obstacle)
        root.after(1900, damage_1, obstacle)
        root.after(2000, remove_obstacle, obstacle)

    def change_color(obstacle):
            canvas.itemconfig(obstacle, fill="red")  # 기둥 색상 변경

    def damage_ (obstacle):
        if canvas.coords(user)[2] >= rx and canvas.coords(user)[0] <= (rx + rwidth) and canvas.coords(user)[3] >= ry and canvas.coords(user)[1] <= (ry + rheight) and canvas.itemcget(obstacle, "fill") == "red":
                    user_health.set(user_health.get() - 1)
                    if user_health.get() == 0:
                       game_over()

    def damage_1 (obstacle):
        if canvas.coords(user)[2] >= rx1 and canvas.coords(user)[0] <= (rx1 + rwidth) and canvas.coords(user)[3] >= ry1 and canvas.coords(user)[1] <= (ry1 + rheight) and canvas.itemcget(obstacle, "fill") == "red":
                    user_health.set(user_health.get() - 1)
                    if user_health.get() == 0:
                       game_over()
                      

    def remove_obstacle(obstacle):
        canvas.delete(obstacle)


    # 게임 오버 처리 함수
    def game_over():
        canvas.unbind("<KeyPress>")  # 키 입력 이벤트 언바인딩
        if monster_health.get() <= 0:
            canvase = Canvas(root, width=400, height=400)
            canvase.pack()
            canvase.create_text(200, 200, text="Win", font=("Arial", 24), fill="green")
            button1 = Button(root, text="메인화면", command=open_main)
            button1.pack()  # 몬스터를 처치한 경우
        else:
            canvase = Canvas(root, width=400, height=400)
            canvase.pack()
            canvase.create_text(200, 200, text="Game Over", font=("Arial", 24), fill="red")
            button1 = Button(root, text="메인화면", command=open_main)
            button1.pack()
            #몬스터에게 패배한 경우

    # 몬스터의 턴 처리 함수
    def monster_turn():
        recover_canvas()
        remove_battleUi()
        # canvas.bind("<KeyPress>", on_key_press)
        count_obstacles(0)  # 총알 여러 개 발사

    # 몬스터의 턴 종료 처리 함수
    def end_monster_turn():
        recover_battleUi()
        remove_canvas()

    def count_obstacles(count):
        if user_health.get() <= 0:
            count = 11
        if count >= 10:
            end_monster_turn()
            if count == 11:
                remove_battleUi()
            return
        
            
        generate_obstacle()
        generate_obstacle1()  
        root.after(2000, lambda: count_obstacles(count + 1))


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
        image = PhotoImage(file="m2.png", master=root)  # 이미지 파일 경로에 맞게 수정
        image = image.subsample(6,6)  # 이미지를 1/2로 축소
        image_label.config(image=image)
        image_label.image = image

    load_image()  # 이미지 로드

    user_turn()  # Start the first turn

    root.mainloop()

if __name__ == "__main__":
    stage2()