import tkinter
from tkinter import ttk
import pyperclip
import os
import imp

root = tkinter.Tk()
root.title("ctftools by 1me")
root.geometry("1024x768")

#-----插件加载begin-----
module_dict = None
plugin_dict = {}
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
                        if plugin_name not in plugin_dict.keys():
                            plugin_dict[plugin_name] ={"path":module_file_path, "name":file, "module":None}
                    break


def get_module_dict(val_name):
    if val_name in plugin_dict.keys():
        if plugin_dict[val_name]["module"] is None:
            try:
                plugin_dict[val_name]["module"] = imp.load_source(plugin_dict[val_name]["name"], plugin_dict[val_name]["path"])
            except Exception as e:
                return None, plugin_dict[val_name]["path"]+"加载失败\r\n"+str(e)
        module_dict = plugin_dict[val_name]
        return module_dict, "ok"
    return None, "error"
#-----------------------------


def go(*args):
    global module_dict
    output_txt.delete("1.0", "end")
    val = comboxlist.get()
    module_dict, ret = get_module_dict(val)
    if ret == "ok":
        output_txt.insert("insert", module_dict["module"].plugin_info)
    else:
        output_txt.insert("insert", "load"+val+ret)
    info_text.set("当前插件:"+module_dict["path"])

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
    if module_dict is not None:
        output_txt.insert("insert", module_dict["module"].run(mm))
    else:
        output_txt.insert("insert", "发生了未知错误")


tkinter.Button(root, text="清空", command=delete_txt).place(x=20, y=20, width=100, height=30, bordermode=tkinter.INSIDE)
tkinter.Button(root, text="复制输出", command=copy_to_pc).place(x=120, y=20, width=100, height=30, bordermode=tkinter.INSIDE)
tkinter.Button(root, text="输出变输入", command=out_to_in).place(x=220, y=20, width=100, height=30, bordermode=tkinter.INSIDE)


comvalue = tkinter.StringVar()
comboxlist = ttk.Combobox(root, textvariable=comvalue)
comboxlist["values"] = list(plugin_dict.keys())
comboxlist.current(0)
comboxlist.bind("<<ComboboxSelected>>", go)
comboxlist.place(x=350, y=20, width=200, height=30, bordermode=tkinter.INSIDE)

tkinter.Button(root, text="run", command=run).place(x=560, y=20, width=100, height=30, bordermode=tkinter.INSIDE)

tkinter.Label(root, text="输入\t请在输入框输入字符串，只支持ascii,utf8", font="tahoma 12 normal").place(x=20, y=70)
input_txt = tkinter.Text(root)
input_txt.place(x=0,  y=100, width=1024, height=250)

tkinter.Label(root, text="输出", font="tahoma 12 normal").place(x=20, y=370)
output_txt = tkinter.Text(root)
output_txt.place(x=0,  y=400, width=1024, height=250)
module_dict, _ = get_module_dict(list(plugin_dict.keys())[0])
output_txt.insert("insert", module_dict["module"].plugin_info)

info_text = tkinter.StringVar()
info = tkinter.Label(root, textvariable= info_text, font="tahoma 12 normal")
info.place(x=5, y=650)
info_text.set("当前插件："+module_dict["path"])
root.mainloop()