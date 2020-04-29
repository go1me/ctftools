import base64
import binascii
plugin_name = "base64解密"
plugin_version = "v1.1"
plugin_author = "1me"
plugin_time = "20200429"
plugin_info = "base64解密"


def run(mm):
    out = base64.b64decode(mm.encode('utf-8'))
    try:
        out = out.decode("utf-8")
    except:
        try:
            out = out.decode("gb2312")
        except:
            out += b"\r\n"+binascii.b2a_hex(out)
    return out
