import string
plugin_name = "字符类型统计"
plugin_version = "v1.1"
plugin_author = "1me"
plugin_time = "20200509"
plugin_test_in="Abcd,W =="
plugin_test_out="None"
plugin_info = '''
统计大小写，标点符号，数字个数
这个用来看大小写字符多少，有的题会用例如故意大写加密等等
'''
def run(ciphertext):
    digitNum = 0
    upperNum = 0
    lowerNum = 0
    spaceNum = 0
    alphaNum = 0
    otherNum = 0
    punctNum = 0
    punc = string.punctuation
    for i in ciphertext:
        if i.isdigit():
            digitNum = digitNum + 1
        elif i.isspace():
            spaceNum = spaceNum + 1
        elif i.isalpha():
            alphaNum += 1
        elif i in punc:
            punctNum+=1
        else:
            otherNum += 1
        if i.isupper():
            upperNum+=1
        elif i.islower():
            lowerNum+=1
    return " digit %d\r\n space %d\r\n alpha %d\r\n upper %d\r\n lower %d\r\n punctuation %d\r\n other %d"%(digitNum,spaceNum,alphaNum,upperNum,lowerNum,punctNum,otherNum)