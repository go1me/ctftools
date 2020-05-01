
plugin_name = "md5加密"
plugin_version = "v1.1"
plugin_author = "1me"
plugin_time = "20200429"
plugin_info = "md5加密 import hashlib"

import hashlib
def run(mm):
    md5_val = hashlib.md5(mm.encode('utf8')).hexdigest()
    return md5_val