plugin_name = "常用命令"
plugin_version = "v1.1"
plugin_author = "1me"
plugin_time = "20200505"
plugin_info = '''
1、stat命令，查看文件属性，一个用法就是，如果一个文件是被seed=time(0)随机数异或加密的，可以获取文件创建时间恢复所有随机数
\thttp://blogs.univ-poitiers.fr/e-laize/2014/12/08/seccon-2014-quals-crypto-decrypt-it/
\t$ stat ecrypt1.bin
\t$ stat --printf=%Y  ecrypt1.bin 
\t1416667590
2、hexdump命令,  hexdump -C -n 20 abc.png 

from ctypes import *
    libc = cdll.LoadLibrary("/lib/x86_64-linux-gnu/libc.so.6")
    libc.srand(1416667590)
    libc.rand()
    
'''


def run(s):
    return plugin_info