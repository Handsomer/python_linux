# -*- coding: utf-8 -*-

"""
来源《python for linux System Administration and Automated Operation》
descript: section 3.2 使用ConfigParse 解析配置文件
整理人： SW
时间：  20180801
"""


import ConfigParser

def use_config_parser():
    """
    section: chapter 3.2
    dircript: 配置文件的读，写，保存。
    """
    cf = ConfigParser.ConfigParser(allow_no_value = True)
    cf.read('my.conf')
    print(cf.sections())
    print(cf.has_section('client'))
    print(cf.options('client'))
    print(cf.get('client','user'))
    print(cf.getint('client','port'))

    cf.set('client', 'port', '3360')
    cf.write(open('my_copy.conf', 'w'))

if __name__ == "__main__":
    use_config_parser()
    print(use_config_parser.__doc__)
