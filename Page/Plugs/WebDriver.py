#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@file: WebDriver.py
@time: 2020/10/31 0031 20:16
@desc:
'''

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import Colorlog

log = Colorlog()

class WebDriver:

    @staticmethod
    def find_element(driver, way):
        """
        by_list = {
                'id',
                'name',
                'className',
                'xpath',
                'css',
                'tagName',
                'linkText',

        }
        https://www.cnblogs.com/guanyf/p/13654159.html
        https://blog.csdn.net/qq_45426233/article/details/99870333
        如果定位方式by没有在by_list中，默认使用xpath定位
        :param driver:
        :param way:
        :return:
        """

        #timeout_error = "定位元素超时，请尝试其它定位方式"
        if "=>" in way:
            by = way[:way.find('=>')]
            element = way[way.find('=>') + 2:]
            if by == "" or element == "":
                # 语法错误，参考id=>element.
                raise NameError("Grammatical errors, reference: 'id=>element'.")

            if by == 'ID':
                return driver.find_element_by_id(element)
            elif by == 'name':
                return driver.find_element_by_name(element)
            elif by == 'className':
                return driver.find_element_by_class_name(element)
            elif by == 'css':
                return driver.find_element_by_css_selector(element)
            elif by == 'tagName':
                return driver.find_element_by_tag_name(element)
            elif by == 'linkText':
                return driver.find_element_by_link_text(element)
            else:
                return driver.find_element_by_xpath(element)
        else:
            xpath = "//*[text()='{}']".format(way)
            return driver.find_element_by_xpath(xpath)

    @staticmethod
    def get_title(driver, title):
        wait = WebDriverWait(driver, 10, 1)
        try:
            wait.until(EC.title_contains(title))
        except TimeoutException as t:
            log.error('OPEN {0} title error'.format(t))
        except Exception as e:
            log.error('Error - {0}'.format(e))

    @staticmethod
    def get_clickable_element(driver, way):
        """
        判断某个元素中是否可见并且是enable的，代表可点击

        元素不可见，就会引发TimeoutException的异常
        :param driver:
        :param way:
        :return:
        """
        wait = WebDriverWait(driver, 10)

        if "=>" in way:
            by = way[:way.find('=>')]
            value = way[way.find('=>') + 2:]
            if by == "" or value == "":
                # 语法错误，参考id=>element.
                raise NameError("Grammatical errors, reference: 'id=>element'.")

            if by == 'id':
                element = wait.until(EC.element_to_be_clickable((By.ID, value)))
                return element
            elif by == 'name':
                element = wait.until(EC.element_to_be_clickable((By.NAME, value)))
                return element
            elif by == 'className':
                element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, value)))
                return element
            elif by == 'css':
                element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, value)))
                return element
            elif by == 'tagName':
                element = wait.until(EC.element_to_be_clickable((By.TAG_NAME, value)))
                return element
            elif by == 'linkText':
                element = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, value)))
                return element
            else:
                element = wait.until(EC.element_to_be_clickable((By.XPATH, value)))
                return element
        else:
            xpath = "//*[text()='{}']".format(way)
            element = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
            return element

    # 判断指定的元素中是否包含了预期的字符串
    # TODO: 未修复bug，未加预期值
    @staticmethod
    def get_text_element(driver, way):
        wait = WebDriverWait(driver, 10)
        if "=>" in way:
            by = way[:way.find('=>')]
            value = way[way.find('=>') + 2:]
            if by == "" or value == "":
                # 语法错误，参考id=>element.
                raise NameError("Grammatical errors, reference: 'id=>element'.")
            if by == 'id':
                element = wait.until(EC.text_to_be_present_in_element(By.ID, value))
                return element
            elif by == 'name':
                element = wait.until(EC.text_to_be_present_in_element(By.NAME, value))
                return element
            elif by == 'className':
                element = wait.until(EC.text_to_be_present_in_element(By.CLASS_NAME, value))
                return element
            elif by == 'css':
                element = wait.until(EC.text_to_be_present_in_element(By.CSS_SELECTOR, value))
                return element
            elif by == 'tagName':
                element = wait.until(EC.text_to_be_present_in_element(By.TAG_NAME, value))
                return element
            elif by == 'linkText':
                element = wait.until(EC.text_to_be_present_in_element(By.LINK_TEXT, value))
                return element
            else:
                element = wait.until(EC.text_to_be_present_in_element(By.XPATH, value))
                return element
        else:
            xpath = "//*[text()='{}']".format(way)
            element = wait.until(EC.text_to_be_present_in_element(By.XPATH, xpath))
            return element

    # 判断指定元素的属性值中是否包含了预期的字符串
    # TODO: 未修复bug，未加预期值
    @staticmethod
    def get_attribute_element(driver, way ,name):
        wait = WebDriverWait(driver, 10)
        if "=>" in way:
            by = way[:way.find('=>')]
            value = way[way.find('=>') + 2:]
            if by == "" or value == "":
                # 语法错误，参考id=>element.
                raise NameError("Grammatical errors, reference: 'id=>element'.")
            if by == 'id':
                element = wait.until(EC.text_to_be_present_in_element_value((By.ID, value),name))
                return element
            elif by == 'name':
                element = wait.until(EC.text_to_be_present_in_element_value((By.NAME, value),name))
                return element
            elif by == 'className':
                element = wait.until(EC.text_to_be_present_in_element_value((By.CLASS_NAME, value),name))
                return element
            elif by == 'css':
                element = wait.until(EC.text_to_be_present_in_element_value((By.CSS_SELECTOR, value),name))
                return element
            elif by == 'tagName':
                element = wait.until(EC.text_to_be_present_in_element_value((By.TAG_NAME, value),name))
                return element
            elif by == 'linkText':
                element = wait.until(EC.text_to_be_present_in_element_value((By.LINK_TEXT, value),name))
                return element
            else:
                element = wait.until(EC.text_to_be_present_in_element_value((By.XPATH, value),name))
                return element

        else:
            xpath = "//*[text()='{}']".format(way)
            element = wait.until(EC.text_to_be_present_in_element_value((By.XPATH, xpath),name))
            return element

    @staticmethod
    def get_switch_iframe_element(driver, way):
        wait = WebDriverWait(driver, 10)

        if "=>" in way:
            by = way[:way.find('=>')]
            value = way[way.find('=>') + 2:]
            if by == "" or value == "":
                # 语法错误，参考id=>element.
                raise NameError("Grammatical errors, reference: 'id=>element'.")
            if by == 'id':
                element = wait.until(EC.frame_to_be_available_and_switch_to_it((By.ID, value)))
                return element
            elif by == 'name':
                element = wait.until(EC.frame_to_be_available_and_switch_to_it((By.NAME, value)))
                return element
            elif by == 'className':
                element = wait.until(EC.frame_to_be_available_and_switch_to_it((By.CLASS_NAME, value)))
                return element
            elif by == 'css':
                element = wait.until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, value)))
                return element
            elif by == 'tagName':
                element = wait.until(EC.frame_to_be_available_and_switch_to_it((By.TAG_NAME, value)))
                return element
            elif by == 'linkText':
                element = wait.until(EC.frame_to_be_available_and_switch_to_it((By.LINK_TEXT, value)))
                return element
            else:
                element = wait.until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, value)))
                return element

        else:
            xpath = "//*[text()='{}']".format(way)
            element = wait.until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, xpath)))
            return element

    # 判断某个元素是否被选中了,一般用在下拉列表
    @staticmethod
    def get_isSelect(driver, way):
        wait = WebDriverWait(driver, 10)

        if "=>" in way:
            by = way[:way.find('=>')]
            value = way[way.find('=>') + 2:]
            if by == "" or value == "":
                # 语法错误，参考id=>element.
                raise NameError("Grammatical errors, reference: 'id=>element'.")
            if by == 'id':
                element = wait.until(EC.element_to_be_selected(WebDriver.find_element(By.ID, value)))
                return element
            elif by == 'name':
                element = wait.until(EC.element_to_be_selected(WebDriver.find_element(By.NAME, value)))
                return element
            elif by == 'className':
                element = wait.until(EC.element_to_be_selected(WebDriver.find_element(By.CLASS_NAME, value)))
                return element
            elif by == 'css':
                element = wait.until(EC.element_to_be_selected(WebDriver.find_element(By.CSS_SELECTOR, value)))
                return element
            elif by == 'tagName':
                element = wait.until(EC.element_to_be_selected(WebDriver.find_element(By.TAG_NAME, value)))
                return element
            elif by == 'linkText':
                element = wait.until(EC.element_to_be_selected(WebDriver.find_element(By.LINK_TEXT, value)))
                return element
            else:
                element = wait.until(EC.element_to_be_selected(WebDriver.find_element(By.XPATH, value)))
                return element

        else:
            xpath = "//*[text()='{}']".format(way)
            element = wait.until(EC.element_to_be_selected(WebDriver.find_element(By.XPATH, xpath)))
            return element

    # 判断某个元素的选中状态是否符合预期
    @staticmethod
    def get_isSelect_state(driver, way):
        wait = WebDriverWait(driver, 10)

        if "=>" in way:
            by = way[:way.find('=>')]
            value = way[way.find('=>') + 2:]
            if by == "" or value == "":
                # 语法错误，参考id=>element.
                raise NameError("Grammatical errors, reference: 'id=>element'.")
            if by == 'id':
                element = wait.until(EC.element_located_selection_state_to_be(By.ID, value))
                return element
            elif by == 'name':
                element = wait.until(EC.element_located_selection_state_to_be(By.NAME, value))
                return element
            elif by == 'className':
                element = wait.until(EC.element_located_selection_state_to_be(By.CLASS_NAME, value))
                return element
            elif by == 'css':
                element = wait.until(EC.element_located_selection_state_to_be(By.CSS_SELECTOR, value))
                return element
            elif by == 'tagName':
                element = wait.until(EC.element_located_selection_state_to_be(By.TAG_NAME, value))
                return element
            elif by == 'linkText':
                element = wait.until(EC.element_located_selection_state_to_be(By.LINK_TEXT, value))
                return element
            else:
                element = wait.until(EC.element_located_selection_state_to_be(By.XPATH, value))
                return element

        else:
            xpath = "//*[text()='{}']".format(way)
            element = wait.until(EC.element_located_selection_state_to_be(By.XPATH, xpath))
            return element

    # 判断页面上是否存在alert,如果有就切换到alert并返回alert的内容
    @staticmethod
    def get_alert_is_present(driver):
        log = Colorlog()
        wait = WebDriverWait(driver, 10)
        try:
            element = wait.until(EC.alert_is_present())
            return element
        except TimeoutException as t:
            log.error('error: 判断页面上是否存在alert超时！- {}'.format(t))
        except Exception as e:
            raise e

