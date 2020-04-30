from urllib import parse
plugin_name = "url编码"
plugin_version = "v1.1"
plugin_author = "1me"
plugin_time = "20200429"
plugin_info = "url编码"


def run(s):
    return parse.quote(s.encode("utf8"))