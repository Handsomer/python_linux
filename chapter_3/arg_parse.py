# -- coding: utf-8 -*-

"""
来源《python for linux System Administration and Automated Operation》
descript: section 3.3 使用argparse 解析命令行参数
整理人： SW
时间：  20180801
"""


from __future__ import print_function
import argparse


def _argparse():
    """
    section: chapter 3.3
    descript: 解析命令行参数
    """
    parser = argparse.ArgumentParser(description="This is description")
    parser.add_argument("--host", action='store', dest='server',
                        default='localhost', help='connect to host')
    parser.add_argument('-t', action='store_true', default=False,
                        dest='boolean_switch', help='set a switch to true')
    return parser.parse_args()


if __name__ == "__main__":
    parser = _argparse()
    print(parser)
    print('host = ', parser.server)
    print('boolean_switch=', parser.boolean_switch)
