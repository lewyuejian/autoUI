#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@file: tackle.py
@time: 2020/11/1 0001 1:26
@desc: 应对、工具
'''
# 自动化回放快慢
# 实现思路
# 1.一般写selenium会自定义findelement函数，来实现查找元素。
#
# 2.在查找函数上加个睡眠时间的装饰器，函数执行完等待若干秒
#
# 3.同理可以举一返三的使用，装饰器，可以实现很多的功能。
import time, os, sys
from functools import wraps
from utils.logger import Colorlog
from utils.readConfig import read_config

BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
if sys.platform == "win32":
    # 获取配置文件路径
    config_file_path = os.path.join(BASE_DIR, "conf", "config.ini").replace('/', '\\')
else:
    config_file_path = os.path.join(BASE_DIR, "conf", "config.ini")
images_dir = read_config(config_file_path, "Image","img_path")

log = Colorlog()


def replay(retime):
    """
    设置回放时间，装饰器
    :param retime: 回放时间,毫秒
    :return: 无
    """
    def _wrapper(func):
        def wrapper(*args,**kwargs):
            ret=func(*args,**kwargs)
            time.sleep(float(retime)/1000)
            return ret
        return wrapper
    return _wrapper

# def Screen(function):
#     @wraps(function)
#     def inner(self,*args, **kwargs):
#         #result = ''
#         try:
#             result = function(self,*args, **kwargs)
#         except:
#             #filePath = images_dir + '{0}.png'.format(time.strftime('%Y-%m-%d_%H_%M_%S', time.localtime()))
#             filePath = r'D:\CodeBase\auto\autoUI\OutPuts\images\imgs\%s.png'% time.strftime("%Y-%m-%d_%H_%M_%S")
#             print(function.__name__filePath)
#             self.driver.get_screenshot_as_file('%s.png' % (function.__name__filePath))
#         else:
#             log.info (" %s 脚本运行正常" % (function.__name__))
#         return result
#     return inner

class Screen(object):
    def __init__(self, driver):
        self.driver = driver

    def __call__(self, func):
        def inner(*args, **kwargs):
            try:
                func(*args, **kwargs)
            except:
                import time
                filePath = images_dir + '{0}.png'.format(time.strftime('%Y-%m-%d_%H_%M_%S', time.localtime()))
                self.driver.get_screenshot_as_file("{0}.png".format(filePath))
                raise
        return inner


# @replay(500)   #等待500毫秒
# def find_element(self,*loc):
#         """
#         在指定时间内，查找元素；否则抛出异常
#         :param loc: 定位器
#         :return: 元素 或 抛出异常
#         """
#         TimeOut = 20
#         try:
#             self.driver.implicitly_wait(TimeOut) #智能等待；超时设置
#
#             element = self.driver.find_element(*loc) #如果element没有找到，到此处会开始等待
#             if self.isDisplayTimeOut(element,TimeOut):
#                 self.hightlight(element)  #高亮显示
#                 self.driver.implicitly_wait(0)  # 恢复超时设置
#                 return element
#             else:
#                 raise ElementNotVisibleException #抛出异常，给except捕获
#
#         except (
#                 NoSuchElementException,
#                 ElementNotVisibleException
#                 ) as ex:
#             self.getImage
#             raise ex
#         else:
#             self.getImage

