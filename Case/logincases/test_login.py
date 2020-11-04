#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@file: test_login.py
@time: 2020/10/28 0028 23:54
@desc:
'''
import os, sys
import pytest
from utils.logger import Colorlog
from TestDatas.LoginDatas import login_datas as LD
from PageObjects.UserMgPage.user_management_page import UserMgPage


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(BASE_DIR)
if sys.platform == "win32":
    # 获取配置文件路径
    config_file_path = os.path.join(BASE_DIR, "conf", "config.ini").replace('/', '\\')
else:
    config_file_path = os.path.join(BASE_DIR, "conf", "config.ini")

log = Colorlog()

@pytest.mark.usefixtures('start_session')
class TestLogin:

    # 正常用例

    @pytest.mark.lucas
    @pytest.mark.smoke

    def test_login_success(self, start_session):
        log.info(" 执行 {0} 测试用例 ".format(sys._getframe().f_code.co_name))
        log.info("<<正常登录测试用例>>")
        start_session[1].login(LD.success_data['username'], LD.success_data['password'])
        log.info("期望值：{0}".format(True))
        log.info("实际值：{0}".format(UserMgPage(start_session[0]).isExist_logout_ele()))
        try:
            assert UserMgPage(start_session[0]).isExist_logout_ele()
            log.info(" 结束执行 {0} 测试用例， 测试结果 --- PASS ".format(sys._getframe().f_code.co_name))
            start_session[1].save_pictuer("{0}-正常截图".format(LD.success_data['name']))
        except:
            log.error(" 结束执行 {0} 测试用例， 测试结果 --- False ".format(sys._getframe().f_code.co_name))
            start_session[1].save_pictuer("{0}-异常截图".format(LD.success_data['name']))
            raise

    def test_add(self):
        print('123')