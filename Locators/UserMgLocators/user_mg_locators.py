#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@file: user_mg_locators.py
@time: 2020/10/31 0031 2:01
@desc:
'''
from selenium.webdriver.common.by import By

class UserMgLocator:
    # 头像
    avatar_loc = ("xpath=>//header[@class='pm--metabar']/div/div/div[5]/img")
    logout_loc = ("xpath=>//header[@class='pm--metabar']/div/div/div[5]/div/div[2]/div[2]/div[2]/a")