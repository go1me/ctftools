import base64
plugin_name = "base64换表解密"
plugin_version = "v1.1"
plugin_author = "1me"
plugin_time = "20200429"
plugin_test_in='''
新表ZYXABCDEFGHIJKLMNOPQRSTUVWzyxabcdefghijklmnopqrstuvw0123456789+/
原表ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/
密码x2dtJEOmyjacxDemx2eczT5cVS9fVUGvWTuZWjuexjRqy24rV29q
'''
plugin_test_out="sh00ting_phish_in_a_barrel@flare-on.com"
plugin_info = '''base64换表解密
代码参考https://www.cnblogs.com/dyhaohaoxuexi/p/11025985.html
'''
plugin_info+=plugin_test_in


def run(mm):
    mm = mm.split("\n")
    if len(mm) !=3:
        return "格式错误\r\n"+plugin_info
    new_table=mm[0][2:].strip()
    old_table=mm[1][2:].strip()
    data = mm[2][2:].strip()
    return base64.b64decode(data.translate(str.maketrans(new_table,old_table)))