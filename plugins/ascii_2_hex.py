import binascii
plugin_name = "字符串转十六进制"
plugin_version = "v1.1"
plugin_author = "1me"
plugin_time = "20200429"
plugin_info = "字符串转十六进制"


def run(s):
    try:
        res = binascii.b2a_hex(s.encode("utf8"))
    except:
        res = "输入字符串，如 Nihao,你好"
    return res