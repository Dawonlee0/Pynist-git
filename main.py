from tkinter import *


# 메인 창 생성
main_window = Tk()
main_window.title("게임")

# 제목 라벨 생성
title_label = Label(main_window, text="게임", font=("Arial", 30))
title_label.pack()

def open_stage_window():
    # 스테이지 선택 창 열기
    main_window.withdraw()  # 메인 창 숨기기
    stage_window = Tk()
    stage_window.title("스테이지 선택")

    # 스테이지 선택 라벨 생성
    stage_label = Label(stage_window, text="스테이지 선택", font=("Arial", 30))
    stage_label.pack()

    # 스테이지 버튼 생성
    button1 = Button(stage_window, text="1번")
    button1.pack(side="left", padx=10, pady=10)
    button2 = Button(stage_window, text="2번")
    button2.pack(side="left", padx=10, pady=10)
    button3 = Button(stage_window, text="3번")
    button3.pack(side="left", padx=10, pady=10)
    button4 = Button(stage_window, text="4번")
    button4.pack(side="left", padx=10, pady=10)

    def back_to_main():
        # 이전으로 돌아가기
        stage_window.destroy()  # 스테이지 선택 창 닫기
        main_window.deiconify()  # 메인 창 다시 보이기

    # 이전으로 돌아가는 버튼 생성
    back_button = Button(stage_window, text="이전", command=back_to_main)
    back_button.pack(pady=10)

def open_story_window():
    # 스토리 설명 창 열기
    main_window.withdraw()  # 메인 창 숨기기
    story_window = Tk()
    story_window.title("스토리 설명")

    # 스토리 설명 라벨 생성
    story_label = Label(story_window, text="스토리 설명", font=("Arial", 30))
    story_label.pack()

    # 스토리 설명 텍스트 입력 공간 생성
    story_text = Text(story_window, width=50, height=10)
    story_text.pack(pady=10)

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

    # 게임 설명 라벨 생성
    desc_label = Label(desc_window, text="게임 설명", font=("Arial", 30))
    desc_label.pack()

    # 게임 설명 텍스트 입력 공간 생성
    desc_text = Text(desc_window, width=50, height=10)
    desc_text.pack(pady=10)
    
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
start_button.pack(side="left", padx=10, pady=10)
story_button.pack(side="left", padx=10, pady=10)
desc_button.pack(side="left", padx=10, pady=10)
quit_button.pack(side="left", padx=10, pady=10)

main_window.mainloop()

# open_main_window()
