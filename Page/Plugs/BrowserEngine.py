#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@file: BrowserEngine.py
@time: 2020/10/27 0027 22:30
@desc:
'''
import os, sys
from telnetlib import EC

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from utils import exceptions
from utils.logger import Colorlog
from utils.readConfig import IniConfig,read_config
from selenium.webdriver.chrome.options import Options
BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
if sys.platform == "win32":
    # 获取配置文件路径
    config_file_path = os.path.join(BASE_DIR, "conf", "config.ini").replace('/', '\\')
else:
    config_file_path = os.path.join(BASE_DIR, "conf", "config.ini")
images_dir = read_config(config_file_path, "Image","img_path")

log = Colorlog()

# 封装浏览器引擎
class BrowserEngine(object):
    def __init__(self):


        # 加一个debug的选项
        self.chrome_options = Options()
        # 和浏览器打开的调试端口进行通信
        # 浏览器要使用 --remote-debugging-port=9222 开启调试
        #self.chrome_options.debugger_address = "127.0.0.1:9222"
        # chrome传入复用参数,没有传入的话，会导致执行时重新打开一个新的浏览器窗口
        # self.driver = webdriver.Chrome(options=chrome_options)
        # 所谓浏览器的无头模式headless，就是浏览器在运行时处于后台操作的模式，不会看到浏览器打开，也就不会干扰你手头的工作。对于自动化测试和网络爬虫都有很大的价值。


    def openBrowser(self):
        u"""打开浏览器 - 最大化 - 隐式等待 - 判断title是否为预期"""
        global driver
        browser_type = read_config(config_file_path, 'BrowserType', 'browserName')
        log.info('You had select {0} - browser.'.format(browser_type))

        cf = IniConfig()
        url = cf.readConfig('URL', 'test_url')

        #driver_path = os.path.dirname(os.path.abspath('..'))
        chrome_driver_path = BASE_DIR + os.sep + 'lib' + os.sep + 'driver' + os.sep + 'chromedriver.exe'
        try:
            if browser_type == 'Chrome':

                driver = webdriver.Chrome(executable_path=chrome_driver_path, options=self.chrome_options)
            elif browser_type == 'Firefox':
                firefox_driver_path = BASE_DIR+ os.sep + 'lib' + os.sep + 'driver' + os.sep + 'geckodriver.exe'
                driver = webdriver.Firefox(executable_path=firefox_driver_path)
            # 早期我们使用 phantomJS 浏览器来实现这种模式，随着 Chrome 和 Firefox 都加入了无头模式， Selenium 逐渐停止对 phantomJS 的支持。
            # elif browser_type == 'headless':
            #     driver = webdriver.PhantomJS()
            elif browser_type == 'ch-headless':

                self.chrome_options.add_argument("--headless")  # => 为Chrome配置无头模式
                driver = webdriver.Chrome(executable_path=chrome_driver_path, options=self.chrome_options)
            elif browser_type == 'ff-headless':
                # Firefox 浏览器的无头模式配置与 Chrome 差不多，只是写法有差异。
                from selenium.webdriver.firefox.options import Options  # => 引入Firefox配置
                firefox_driver_path = BASE_DIR + os.sep + 'lib' + os.sep + 'driver' + os.sep + 'geckodriver.exe'
                ff_options = Options()
                ff_options.headless = True  # => 设置无头模式为 True
                driver = webdriver.Firefox(executable_path=firefox_driver_path, firefox_options=ff_options)  # => 注意这里的参数
            elif browser_type == 'IE':
                driver = webdriver.Ie()
            else:
                driver = webdriver.Chrome(executable_path=chrome_driver_path)
                log.debug('Not found the browser - 默认使用Chrome<有界面>')
            driver.maximize_window()
            log.info("Maximize the current window.")
            driver.implicitly_wait(5)
            log.info("Set implicitly wait 10 seconds.")
            driver.get(url)
            log.info("Visit the web url - {0}.".format(url))
            # 判断title是否为预期
            #WebDriverWait(driver, 10, 1).until(EC.title_contains(title))

            return driver
        except exceptions.BrowserNotFound:
            err_msg = u"BrowserError: Get Browser Engine error - {0}".format(browser_type)
            log.error(err_msg)


    def quitBrowser(self):
        """
        退出浏览器
        """
        try:
            self.openBrowser().quit()
            log.info("Exit the browser...")
        except exceptions.QuitUpError as e:
            log.error('Failed to quit the browser - {0}'.format(e))

    def closeBrowser(self):
        try:
            self.openBrowser().close()
            log.info("ShutDown the browser...")
        except exceptions.CloseUpError as e:
            log.error('Failed to closed the browser - {0}'.format(e))

