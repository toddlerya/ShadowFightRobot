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
from config.tap_config import *
from utils.operate import adb_shell, pull_screenshot
from utils.image import read_image, ssim_score, verify_image


class EventManager:
    def __init__(self):
        self.open_game_event_cmd = ''
        self.close_shop_ad_event_cmd = ''
        self.close_new_season_event_cmd = ''
        self.click_duel_button_event_cmd = ''
        self.start_fight_button_event_cmd = ''
        self.combo_event_cmd = ''
        self.end_fight_click_continue_event_cmd = ''
        self.gold_details_click_continue_event_cmd = ''
        self.receive_award_gold_click_continue_event_cmd = ''
        self.lose_fight_tip_click_continue_event_cmd = ''
        self.ann_images = list()
        self.running_event = None

    @staticmethod
    def __set_short_tap_event(event):
        return f'input tap {event["x"]} {event["y"]}'

    @staticmethod
    def __set_long_tap_event(event):
        return f'input touchscreen swipe {event["x"]} {event["y"]} {event["x"]} {event["y"]} 100'

    def loader(self):
        """
        加载并构建sendevent命令
        """
        # self.open_game_event_cmd = self.__set_event(OPEN_GAME_EVENT['value'])]
        # self.close_shop_ad_event_cmd = self.__set_event(CLOSE_SHOP_AD_EVENT['value'])]
        # self.close_new_season_event_cmd = self.__set_event(CLOSE_NEW_SEASON_DIALOG_EVENT['value'])]
        self.click_duel_button_event_cmd = self.__set_short_tap_event(CLICK_DUEL_BUTTON_EVENT['value'])
        self.start_fight_button_event_cmd = self.__set_short_tap_event(CLICK_START_FIGHT_BUTTON_EVENT['value'])
        self.combo_event_cmd = self.__set_long_tap_event(COMBO_EVENT['value'])
        self.end_fight_click_continue_event_cmd = self.__set_short_tap_event(END_FIGHT_CLICK_CONTINUE_EVENT['value'])
        self.gold_details_click_continue_event_cmd = self.__set_short_tap_event(GOLD_DETAILS_CONTINUE_EVENT['value'])
        self.receive_award_gold_click_continue_event_cmd = self.__set_short_tap_event(
            RECEIVE_AWARD_GOLD_CLICK_CONTINUE_EVENT['value'])
        self.lose_fight_tip_click_continue_event_cmd = self.__set_short_tap_event(
            LOSE_FIGHT_TIP_CLICK_CONTINUE_EVENT['value'])
        self.ann_images = glob.glob(f'{str(pathlib.Path(ANNOTATION_IMAGE_PATH).absolute())}/*.png')

    def sender(self, event_name):
        """
        执行sendevent命令
        """
        logger.info(f'input tap {event_name}')
        if event_name == '打开游戏':
            adb_shell(self.open_game_event_cmd)
            time.sleep(60)
        if event_name == '关闭商店活动广告':
            adb_shell(self.close_shop_ad_event_cmd)
            time.sleep(5)
        if event_name == '打开决斗':
            adb_shell(self.click_duel_button_event_cmd)
            time.sleep(15)
        if event_name == '开始战斗':
            adb_shell(self.start_fight_button_event_cmd)
            time.sleep(3)
            self.fight()
        if event_name == '结束战斗':
            adb_shell(self.end_fight_click_continue_event_cmd)
            time.sleep(3)
        if event_name == '展示金币明细':
            adb_shell(self.gold_details_click_continue_event_cmd)
        if event_name == '领取战斗金币奖励':
            adb_shell(self.receive_award_gold_click_continue_event_cmd)
        if event_name == '开始攻击':
            self.fight()
        if event_name == '输了比赛':
            adb_shell(self.lose_fight_tip_click_continue_event_cmd)

    @logger.catch(reraise=True)
    def fight(self):
        logger.info('开始攻击')
        for i in range(60):
            logger.info(f'第{i + 1}次攻击')
            adb_shell(self.combo_event_cmd)
            time.sleep(0.1)

    @logger.catch(reraise=True)
    def chose_event(self):
        """
        根据当前屏幕图像，匹配图片事件标记，选择执行的事件
        """
        max_score = 0.0
        similarity_img = ''
        for each in self.ann_images:
            temp_image_name = pathlib.Path(each).name
            # 如果图片没获取完整，0.5秒后重试一下
            if not verify_image(IMAGE_NAME):
                time.sleep(0.5)
                self.chose_event()
            temp_img = read_image(IMAGE_NAME)
            for _ in range(10):
                if temp_img is None:
                    time.sleep(0.5)
                    temp_img = read_image(IMAGE_NAME)
                else:
                    break
            each_ann_img = read_image(each)
            __score = ssim_score(img_1=temp_img, img_2=each_ann_img)
            logger.info(f'当前正在比对标注图片: {temp_image_name} {__score}')
            if __score > max_score:
                max_score = __score
                similarity_img = temp_image_name
        recommend_event = annotation_event_map[similarity_img]
        logger.info(f'推荐事件: {recommend_event["desc"]}, 匹配成功图片: {similarity_img}, 相似度: {max_score}')
        return recommend_event

    @logger.catch(reraise=True)
    def run_event(self):
        """
        执行事件
        """
        logger.info('调度执行事件')
        __event = self.chose_event()
        __event_desc = __event['desc']
        logger.info(f'开始执行事件: {__event_desc}')
        self.sender(__event_desc)


@logger.catch(reraise=True)
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
        Image.open(IMAGE_NAME).load()
    except Exception as err:
        logger.error(f'无法读取截图数据: {err}')


def run():
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
    check_screenshot()
    run()
