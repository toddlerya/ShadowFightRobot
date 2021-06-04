#!/usr/bin/env python
# coding: utf-8
# @Time     : 6/3/21 11:15 PM
# @Author   : toddlerya 
# @FileName : serial_chose_event.py
# @Project  : ShadowFightRobot


import pathlib
import glob
import datetime
import time
import multiprocessing as mp

from loguru import logger

from config import IMAGE_NAME, ANNOTATION_IMAGE_PATH
from utils.image import read_image, ssim_score, verify_image

all_ann_images = glob.glob(f'{str(pathlib.Path(ANNOTATION_IMAGE_PATH).absolute())}/*.png')


def chose_event():
    max_score = 0.0
    similarity_img = ''
    for each in all_ann_images:
        temp_image_name = pathlib.Path(each).name
        # 如果图片没获取完整，0.5秒后重试一下
        if not verify_image(IMAGE_NAME):
            time.sleep(0.5)
            chose_event()
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
    logger.info(f'匹配成功图片: {similarity_img}, 相似度: {max_score}')


if __name__ == '__main__':
    start_t = datetime.datetime.now()
    chose_event()
    end_t = datetime.datetime.now()
    elapsed_sec = (end_t - start_t).total_seconds()
    logger.info("串行计算 共消耗: " + "{:.2f}".format(elapsed_sec) + " 秒")