# _*_ coding:utf-8 _*_  https://blog.csdn.net/weixin_49892805/article/details/134362100
# @Time    : 2022/11/17 11:50
# @Author  : ice_Seattle
# @File    : RC接口.py
# @Software: PyCharm
# 公司需要在表单字段中调用其它数据库数据,需要使用ajax脚本接口调取

# 对此,每次修改对应的数据并一一核对,程序容易出错,也比较麻烦,费时间

# 因此,对于这种偏重复的工作我写了一个程序:“用代码写代码”

import ctypes, time
from tkinter import *
import tkinter as tk
import tkinter.messagebox
import tkinter.filedialog
import pandas as pd
from tkinter import scrolledtext
# import win32api
# import win32con


def get_all():pass
    # win32api.keybd_event(17, 0, 0, 0)  # ctrl键位码是17
    # win32api.keybd_event(65, 0, 0, 0)  # c键位码是65
    # win32api.keybd_event(65, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放按键
    # win32api.keybd_event(17, 0, win32con.KEYEVENTF_KEYUP, 0)


def get_copy():pass
    # win32api.keybd_event(17, 0, 0, 0)  # ctrl键位码是17
    # win32api.keybd_event(67, 0, 0, 0)  # c键位码是67
    # win32api.keybd_event(67, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放按键
    # win32api.keybd_event(17, 0, win32con.KEYEVENTF_KEYUP, 0)


field_sync_l = []
field_sync_r = []


# 选择文件安放的位置
def get_file():
    # filedialog.askopenfilenames可以返回多个文件名
    data_1 = tkinter.filedialog.askopenfilename(title="选择文件")
    data = data_1
    print('路径为:', data)
    x = pd.read_excel(data)
    for o in range(0, len(x.columns)):
        field_sync_l.append(x.loc[0][o])

    # print(x.loc[0][1])
    print(field_sync_l)
    for o in range(0, len(x.columns)):
        field_sync_r.append(x.loc[1][o])
    print(field_sync_r)
    entry.delete(0, END)
    entry.insert(0, data)


# GUI界面
ctypes.windll.shcore.SetProcessDpiAwareness(1)
ScaleFactor = ctypes.windll.shcore.GetScaleFactorForDevice(0)
window = tk.Tk()
window.title("RC_ajax代码转换器")
window.tk.call('tk', 'scaling', ScaleFactor/75)
width = 800
height = 450
window.geometry(f'{width}x{height}')
# 计算中心坐标点
screen_width = window.winfo_screenwidth() / 2 - width / 2
screen_height = window.winfo_screenheight() / 2 - height / 2
window.geometry(f"+{int(screen_width)}+{int(screen_height)}")
window.config(bg="#FAFAFA")       # bg="#000000"
window.tk.call('tk', 'scaling', ScaleFactor/75)
# 设置窗口是否可以变化长宽,默认可变
window.resizable(width=False, height=False)
lb = Label(window, text="Excal文件位置:", font=('微软雅黑', 12), fg='black', bg="#FAFAFA")
lb.place(x=12, y=56)
lb_1 = Label(window, text="代码:", font=('微软雅黑', 12), fg='black', bg="#FAFAFA")
lb_1.place(x=20, y=106)
entry = Entry(window, font=('微软雅黑', 12), width=30, bg='white')
entry.place(x=150, y=60)


code_ares = scrolledtext.ScrolledText(window, width=100, height=10)
code_ares.place(x=15, y=150, width=750, height=250)


def in_data():
    fun = 'GetDataTableBySql?'
    API = '/RunVser/'
    TABLE_L = field_sync_l[0]  # 使用表
    TABLE_R = field_sync_r[0]  # 来源表
    field_invoke = 'xingming'
    field_invoke = field_invoke.upper()
    field_source = 'xingming'
    # field_sync_l = ['xingming'], ['gonghao']
    # field_sync_r = ['Xingming'], ['gonghao']
    sql = f"select top 1 * from {TABLE_R} where {field_source}=\\''"
    a = """this.ajax.post('{API}{fun}sql={sql}+this.formData["{TABLE_L}-{field_invoke}"]""" \
        .format(API=API, fun=fun, sql=sql, TABLE_L=TABLE_L, field_invoke=field_invoke, TABLE_R=TABLE_R)
    b = """+'\\'').then((data) => { """
    c = """  if (data.success) {
        console.log(data.data);
        let json = data.data;"""
    d = ['']
    for i in range(0, len(field_sync_l) - 1):
        d.append('')
        # print(d)
    for i in range(1, len(field_sync_l) - 1):
        d[
            i] = f"""    this.$set(this.formData, "{TABLE_L}-{''.join(map(str, field_sync_l[i])).upper()}", json.{''.join(map(str, field_sync_r[i])).lower()});"""
        x = '\n'.join(map(str, d))
    e = """  } else {
        alert(data.msg);
        }
    }).catch((e) => {
        console.log(e);
    });"""
    m = f'{a}\n{b}\n{c}\n{x}\n{e}'
    code_ares.insert(INSERT, m)
    print(m)


def clear_content():
    code_ares.delete('1.0', END)


# 选择路径按钮
btn_select = Button(
    window, text="...", font=("华文彩云", 10),
    bg='Snow', activeforeground='pink', activebackground='black',
    fg="black", command=get_file
)
btn_select.place(x=480, y=60, width=35)
btn_select = Button(
    window, text="确认", font=("华文彩云", 10),
    bg='Snow', activeforeground='pink', activebackground='black',
    fg="black", command=lambda: in_data()
)
btn_select.place(x=520, y=60, width=120)
# 清空按钮
btn_select = Button(
    window, text="清空", font=("华文彩云", 10),
    bg='Snow', activeforeground='pink', activebackground='black',
    fg="black", command=lambda: clear_content()
)
btn_select.place(x=650, y=60, width=120)
# 全选按钮
btn_all = Button(
    window, text="全选", font=("华文彩云", 12),
    bg='Snow', activeforeground='pink', activebackground='black',
    fg="black", command=get_all
)
btn_all.place(x=525, y=400, width=120)
# 复制按钮
btn_copy = Button(
    window, text="复制", font=("华文彩云", 12),
    bg='Snow', activeforeground='pink', activebackground='black',
    fg="black", command=get_copy
)
btn_copy.place(x=645, y=400, width=120)


def get_time():
    # 获取当前时间
    dstr.set(time.strftime("%H:%M:%S"))
    # 每隔 1s 调用一次 get_time()函数来获取时间
    window.after(1000, get_time)


dstr = tk.StringVar()  # 生成动态字符串
# 利用 textvariable 来实现文本变化
lb_t = tk.Label(window, textvariable=dstr, bg='white', fg='green', font=("微软雅黑", 10))
lb_t.pack(side="top")
# 调用生成时间的函数
get_time()



# 显示窗口
window.mainloop()


# field_sync_l = [[x] for x in field_sync_l]
# field_sync_r = [[x] for x in field_sync_r]
# # field_sync_l = sum(field_sync_l, [])
# print(field_sync_l)


# """


