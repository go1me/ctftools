plugin_name = "培根解密"
plugin_version = "v1.1"
plugin_author = "1me"
plugin_time = "20200504"
plugin_test_in="aababababbaaaaaaabba"
plugin_test_out="flag"
plugin_info = '''
参考
培根密码有两种，详情见
https://blog.csdn.net/weixin_42109012/article/details/97644262?utm_medium=distribute.pc_relevant.none-task-blog-baidujs-2
'''
plugin_info+="例子\r\n输入\r\n"+plugin_test_in+"\r\n输出\r\n"+plugin_test_out

letters1 = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G',
    'H', 'I', 'J', 'K', 'L', 'M', 'N',
    'O', 'P', 'Q', 'R', 'S', 'T',
    'U', 'V', 'W', 'X', 'Y', 'Z',
]
letters2 = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g',
    'h', 'i', 'j', 'k', 'l', 'm', 'n',
    'o', 'p', 'q', 'r', 's', 't',
    'u', 'v', 'w', 'x', 'y', 'z',
]
cipher1 = [
    "aaaaa", "aaaab", "aaaba", "aaabb", "aabaa", "aabab", "aabba",
    "aabbb", "abaaa", "abaab", "ababa", "ababb", "abbaa", "abbab",
    "abbba", "abbbb", "baaaa", "baaab", "baaba", "baabb",
    "babaa", "babab", "babba", "babbb", "bbaaa", "bbaab",
]
cipher2 = [
    "AAAAA", "AAAAB", "AAABA", "AAABB", "AABAA", "AABAB", "AABBA",
    "AABBB", "ABAAA", "ABAAA", "ABAAB", "ABABA", "ABABB", "ABBAA",
    "ABBAB", "ABBBA", "ABBBB", "BAAAA", "BAAAB", "BAABA",
    "BAABB", "BAABB", "BABAA", "BABAB", "BABBA", "BABBB",
]


def bacon1(string):
    result = ""
    lists = []
    # 分割，五个一组
    for i in range(0, len(string), 5):
        lists.append(string[i:i+5])
    # print(lists)
    # 循环匹配，得到下标，对应下标即可
    for i in range(0, len(lists)):
        for j in range(0, 26):
            if lists[i] == cipher1[j]:
                # print(j)
                result+=letters1[j]
    return result
    


def bacon2(string):
    result = ""
    lists = []
    # 分割，五个一组
    for i in range(0, len(string), 5):
        lists.append(string[i:i+5])
    # print(lists)
    # 循环匹配，得到下标，对应下标即可
    for i in range(0, len(lists)):
        for j in range(0, 26):
            if lists[i] == cipher2[j]:
                # print(j)
                result+=letters2[j]
    return result


def run(s):
    s = s.strip()
    for i in s:
        if i !="a" and i !="A" and i!="b" and i !="B":
            return "不是培根密码"
    if i == "A" or i == "B":
        return bacon2(s)

    if i == "a" or i == "b":
        return bacon1(s)
    
    