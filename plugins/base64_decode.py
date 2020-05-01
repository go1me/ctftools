import base64
import binascii
plugin_name = "base64解密"
plugin_version = "v1.1"
plugin_author = "1me"
plugin_time = "20200429"
plugin_info = "base64解密"


def run(mm):
    out =""
    mm = mm.split("\n")
    for i in mm:
        if i =="":
            continue
        line = i.strip()
        xx = base64.b64decode(line.encode('utf-8'))
        try:
            out += xx.decode("utf-8")
        except:
            try:
                out += xx.decode("gb2312")
            except:
                out += b"\r\n"+binascii.b2a_hex(xx)
        out += "\r\n"
    return out
