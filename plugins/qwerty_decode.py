plugin_name = "qwerty键盘解码"
plugin_version = "v1.1"
plugin_author = "1me"
plugin_time = "20200504"
plugin_test_in="ysqu"
plugin_test_out="flag"
plugin_info = '''
参考
https://blog.csdn.net/weixin_42109012/article/details/97532738?utm_medium=distribute.pc_relevant.none-task-blog-baidujs-4
'''
plugin_info+="例子\r\n输入\r\n"+plugin_test_in+"\r\n输出\r\n"+plugin_test_out

letter = {
    'q': 'a', 'w': 'b', 'e': 'c', 'r': 'd', 't': 'e', 'y': 'f', 'u': 'g',
    'i': 'h', 'o': 'i', 'p': 'j', 'a': 'k', 's': 'l', 'd': 'm', 'f': 'n',
    'g': 'o', 'h': 'p', 'j': 'q', 'k': 'r', 'l': 's', 'z': 't',
    'x': 'u', 'c': 'v', 'v': 'w', 'b': 'x', 'n': 'y', 'm': 'z',

    'Q': 'A', 'W': 'B', 'E': 'C', 'R': 'D', 'T': 'E', 'Y': 'F', 'U': 'G',
    'I': 'H', 'O': 'I', 'P': 'J', 'A': 'K', 'S': 'L', 'D': 'M', 'F': 'N',
    'G': 'O', 'H': 'P', 'J': 'Q', 'K': 'R', 'L': 'S', 'Z': 'T',
    'X': 'U', 'C': 'V', 'V': 'W', 'B': 'X', 'N': 'Y', 'M': 'Z',
}


def run(letters):
    flag = ''
    for i in range(0, len(letters)):
        flag = flag + letter.get(letters[i])
    return flag