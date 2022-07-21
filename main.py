import tkinter
from tkinter import ttk
from tkinter import filedialog
import pyperclip
import os
#import imp
#import importlib

import importlib.machinery

root = tkinter.Tk()
root.title("ctftools by 1me")
root.geometry("1024x768")

#-----插件加载begin-----
plugin_now = None
plugins_dict = {}
pwd_path = os.getcwd()
plugin_path = os.path.join(pwd_path, "plugins")
def find_chr_all_position(the_str,the_chr):
    pos_list = []
    for i in range(len(the_str)):
        if the_chr == the_str[i]:
            pos_list.append(i)
    return pos_list

for root_path, dirs, files in os.walk(plugin_path):
    for file in files:
        if file.endswith('.py'):
            module_file_path = os.path.join(root_path, file)
            ff = open(module_file_path, "r", encoding="utf-8")
            lines = ff.readlines()
            ff.close()
            for i in lines:
                line = i.strip()
                if "plugin_name" in line:
                    pos_list = find_chr_all_position(line, "\"")
                    if len(pos_list) >= 2 and pos_list[-1] < len(line):
                        plugin_name = line[pos_list[0]+1:pos_list[-1]]
                        if plugin_name not in plugins_dict.keys():
                            plugins_dict[plugin_name] ={"path":module_file_path, "name":file, "module":None}
                    break


def get_plugin_now(val_name):
    if val_name in plugins_dict.keys():
        if plugins_dict[val_name]["module"] is None:
            try: 
                plugins_dict[val_name]["module"] = importlib.machinery.SourceFileLoader(plugins_dict[val_name]["name"], plugins_dict[val_name]["path"]).load_module()
                #imp.load_source(plugins_dict[val_name]["name"], plugins_dict[val_name]["path"])
            except Exception as e:
                return None, plugins_dict[val_name]["path"]+"加载失败\r\n"+str(e)
        plugin_now = plugins_dict[val_name]
        return plugin_now, "ok"
    return None, "error"
#-----------------------------
def get_plugin_info(plugin):
    result = ""
    try:
        if plugin["module"] is not None:
            result = "插件名称:"+plugin["module"].plugin_name
            result += "\t\t版本:"+plugin["module"].plugin_version
            result += "\t\t作者:"+plugin["module"].plugin_author
            result += "\t\t时间:"+plugin["module"].plugin_time
            result += "\r\n插件简介:"+plugin["module"].plugin_info
    except:
        pass
    return result

def comboxlist_callback(*args):
    global plugin_now
    output_txt.delete("1.0", "end")
    val = comboxlist.get()
    plugin_now, ret = get_plugin_now(val)
    if ret == "ok":
        output_txt.insert("insert", get_plugin_info(plugin_now))
    else:
        output_txt.insert("insert", "load"+val+ret)
    info_text.set("当前插件:"+plugin_now["path"])

def delete_txt():
    input_txt.delete("1.0", "end")
    #output_txt.delete("1.0", "end")


def copy_to_pc():
    pyperclip.copy(output_txt.get("0.0", "end").strip())


def out_to_in():
    input_txt.delete("1.0", "end")
    mm = output_txt.get("0.0", "end").strip()
    input_txt.insert("insert", mm)
    #output_txt.delete("1.0", "end")


def run():
    output_txt.delete("1.0", "end")
    mm = input_txt.get("0.0", "end").strip()
    if plugin_now is not None:
        output_txt.insert("insert", plugin_now["module"].run(mm))
    else:
        output_txt.insert("insert", "发生了未知错误")

def openfile_2_input():
    file_name = filedialog.askopenfilename(title="导入文件",filetypes=[('All Files','*'),('text',"*.txt")])
    ff = open(file_name,"r",encoding="utf-8")
    read=ff.read()
    ff.close()
    input_txt.delete("0.0","end")
    input_txt.insert("insert",read)

def input_2_file():
    file_name = filedialog.asksaveasfilename(title="保存到",filetypes=[('All Files','*'),('text',"*.txt")])
    ff = open(file_name,"w",encoding="utf-8")
    ff.write(input_txt.get("0.0","end"))
    ff.close()

def output_2_file():
    file_name = filedialog.asksaveasfilename(title="保存到",filetypes=[('All Files','*'),('text',"*.txt")])
    ff = open(file_name,"w",encoding="utf-8")
    ff.write(output_txt.get("0.0","end"))
    ff.close()

def cp_plugin_path():
    pyperclip.copy(plugin_now["path"])

def test_2_input():
    if "plugin_test_in" in dir(plugin_now["module"]):
        input_txt.delete("0.0","end")
        input_txt.insert("insert", plugin_now["module"].plugin_test_in)

def menu_callback(arg):
    global plugin_now
    output_txt.delete("0.0","end")
    plugin_now, ret = get_plugin_now(arg)
    if ret == "ok":
        output_txt.insert("insert", get_plugin_info(plugin_now))
        info_text.set("当前插件:"+plugin_now["path"])
        comboxlist.set(arg)
    else:
        output_txt.insert("insert", "导入插件失败\r\n"+ret)

#创建一个顶级菜单
menubar = tkinter.Menu(root)
#menubar.config(font="tahoma 24 normal")
filemenu = tkinter.Menu(menubar,tearoff=False)
filemenu.add_command(label="导入到输入", command= openfile_2_input)
filemenu.add_command(label="保存输入到文件", command= input_2_file)
filemenu.add_command(label="保存输出到文件", command= output_2_file)
filemenu.add_separator()
filemenu.add_command(label="退出", command= root.quit)
menubar.add_cascade(label="文件", menu=filemenu)
#--------------------------------------
editmenu = tkinter.Menu(menubar,tearoff=False)
editmenu.add_command(label="清空", command= delete_txt)
editmenu.add_command(label="复制输出", command= copy_to_pc)
editmenu.add_command(label="输出变输入", command= out_to_in)
editmenu.add_command(label="复制当前插件路径", command= cp_plugin_path)
editmenu.add_command(label="导入测试用例", command= test_2_input)
menubar.add_cascade(label="编辑", menu=editmenu)
#---------------------------------------
decodemenu = tkinter.Menu(menubar,tearoff=False)
encodemenu = tkinter.Menu(menubar,tearoff=False)
exchangemenu = tkinter.Menu(menubar,tearoff=False)
rsamenu = tkinter.Menu(menubar,tearoff=False)
othermenu = tkinter.Menu(menubar,tearoff=False)
for i in plugins_dict:
    if "解密" in i or "解码" in i or "暴力破解" in i:
        decodemenu.add_command(label=i, command=lambda arg=i:menu_callback(arg))
    elif "加密" in i or "编码" in i:
        encodemenu.add_command(label=i, command=lambda arg=i:menu_callback(arg))
    elif "转" in i:
        exchangemenu.add_command(label=i, command=lambda arg=i:menu_callback(arg))
    elif "rsa" in i:
        rsamenu.add_command(label=i, command=lambda arg=i:menu_callback(arg))
    else:
        othermenu.add_command(label=i, command=lambda arg=i:menu_callback(arg))

menubar.add_cascade(label="解密", menu=decodemenu)
menubar.add_cascade(label="加密", menu=encodemenu)
menubar.add_cascade(label="转换", menu=exchangemenu)
menubar.add_cascade(label="rsa", menu=rsamenu)
menubar.add_cascade(label="其他", menu=othermenu)

#显示菜单
root.config(menu=menubar)

tkinter.Button(root, text="清空", command=delete_txt).place(x=20, y=20, width=100, height=30, bordermode=tkinter.INSIDE)
tkinter.Button(root, text="复制输出", command=copy_to_pc).place(x=120, y=20, width=100, height=30, bordermode=tkinter.INSIDE)
tkinter.Button(root, text="输出变输入", command=out_to_in).place(x=220, y=20, width=100, height=30, bordermode=tkinter.INSIDE)


comvalue = tkinter.StringVar()
comboxlist = ttk.Combobox(root, textvariable=comvalue)
comboxlist["values"] = list(plugins_dict.keys())
comboxlist.current(0)
comboxlist.bind("<<ComboboxSelected>>", comboxlist_callback)
comboxlist.place(x=350, y=20, width=200, height=30, bordermode=tkinter.INSIDE)

tkinter.Button(root, text="run", command=run).place(x=560, y=20, width=100, height=30, bordermode=tkinter.INSIDE)

tkinter.Label(root, text="输入\t通过菜单或者下拉框选择插件,输入框输入字符串，run运行，只支持ascii,utf8", font="tahoma 12 normal").place(x=20, y=70)
input_txt = tkinter.Text(root)
input_txt.place(x=0,  y=100, width=1024, height=250)

tkinter.Label(root, text="输出", font="tahoma 12 normal").place(x=20, y=370)
output_txt = tkinter.Text(root)
output_txt.place(x=0,  y=400, width=1024, height=330)
plugin_now, errosss = get_plugin_now(list(plugins_dict.keys())[0])
output_txt.insert("insert", get_plugin_info(plugin_now))

info_text = tkinter.StringVar()
info = tkinter.Label(root, textvariable= info_text, font="tahoma 12 normal")
info.place(x=5, y=730)
info_text.set("当前插件："+plugin_now["path"])
root.mainloop()