#!/usr/bin/env python
# coding: utf-8
# @Time     : 3/20/21 10:44 PM
# @Author   : toddlerya 
# @FileName : robot.py
# @Project  : ShadowFightRobot


import subprocess
import sys
import os
import time

from PIL import Image

from common.config import _get_screen_size
from setting import *


screenshot_way = 2


def pull_screenshot_temp():
    """
    获取临时
    :return:
    """
    process = subprocess.Popen('adb shell screencap -p', shell=True, stdout=subprocess.PIPE)
    screenshot = process.stdout.read()
    if sys.platform == 'win32':
        screenshot = screenshot.replace(b'\r\r\n', b'\n')
    f = open('shadowfight_temp.png', 'wb')
    f.write(screenshot)
    f.close()


def pull_screenshot():
    process = subprocess.Popen('adb shell screencap -p', shell=True, stdout=subprocess.PIPE)
    screenshot = process.stdout.read()
    if sys.platform == 'win32':
        screenshot = screenshot.replace(b'\r\r\n', b'\n')
    f = open('shadowfight.png', 'wb')
    f.write(screenshot)
    f.close()


def check_screenshot():
    """
    检查获取截图的方式
    """
    global screenshot_way
    if os.path.isfile('shadowfight.png'):
        os.remove('shadowfight.png')
    if (screenshot_way < 0):
        print('暂不支持当前设备')
        sys.exit()
    pull_screenshot()
    try:
        Image.open('./shadowfight.png').load()
        print('采用方式 {} 获取截图'.format(screenshot_way))
    except Exception:
        screenshot_way -= 1
        check_screenshot()


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


def adb_shell(cmd):
    """
    长按
    :param cmd:
    :return:
    """
    status = os.system('adb shell "{}"'.format(cmd))
    if status == 0:
        return True
    else:
        return False


def front_fist_fist():
    """
    前拳拳
    :return:
    """
    adb_shell(FRONT_FIST_FIST)


def entry_week_job():
    """
    进入每周活动
    :return:
    """
    if short_tap(WEEK_JOB_POINT):
        print('进入任务活动页面')
        if short_tap(REGISTERED_JOB):
            print('注册任务')
            if short_tap(PAY_JOB):
                print('付款成功')
    else:
        print('进入任务活动页面失败')


def fight():
    """
    战斗
    :return:
    """
    while True:
        front_fist_fist()
        time.sleep(0.01)


if __name__ == '__main__':
    check_screenshot()
    # entry_week_job()
    fight()
