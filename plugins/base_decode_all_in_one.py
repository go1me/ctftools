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


plugin_name = "base解密全家桶"
plugin_version = "v1.1"
plugin_author = "1me"
plugin_time = "20200505"
plugin_test_in="ZmxhZw=="
plugin_test_out="None"
plugin_info = '''
对输入的字符串进行base 16 24 32 36 58 62 64 85 91 92 128解密
使用之前需要
pip3 install pybase24 
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
    mm = s.strip().encode("utf8")
    output=""
    try:
        output += "base16:"+base64.b16decode(mm).decode("utf8")
    except:
        output+="base16:失败"
    try:
        output+="\r\nbase24:"+pybase24.decode24(mm)
    except:
        output+="\r\nbase24:失败,pybase24解密貌似代码有问题"
    try:
        output +="\r\nbase32:"+base64.b32decode(mm).decode("utf8")
    except:
        output+="\r\nbase32:失败"
    try:
        output+="\r\nbase36"+str(base36.dumps(int(mm,10)))
    except:
        output+="\r\nbase36:失败"
    try:
        output+="\r\nbase58:"+base58.b58decode(mm).decode("utf8")
    except:
        output+="\r\nbase58:失败"
    try:
        output+="\r\nbase62:"+base62.decodebytes(mm.decode("utf8")).decode("utf8")
    except:
        output+="\r\nbase62:失败"
    try:
        output+="\r\nbase64:"+base64.b64decode(mm).decode("utf8")
    except:
        output+="\r\nbase64:失败"
    try:
        output+="\r\nbase85:"+base64.b85decode(mm).decode("utf8")
    except:
        output+="\r\nbase85:失败"
    try:
        output+="\r\nbase91:"+base91.decode(mm)
    except:
       output+="\r\nbase91:失败" 
    try:
        output+="\r\nbase92:"+base92.b92decode(mm).decode("utf8")
    except:
        output+="\r\nbase92:失败"
    try:
        output+="\r\nbase128:"+base128.decode(mm).decode("utf8")
    except:
        output+="\r\nbase128:失败"
    return output
