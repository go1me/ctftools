import base64
plugin_name = "base64加密" #插件名称，必选，且不能重复
plugin_version = "v1.1"    #插件版本号
plugin_author = "1me"      #插件作者
plugin_time = "20200429"   #插件编写时间
plugin_test_in="flag"      #测试用例的输入
plugin_test_out="ZmxhZw==" #测试用例的输出
plugin_info = "base64加密" #插件简介

#插件处理函数，mm为字符串输入，从输入框获取，return的字符串会在输出框显示
def run(mm):
    return base64.b64encode(mm.encode('utf-8'))

if __name__ == "__main__":
    print(run(plugin_test_in))
    print(plugin_test_out)
