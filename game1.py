from tkinter import *
import random
import subprocess

def stage1():
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

    # 총알을 이동시키는 함수
    def move_bullets():
        bullets_to_remove = []  # 삭제할 총알 목록
        for bullet in bullets:
            canvas.move(bullet, bullets[bullet][0], bullets[bullet][1])  # 총알 이동
            bullet_coords = canvas.coords(bullet)  # 총알 좌표 확인

            # 사용자와 총알 충돌 확인
            if bullet_coords[2] >= canvas.coords(user)[0] and bullet_coords[0] <= canvas.coords(user)[2] and bullet_coords[3] >= canvas.coords(user)[1] and bullet_coords[1] <= canvas.coords(user)[3]:
                user_health.set(user_health.get() - 10)  # 사용자 체력 감소
                bullets_to_remove.append(bullet)  # 충돌한 총알 추가
                if user_health.get() == 0:
                    game_over()  # 사용자 체력이 0 이하이면 게임 오버

            # 총알이 화면 밖으로 벗어나면 삭제
            if bullet_coords[3] >= 400:
                bullets_to_remove.append(bullet)  # 범위를 벗어난 총알 추가

        # 삭제할 총알들을 제거하고 새로운 총알 이동을 위해 재귀적으로 호출
        for bullet in bullets_to_remove:
            canvas.delete(bullet)
            bullets.pop(bullet)
        root.after(50, move_bullets)

    # 총알을 발사하는 함수
    def shoot_bullet():
        x = random.randint(0, 380)  # x 좌표 랜덤 생성
        y = 0
        bullet = canvas.create_rectangle(x, y, x + 20, y + 20, fill="red")  # 총알 생성
        bullets[bullet] = (0, 7.5)  # 총알의 이동 속도 설정

    # 게임 오버 처리 함수
    def game_over():
        canvas.unbind("<KeyPress>")  # 키 입력 이벤트 언바인딩
        if monster_health.get() <= 0:
            canvas.create_text(200, 200, text="Win", font=("Arial", 24), fill="green")  # 몬스터를 처치한 경우
        else:
            canvase = Canvas(root, width=400, height=400)
            canvase.pack()
            canvase.create_text(200, 200, text="Game Over", font=("Arial", 24), fill="red")
            button1 = Button(root, text="메인화면", command=open_main)
            button1.pack() # 몬스터에게 패배한 경우

    # 몬스터의 턴 처리 함수
    def monster_turn():
        recover_canvas()
        remove_battleUi()
        # canvas.bind("<KeyPress>", on_key_press)
        shoot_bullets(0)  # 총알 여러 개 발사

    # 몬스터가 총알을 발사하는 함수
    def shoot_bullets(count):
        if user_health.get() <= 0:
            count = 16
        if count >= 15:  # 총알을 10개 발사하면 종료
            end_monster_turn()
            if count == 16:
                remove_battleUi()
            return
        

        shoot_bullet()  # 총알 발사
        root.after(1200, lambda: shoot_bullets(count + 1))  # 2초 간격으로 총알 발사

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


    


    remove_canvas()

    def load_image():
        image = PhotoImage(file="1.png", master=root)  # 이미지 파일 경로에 맞게 수정
        image = image.subsample(4)  # 이미지를 1/2로 축소
        image_label.config(image=image)
        image_label.image = image

    load_image()  # 이미지 로드

    root.after(1000, move_bullets)  # 1초 후에 move_bullets 함수 호출하여 총알 이동

    user_turn()  # Start the first turn

    root.mainloop()

if __name__ == "__main__":
    stage1()

# game2()
