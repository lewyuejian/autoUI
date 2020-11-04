#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@file: exceptions.py
@time: 2020/10/27 0027 22:43
@desc:
'''
class MyBaseError(Exception):
    pass

class FileFormatError(MyBaseError):
    pass

class NotFoundError(MyBaseError):
    pass

class FileNotFound(FileNotFoundError,NotFoundError):
    pass

class JSONDecodeError(NotFoundError):
    pass

class CSVNotFound(NotFoundError):
    pass

class YAMLNotFound(NotFoundError):
    pass

class TEXTNotFound(NotFoundError):
    pass

class BrowserNotFound(NotFoundError):
    pass

class ValueNotFound(NotFoundError):
    pass

class HandleError(MyBaseError):
    pass
class CloseUpError(HandleError):
    pass

class QuitUpError(HandleError):
    pass