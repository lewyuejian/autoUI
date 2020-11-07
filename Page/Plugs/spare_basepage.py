#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@file: spare_basepage.py
@time: 2020/11/1 0001 19:49
@desc:
'''
import time, datetime, os, sys

from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import Colorlog
from utils.readConfig import read_config


BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
if sys.platform == "win32":
    # 获取配置文件路径
    config_file_path = os.path.join(BASE_DIR, "conf", "config.ini").replace('/', '\\')
else:
    config_file_path = os.path.join(BASE_DIR, "conf", "config.ini")
images_dir = read_config(config_file_path, "Image","img_path")

log = Colorlog()


# 封装基本函数 - 执行日志、 异常处理、 截图
class BasePage(object):

    def __init__(self, driver):
        self.driver = driver

    # 截图
    def save_pictuer(self, doc=''):
        filePath = images_dir + '{0}_{1}.png'.format(doc, time.strftime('%Y-%m-%d_%H_%M_%S', time.localtime()))
        try:
            self.driver.save_screenshot(filePath)
            log.logger.info('{0}截图成功，图片路径为: {0}'.format(doc, filePath))
        except:
            log.logger.info('{0}截图 失败'.format(doc))

    # 等待页面元素可见
    def wait_eleVisible(self, locator, doc=''):
        try:
            start = datetime.datetime.now()
            WebDriverWait(self.driver, timeout=20, poll_frequency=0.5).until(EC.visibility_of_element_located(locator))
            end = datetime.datetime.now()
            wait_time = (end - start).seconds
            log.logger.info('{0},等待页面元素:{1}:可见，共耗时{2}s '.format(doc, locator, wait_time))
        except:
            log.logger.info('{0},等待页面元素:{1} 失败！！！'.format(doc, locator))
            self.save_pictuer(doc)

    # 等待页面元素存在
    def wait_elePresence(self):
        pass

    # 查找页面元素
    def get_element(self, locator, doc=''):
        print(locator)
        log.logger.info('{0},查找页面元素:{1}'.format(doc, locator))
        try:
            self.wait_eleVisible(locator, doc)
            return self.driver.find_element(*locator)
        except:
            log.logger.info('{0},查找页面元素:{1} 失败！！！'.format(doc, locator))
            raise

    # 点击页面元素
    def click_element(self, locator, doc=''):
        log.logger.info('{0},点击页面元素:{1}'.format(doc, locator))
        try:
            self.get_element(locator, doc).click()
        except:
            log.logger.info('点击页面元素:{0},失败！！！'.format(locator))
            raise

    # 输入操作
    def input_element(self, locator, key, doc=''):
        log.logger.info('{0},页面元素:{1} 输入值 {2}'.format(doc, locator, key))
        try:
            self.wait_eleVisible(locator, doc)
            self.get_element(locator, doc).send_keys(key)
        except:
            log.logger.info('{0},页面元素输入失败！！！'.format(doc))
            raise

    # 获取文本
    def get_element_text(self, locator, doc=''):
        log.logger.info('{0},获取页面元素:{1}'.format(doc, locator))
        try:
            self.wait_eleVisible(locator, doc)
            return self.get_element(locator, doc).text
        except:
            log.logger.info('{0},页面元素的文本获取失败！！！'.format(doc))
            raise

    # 获取页面元素属性
    def get_element_attribute(self, attr, locator, doc=''):
        log.logger.info('{0},获取页面元素属性:{1}'.format(doc, locator))
        try:
            self.wait_eleVisible(locator, doc)
            return self.get_element(locator, doc).get_attribute(attr)
        except:
            log.logger.info('{0},页面元素的属性获取 失败！！！'.format(doc))
            raise

    # alter 处理
    def alter_action(self):
        pass

    #iframe 切换
    def switch_iframe(self, locator, doc=''):
        log.logger.info('{0},切换页面表单:{1}'.format(doc, locator))
        try:
            self.wait_eleVisible(locator, doc)

            #
            # WebDriverWait(self.driver, timeout=20, poll_frequency=0.5).until(
            #     EC.frame_to_be_available_and_switch_to_it(*locator))
            try:
                WebDriverWait(self.driver, timeout=30, poll_frequency=0.5).\
                    until(EC.frame_to_be_available_and_switch_to_it(self.get_element(locator, doc)))
            except TimeoutException as t:
                log.logger.error('error: found "{}" timeout！'.format((locator), t))
            except NoSuchElementException as e:
                log.logger.error('error: no such "{}"'.format((locator), e))
            except Exception as e:
                raise e


        except:
            log.logger.error('{0},切换页面表单 失败！！！'.format(doc))
            raise

    # windows 切换
    def switch_window(self):
        pass

    # 上传操作
    def upload_file(self):
        pass

    # 滚动条处理

    def find_element(self, locator, timeout=10):
        try:
            log.logger.info("start find the elements {} by {}!".format(locator,self))
            element = WebDriverWait(self.driver, timeout).until(lambda driver: driver.find_element(locator))

        except TimeoutException as t:
            log.logger.error('error: found "{}" timeout!'.format((locator), t))
        except NoSuchElementException as e:
            log.logger.error('error: no such "{}"'.format((locator), e))
        except Exception as e:
            raise e
        else:
            return element

    # TODO: 定位一组元素
    def find_elements(self, by, locator, timeout=10):
        pass
