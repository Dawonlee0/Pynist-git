from tkinter import *
from game1 import stage1
from game2 import stage2
from game3 import stage3

# 메인 창 생성

main_window = Tk()
scw = main_window.winfo_screenwidth()
sch = main_window.winfo_screenheight()
x = (scw - 800)/2
y = (sch - 450)/2
main_window.title("게임")
main_window.geometry('%dx%d+%d+%d' % (800, 450, x, y))

# 제목 라벨 생성
title_label = Label(main_window, text="게임", font=("Arial", 30))
title_label.pack()

def open_stage_window():
    global stage_window
    # 스테이지 선택 창 열기
    main_window.withdraw()  # 메인 창 숨기기
    stage_window = Tk()
    stage_window.title("스테이지 선택")
    stage_window.geometry('%dx%d+%d+%d' % (800, 450, x, y))

    # 스테이지 선택 라벨 생성
    stage_label = Label(stage_window, text="스테이지 선택", font=("Arial", 30))
    stage_label.pack()


    button1 = Button(stage_window, text="약초1", command=stage1)
    button1.pack(side="left", padx=30, pady=10)
    button2 = Button(stage_window, text="약초2", command=stage2)
    button2.pack(side="left", padx=30, pady=10)
    button3 = Button(stage_window, text="약초3", command=stage3)
    button3.pack(side="left", padx=30, pady=10)
    button4 = Button(stage_window, text="약초4")
    button4.pack(side="left", padx=30, pady=10)
    
    def back_to_main():
        # 이전으로 돌아가기
        stage_window.destroy()  # 스테이지 선택 창 닫기
        main_window.deiconify()  # 메인 창 다시 보이기

    # 이전으로 돌아가는 버튼 생성
    back_button = Button(stage_window, text="이전", command=back_to_main)
    back_button.pack(side="left", padx=30)

def open_story_window():
    # 스토리 설명 창 열기
    main_window.withdraw()  # 메인 창 숨기기
    story_window = Tk()
    story_window.title("스토리 설명")
    story_window.geometry('%dx%d+%d+%d' % (800, 450, x, y))

    # 스토리 설명 라벨 생성
    story_label = Label(story_window, text="스토리 설명", font=("Arial", 30))
    story_label.pack()

    # 스토리 설명 텍스트 입력 공간 생성
    story_text = Text(story_window, width=50, height=10)
    story_text.pack(pady=10)
    story_text.insert("3.0", "어느 마을을 지켜주는 세계수가 어둠의 힘에 의해 병에 걸리게 되었다.\n주인공은 우연히 특정 약초들을 모아서 약을 만들면 세계수를 치료할 수 있다는 소식을 들었지만 재료가 되는 약초들도 어둠의 힘에 의해서 공격성을 가진\n몬스터가 되어버렸는데...\n주인공은 위험을 무릅쓰고 세계수를 치료해 마을을\n구하기 위해 몬스터가 된 약초를 제압하고 재료를\n수집하기 위해서 떠난다")  # 초기 내용 입력
    
    def back_to_main():
        # 이전으로 돌아가기
        story_window.destroy()  # 스토리 설명 창 닫기
        main_window.deiconify()  # 메인 창 다시 보이기

    # 이전으로 돌아가는 버튼 생성
    back_button = Button(story_window, text="이전", command=back_to_main)
    back_button.pack(pady=10)

def open_desc_window():
    # 게임 설명 창 열기
    main_window.withdraw()  # 메인 창 숨기기
    desc_window = Tk()
    desc_window.title("게임 설명")
    desc_window.geometry('%dx%d+%d+%d' % (800, 450, x, y))

    # 게임 설명 라벨 생성
    desc_label = Label(desc_window, text="게임 설명", font=("Arial", 30))
    desc_label.pack()

    # 게임 설명 텍스트 입력 공간 생성
    desc_text = Text(desc_window, width=50, height=10)
    desc_text.pack(pady=10)
    desc_text.insert("1.0", "attack - 몬스터를 공격해 피해를 줍니다.\nheal - 플레이어가 체력을 회복합니다.\n방향키 - 이동\n몬스터의 턴에 공격을 피하지 못하면 플레이어가 피해를 입습니다.")  # 초기 내용 입력
    
    # 이전으로 돌아가기
    def back_to_main():
        desc_window.destroy()  # 게임 설명 창 닫기
        main_window.deiconify()  # 메인 창 다시 보이기

    # 이전으로 돌아가는 버튼 생성
    back_button = Button(desc_window, text="이전", command=back_to_main)
    back_button.pack(pady=10)

# 버튼 생성
start_button = Button(main_window, text="게임 시작", command=open_stage_window)
story_button = Button(main_window, text="스토리 설명", command=open_story_window)
desc_button = Button(main_window, text="게임 설명", command=open_desc_window)
quit_button = Button(main_window, text="끝내기", command=main_window.destroy)

# 버튼 일자로 배치
quit_button.pack(side="bottom", padx=10, pady=10)
desc_button.pack(side="bottom", padx=10, pady=10)
story_button.pack(side="bottom", padx=10, pady=10)
start_button.pack(side="bottom", padx=10, pady=10)

main_window.mainloop()

