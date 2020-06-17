from tkinter import *
from tkinter improt messagebox


## 함수 선언 부분 ##
def bodymenu():
    button1 = Button(window, text="상 하체 모두 뚱뚱한 체형", command=)
    button2 = Button(window, text="상체 비만")
    button3 = Button(window, text="하체 비만")
    button4 = Button(window, text="하체 비만")
    button5 = Button(window, text="마른 체형")
    button6 = Button(window, text="잘 모르겠음", command=BMIcalc)


def BMIcalc():
    heightsize = askinteger("키", "키를 입력하세요 (단위는 cm)", minvalue=0, maxvalue=200)
    kgsize = askinteger("몸무게", "몸무게를 입력하세요 (단위는 kg)", minvale=0, maxvalue=200)
    sexbutton1 = Button(window, text="여성")
    sexbutton2 = Button(window, text="남성")


def placemenu():
    button1 = Button(window, text="학교", command=)
    button2 = Button(window, text="회사")
    button3 = Button(window, text="결혼식")


def jobmenu():
    button1 = Button(window, text="학생", command=)
    button2 = Button(window, text="교수")
    button3 = Button(window, text="회사원")


def weathermenu():
    button1 = Button(window, text="비", command=)
    button2 = Button(window, text="바람 많음")
    button3 = Button(window, text="해 쨍쨍")
    button4 = Button(window, text="오늘의 날씨 알아보기")


def colormenu():
    button1 = Button(window, text="red", command=)
    button2 = Button(window, text="black")
    button3 = Button(window, text="white")


window = Tk()
maiMenu = Menu(window)
window.config(menu=mainMenu)
window.title("P, W, C를 입다")

fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label="실행 및 종료", menu=fileMenu)
fileMenu.add_command(label="실행", command=)
fileMenu.add_separator()
fileMenu.add_command(label="종료", command=quit)

fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label="원하는 시스템 고르기", menu=fileMenu)
fileMenu.add_command(label="체형", command=bodymenu)
fileMenu.add_separator()
fileMenu.add_command(label="장소", command=placemenu)
fileMenu.add_separator()
fileMenu.add_command(label="직업", command=jobmenu)
fileMenu.add_separator()
fileMenu.add_command(label="날씨", command=weathermenu)
fileMenu.add_separator()
fileMenu.add_command(label="색상", command=coloarmenu)

window.mainloop()
