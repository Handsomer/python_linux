# -*- coding: utf-8 -*-

"""
来源《python for linux System Administration and Automated Operation》
整理人： SW
时间：  20180731
"""

from __future__ import print_function
import sys
import fileinput


def std_in():
    """
    章节：  chapter 三 3.1.2
    descript: 标准输入的方法一， 使用sys.stdin读取标准输入
    执行 a:   cat file_path | python std_in.py
    执行 b:   python std_in.py < file_path
    执行 c:   python std_in.py file_path file_path
    """
    for line in sys.stdin:
        print(line,end='')



def file_input():
    """
    descript: 标准输入的方法二,此方法调用时可以传入多个文件
    """
    for line in fileinput.input():
        meta = [fileinput.filename(), fileinput.fileno(), fileinput.filelineno(), fileinput.isfirstline(), fileinput.isstdin()]
        print(*meta, end = '')
        print(line, end='')


def test_stdout_std_error():
    """
    章节：  chapter 三 3.1.3
    descript: 使用SystemExit异常打印错误信息
    执行 a：
        python std_in.py
        命令行下输出所有的信息，包括标准输出和错误输出
    执行 b：
        python std_in.py  2> tmp_1
        命令行下输出标准输出， 错误输出重定向到tmp_1中
    执行 c：
        python std_in.py  > tmp
        命令行下输出错误输出， 标准输出重定向到tmp中
    """
    sys.stdout.write("hello \n")
    sys.stderr.write("world \n")


def raise_except():
    # sys.stderr.write('error msg \n')
    # exit(6)
    raise SystemExit("error msg")

import getpass

def get_pass():
    """
    章节：  chapter 三 3.1.4
    descript：使用getpass 库读取密码
    """
    user = getpass.getuser()
    passwd = getpass.getpass("enter your passwd: ")
    print(user, passwd)

if __name__ == '__main__':
    # std_in()
    # file_input()
    # test_stdout_std_error()
    # raise_except()
    get_pass()
