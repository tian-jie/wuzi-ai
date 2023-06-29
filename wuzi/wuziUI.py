from tkinter import *
from wuziplay import WuziPlay

size = 25
gridSize = 20

wuziPlay = WuziPlay(chessBoardSize=size)

isPlaying = False

def paint(player, x, y):
    # 让棋子下在棋盘点上
    x1, y1 = (x*gridSize + gridSize - 10), (y*gridSize + gridSize - 10)
    x2, y2 = (x*gridSize + gridSize + 10), (y*gridSize + gridSize + 10)

    if(player == 0):
        canvas.create_oval(x1, y1, x2, y2, fill="black", tags="oval")
    else:
        canvas.create_oval(x1, y1, x2, y2, fill="white", tags="oval")


def putChess(event):
    global wuziPlay

    print("putChess, isPlaying=", wuziPlay.isPlaying)
    if not wuziPlay.isPlaying:
        return

    x, y = (event.x-gridSize//2) // gridSize, (event.y-gridSize//2) // gridSize

    # 边缘检测
    if x > size-1:
        x = size-1
    if y > size-1:
        y = size-1
    if x < 0:
        x = 0
    if y < 0:
        y = 0

    currentPlayer = wuziPlay.currentPlayer
    res = wuziPlay.putChess(x, y)
    if res != -1:
        paint(currentPlayer, x, y)

    if res == -1:
        return
    elif res == 0:
        showWinInfo(currentPlayer)
        return
    elif res == 1:
        showWinInfo(currentPlayer)
        return
    else:
        pass


def showWinInfo(player):  # 提示窗口
    # global stop
    # tkinter.messagebox.showinfo("", "Game over")
    global isPlaying
    isPlaying = False
    canvas.create_text(250, 250, text="Game over! Player " + str(player) + " WIN!", font=("Arial", 20), fill="red", tags="oval")



def start():
    canvas.delete('oval')
    wuziPlay.start()

top = Tk()
top.title("五子棋")
top.geometry(str(gridSize*size+80)+"x"+str(gridSize*size+110))

canvas = Canvas(top, width=gridSize*size+gridSize,
                height=gridSize*size+gridSize, background="#D3D3D3")
canvas.pack(expand=YES, fill=BOTH)
canvas.bind("<Button-1>", putChess)  # 每次点击鼠标左键（事件）,触发paint函数

# 画棋盘
for num in range(1, size+1):
    canvas.create_line(num*gridSize, gridSize,
                       num*gridSize, gridSize*size,
                       width=2)
    canvas.create_line(gridSize, num*gridSize,
                       gridSize*size, num*gridSize,
                       width=2)


buttonStart = Button(top, text="Start", command=start)
buttonStart.pack()

start()

top.mainloop()
