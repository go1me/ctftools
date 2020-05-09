plugin_name = "猪圈密码解码"
plugin_version = "v1.1"
plugin_author = "1me"
plugin_time = "20200509"
plugin_test_in="ocjp{zkii_3sA}"
plugin_test_out="flag{vbrr_3wJ}"
plugin_info = '''
猪圈密码[pigpen cipher]（亦称朱高密码、共济会暗号、共济会密码或共济会员密码），是一种以格子为基础的简单替代式密码。即使使用符号，也不会影响密码分析，亦可用在其它替代式的方法。
参考https://blog.csdn.net/weixin_34393428/article/details/92191782
'''

def run(s):
    table = {
    'a':'j','b':'k','c':'l','d':'m','e':'n','f':'o','g':'p','h':'q','i':'r','j':'a','k':'b',
    'l':'c','m':'d','n':'e','o':'f','p':'g','q':'h','r':'i','s':'w','t':'x','u':'y','v':'z',
    'w':'s','x':'t','y':'u','z':'v','A':'J','B':'K','C':'L','D':'M','E':'N','F':'O','G':'P',
    'H':'Q','I':'R','J':'A','K':'B','L':'C','M':'D','N':'E','O':'F','P':'G','Q':'H','R':'I',
    'S':'W','T':'X','U':'Y','V':'Z','W':'S','X':'T','Y':'U','Z':'V'
    }

    data = s
    new = ""
    for ch in data:
        if ch.isalpha():
            new += table[ch]
        else:
            new += ch
    return new