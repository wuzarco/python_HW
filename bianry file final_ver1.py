import tkinter as tk
from tkinter import filedialog
import tkinter.messagebox
from tkinter import scrolledtext#使用滾動條功能要import
import binascii
import os
import re
#美化版本  20191128
num='AAAAAAAAAA'
print(num)
num2= re.sub(r"(?<=\w)(?=(?:\w\w)+$)", " ", num)
print(num2)

# from tkinter.filedialog import asksaveasfile


def insert_txt():
    text_block.delete('1.0', 'end')
    database = open(path, "rb")
    var = database.read().hex()
    text_block.insert('insert', var)

# def savefunction():
#     savebolck = inputblock.get()
#     print(savebolck)
#     print(path)
#     # savebolck.save(path)
def savefunction():
    open_file1 = open('register.txt', "w+")  #開啟暫存文件檔, 將文字檔丟入.
    open_file2 = text_block.get("1.0",'end-1c')
    # print(open_file2)    #驗證用
    open_file1.write(open_file2)
    open_file1.close()
    # 將ascii檔存成bianry
    getdata= text_block.get("1.0",'end-1c')
    txtfile = path
    # print(f)
    with open('register.txt') as getdata, open(txtfile, 'rb+') as getdataout:
        for line in getdata:
            getdataout.write(
                binascii.unhexlify(''.join(line.split()))
            )
    os.remove('register.txt')


def comparefunction():   #目前無法使用
    text_block.delete('1.0','end')
    findname = inputblock.get()
    txtfile = open(path,"rb")
    for line in txtfile:
        inputcheck = line.find(findname)
        if inputcheck != -1:
            input = line
            text_block.insert('insert', input)
            # print(inputcheck)
            break
    else:
        # print('inputcheck') 檢查用
        tk.messagebox.showinfo('提示', '找不到此關鍵字')
    # if not inputcheck :
    #     print('inputcheck')
                # tk.messagebox.showinfo('提示', '找不到')
        # elif len(line) == 0:
        # elif inputcheck == -1 :
        #     print(inputcheck)
        #     tk.messagebox.showinfo('提示', '找不到')
            # break
# def searchfuction():
#     text_block.delete('1.0','end')
#     findname = inputblock.get()
#     txtfile = open(path,"r")
#     for line in txtfile:
#         RSODcheck = line.find(findname)
#         if RSODcheck != -1:
#             RSOD = line.split(" ")[4]
#             text_block.insert('insert', RSOD)

def openfilefun():
    text_block.delete('1.0', 'end')
    window = tk.Tk()
    window.withdraw()
    file_path = filedialog.askopenfilename()
    global path
    path= file_path
    open_file = open(file_path, "rb+")
    for i in range(5):
        text_block.insert('insert', open_file.readline().hex())
    getdata= text_block.get("1.0",'end-1c')
    getdata=re.sub(r"(?<=\w)(?=(?:\w\w)+$)", " ", getdata)
    print(getdata)
    text_block.delete('1.0', 'end')
    text_block.insert('insert', getdata.upper())
    open_file.close()

# def hex1button():
#     # AAA = inputblock.get()
#     insert = hex(1)
#     inputblock.insert('insert', insert)

def quit():
    quit = tk.messagebox.askokcancel('提示', '關閉程式？')
    if quit == True:
        window.destroy()

#視窗設定
window = tk.Tk()
window.title('search function')
window.geometry('600x450')
#練習用place配置位置
tk.Label(window, text='search function(please insert key word. ex:s00)', font=('Arial',10), ).place(x=0, y=30, anchor='nw')
#輸入欄
inputblock = tk.Entry(window, show = None)
inputblock.place(x=5, y=50, anchor='nw')

result_label =tk.Label(window, bg= 'white',text='00　01 CC',font=('Monofonto',9)).place(x=1, y=115, anchor='nw')
openfile_illustrate_label =tk.Label(window, text='打開指定檔並顯示前五行').place(x=65, y=3, anchor='nw')
# text_block = tk.Text(window, height=5)   #陽春版視窗
text_block = scrolledtext.ScrolledText(window,width=47,height=20,wrap=tk.WORD)#wrap=tk.WORD  滾動條文件視窗
text_block.place(x=3, y=140, anchor='nw')
#按鈕配置
show_all_text_button =tk.Button(window, text='顯示全部內容', command=insert_txt).place(x=5, y=415, anchor='nw')
# show_line_button =tk.Button(window, text='compare', command=comparefunction).place(x=5, y=75, anchor='nw')
# tk.Button(window, text='search', command=searchfuction).place(x=5, y=71, anchor='nw')
openfile_button =tk.Button(window, text='open file', command=openfilefun).place(x=0, y=0, anchor='nw')
save_button =tk.Button(window, text='save', command= savefunction).place(x=95, y=415, anchor='nw')
# hex1 =tk.Button(window, text='1', command= hex1button ).place(x=135, y=415, anchor='nw')
quit_button = tk.Button(window, text='退出', command=quit)
quit_button.pack(side=tk.BOTTOM)



window.mainloop()
#函式放上面
# ######
# 筆記
# def savefunction():
#     open_file1 = open('test1.txt', "r+")
#     open_file2 = text_block.get("1.0",'end-1c')
#     print(open_file2)
#     open_file1.write(open_file2)  #想辦法存到另一個檔案
#     open_file1.close()
#
#     # 將ascii檔存成bianry
#     f= text_block.get("1.0",'end-1c')
#     txtfile = path
#     with open('test1.txt') as getdata, open(txtfile, 'rb+') as fout:
#         for line in f:
#             fout.write(
#                 binascii.unhexlify(''.join(line.split()))
#             )     #f為可任意更改變數