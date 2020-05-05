import binascii
plugin_name = "二进制转字符串"
plugin_version = "v1.1"
plugin_author = "1me"
plugin_time = "20200505"
plugin_test_in="1100110011011000110000101100111"
plugin_test_out="flag"
plugin_info = '''
二进制转字符串
格式为:
'''
plugin_info+=plugin_test_in

def run(s):
    try:
        res = str(hex((int(s,2))))[2:]
        return binascii.a2b_hex(res).decode("utf8")
    except:
        return "格式错误，或者解码后不符合ascii或者utf8编码"+plugin_info