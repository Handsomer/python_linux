#!/usr/local/bin/python
# -- coding: utf-8 -*-

"""
来源《python for linux System Administration and Automated Operation》
descript: section 3.4 使用logging 写日志
整理人： SW
时间：  20180802
"""


import logging
import logging.config


def use_logger():
    logging.config.fileConfig('logging.cnf')
    logging.debug('debug msg')
    logging.info('info msg')
    logging.warn('warn msg')
    logging.error('error msg')
    logging.critical('critical msg')
    


if __name__ == "__main__":
    use_logger()