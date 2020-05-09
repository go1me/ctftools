plugin_name = "栅栏密码暴力破解"
plugin_version = "v1.1"
plugin_author = "1me"
plugin_time = "20200504"
plugin_test_in="fg2ivyo}l{2s3_o@aw__rcl@"
plugin_test_out="flag"
plugin_info = '''
'''
def run(e):
    res = ""
    elen = len(e)  # 计算字符串长度
    field = []
    for i in range(2, elen):  # 做一个循环，从2开始到数字elen（字符串长度）
        if elen % i == 0:  # 计算那些数字能整除字符串长度
            field.append(i)  # 将能整出的数字加入到field里面

    for f in field:
        b = elen // f  # 用字符串实际长度除以上面计算出能整出的数字f
        result = {x: '' for x in range(b)}
        for i in range(elen):  # 字符串有多少位，就循环多少次
            a = i % b
            result.update({a: result[a] + e[i]})  # 字符串截断，并更新数据
        d = ''
        for i in range(b):
            d += result[i]
        res+='分为'+str(f)+'栏时，解密结果为：'+d+'\n'
    return res
