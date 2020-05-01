plugin_name = "多组密文同一密钥解体过程"
plugin_version = "v1.1"
plugin_author = "1me"
plugin_time = "20200429"
plugin_info = '''
首先把所有密文拼接后到https://quipqiup.com/去初步解密
然后用初步解密结果拿https://github.com/Jwomers/many-time-pad-attack爆破密钥
最后再拿密钥用如下代码解密
from crypto_commons.generic import xor_string
xor_string(str1,str2)
'''


def run(s):
    return plugin_info