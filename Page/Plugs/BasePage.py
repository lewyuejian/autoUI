#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@file: BasePage.py
@time: 2020/10/27 0027 22:17
@desc:
'''

import os
import sys
import time
import datetime
from selenium.webdriver.support.select import Select
from PIL import Image,ImageEnhance
import pytesseract

from utils import exceptions
from utils.logger import Colorlog
from utils.readConfig import IniConfig,read_config
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from Page.Plugs.WebDriver import WebDriver as wd



BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
if sys.platform == "win32":
    # 获取配置文件路径
    config_file_path = os.path.join(BASE_DIR, "conf", "config.ini").replace('/', '\\')
else:
    config_file_path = os.path.join(BASE_DIR, "conf", "config.ini")
images_dir = read_config(config_file_path, "Image","img_path")

verify_code = read_config(config_file_path, "VerifyCode","verify_code_path")

log = Colorlog()

class BasePage(object):
    def __init__(self, driver):


        self.driver = driver


    def save_pictuer(self, doc=''):
        filePath = images_dir + '{0}_{1}.png'.format(doc, time.strftime('%Y-%m-%d_%H_%M_%S', time.localtime()))
        try:
            self.driver.save_screenshot(filePath)
            log.logger.info('{0}截图成功，图片路径为: {0}'.format(doc, filePath))
        except:
            log.logger.info('{0}截图 失败'.format(doc))

    def get_screen_as_file(self, func):
        u"""异常自动截图"""
        def inner(*args, **kwargs):
            try:
                func(*args, **kwargs)
            except:
                self.save_pictuer()
                raise
        return inner



    # 等待页面元素可见
    def wait_eleVisible(self, locator, doc=''):
        try:
            start = datetime.datetime.now()
            WebDriverWait(self.driver, timeout=10, poll_frequency=0.5).until(
                EC.visibility_of_element_located(locator))
            end = datetime.datetime.now()
            wait_time = (end - start).seconds
            log.logger.info('{0},等待页面元素:{1}:可见，共耗时{2}s '.format(doc, locator, wait_time))
        except TimeoutException as t:
            log.logger.error('{0} - 等待页面元素超时！'.format((locator), t))
        except:
            log.logger.error('{0} - 等待页面元素:{1} 失败！！！'.format(doc, locator))
            self.save_pictuer(doc)

    # 等待页面元素存在，不可见
    def wait_elePresence(self,locator, doc=''):
        try:
            start = datetime.datetime.now()
            WebDriverWait(self.driver, timeout=10, poll_frequency=0.5).until(
                EC.presence_of_element_located(locator)
            )
            end = datetime.datetime.now()
            wait_time = (end - start).seconds
            log.logger.info('{0} - 等待页面元素存在:{1}:不可见，共耗时{2}'.format(doc, locator, wait_time))
        except TimeoutException as t:
            log.logger.error('{0} - 等待页面加载超时！'.format((locator), t))
        except:
            log.logger.error('{0} - 等待页面元素:{1} 失败！！！'.format(doc, locator))
            self.save_pictuer(doc)


    # 查找页面元素
    def get_element(self, driver, by, doc=''):
        log.logger.debug(by)
        log.logger.info('{0} - 查找页面元素:{1}'.format(doc, by))
        try:
            self.wait_eleVisible(by, doc)
            return wd.find_element(driver, by)
        except:
            log.logger.error('{0},查找页面元素:{1} 失败！！！'.format(doc, by))
            raise (NoSuchElementException, TimeoutException)


    def click_element(self, driver, by, doc=''):
        #self.wait_eleVisible(way, doc)
        log.logger.info('{0} - 点击页面元素:{1}'.format(doc, by))
        try:
            element = wd.get_clickable_element(driver, by)
            element.click()
        except:
            log.logger.error('点击页面元素:{0},失败！！！'.format(by))
            raise

    # 输入操作
    def input_element(self, driver, by, value, doc=''):
        log.logger.info('{0} - 页面元素:{1} 输入值 {2}'.format(doc, by, value))
        try:
            element = wd.get_clickable_element(driver, by)
            element.send_keys(value)
        except:
            log.logger.error('{0} - 页面元素输入失败！！！'.format(doc))
            raise

    # 获取文本
    def get_element_text(self, driver, by, doc=''):
        log.logger.info('{0} - 获取页面元素:{1}'.format(doc, by))
        try:
            element = wd.find_element(driver, by).text
            return element
        except:
            log.logger.error('{0},页面元素的文本获取失败！！！'.format(doc))
            raise


    # 获取页面元素属性
    # TODO: 未修复bug，未加预期值
    def get_element_attribute(self, driver, by, name, doc=''):
        log.logger.info('{0},获取页面元素属性:{1}'.format(doc, by))
        try:
            element = wd.get_attribute_element(driver, by, name)
            return element
        except:
            log.logger.error('{0},页面元素的属性获取 失败！！！'.format(doc))
            raise

    # alter 处理
    def alter_action(self, driver, doc=''):
        log.logger.info('{0} - 处理页面的alter'.format(doc))
        try:
            element = wd.get_alert_is_present(driver)
            content = element.text
            log.logger.info('{0} - alter的内容:{1}'.format(doc, content))
            # 接受alter
            element.accept()
            return content
        except:
            log.logger.error('{0} - 页面元素的alter获取 失败！！！'.format(doc))
            raise


    def switch_iframe(self, driver, by, doc=''):
        log.logger.info('{0} - 切换页面表单:{1}'.format(doc, by))
        try:

            wd.get_switch_iframe_element(driver,by)
        except TimeoutException as t:
            log.logger.error('error: found "{}" timeout！'.format((by), t))
        except NoSuchElementException as e:
            log.logger.error('error: no such "{}"'.format((by), e))
        except Exception as e:
            raise e


    # 切换到主页面
    def switch_default_iframe(self, driver, doc=''):
        log.logger.info('{0} - 切回主页面 - switch back to default iframe'.format(doc))
        try:
            driver.switch_to.default_content()
        except:
            log.logger.error('{0} - 切换到主页面 失败！！！'.format(doc))
            raise

    def forward(self,driver):
        u"""前进到新窗口"""
        driver.forward()

    def back(self, driver):
        u"""返回到旧的窗口"""
        driver.back()

    def get_title(self, driver):
        u"""获取当前窗口的title"""
        return driver.title

    def get_current_url(self, driver):
        u"""获取当前页面的url"""
        return driver.current_url

    def get_browser_log_level(self, driver):
        u"""获取浏览器错误日志级别"""
        lists = driver.get_log("browser")
        list_value = []
        if lists.__len__() != 0:
            for dicts in lists:
                for key, value in dicts.items():
                    list_value.append(value)
        if 'SERVER' in list_value:
            return "SERVER"
        elif 'WARNING' in list_value:
            return "WARNING"
        return "SUCCESS"

    # 执行js
    def js_execute(self, driver, jsxt):
        log.logger.info('{0} - 开始执行 js ......')
        driver.execute_script(jsxt)

    # 聚焦元素
    def js_fours_element(self, driver, by, doc=''):
        log.logger.info('{0} - 聚焦元素'.format(doc))
        try:
            element = wd.find_element(driver, by)
            driver.execute_script("arguments[0].scrollIntoView();",element)
        except:
            log.logger.error('{0} - 聚焦元素失败！！！'.format(doc))

    # 滑动到页面顶部
    def js_scroll_top(self, driver):
        js = "window.scrollTo(0,0)"
        driver.execute_script(js)

     # 滑动到页面底部
    def js_scroll_end(self, driver):
        js = "window.scrollTo(0,document.body.scrollHeight)"
        driver.execute_script(js)

    def slect_by_index(self, driver, by, index):
        u"""通过多有index，0开始，定位元素"""
        element = wd.find_element(driver, by)
        Select(element).select_by_index(index)

    def select_by_value(self, driver, by, value):
        u"""通过value定位元素"""
        element = wd.find_element(driver, by)
        Select(element).select_by_value(value)

    def select_by_text(self, driver, by, text):
        u"""通过text定位元素"""
        element = wd.find_element(driver, by)
        Select(element).select_by_visible_text(text)

    def get_verify_code(self, driver, by):
        u"""获取图片验证码"""
        # 验证码图片保存地址
        screenImg = verify_code
        # 浏览器页面截图
        driver.get_screenshot_as_file(screenImg)
        # 定位验证码大小
        location = wd.find_element(driver, by).location
        size = wd.find_element(driver, by).size

        left = location['x']
        top = location['y']
        right = location['x'] + size['width']
        bottom = location['y'] + size['height']

        # 从文件读取截图，截取验证码位置再次保存
        img = Image.open(screenImg).crop((left, top, right, bottom))
        img.convert('L') # 转换模式：L|RGB
        img = ImageEnhance.Contrast(img) # 增加对比度
        img = img.enhance(2.0) # 增加饱和度
        img.save(screenImg)
        # 再次读取验证码
        img = Image.open(screenImg)
        time.sleep(1)
        code = pytesseract.image_to_string(img)
        return code

    # # windows 切换
    def switch_window(self):
        pass

    # 上传操作
    def upload_file(self):
        pass

    # 滚动条处理



    # 鼠标悬浮
    #https://blog.logger.csdn.net/qq969887453/article/details/89607331
    def move_actionchains_element(self, driver, by, doc=''):
        log.logger.info('{0} - 鼠标悬停操作'.format(doc))
        try:
            element = wd.find_element(driver, by)
            ActionChains(self.driver).move_to_element(element).perform()
        except:
            log.logger.error('{0} - 鼠标悬停操作 失败！！！'.format(doc))
            raise

    # 获取翻页的列表数据
    #https://blog.logger.csdn.net/u014703798/article/details/85003546
