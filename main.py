import tkinter
from tkinter import ttk
import pyperclip
import plugins

root = tkinter.Tk()
root.title("ctftools by 1me")
root.geometry("1024x768")

#-----插件加载begin-----
ex_pag = ['_', '__builtins__', '__cached__', '__doc__',
         '__file__', '__loader__', '__name__', '__package__',
         '__path__', '__spec__', 'abfile',
         'file', 'os', 'pkgapth', 'pkgname', 'pkgutil']
pag_list = []
for i in dir(plugins):
    if i not in ex_pag:
        pag_list.append(getattr(plugins,i))
#-----------------------------


def go(*args):
    output_txt.delete("1.0", "end")
    val = comboxlist.get()
    for i in pag_list:
        if val == i.plugin_name:
            output_txt.insert("insert",i.plugin_info)


def delete_txt():
    input_txt.delete("1.0", "end")
    output_txt.delete("1.0", "end")


def copy_to_pc():
    pyperclip.copy(output_txt.get("0.0", "end").strip())

def out_to_in():
    input_txt.delete("1.0", "end")
    mm = output_txt.get("0.0", "end").strip()
    input_txt.insert("insert", mm)
    output_txt.delete("1.0", "end")

def run():
    output_txt.delete("1.0", "end")
    mm = input_txt.get("0.0", "end").strip()
    val = comboxlist.get()
    for i in pag_list:
        if val == i.plugin_name:
            output_txt.insert("insert", i.run(mm))
            return
    output_txt.insert("insert", "发送了未知错误")


tkinter.Button(root, text="清空", command=delete_txt).place(x=20, y=20, width=100, height=30, bordermode=tkinter.INSIDE)
tkinter.Button(root, text="复制输出", command=copy_to_pc).place(x=120, y=20, width=100, height=30, bordermode=tkinter.INSIDE)
tkinter.Button(root, text="输出变输入", command=out_to_in).place(x=220, y=20, width=100, height=30, bordermode=tkinter.INSIDE)

comvalue = tkinter.StringVar()
comboxlist = ttk.Combobox(root, textvariable=comvalue)
comboxlist["values"] = [i.plugin_name for i in pag_list]
comboxlist.current(0)
comboxlist.bind("<<ComboboxSelected>>", go)
comboxlist.place(x=350, y=20, width=200, height=30, bordermode=tkinter.INSIDE)

tkinter.Button(root, text="run", command=run).place(x=560, y=20, width=100, height=30, bordermode=tkinter.INSIDE)

tkinter.Label(root, text="输入", font="tahoma 12 normal").place(x=20, y=70)
input_txt = tkinter.Text(root)
input_txt.place(x=0,  y=100, width=1024, height=250)

tkinter.Label(root,text="输出", font="tahoma 12 normal").place(x=20,y=370)
output_txt = tkinter.Text(root)
output_txt.place(x=0,  y=400, width=1024, height=250)

output_txt.insert("insert",pag_list[0].plugin_info)
root.mainloop()