#usr/bin/env python
#-*- coding:utf-8- -*-
import tkinter as tk
import random
import time
import tkinter.font as tkFont # 引入字体模块

# ===常量设置===
# 素材——图片
IMGPATH = "../img/001.gif"
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
BUTTONHEIGHT=30
# 窗口
WINWIDTH=800
WINHEIGHT=600
WINX=400
WINY=100
TOPWIDTH=100
TOPHEIGHT=50
LEFTX=180  # 左边间距

# 变量
# NO按钮位置
by=550
bx=500


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
# 图片
photo = tk.PhotoImage(file=IMGPATH)
imgLabel = tk.Label(frame,image=photo)
imgLabel.place(x=LEFTX,y=80)


# 按钮
def clickyes():
    top = tk.Toplevel()
    # 设置弹出窗口位置为正中间
    top_x=int(WINX+WINWIDTH/2-TOPWIDTH/2)
    top_y=int(WINY+WINHEIGHT/2-TOPHEIGHT/2)
    top_loc="{}x{}+{}+{}".format(TOPWIDTH,TOPHEIGHT,top_x,top_y)
    top.geometry(top_loc)
    # 添加内容
    tk.Label(top, text = YESREPLY).pack()
    win.update()
    time.sleep(1)
    # 关闭程序
    exit()

b0=tk.Button(frame,text=YES,font=ansft,command=clickyes)
b0.place(x=LEFTX,y=by,width=BUTTONWIDTH,height=BUTTONHEIGHT)

b1=tk.Button(frame,text=NO,font=ansft)
b1.place(x=bx,y=by,width=BUTTONWIDTH,height=BUTTONHEIGHT)

def clickno(event):
    global bx, by
    bx, by = random.randint(SPACE, WINWIDTH-SPACE), random.randint(SPACE, WINHEIGHT-SPACE)
    b1.place(x=bx,y=by)
    # print(event.x_root,event.y_root)

b1.bind("<Motion>",clickno)
win.mainloop()

