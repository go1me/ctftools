plugin_name = "常用代码"
plugin_version = "v1.1"
plugin_author = "1me"
plugin_time = "20200505"
plugin_info = '''
1、from ctypes import *
libc = cdll.LoadLibrary("/lib/x86_64-linux-gnu/libc.so.6")
libc.srand(1416667590)
libc.rand()

2、python3，open(xx,wb) 写文件问题
如果你int型用chr(i).encode("utf8")写文件会，文件第一个字符或多一个\xc2
改成chr(165).encode('latin1')
参考https://blog.csdn.net/weixin_44266650/article/details/99726486

3、中国剩余定理
参考
http://blogs.univ-poitiers.fr/e-laize/2014/12/08/seccon-2014-quals-crypto-decrypt-it/
https://gist.github.com/volpino/175ba3d0e4e8b495bca4
https://www.tasteless.eu/post/2014/12/seccon-quals-2014-decrypt-it-easy-crypto200/

'''


def run(s):
    return plugin_info


