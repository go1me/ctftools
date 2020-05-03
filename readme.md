因为网上找的一些工具感觉都不是很顺手，而且也怕加料，因此自己再造一副轮子，也算是练手  
练手有练手的好处，可以把常用的代码集中在这个工具下，抄的时候，额，不是，是找的时候好找  
这是一个基于tkinter的gui的ctf工具集，所有工具实现插件化编程,目前只支持python3    
所有插件均是选中时才加载，防止一股脑加载有些包没有导致全线崩溃  
如果你想增加自己的工具，只要在plugins目录下面新建py文件编写程序即可自动加入gui  
下面是个demo  
```python
import base64
plugin_name = "base64加密" #插件名称，重要，不能重复，必选
plugin_version = "v1.1"
plugin_author = "1me"
plugin_time = "20200429"
plugin_info = "base64加密，需要import base64" #插件信息，可以写一些demo，必选

#插件运行函数
def run(mm):
    return base64.b64encode(mm.encode('utf-8'))
```  
  
插件支持自动分组到menu，只要你的plugin_name里含有 加密/编码  解密/解码 转 等字段，就会按照功能自动分组到相应menu  


![](https://github.com/haysengithub/ctftools/blob/master/res/gui.JPG)
用法：  
根目录下python3 main.py运行程序    
1、通过菜单或下拉框选择插件  
2、在输入框输入需要操作的字符/或者选择文件菜单导入字符到输入框  
3、点击run
4、查看输入框  

其实我已经写了很多插件，稍后慢慢上去  

2020-05-03 增加了ecc常用攻击插件，额，并没有实现方法，只是记了点网址    
2020-05-03 下拉框太长了，影响选取增加了menu；增加了文件导入到输入框，增加了输入框和输出口到处到文件

