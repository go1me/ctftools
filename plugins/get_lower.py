plugin_name = "获取小写字符"
plugin_version = "v1.1"
plugin_author = "1me"
plugin_time = "20200505"
plugin_test_in="Abcd,W =="
plugin_test_out="None"
plugin_info = '''
获取输入字符中的小写字符
'''

def run(ciphertext):
	mm=""
	for i in ciphertext:
		if i.islower():
			mm+=i
	return mm