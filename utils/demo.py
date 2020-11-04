#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@file: demo.py
@time: 2020/10/31 0031 0:05
@desc:
'''
way = 'xpath=>//*[@id="app"]/header/div/div/div[4]/span'
if "=>" in way:
    by = way[:way.find('=>')]
    value = way[way.find('=>')+2:]
    print(by)
    print(value)