import binascii
plugin_name = "凯撒密码暴力破解"
plugin_version = "v1.1"
plugin_author = "1me"
plugin_time = "20200505"
plugin_test_in="p ht ihjr"
plugin_test_out="i am back"
plugin_info = '''
凯撒密码暴力破解
代码参考
https://blog.csdn.net/rectsuly/article/details/78256037
例子:
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
    output=""
    for offset in range(1,26+1):
        output += "offset="+str(offset)+" "+getTranslatedMessage('decrypt', s, offset)+"\r\n"
    return output