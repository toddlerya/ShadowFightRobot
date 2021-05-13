#!/usr/bin/env python
# coding: utf-8
# @Time     : 3/20/21 10:44 PM
# @Author   : toddlerya 
# @FileName : robot.py
# @Project  : shadow_fightRobot


import subprocess
import sys
import os
import time

from loguru import logger
from PIL import Image

from common.config import get_screen_size, IMAGE_NAME, CLICK_DUEL_BUTTON_EVENT, START_FIGHT_EVENT
from setting import *


class EventManager:
    def __init__(self):
        self.click_duel_button_event_cmd_list = list()
        self.start_fight_button_event_cmd_list = list()

    @staticmethod
    def __set_event(event):
        for line in event.strip().split('\n'):
            __send_event_cmd = f"sendevent {line.replace(':', '')}"
            yield __send_event_cmd

    def loader(self):
        """
        加载并构建sendevent命令
        """
        self.click_duel_button_event_cmd_list = [ele for ele in self.__set_event(CLICK_DUEL_BUTTON_EVENT)]
        self.start_fight_button_event_cmd_list = [ele for ele in self.__set_event(START_FIGHT_EVENT)]

    def sender(self, event_name):
        """
        执行sendevent命令
        """
        if event_name == CLICK_DUEL_BUTTON_EVENT:
            for cmd in self.click_duel_button_event_cmd_list:
                adb_shell(cmd)
                time.sleep(0.1)
        if event_name == START_FIGHT_EVENT:
            for cmd in self.start_fight_button_event_cmd_list:
                adb_shell(cmd)


@logger.catch
def pull_screenshot():
    temp_path = '/data/local/tmp/'
    subprocess.check_output(f'adb shell screencap -p {temp_path}/{IMAGE_NAME}', shell=True)
    subprocess.check_output(f'adb pull {temp_path}/{IMAGE_NAME} .', shell=True)


@logger.catch
def check_screenshot():
    """
    检查获取截图的方式
    """
    logger.info('检查获取截图功能...')
    if os.path.isfile(IMAGE_NAME):
        os.remove(IMAGE_NAME)
    try:
        pull_screenshot()
    except Exception as err:
        logger.error(f'无法执行adb shell截图: {err}')
    try:
        Image.open('tag_images/home_page.png').load()
    except Exception as err:
        logger.error(f'无法读取截图数据: {err}')
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


@logger.catch
def adb_shell(cmd):
    """
    长按
    :param cmd:
    :return:
    """
    __cmd = f'adb shell {cmd}'
    logger.info(__cmd)
    status = subprocess.check_output(__cmd, shell=True)


def click_duel_button():
    """
    点击开始决斗按钮
    """
    for line in CLICK_DUEL_BUTTON_EVENT:
        print(repr(line))
        adb_shell(f"sendevent {line.replace(':', '')}")


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
    em = EventManager()
    em.loader()
    em.sender(CLICK_DUEL_BUTTON_EVENT)
    # entry_week_job()
    # fight()
