import base64
plugin_name = "base64加密"
plugin_version = "v1.1"
plugin_author = "1me"
plugin_time = "20200429"
plugin_info = "base64加密"


def run(mm):
    return base64.b64encode(mm.encode('utf-8'))
