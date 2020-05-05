import binascii
plugin_name = "凯撒密码加密"
plugin_version = "v1.1"
plugin_author = "1me"
plugin_time = "20200505"
plugin_test_in='''offset=7
i am back
'''
plugin_test_out="p ht ihjr"
plugin_info = '''
凯撒密码加密
代码参考
https://blog.csdn.net/rectsuly/article/details/78256037
输入格式：
'''
plugin_info+=plugin_test_in

def getTranslatedMessage(mode, message, key):
    if mode[0] == 'd':
        key = -key
    translated = ''
    for symbol in message:
        if symbol.isalpha():
            num = ord(symbol)
            num += key
            if symbol.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif symbol.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26

            translated += chr(num)
        else:
            translated += symbol
    return translated


def run(s):
    output = ""
    s = s.split("\n")
    if len(s) !=2:
        return "格式不对\r\n"+plugin_info
    if "offset" not in s[0]:
        return "格式不对\r\n"+plugin_info
    offset = int(s[0].split("=")[1].strip(),10)
    return getTranslatedMessage('encrypt', s[1].strip(), offset)