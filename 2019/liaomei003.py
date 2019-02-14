#usr/bin/env python
#-*- coding:utf-8- -*-
import tkinter as tk
import random
import time
import tkinter.font as tkFont # 引入字体模块


# ===常量设置===
# 素材——图片
IMGPATH="img/003.gif"
# 文字
TITLE="小朋友问我："
QUES="大爽哥哥，你到底有几个铝朋友啊？"
# 尺寸
SPACE=100
BUTTONWIDTH=120
BUTTONHEIGHT=40
# 窗口
WINWIDTH=800
WINHEIGHT=600
WINX=400
WINY=100
TOPWIDTH=400
TOPHEIGHT=400
LEFTX=100  # 左边间距
BUTTONDICT={
    "100个":{
        "reply":0,
        "x":100,
        "y":200
    },
    "10个":{
        "reply":0,
        "x":340,
        "y":200
    },
    "1个":{
        "reply":0,
        "x":580,
        "y":200
    },
    "0个":{
        "reply":1,
        "x":100,
        "y":400
    },
    "None":{
        "reply":1,
        "x":340,
        "y":400
    },
    "undefined":{
        "reply":1,
        "x":580,
        "y":400
    },
}


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
q.place(x=LEFTX,y=50)

# 按钮
def clickyes():
    top = tk.Toplevel()
    # 设置弹出窗口位置为正中间
    top_x=int(WINX+WINWIDTH/2-TOPWIDTH/2)
    top_y=int(WINY+WINHEIGHT/2-TOPHEIGHT/2)
    top_loc="{}x{}+{}+{}".format(TOPWIDTH,TOPHEIGHT,top_x,top_y)
    top.title("")
    top.geometry(top_loc)
    # 添加内容
    photo = tk.PhotoImage(file=IMGPATH)
    tk.Label(top,image=photo).pack()
    win.update()
    time.sleep(1)
    # 关闭程序
    exit()


def clickno(event):
    global bx,by
    bx, by = random.randint(SPACE, WINWIDTH-SPACE), random.randint(SPACE, WINHEIGHT-SPACE)
    event.widget.place(x=bx,y=by)
    # print(event.x_root,event.y_root)


for name in BUTTONDICT:
    if BUTTONDICT[name]['reply']==1:
        tk.Button(frame,text=name,font=ansft,command=clickyes).place(x=BUTTONDICT[name]['x'],y=BUTTONDICT[name]['y'],width=BUTTONWIDTH,height=BUTTONHEIGHT)
    else:
        b=tk.Button(frame,text=name,font=ansft)
        b.place(x=BUTTONDICT[name]['x'],y=BUTTONDICT[name]['y'],width=BUTTONWIDTH,height=BUTTONHEIGHT)
        b.bind("<Motion>",clickno)

win.mainloop()
