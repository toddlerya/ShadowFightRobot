#!/usr/bin/env python
# coding: utf-8
# @Time     : 3/20/21 10:42 PM
# @Author   : toddlerya 
# @FileName : config.py
# @Project  : ShadowFightRobot

"""
调取配置文件和屏幕分辨率的代码
"""

import sys
import os
import re


def _get_screen_size():
    """
    获取手机屏幕大小
    """
    size_str = os.popen('adb shell wm size').read()
    if not size_str:
        print('请安装 ADB 及驱动并配置环境变量')
        sys.exit()
    m = re.search(r'(\d+)x(\d+)', size_str)
    if m:
        return "{height}x{width}".format(height=m.group(2), width=m.group(1))
    else:
        return None
