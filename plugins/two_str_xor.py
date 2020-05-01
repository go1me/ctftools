from crypto_commons.generic import xor_string
plugin_name = "两个字符串异或操作"
plugin_version = "v1.1"
plugin_author = "1me"
plugin_time = "20200429"
plugin_info = '''
两个字符串异或操作
格式:
str1=abcdefghigk
str2=efg
----------------------
代码:
from crypto_commons.generic import xor_string
xor_string(str1,str2)
'''


def run(s):
    lines = s.split("\n")
    for line in lines:
        lin = line.strip()
        if "str1" in lin:
            str1 = lin[5:]
        if "str2" in lin:
            str2 = lin[5:]
        
    return xor_string(str1,str2)