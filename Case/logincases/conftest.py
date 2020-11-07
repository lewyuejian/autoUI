#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@file: conftest.py
@time: 2020/10/29 0029 22:13
@desc:
'''
from time import sleep

import pytest
from utils.logger import Colorlog
from PageObjects.LoginPage.login_page import LoginPage

log = Colorlog()

#driver = None

@pytest.fixture(scope='class')
def start_module(project_module_start):
    log.logger.info("==========开始执行测试用例集===========")
    global driver
    driver = project_module_start
    # bg = BasePage(driver)
    # bg.openPage()
    lg = LoginPage(driver)
    yield (driver, lg)
    log.logger.info("==========结束执行测试用例集===========")
    driver.quitBrowser()

@pytest.fixture(scope='class')
def start_session(project_session_start):
    '''
    所有模块只打开一次浏览器
    :param project_session_start: 所有模块只打开一次浏览器
    :return: driver lg
    '''
    log.logger.info("==========开始执行测试用例集===========")
    global driver
    driver = project_session_start

    log.logger.info("-------------------- " + str(driver) + " ------------------------")
    # bg = BasePage(driver)
    # bg.openPage()

    lg = LoginPage(driver)
    yield (driver,lg)

    log.logger.info("==========结束执行测试用例集===========")


# @pytest.fixture()
# def refresh_page():
#     yield
#     driver.refresh()
#     sleep(3)