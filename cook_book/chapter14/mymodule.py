#14.1.2 
#函数输出一个字符串
def urlPrint(protocol, host, domain):
    url = '{}://{}.{}'.format(protocol, host, domain)
    print(url)