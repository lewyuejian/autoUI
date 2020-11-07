#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@file: login_locators.py
@time: 2020/10/30 0030 23:22
@desc:
'''

class LoginLocator:
    login_btn_entry_loc = ("xpath=>//header[@class='pm--metabar']//div/div[4]/span")
    switch_login_with_account = ("xpath=>//iframe[starts-with(@id, 'top_login_frame')]")
    login_with_account = ("xpath=>//div[@class='tc-lo-main height515']/div[3]")
    username_loc = ("xpath=>//div[@class='password-login-content wcc-small-form']/form/ul/li/input")
    password_loc = ("xpath=>//div[@class='password-login-content wcc-small-form']/form/ul/li[2]/input")
    login_btn_loc = ("xpath=>//div[@class='password-login-content wcc-small-form']/form/p")
    error_msg_loc = ("xpath=>//div[@class='password-login-content wcc-small-form']/form/div/p")