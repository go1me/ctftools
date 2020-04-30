from urllib import parse
plugin_name = "url解码"
plugin_version = "v1.1"
plugin_author = "1me"
plugin_time = "20200429"
plugin_info = '''url解码
输入格式为%28pkg%34
'''


def run(s):
    return parse.unquote(s)