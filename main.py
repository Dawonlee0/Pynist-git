from tkinter import *

# 게임 설명 창 열기
def open_desc_window():
    global desc_window
    
    if desc_window:
        desc_window.lift()
        return

    desc_window = Toplevel()
    desc_window.title("게임 설명")

    desc_label = Label(desc_window, text="게임 설명", font=("Arial", 24))
    desc_label.pack(pady=20)

    desc_text = Text(desc_window, width=50, height=10)
    desc_text.pack(padx=20, pady=20)

    desc_text.insert(END, "게임 설명을 입력하세요.")

    desc_window.mainloop()

# 윈도우 생성
window = Tk()
window.title("게임 제목")

# 제목 라벨 생성
title_label = Label(window, text="게임 제목", font=("Arial", 24))
title_label.pack(pady=20)

# 게임 설명 창 생성
desc_window = None

# 버튼 3개 생성
start_button = Button(window, text="게임 시작")
story_button = Button(window, text="스토리 설명")
desc_button = Button(window, text="게임 설명", command=open_desc_window)
quit_button = Button(window, text="끝내기", command=window.destroy)

# 버튼 일자로 배치
start_button.pack(side=LEFT, padx=10, pady=10)
story_button.pack(side=LEFT, padx=10, pady=10)
desc_button.pack(side=LEFT, padx=10, pady=10)
quit_button.pack(side=LEFT, padx=10, pady=10)

# 윈도우 실행
window.mainloop()
