# -*- coding: utf-8 -*-
from tkinter import *
# from GatewayControl_CodeGenerator import *
# from DeviceControl_CodeGenerator import *
from Demo_CodeGenerator import BuildCode_Dev

def GWMsg():
     txt.delete(1.0,END)
     Input = str(inputData.get(1.0,END))
     
    #  Cmd_Gw = BuildCode_GW(Input)
    #  CodeRst = Cmd_Gw.Generate()
    #  s = 'Code_GW.txt Generate Success:\n\n'
    #  txt.insert(END, s)
    #  txt.insert(END, CodeRst) 
     #inputData.delete(0.0, END)  

def DevMsg():
     txt.delete(1.0,END)
     Input = str(inputData.get(1.0,END))
     
     Cmd_Dev = BuildCode_Dev(Input)
     CodeRst = Cmd_Dev.Generate()
     s = 'Code_Dev.txt Generate Success:\n\n'
     txt.insert(END, s)
     txt.insert(END, CodeRst) 
     #inputData.delete(0.0, END)     

def clearContent():
     inputData.delete(1.0, END)  
     txt.delete(1.0,END)


root = Tk()
root.geometry('1000x600')
root.title(' Code Generator')
root.config(bg='#f0ffff')

#Lable
intro = Label(root,text='请在左侧输入消息/命令名字, 然后选择相应按钮生成代码',\
                       bg='#d3fbfb',\
                       fg='red',\
                       font=('华文新魏',11),\
                       width=20,\
                       height=2,\
                       relief=RIDGE)

intro.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.1)

#Input
inputData = Text(root, font = ('',14))
inputData.place(relx=0.1, rely=0.2, relwidth=0.3, relheight=0.6)

#Output
txt = Text(root, font = ('',9))
txt.place(relx=0.6, rely=0.2, relwidth=0.3, relheight=0.6)

#Button 
bt_json2bin = Button(root, text='**Demo Control', command=GWMsg, fg ='blue')
bt_json2bin.place(relx=0.4, rely=0.25, relwidth=0.2, relheight=0.1)

bt_bin2json = Button(root, text='**Demo Control', command=DevMsg, fg ='blue')
bt_bin2json.place(relx=0.4, rely=0.45, relwidth=0.2, relheight=0.1)

bt_clear = Button(root, text='Clear', command=clearContent, fg ='blue')
bt_clear.place(relx=0.4, rely=0.65, relwidth=0.2, relheight=0.1) 

intro = Label(root,text='产生的完整代码在 Code_GW.txt或Code_Dev.txt中(当前目录 ), 问题联系人：Howard',\
                       bg='#d3fbfb',\
                       fg='red',\
                       font=('华文新魏',11),\
                       width=20,\
                       height=2,\
                       relief=RIDGE)

intro.place(relx=0.1, rely=0.8, relwidth=0.8, relheight=0.1)

root.mainloop()