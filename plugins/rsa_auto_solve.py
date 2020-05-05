import libnum
import os
import requests
plugin_name = "rsa自动解题"
plugin_version = "v1.1"
plugin_author = "1me"
plugin_time = "20200505"
plugin_test_in='''
n=920139713
e=19
c=704796792
'''
plugin_test_out="None"
plugin_info = '''输入n,e,d,p,q,c,m等自动解题
需要 os,libnum,requests三个包
目前实现了几个简单计算
比如通过pq计算n
通过pqe计算d
n查factordb.com等等
其他的先弃坑了，等有空再补
输入格式为
'''
plugin_info+=plugin_test_in

def get_factor(n):
    result="\r\n分解n的方法\r\n"
    result+="\t1、利用yafu，yafu factor("+str(n)+")\r\n"
    result+="\t2、利用kali自带的factor，factor "+str(n)+"\r\n"
    result+="\t3、rsactftools直接n e 求私钥\r\n"
    result+="\t4、利用https://factordb.com 查\r\n"
    result+="本程序尝试用factordb查，如果查不到，请自行手工再按上述方法处理\r\n"

    r = requests.get("http://factordb.com/api?query="+str(n))
    p=-1
    q=-1
    res = r.json()
    if "status" in res.keys():
        if res["status"] =="FF":
            if "factors" in res.keys():
                factors = res["factors"]
                if len(factors) ==2:
                    p = int(factors[0][0],10)
                    q = int(factors[1][0],10)
    return result,p,q


def run(s):
    n=[]
    p=[]
    q=[]
    e=[]
    d=[]
    c=[] #密文
    m=[] #明文
    result =""

    lines = s.split("\n")
    for line in lines:
        temp = line.strip()
        temp = temp.split("=")
        if len(temp)!=2:
            return line+"输入格式不对\r\n"+plugin_info
        param_name = temp[0].strip()
        param_value = temp[1].strip()
        if param_value.startswith("0x"):
            param_value = int(param_value,16)
        else:
            param_value = int(param_value,10)
        if "n" in param_name:
            n.append(param_value)
        if "p" in param_name:
            p.append(param_value)
        if "q" in param_name:
            q.append(param_value)
        if "e" in param_name:
            e.append(param_value)
        if "d" in param_name:
            d.append(param_value)
        if "c" in param_name:
            c.append(param_value)
        if "m" in param_name:
            m.append(param_value)
    if len(e)==1 and len(n) ==1 and len(p) ==0 and len(q)==0 and len(d)==0 and len(c)==0:
        result +="./RsaCtfTool.py --private -e "+str(e[0])+" -n "+str(n[0])+" --attack all"
        result +="后面的那个all可以换成其他的可选攻击方式，具体参考RsaCtfTool"
    if len(n)==1 and len(p) ==0 and len(q) ==0:
        res , pn, qn = get_factor(n[0])
        result +=res
        if pn!=-1 and qn!=-1:
            p.append(pn)
            q.append(qn)
            result +="p="+str(p[-1])+"\r\n"
            result +="q="+str(q[-1])+"\r\n"
    
    if len(p)==1 and len(q) == 1 and len(n) ==0:
        n.append(p[0]*q[0])
        result +="n="+str(n[-1])+"\r\n"

    if len(p)==1 and len(q) == 1 and len(e) ==1:
        d.append(libnum.invmod(e[0],(p[0]-1)*(q[-1]-1)))
        result +="d="+str(d[-1])+"\r\n"
        
    
    if len(c)==1 and len(d) ==1 and len(n) ==1:
        m.append(pow(c[-1],d[-1],n[-1]))
        result+="m="+str(m[-1])+"\t#解密结果\r\n"
    if len(m)==1 and len(e) ==1 and len(n) ==1:
        c.append(pow(m[-1],e[-1],n[-1]))
        result+="c="+str(c[-1])+"\t#加密结果\r\n"
    return result
