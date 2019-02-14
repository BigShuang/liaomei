#usr/bin/env python
#-*- coding:utf-8- -*-

#usr/bin/env python
#-*- coding:utf-8- -*-
import tkinter as tk
import random
import time
import tkinter.font as tkFont # 引入字体模块

# ===常量设置===
# 文字
TITLE="大妹子"
QUES="我喜欢你，有机会吗？"
YES="有"
NO="没有"
YESREPLY="(*/ω\*)"
NOREPLY="..." # 暂不用
# 尺寸
SPACE=100
BUTTONWIDTH=100
BUTTONHEIGHT=50
# 窗口
WINWIDTH=800
WINHEIGHT=600
WINX=400
WINY=100
TOPWIDTH=100
TOPHEIGHT=50
LEFTX=200  # 左边间距
LINEY=200
LINELENGTH=300
LINEWIDTH=4

# 变量
# NO按钮位置
by=360
bx=500
changed=False

# 新建无法直接关闭的TK类
class NewTk(tk.Tk):
    def destroy(self):
        # 点击界面右上角的关闭按钮时，会调用本函数，
        # 覆盖掉了父类的关闭方法，使得界面无法关闭
        pass


# 建立窗口
win=NewTk()
win_loc="{}x{}+{}+{}".format(WINWIDTH,WINHEIGHT,WINX,WINY)
win.geometry(win_loc)
win.title(TITLE)
frame = tk.Frame(win, width=WINWIDTH, height=WINHEIGHT)
frame.pack()

# 字体设置，需要在窗口建立后创建不然会报错
quesft=tkFont.Font(family="微软雅黑",size=20, weight=tkFont.BOLD)
ansft=tkFont.Font(family="微软雅黑",size=20, weight=tkFont.BOLD)

# 问题
q=tk.Label(frame,text=QUES,font=quesft)
q.place(x=LEFTX,y=20)

# 中间线
canvas=tk.Canvas(frame,width=LINEWIDTH)
canvas.place(x=WINWIDTH//2,y=LINEY)
canvas.create_line(0,0,0,LINELENGTH,width=LINEWIDTH*2)
# 按钮
def clickyes():
    top = tk.Toplevel()
    # 设置弹出窗口位置为正中间
    top_x=int(WINX+WINWIDTH/2-TOPWIDTH/2)
    top_y=int(WINY+WINHEIGHT/2-TOPHEIGHT/2)
    top_loc="{}x{}+{}+{}".format(TOPWIDTH,TOPHEIGHT,top_x,top_y)
    top.geometry(top_loc)
    # 添加内容
    tk.Label(top,text = YESREPLY).pack()
    win.update()
    time.sleep(1)
    # 关闭程序
    exit()

b0=tk.Button(frame,text=YES,font=ansft,command=clickyes)
b0.place(x=LEFTX,y=by,width=BUTTONWIDTH,height=BUTTONHEIGHT)

b1=tk.Button(frame,text=NO,font=ansft)
b1.place(x=bx,y=by,width=BUTTONWIDTH,height=BUTTONHEIGHT)

def clickno(event):
    global changed
    if changed:
        b1.place(x=bx,y=by)
        b0.place(x=LEFTX,y=by)
        changed=False
    else:
        b0.place(x=bx,y=by)
        b1.place(x=LEFTX,y=by)
        changed=True


b1.bind("<Motion>",clickno)


def moveMouse(event):
    global changed
    if event.x>WINWIDTH/2 and not changed:
        b0.place(x=bx,y=by)
        b1.place(x=LEFTX,y=by)
        changed=True
    if event.x<WINWIDTH/2 and changed:
        b1.place(x=bx,y=by)
        b0.place(x=LEFTX,y=by)
        changed=False

frame.bind("<Motion>",moveMouse)
win.mainloop()

