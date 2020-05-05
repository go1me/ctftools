plugin_name = "求余的逆运算"
plugin_version = "v1.1"
plugin_author = "1me"
plugin_time = "20200505"
plugin_test_in="None"
plugin_test_out="None"
plugin_info = '''
K%a = 1/libnum.invmod(K,a))%a

c = (m*K)%a
m=(c*libnum.invmod(K,a))%a

c=(m+K)%a
这个不会，遇到再说

'''

def run(s):
    return plugin_info