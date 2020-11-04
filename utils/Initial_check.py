#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@file: Initial_check.py
@time: 2020/10/27 0027 21:32
@desc:
'''

import platform,os
from utils.logger import Colorlog

BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

log = Colorlog()

# 检测操作系统


def platformSystem():

    log.info('----------Operation System--------------------------')
    log.debug(platform.architecture())
    oper_system = platform.system()
    #oper_system = sys.platform

    log.debug('Operation System - {0}'.format(oper_system))
    return oper_system

# python 版本号
def pythonVersion():
    log.info('--------------Python Version-------------------------')
    python_version = platform.python_version()
    log.debug('Python Version - {0}'.format(python_version))
    return python_version

if __name__ == '__main__':
    platformSystem()
