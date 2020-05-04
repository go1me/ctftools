plugin_name = "rot13解码"
plugin_version = "v1.1"
plugin_author = "1me"
plugin_time = "20200504"
plugin_info = '''
rot13解码
Ubj pna lbh gryy na rkgebireq sebz na vagebireg ng AFN?
'''


def run(s):
    offset = 13
    def encodeCh(ch):
        f=lambda x:chr((ord(ch)-x+offset)%26+x)
        return f(97) if ch.islower() else (f(65) if ch.isupper() else ch)
    return ''.join(encodeCh(c) for c in s)