#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@file: user_management_page.py
@time: 2020/10/31 0031 1:56
@desc:
'''
import allure
from Page.Plugs.BasePage import BasePage
from Locators.UserMgLocators.user_mg_locators import UserMgLocator as loc

class UserMgPage(BasePage):

    def isCheck_login_ele(self):
        doc = '用户管理页面_验证登录功能'
        self.move_actionchains_element(self.driver, loc.avatar_loc, doc)

    def isExist_logout_ele(self):
        try:
            doc = '用户管理页面_验证登录功能'
            self.move_actionchains_element(self.driver, loc.avatar_loc, doc)
            text = self.get_element_text(self.driver, loc.logout_loc, doc)
            print(text)
            if text == '退出登录':
                return True
        except:
            return False

    @allure.feature("退出功能")
    def logout(self):
        doc = '用户管理页面_退出功能'
        self.click_element(self.driver, loc.logout_loc, doc)