#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@file: conftest.py
@time: 2020/10/29 0029 22:20
@desc:
'''
import pytest

from utils.logger import Colorlog
from Page.Plugs.BrowserEngine import BrowserEngine


log = Colorlog()

driver = None

@pytest.fixture(scope='session')
def project_session_start():
    log.logger.info("==========开始 UI自动化项目 执行测试===========")
    global driver
    be = BrowserEngine()
    driver = be.openBrowser()
    yield driver
    log.logger.info("==========结束 UI自动化项目 测试===========")

@pytest.fixture(scope='module')
def project_module_start():
    log.logger.info("==========开始 XX模块 执行测试===========")
    global driver
    be = BrowserEngine()
    driver = be.openBrowser()

    yield driver
    #be.quitBrowser()
    log.logger.info("==========结束 XX模块 测试===========")

@pytest.fixture()
def project_func():
    print("project_func")



def pytest_configure(config):
    # 标签名集合
    marker_list = ['smoke', 'lucas']
    for markers in marker_list:
        config.addinivalue_line('markers', markers)