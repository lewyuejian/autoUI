#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@file: login_page.py
@time: 2020/10/31 0031 1:37
@desc:
'''
from Page.Plugs.BasePage import BasePage
from Locators.LoginLocators.login_locators import LoginLocator as loc



class LoginPage(BasePage):
    def __init__(self, driver):
        super(LoginPage, self).__init__(driver)
        self.driver = driver
    # 登录

    def login(self, username, password):
        doc = '登录页面_登录功能'
        self.click_element(self.driver, loc.login_btn_entry_loc, doc)
        self.switch_iframe(self.driver, loc.switch_login_with_account, doc)
        self.click_element(self.driver, loc.login_with_account, doc)
        self.input_element(self.driver, loc.username_loc, username, doc)
        self.input_element(self.driver, loc.password_loc, password, doc)
        self.click_element(self.driver, loc.login_btn_loc, doc)
        self.switch_default_iframe(self.driver, doc)
