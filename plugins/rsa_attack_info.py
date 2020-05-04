import binascii
plugin_name = "rsa各种攻击方法参考"
plugin_version = "v1.1"
plugin_author = "1me"
plugin_time = "20200429"
plugin_info = '''不用点run，这个没有实现方法
rsa各种攻击方法参考
https://blog.csdn.net/weixin_41038905/article/details/105827655
https://findneo.github.io/180727rsa-attack/
https://github.com/findneo/RSA-ATTACK
http://factordb.com/api?query=1234 查factor
-------------------------------------------
参考代码
#n e d c m pow
https://blog.csdn.net/vhkjhwbs/article/details/101026050#1
#pycrypto
https://blog.csdn.net/mouday/article/details/82707535
#rsa
https://www.cnblogs.com/52python/p/6589869.html

1、求逆元
gmpy2.invert(a,b)
libnum.invmod(a,b)
primefac.modinv(a,b)
2、开方
gmpy.root(9,2)
gmpy2.iroot(9,2)
3、求公约数
libnum.gcd(a,b)
primefac.gcd(a,b)
4、求同余
pow(m,e,n)
pow(c,d,n)
5、贝组等式求解
libnum.xgcd(a,b)
6、中国剩余定理求解
有物不知其数，三三数之剩二，五五数之剩三，七七数之剩二，问物几何？
libnum.solve_crt([m1,m2,m3],[n1,n2,n3])
7、数字转字符串
libnum.n2s(a)

'''


def run(s):
    return plugin_info