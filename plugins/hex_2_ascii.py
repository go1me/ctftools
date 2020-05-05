import binascii
plugin_name = "十六进制转字符串"
plugin_version = "v1.1"
plugin_author = "1me"
plugin_time = "20200505"
plugin_test_in="6920616d206261636b"
plugin_test_out="i am back"
plugin_info = '''
十六进制转字符串
格式为:
'''
plugin_info+=plugin_test_in

def run(s):
    try:
        return binascii.a2b_hex(s).decode("utf8")
    except:
        return "格式错误，或者不符合ascii或者utf8编码"+plugin_info