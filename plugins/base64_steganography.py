import base64
plugin_name = "base64隐写解密"
plugin_version = "v1.1"
plugin_author = "1me"
plugin_time = "20200429"
plugin_info = '''base64隐写解密
代码来自https://blog.csdn.net/weixin_43900387/article/details/101040262
'''


def run(s):
    b64chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
    bin_str = ''
    result = ""
    for line in s.split("\n"):
        if line == "":
            continue
        line = line.strip()
        stegb64 = ''.join(line.split())
        rowb64 =  ''.join(base64.b64encode(base64.b64decode(stegb64)).decode("utf-8").split())
        #rowb64 =  ''.join(stegb64.decode('base64').encode('base64').split())

        offset = abs(b64chars.index(stegb64.replace('=','')[-1])-b64chars.index(rowb64.replace('=','')[-1]))

        equalnum = stegb64.count('=') #no equalnum no offset

        if equalnum:

            bin_str += bin(offset)[2:].zfill(equalnum * 2)

        result =  ''.join([chr(int(bin_str[i:i + 8], 2)) for i in range(0, len(bin_str), 8)])
    return result