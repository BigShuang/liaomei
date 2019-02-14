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
BUTTONPADX=10
BUTTONPADY=5
BUTTONWIDTH=100
BUTTONHEIGHT=50
# 窗口
WINWIDTH=800
WINHEIGHT=600
WINX=400
WINY=100
TOPWIDTH=100
TOPHEIGHT=50
LEFTX=100  # 左边间距
BUTTONY=200
RNUM=4
CNUM=6

xi,yi=0,1
xj,yj=CNUM-1,1
# 变量
# NO按钮位置
button_list=[
    [None for j in range(CNUM)] for i in range(RNUM)
]


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
b0.place(x=xi*BUTTONWIDTH+LEFTX,y=yi*BUTTONHEIGHT+BUTTONY,width=BUTTONWIDTH-BUTTONPADX,height=BUTTONHEIGHT-BUTTONPADY)
button_list[yi][xi]=b0

b1=tk.Button(frame,text=NO,font=ansft)
b1.place(x=xj*BUTTONWIDTH+LEFTX,y=yj*BUTTONHEIGHT+BUTTONY,width=BUTTONWIDTH-BUTTONPADX,height=BUTTONHEIGHT-BUTTONPADY)
button_list[yj][xj]=b1

inclick=False
count=1
def clickno(event):
    global xj,yj,inclick
    global count
    count+=1
    if inclick:
        return
    print(event.x,event.y)
    print(count)
    inclick=True
    blank_button_num=0
    blank_button_xy=[]
    for y in range(RNUM):
        for x in range(CNUM):
            if button_list[y][x] is None:
                blank_button_num+=1
                blank_button_xy.append((x,y))
    if blank_button_num>0:
        bi=random.randint(0, blank_button_num-1)
        newxj,newyj = blank_button_xy[bi]
        b=tk.Button(frame,text=YES,font=ansft,command=clickyes)
        b.place(x=xj*BUTTONWIDTH+LEFTX,y=yj*BUTTONHEIGHT+BUTTONY,width=BUTTONWIDTH-BUTTONPADX,height=BUTTONHEIGHT-BUTTONPADY)
        button_list[yj][xj]=b
        b1.place(x=newxj*BUTTONWIDTH+LEFTX,y=newyj*BUTTONHEIGHT+BUTTONY)
        button_list[newyj][newxj]=b1
    else:
        newxj,newyj = random.randint(0, CNUM-1), random.randint(0, RNUM-1)
        b1.place(x=newxj*BUTTONWIDTH+LEFTX,y=newyj*BUTTONHEIGHT+BUTTONY)
        button_list[newyj][newxj].place(x=xj*BUTTONWIDTH+LEFTX,y=yj*BUTTONHEIGHT+BUTTONY)
        button_list[yj][xj]=button_list[newyj][newxj]
        button_list[newyj][newxj]=b1
    xj,yj=newxj,newyj
    inclick=False



b1.bind("<Motion>",clickno)
win.mainloop()

