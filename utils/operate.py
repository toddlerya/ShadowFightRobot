#!/usr/bin/env python
# coding: utf-8
# @Time     : 2021/5/14 22:23
# @Author   : toddler
# @FileName : operate.py
# @Project  : ShadowFightRobot


import os
import sys
import subprocess
import re

from loguru import logger

from config import IMAGE_NAME


def get_screen_size():
    """
    获取手机屏幕大小
    """
    size_str = os.popen('adb shell wm size').read()
    if not size_str:
        logger.error('请安装 ADB 及驱动并配置环境变量')
        sys.exit()
    m = re.search(r'(\d+)x(\d+)', size_str)
    if m:
        return "{height}x{width}".format(height=m.group(2), width=m.group(1))
    else:
        return None


@logger.catch
def pull_screenshot():
    temp_path = '/data/local/tmp/'
    subprocess.check_output(f'adb shell screencap -p {temp_path}/{IMAGE_NAME}', shell=True)
    subprocess.check_output(f'adb pull {temp_path}/{IMAGE_NAME} .', shell=True)


@logger.catch
def adb_shell(cmd):
    """
    长按
    :param cmd:
    :return:
    """
    __cmd = f'adb shell {cmd}'
    # logger.debug(__cmd)
    subprocess.check_output(__cmd, shell=True)


def short_tap(point):
    """
    点击
    :param point:
    :return:
    """
    x = point.get('x')
    y = point.get('y')
    status = os.system('adb shell input tap {X} {Y}'.format(X=x, Y=y))
    if status == 0:
        return True
    else:
        return False


def long_tap(point, delay=2000):
    """
    长按
    :param point:
    :param delay:
    :return:
    """
    x = point.get('x')
    y = point.get('y')
    status = os.system('adb shell input touchscreen swipe {X} {Y} {X} {Y} {TIME}'.format(X=x, Y=y, TIME=delay))
    if status == 0:
        return True
    else:
        return False

