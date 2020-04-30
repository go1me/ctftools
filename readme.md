因为网上找的一些工具感觉都不是很顺手，而且也怕加料，因此自己再造一副轮子，也算是练手  
练手有练手的好处，可以把常用的代码集中在这个工具下，抄的时候，不是是找的时候好找  
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
运行程序，目录下python3 main.py

![](https://github.com/haysengithub/ctftools/blob/master/res/gui.JPG)
用法就不多说了吧，其实我已经写了很多插件，稍后慢慢上去  

