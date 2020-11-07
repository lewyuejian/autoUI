#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@file: login_page.py
@time: 2020/10/31 0031 1:37
@desc:
'''
from Page.Plugs.BasePage import BasePage
from Locators.LoginLocators.login_locators import LoginLocator as loc
import allure


class LoginPage(BasePage):
    def __init__(self, driver):
        super(LoginPage, self).__init__(driver)
        self.driver = driver
    # 登录
    @allure.feature("登录功能")
    def login(self, username, password):
        doc = '登录页面_登录功能'
        self.click_element(self.driver, loc.login_btn_entry_loc, doc)
        self.switch_iframe(self.driver, loc.switch_login_with_account, doc)
        self.click_element(self.driver, loc.login_with_account, doc)
        with allure.step("输入用户名"):
            self.input_element(self.driver, loc.username_loc, username, doc)
        with allure.step("输入密码"):
            self.input_element(self.driver, loc.password_loc, password, doc)
        self.click_element(self.driver, loc.login_btn_loc, doc)
        #self.switch_default_iframe(self.driver, doc)

    def isPasswordMissing(self):
        doc = '登录页面_获取登录失败提示'
        try:
            with allure.step("获取登录失败的提示"):

                text = self.get_element_text(self.driver, loc.error_msg_loc, doc)
                print(text)
                if text == "请输入密码":
                    return True
        except:
            return False
