import base64
import base36
import base58
import base62
import base91
import pybase24
try:
    import base92
    import base128
except:
    pass


plugin_name = "base加密全家桶"
plugin_version = "v1.1"
plugin_author = "1me"
plugin_time = "20200505"
plugin_test_in="flag"
plugin_test_out="None"
plugin_info = '''
对输入的字符串进行base 16 24 32 36 58 62 64 85 91 92 128加密
使用之前需要
pip3 install pybase24 只能加密长度为4的倍数的字符
pip3 install base64
pip3 install base36
pip3 install base58
pip3 install pybase62
pip3 install base91
pip3 install base92 这个装的时候有问题
pip3 install base128 这个windows下面不太好装
测试用例
'''
plugin_info+=plugin_test_in

def run(s):
    mm = s.encode("utf8")
    output=""
    output += "base16:"+base64.b16encode(mm).decode("utf8")
    try:
        output+="\r\nbase24:"+pybase24.encode24(mm)
    except:
        output+="\r\nbase24:失败"
    output +="\r\nbase32:"+base64.b32encode(mm).decode("utf8")
    try:
        output+="\r\nbase36:"+str(base36.loads(mm))
    except:
        output+="\r\nbase36:失败"
    output+="\r\nbase58:"+base58.b58encode(mm).decode("utf8")
    output+="\r\nbase62:"+base62.encodebytes(mm)
    output+="\r\nbase64:"+base64.b64encode(mm).decode("utf8")
    output+="\r\nbase85:"+base64.b85encode(mm).decode("utf8")
    output+="\r\nbase91:"+base91.encode(mm)
    try:
        output+="\r\nbase92:"+base92.b92encode(mm).decode("utf8")
    except:
        output+="\r\nbase92:失败"
    try:
        output+="\r\nbase128:"+base128.encode(mm).decode("utf8")
    except:
        output+="\r\nbase128:失败"
    return output
