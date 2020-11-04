# _*_ coding: utf-8 _*_
#!/usr/bin/env python

import sys
import os
import shutil
import logging
from logging import handlers
from colorama import Fore,Style,init,Back



import datetime

BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

from utils.readConfig import IniConfig

if sys.platform == "win32":
    # 获取配置文件路径
    config_file_path = os.path.join(BASE_DIR, "conf", "config.ini").replace('/', '\\')
else:
    config_file_path = os.path.join(BASE_DIR, "conf", "config.ini")
# 超过了Python的最大递归深度
# sys.setrecursionlimit(1000000)


PROJECT_NAME = "autoUI"

class Colorlog(object):

    #init(autoreset=False,wrap=False)
    # 如果未设置autoreset=True，需要使用如下代码重置终端颜色为初始设置
    # print(Fore.RESET + Back.RESET + Style.RESET_ALL)  autoreset=True
    # init(autoreset=False) # 初始化，并且设置颜色设置自动恢复
    # windows终端输出颜色要使用
    # 避免所有的输出也打印一样的颜色，多打印一行 Style。RESET_ALL(关闭colorama的作用范围)
    # 在windows系统终端输出颜色要使用init(wrap=True)
    init(wrap=False)
    #Style.BRIGHT  字体加粗
    info_color = Fore.GREEN + Style.BRIGHT
    warn_color = Fore.YELLOW
    debug_color = Fore.MAGENTA + Style.BRIGHT
    error_color = Fore.RED + Style.BRIGHT
    critical_color = Fore.CYAN

    def __init__(self):
        ini_path = r"D:\CodeBase\SpaceSharkTT\conf\config.ini"

        self.cf = IniConfig()
        # 读取控制台日志开关
        self.console_switch = self.cf.read_log_config('LogConfig','ConsoleSwitch')[0]
        #print(self.console_switch)
        # 读取文件日志开关
        self.file_switch = self.cf.read_log_config('LogConfig','FileSwitch')[0]
        # 读取错误日志开关
        self.error_switch = self.cf.read_log_config('LogConfig','ErrorSwitch')[0]
        #print(self.error_switch)
        # 日志等级
        self.console_output_level = self.cf.read_log_config('LogConfig','ConsoleLevel')[0]
        self.file_output_level = self.cf.read_log_config('LogConfig','FileLevel')[0]
        self.error_output_level = self.cf.read_log_config('LogConfig','ErrorLevel')[0]
        #print(self.error_output_level)

        # 日志格式
        log_format = '%(asctime)s - %(pathname)s [line:%(lineno)d] - %(process)d - %(thread)d - %(name)s - %(levelname)s: %(message)s'
        #log_format = "%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s"
        filetime = datetime.datetime.now()
        self.logger = logging.getLogger(PROJECT_NAME + '-' + str(filetime.strftime('%Y_%m_%d')))

        self.logger.handlers = []

        self.logger.removeHandler(self.logger.handlers)
        # 在logger中添加日志句柄并返回，如果logger已经有句柄，则直接返回
        if not self.logger.handlers:
            # 配置日志等级
            self.logger.setLevel(logging.DEBUG)

            PROJECT_PATH = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
            print("项目目录：%s" % BASE_DIR)
            # 所有日志
            LOG_FILE = PROJECT_NAME + '-' + str(filetime.strftime('%Y_%m_%d') + '.log')
            # 错误日志 不要求日志切割
            ERROR_FILE = 'error.log'
            # 日志文件的绝对路径
            logfile_path = os.path.join(PROJECT_PATH,"OutPuts","logs",LOG_FILE)
            error_log_file_path = os.path.join(PROJECT_PATH,"OutPuts","logs",ERROR_FILE)

            print(os.path.join(PROJECT_PATH,"OutPuts","logs"))
            if not os.path.exists(os.path.join(PROJECT_PATH,"OutPuts","logs")):
                os.mkdir(os.path.join(PROJECT_PATH, "OutPuts","logs"))


            # 生成错误日志文件
            # 错误日志开关
            if self.error_switch:
                self.err_file_handler = logging.FileHandler(error_log_file_path, encoding='utf-8')
                self.err_file_handler.setLevel(self.error_output_level)
                err_format = "%(asctime)s - %(levelname)s - %(filename)s[:%(lineno)d] - %(message)s"

                self.err_file_handler.setFormatter(logging.Formatter(err_format))
                self.logger.addHandler(self.err_file_handler)


            # 控制台日志开关
            if self.console_switch:
                console_format = logging.Formatter(fmt=log_format, datefmt='%Y-%m-%d %H:%M:%S')
                console_handler = logging.StreamHandler()
                console_handler.setLevel(self.console_output_level)
                console_handler.setFormatter(console_format)

                self.logger.addHandler(console_handler)
            # 文件日志开关
            if self.file_switch:
                # backupCount 保存日志的数量，过期自动删除
                # when 按什么日志格式切分
                ## 每天创建一个日志文件，文件数不超过20个
                file_format = logging.Formatter(fmt=log_format)
                self.file_handler = handlers.TimedRotatingFileHandler(
                    logfile_path, when="D", interval=1, backupCount=20, encoding='utf-8')
                # self.file_handler = logging.FileHandler(logfile_path,encoding='utf-8')
                #self.file_handler.setLevel(self.file_output_level)
                self.file_handler.setFormatter(file_format)
                self.logger.addHandler(self.file_handler)

    # 有颜色的写法
    def warning(self,message):
        self.logger.warning(Colorlog.warn_color + str(message) + Style.RESET_ALL)
        self.logger.removeHandler(self.logger.handlers)

    def info(self,message):
        self.logger.info(Colorlog.info_color + str(message) + Style.RESET_ALL)
        self.logger.removeHandler(self.logger.handlers)

    def error(self,message):
        self.logger.error(Colorlog.error_color + str(message) + Style.RESET_ALL)
        self.logger.removeHandler(self.logger.handlers)

    def debug(self,message):
        self.logger.debug(Colorlog.debug_color + str(message) + Style.RESET_ALL)
        self.logger.removeHandler(self.logger.handlers)


    def critical(self,message):
        self.logger.critical(Colorlog.critical_color + str(message) + Style.RESET_ALL)
        self.logger.removeHandler(self.logger.handlers)



    # 以下皆为重写方法，并且每次记录后清除logger
    # 没有颜色写法
    # def info(self,message=None):
    #     #self.__init__()
    #     self.logger.info(message)
    #     self.logger.removeHandler(self.logger.handlers)
    #
    # def debug(self,message=None):
    #     #self.__init__()
    #     self.logger.debug(message)
    #     self.logger.removeHandler(self.logger.handlers)
    #
    # def warn(self,message=None):
    #     #self.__init__()
    #     self.logger.warning(message)
    #     self.logger.removeHandler(self.logger.handlers)
    #
    # def error(self,message=None):
    #     #self.__init__()
    #     self.logger.error(message)
    #     self.logger.removeHandler(self.logger.handlers)
    #
    # def critical(self,message=None):
    #     self.__init__()
    #     self.logger.critical(message)
    #     self.logger.removeHandler(self.logger.handlers)

if __name__ == '__main__':
    log = Colorlog()
    log.info('12334')
    log.warning('异常')
    log.error('yic')
    log.debug('官方调式')
    log.info(os.path.dirname(__file__))





