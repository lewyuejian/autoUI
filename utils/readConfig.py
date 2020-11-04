#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@file: readConfig.py
@time: 2020/10/11 0011 21:01
@desc:
'''

from configparser import ConfigParser

import os, sys
import re
from utils import exceptions

# 获取上级目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

if sys.platform == "win32":
    # 获取配置文件路径
    config_file_path = os.path.join(BASE_DIR, "conf", "config.ini").replace('/', '\\')
else:
    config_file_path = os.path.join(BASE_DIR, "conf", "config.ini")

class IniConfig:
    def __init__(self):

        self.cf = ConfigParser()
        self.cf.read(config_file_path, encoding='utf-8')

    def get_driver_config(self):
        #self.cf.read(os.path.join(os.environ['INIHOME'], 'iselenium.ini'))
        from utils.Initial_check import platformSystem

        if platformSystem() == 'Windows':
            return self.cf.get('Driver', 'windows_chrome_driver')
        elif platformSystem() == 'Linux':
            return self.cf.get('Driver', 'linux_chrome_driver')

    def readConfig(self, section, option):
        value = ""
        try:
            value = self.cf.get(section, option)
        except exceptions.ValueNotFound:
            err_msg = u"未获取到配置 - {0}{1}".format(section, option)
            print(err_msg)
            value = ""
        return value

    def setConfig(self, section, option, value):
        try:
            self.cf.set(section, option, value)
            self.cf.write(open(config_file_path,'w'))
        except:
            return False
        return True




    # def read_config(self, option):
    #     # 获取某个section中所有的值，将其转化为字典
    #     items = dict(self.cf.items(option))
    #     return items


    def read_log_config(self, section=None, option=None):
        """
        异常处理语句 try ... except ...
        在except代码块中不抛出异常，而是打印异常栈，并使用默认的配置值。这样做是为了保证框架的健全性，不会因为读取配置文件出错时退出。
        :param section:
        :param option:
        :return:
        """
        value = []
        try:
            if option == 'ConsoleSwitch':
                _console_switch = self.cf.get('LogConfig','ConsoleSwitch')
                ConsoleSwitch = True if _console_switch != 'False' else False
                value.append(ConsoleSwitch)
            elif option == 'FileSwitch':
                _file_switch = self.cf.get('LogConfig','FileSwitch')
                FileSwitch = True if _file_switch != 'False' else False
                value.append(FileSwitch)
            elif option == 'ErrorSwitch':
                _error_switch = self.cf.get('LogConfig','ErrorSwitch')
                ErrorSwitch = True if _error_switch != 'False' else False
                value.append(ErrorSwitch)
            elif option == 'ConsoleLevel':
                ConsoleLevel = self.cf.get('LogConfig','ConsoleLevel')
                value.append(ConsoleLevel)
            elif option == 'ErrorLevel':
                ErrorLevel = self.cf.get('LogConfig','ErrorLevel')
                value.append(ErrorLevel)
            else:
                FileLevel = self.cf.get('LogConfig','FileLevel')
                value.append(FileLevel)

        except Exception as e:
            print('[config.ini] read error,so use default - {0}'.format(e))
            log_conf = {
                'ConsoleSwitch': True,
                'FileSwitch': True,
                'ErrorSwitch': True,
                'ConsoleLevel': 'INFO',
                'FileLevel': 'DEBUG',
                'ErrorLevel': 'ERROR',
            }

            value.append(log_conf[option])
        return value

def read_config(config_file_path, section, option):
    rf = ConfigParser()
    try:
        rf.read(config_file_path, encoding='utf-8-sig')
        if sys.platform == "win32":
            result = rf.get(section, option).replace('base_dir',str(BASE_DIR)).replace('/','\\')
        else:
            result = rf.get(section, option).replace('base_dir', str(BASE_DIR))
    except:
        sys.exit(1)
    return  BASE_DIR + os.path.sep + result

def write_config(config_file_path, section, option ,value):
    wf = ConfigParser()
    try:
        wf.read(config_file_path)
        wf.set(section, option, value)
        wf.write(open(config_file_path, 'w'))
    except:
        sys.exit(1)
    return True



#因为在测试的时候涉及到对测试数据的参数化配置，这就会涉及到参数的替换，所以我单独写了一个类来进行参数替换，使用正则表达式的方法，调用起来比较的方便，比用replace的方法要方便一点。
class Regular():
    def regular(self, old_str, new_str, param):
        old_str = str(old_str)
        if re.search(old_str,str(param)) != None:
            result = re.sub(old_str,new_str,param)
            return result
        else:
            return param

class IniCfg():
    def __init__(self):
        self.conf = ConfigParser()
        self.cfgpath = ''

    def check_section(self, section):
        try:
            self.conf.items(section)
        except Exception:
            print(">> 无此section，请核对[%s]" % section)
            return None
        return True

    # 读取ini，并获取所有的section名
    def readSectionItems(self, cfgpath):
        if not os.path.isfile(cfgpath):
            print(">> 无此文件，请核对路径[%s]" % cfgpath)
            return None
        self.cfgpath = cfgpath
        self.conf.read(cfgpath, encoding="utf-8")
        return self.conf.sections()

    # 读取一个section，list里面对象是元祖
    def readOneSection(self, section):
        try:
            item = self.conf.items(section)
        except Exception:
            print(">> 无此section，请核对[%s]" % section)
            return None
        return item

    # 读取一个section到字典中
    def prettySecToDic(self, section):
        if not self.check_section(section):
            return None
        res = {}
        for key, val in self.conf.items(section):
            res[key] = val
        return res

    # 读取所有section到字典中
    def prettySecsToDic(self):
        res_1 = {}
        res_2 = {}
        sections = self.conf.sections()
        for sec in sections:
            for key, val in self.conf.items(sec):
                res_2[key] = val
            res_1[sec] = res_2.copy()
            res_2.clear()
        return res_1

    # 删除一个 section中的一个item（以键值KEY为标识）
    def removeItem(self, section, key):
        if not self.check_section(section):
            return
        self.conf.remove_option(section, key)

    # 删除整个section这一项
    def removeSection(self, section):
        if not self.check_section(section):
            return
        self.conf.remove_section(section)

    # 添加一个section
    def addSection(self, section):
        self.conf.add_section(section)

    # 往section添加key和value
    def addItem(self, section, key, value):
        if not self.check_section(section):
            return
        self.conf.set(section, key, value)

    # 执行write写入, remove和set方法并没有真正的修改ini文件内容，只有当执行conf.write()方法的时候，才会修改ini文件内容
    def actionOperate(self, mode):
        if mode == 'r+':
            self.conf.write(open(self.cfgpath, "r+", encoding="utf-8"))  # 修改模式
        elif mode == 'w':
            self.conf.write(open(self.cfgpath, "w"))  # 删除原文件重新写入
        elif mode == 'a':
            self.conf.write(open(self.cfgpath, "a"))  # 追加模式写入

if __name__ == '__main__':

    filepath = r"D:\CodeBase\auto\autoUI\conf\config.ini"
    # a = IniConfig(filepath).read_log_config('LogConfig','ConsoleSwitch')
    # print(a[0])
    a = IniConfig().readConfig('URL','test_url')
    print(a)

