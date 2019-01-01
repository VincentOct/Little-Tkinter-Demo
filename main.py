from tkinter import *
from tkinter import messagebox
from random import *
from copy import deepcopy
from all_results import *  # 需要现实的所有可能结果已经保存在了 all_results.py 中，这里直接 import 进来

all_results = tuple(all_results)
root = Tk()
root.title('Eightqueens Visualization')
root.resizable(0, 0)


# Set frame 框架
f_1 = LabelFrame(root, text='Select Model', width=450, height=70, labelanchor='nw')
f_1.pack(fill='both')
f_2 = LabelFrame(root, text='Result', width=450, height=400, labelanchor='nw')
f_2.pack(fill='both')
f_3 = LabelFrame(root, text='Notes', labelanchor='nw')
f_3.pack(fill='both')


# Set Button&Entry 按钮&输入框
# 初始化两个变量，一个整形，一个字符串。继承自 tkinter 内置的类。

var_entry = IntVar()
bottom_text = StringVar()


# Func 函数部分

def painting(blueprint):  # 绘制函数， blueprint 应该是一个包含了8*8的元素的列表
    for i in range(8):
        for j in range(8):
            if blueprint[i][j] == 0:
                chessboard.create_image(j * 50, i * 50, anchor='nw',
                                        image=image_white_bg)
            elif blueprint[i][j] == 1:
                chessboard.create_image(j * 50, i * 50, anchor='nw',
                                        image=image_black_bg)
            elif blueprint[i][j] == 2:
                chessboard.create_image(j * 50, i * 50, anchor='nw',
                                        image=image_white_queen)
            else:
                chessboard.create_image(j * 50, i * 50, anchor='nw',
                                        image=image_black_queen)
    chessboard.addtag_all('item')


def flush():  # 刷新界面函数
    chessboard.delete('item')
    painting(board_inti)
    print('Flushed Successfully.')
    bottom_text.set('Waiting for a command.')
    Label_1.config(text=bottom_text.get())


def get_random_result():  # 抽取随机结果函数
    chessboard.delete('item')
    num = randrange(0, 92)
    bottom_text.set('Solution No.' + str(num + 1))
    Label_1.config(text=bottom_text.get())
    random_result = all_results[num]  # 从所有结果中随机取出一个
    random_blueprint = deepcopy(board_inti)
    for i in range(8):
        if random_blueprint[i][random_result[i]] == 0:
            var = 2
        else:
            var = 3
        random_blueprint[i][random_result[i]] = var
    painting(random_blueprint)
    print('Have displayed a random result Successfully.')


def get_specific_result():  # 获取特定解函数
    num = var_entry.get()
    if (num > 92) or (num < 1):
        messagebox.showerror(title='Error',
                             message='The number must between 1 and 92.')
    else:
        bottom_text.set('Solution No.' + str(num))
        Label_1.config(text=bottom_text.get())
        specific_result = all_results[num - 1]
        specific_blueprint = deepcopy(board_inti)
        for i in range(8):
            if specific_blueprint[i][specific_result[i]] == 0:
                var = 2
            else:
                var = 3
            specific_blueprint[i][specific_result[i]] = var
        painting(specific_blueprint)
        print('Got specific result Successfully.')


# 部署按钮到面板

btn_1 = Button(f_1, text='Get a random result', command=get_random_result, width=20, )
btn_1.place(x=30, y=8, anchor='nw')
btn_2 = Button(f_1, text='Set a number:', command=get_specific_result, width=13, )
btn_2.place(x=205, y=8, anchor='nw')
btn_3 = Button(f_1, text='Flush', command=flush, )
btn_3.place(x=375, y=8, anchor='nw')
entry_1 = Entry(f_1, textvariable=var_entry, width=5, )
entry_1.place(x=310, y=13, anchor='nw')
Label_1 = Label(f_3, text='Waiting for a command.')
Label_1.pack()

# Set Canvas 画布设置

chessboard = Canvas(f_2, height=400, width=400, relief=FLAT)

image_black_queen = PhotoImage(file=r'images\black_queen.gif')
image_white_queen = PhotoImage(file=r'images\white_queen.gif')
image_black_bg = PhotoImage(file=r'images\black_bg.gif')
image_white_bg = PhotoImage(file=r'images\white_bg.gif')

chessboard.pack()
painting(board_inti)


# 主循环

root.mainloop()
