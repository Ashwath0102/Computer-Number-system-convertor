import tkinter as tk
from functools import partial
import time
import random
timeleft = 6
tl=2
tempVal = "Decimal"
    # getting drop down value
def store_temp(sel_temp):
    global tempVal
    tempVal = sel_temp
#converting give code into decimal
def conv(n,D):
    num = n
    dec_value = 0
    base = 1
    temp = num
    while (temp):
        # Extracting last digit
        last_digit = temp % 10
        temp = int(temp / 10)
        dec_value += last_digit * base
        base = base * D
    return dec_value
    # the main conversion
def call_convert(rlabel1, rlabe12,rlabe13,timeLabel,inputn):
    timeLabel.config(text="RESULTS",font=('Helvetica', 14,'bold'))
    tem = inputn.get()
    tem=float(tem)
    if tempVal == 'Decimal':
        b= bin(int(tem))
        o=oct(int(tem))
        h=hex(int(tem))
        rlabel1.config(text="Binary= "+str(b),font=('Helvetica', 11,'bold'))
        rlabe12.config(text="Octal= "+str(o),font=('Helvetica', 11,'bold'))
        rlabe13.config(text=" Hexadecimal= "+str(h),font=('Helvetica', 11,'bold'))
    if tempVal == 'Binary':
        de=conv(tem,2)
        o = oct(int(de))
        h = hex(int(de))
        rlabel1.config(text="Decimal= "+str(de),font=('Helvetica', 11,'bold'))
        rlabe12.config(text="Octal= "+str(o),font=('Helvetica', 11,'bold'))
        rlabe13.config(text=" Hexadecimal= "+str(h),font=('Helvetica', 11,'bold'))
    if tempVal == 'octal':
        de = conv(tem,8)
        b = bin(int(de))
        h = hex(int(de))
        rlabel1.config(text="Binary= "+str(b),font=('Helvetica', 11,'bold'))
        rlabe12.config(text="Decimal= "+str(de),font=('Helvetica', 11,'bold'))
        rlabe13.config(text=" Hexadecimal= "+str(h),font=('Helvetica', 11,'bold'))
    if tempVal == 'Hexadecimal':
        de = conv(tem, 16)
        b = bin(int(de))
        o = oct(int(de))
        rlabel1.config(text="Binary= "+str(b),font=('Helvetica', 11,'bold'))
        rlabe12.config(text="Octal= "+str(o),font=('Helvetica', 11,'bold'))
        rlabe13.config(text="Decimal= "+str(de),font=('Helvetica', 11,'bold'))
    return
# app window configuration and UI
global c
c=["goldenrod"]
i=0
root = tk.Tk()
root.geometry('400x310+100+200')
root.title('Coded Information Converter')
root.configure(background=c[i])
root.resizable(width=False, height=False)
root.grid_columnconfigure(1, weight=1)
global label_info
label_info=tk.Label(root)
label_info = tk.Label(root, font = ('arial',19,'bold'), text ="Coded Converter",background='#FFFFFF', fg = c[i], bd = 10, anchor = 'w')
label_info.grid(row =1, columnspan=4)
#root.grid_rowconfigure(0, weight=1)
numberInput = tk.StringVar()
var = tk.StringVar()
#time & date set
local_time = time.asctime(time.localtime(time.time()))
time1=''
label_inf = tk.Label(root,font = ('arial',15,'bold'), text = local_time, fg = "#FFFFFF", bg=c[i], bd = 10, anchor = 'w')
label_inf.grid(row=2, columnspan=4)
def tick():
    global time1
    time2=time.strftime('%H:%M:%S\n%D')
    if time2!=time1:
        time1=time2
        label_inf.config(text=time2)
    label_inf.after(200,tick)
tick()
# label and entry field

input_label = tk.Label(root, text="Enter Number",font = ('arial',11,'bold'), background=c[i], foreground="#FFFFFF")
input_entry = tk.Entry(root, textvariable=numberInput,bd=8,font = ('arial',11,'bold'))

input_label.grid(row=3)
input_entry.grid(row=3, column=1)
# result label's for showing the others
result_label1 = tk.Label(root, background=c[i], foreground="#FFFFFF")
result_label1.grid(row=6, columnspan=4)
result_label2 = tk.Label(root, background=c[i], foreground="#FFFFFF")
result_label2.grid(row=7, columnspan=4)
result_label3 = tk.Label(root, background=c[i], foreground="#FFFFFF")
result_label3.grid(row=8, columnspan=4)
# drop down initalization and setup
dropDownList = ["Decimal", "Binary", "octal", "Hexadecimal"]
dropdown = tk.OptionMenu(root, var, *dropDownList, command=store_temp)
var.set(dropDownList[0])
dropdown.grid(row=3, column=3)
dropdown.config(background=c[i], foreground="#FFFFFF",font = ('arial',12,'bold'),bd=6)
dropdown["menu"].config(background=c[i], foreground="#FFFFFF",font = ('arial',12,'bold'))
timeLabel = tk.Label(root,font=('Helvetica', 12), background=c[i], foreground="#FFFFFF")
timeLabel.grid(row=5, columnspan=4)
# button click
def countdown():
    global timeleft
    global tl
    if timeleft > 0:
        timeleft -= 1
        timeLabel.config(text="Initial Process\nLoading "+ str(timeleft)+" seconds..\n"+". "*(9-timeleft),font=('Helvetica', 14,'bold'))
        timeLabel.after(1000, countdown)
    if timeleft==0:
        if tl>0:
            tl-=1
            timeLabel.config(text="Loaded..",font=('Helvetica', 24))
            timeLabel.after(1000, countdown)
        #timeLabel.config(text="")
        else:
            call_convert(result_label1, result_label2,result_label3,timeLabel,numberInput)
global coun
def coun():
    countdown()
#call_convert = partial(call_convert, result_label1, result_label2,result_label3,timeLabel,numberInput)
result_button = tk.Button(root, text="Convert", command=coun, background=c[i],font = ('arial',11,'bold'),bd=6, foreground="#FFFFFF",activebackground="white",activeforeground="black")
result_button.grid(row=4, columnspan=4)
root.mainloop()
