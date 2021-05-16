#!/usr/bin/env python
# coding: utf-8
# @Time     : 3/20/21 10:44 PM
# @Author   : toddlerya 
# @FileName : robot.py
# @Project  : shadow_fightRobot


import os
import time
import glob
import pathlib


from loguru import logger
from PIL import Image
from apscheduler.schedulers.background import BlockingScheduler

from config import IMAGE_NAME, ANNOTATION_IMAGE_PATH
from config.event_config import *
from utils.trans import hex2dec
from utils.operate import adb_shell, pull_screenshot
from utils.image import read_image, ssim_score


class EventManager:
    def __init__(self):
        self.open_game_event_cmd_list = list()
        self.close_shop_ad_event_cmd_list = list()
        self.close_new_season_event_cmd_list = list()
        self.click_duel_button_event_cmd_list = list()
        self.start_fight_button_event_cmd_list = list()
        self.combo_event_cmd_list = list()
        self.ann_images = list()
        self.running_event = None

    @staticmethod
    def __set_event(event):
        for line in event.strip().split('\n'):
            line = hex2dec(line)
            __send_event_cmd = f"sendevent {line.replace(':', '')}"
            yield __send_event_cmd

    def loader(self):
        """
        加载并构建sendevent命令
        """
        self.open_game_event_cmd_list = [ele for ele in self.__set_event(OPEN_GAME_EVENT['value'])]
        self.close_shop_ad_event_cmd_list = [ele for ele in self.__set_event(CLOSE_SHOP_AD_EVENT['value'])]
        self.close_new_season_event_cmd_list = [ele for ele in self.__set_event(CLOSE_NEW_SEASON_DIALOG_EVENT['value'])]
        self.click_duel_button_event_cmd_list = [ele for ele in self.__set_event(CLICK_DUEL_BUTTON_EVENT['value'])]
        self.start_fight_button_event_cmd_list = [ele for ele in self.__set_event(CLICK_START_FIGHT_BUTTON_EVENT['value'])]
        self.combo_event_cmd_list = [ele for ele in self.__set_event(COMBO_EVENT['value'])]
        self.ann_images = glob.glob(f'{str(pathlib.Path(ANNOTATION_IMAGE_PATH).absolute())}/*.png')

    def sender(self, event_name):
        """
        执行sendevent命令
        """
        logger.info(f'sendevent {event_name}')
        if event_name == '打开游戏':
            for cmd in self.open_game_event_cmd_list:
                adb_shell(cmd)
            time.sleep(60)
        if event_name == '关闭商店活动广告':
            for cmd in self.close_shop_ad_event_cmd_list:
                adb_shell(cmd)
            time.sleep(5)
        if event_name == '打开决斗':
            for cmd in self.click_duel_button_event_cmd_list:
                adb_shell(cmd)
            time.sleep(30)
        if event_name == '开始战斗':
            for cmd in self.start_fight_button_event_cmd_list:
                adb_shell(cmd)
            time.sleep(3)
            logger.info('开始攻击')
            for i in range(30):
                logger.info(f'第{i+1}次攻击')
                for cmd in self.combo_event_cmd_list:
                    adb_shell(cmd)
                time.sleep(0.5)

    def chose_event(self):
        """
        根据当前屏幕图像，匹配图片事件标记，选择执行的事件
        """
        max_score = 0.0
        similarity_img = ''
        for each in self.ann_images:
            temp_image_name = pathlib.Path(each).name
            temp_img = read_image(IMAGE_NAME)
            each_ann_img = read_image(each)
            __score = ssim_score(img_1=temp_img, img_2=each_ann_img)
            logger.info(f'当前正在比对标注图片: {temp_image_name} {__score}')
            if __score > max_score:
                max_score = __score
                similarity_img = temp_image_name
        recommend_event = annotation_event_map[similarity_img]
        logger.info(f'推荐事件: {recommend_event["desc"]}, 匹配成功图片: {similarity_img}, 相似度: {max_score}')
        return recommend_event

    @logger.catch
    def run_event(self):
        """
        执行事件
        """
        logger.info('调度执行事件')
        __event = self.chose_event()
        __event_desc = __event['desc']
        if self.running_event is None:
            logger.info(f'开始执行事件: {__event_desc}')
            self.sender(__event_desc)
            # if __event == COMBO_EVENT:
            #     self.running_event = __event
            #     time.sleep(10)
        else:
            __event = self.chose_event()
            logger.info(f'开始执行事件: {__event_desc}')
            self.sender(__event_desc)


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
        Image.open('annotation_images/game_home_page.png').load()
    except Exception as err:
        logger.error(f'无法读取截图数据: {err}')
        check_screenshot()


def run():
    check_screenshot()
    em = EventManager()
    em.loader()

    scheduler = BlockingScheduler()

    scheduler.add_job(
        pull_screenshot,
        trigger='interval',
        seconds=2
    )
    scheduler.add_job(
        em.run_event,
        trigger='interval',
        seconds=6
    )

    scheduler.start()


if __name__ == '__main__':
    run()
