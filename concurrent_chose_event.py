#!/usr/bin/env python
# coding: utf-8
# @Time     : 6/3/21 11:15 PM
# @Author   : toddlerya 
# @FileName : concurrent_chose_event.py
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


def load_all_ann_data():
    """
    加载读取所有标注图片
    :return:
    """
    all_data = dict()
    for each in all_ann_images:
        image_name = pathlib.Path(each).name
        all_data[image_name] = read_image(each)
    return all_data


def calc_score(ann_img_name, calc_data):
    """
    计算相似度得分
    :param ann_img_name:
    :param calc_data:
    :return:
    """
    ann_img_data = calc_data['ann_img_data']
    temp_img_data = calc_data['temp_img_data']
    __score = ssim_score(img_1=ann_img_data, img_2=temp_img_data)
    return {ann_img_name: __score}


def concurrent():
    if not verify_image(IMAGE_NAME):
        time.sleep(0.5)
        concurrent()
    temp_img_data = read_image(IMAGE_NAME)
    for _ in range(10):
        if temp_img_data is None:
            time.sleep(0.5)
            temp_img_data = read_image(IMAGE_NAME)
        else:
            break
    all_ann_data = load_all_ann_data()
    tasks = dict()
    for k, v in all_ann_data.items():
        tasks.update(
            {
                k: {
                    'ann_img_data': v,
                    'temp_img_data': temp_img_data
                }
            }
        )
    logger.info(f'共{len(tasks)}个标注场景')
    cpu_count = int(mp.cpu_count())
    logger.info(f'cpu number: {cpu_count}')
    pool = mp.Pool(cpu_count)
    start_t = datetime.datetime.now()
    results = [pool.apply_async(calc_score, args=(ann_img_name, calc_data)) for ann_img_name, calc_data in
               tasks.items()]
    results = [p.get() for p in results]
    score_data = dict()
    [score_data.update(ele) for ele in results]
    sort_score_data = sorted(score_data.items(), key=lambda x: x[1], reverse=True)[0]
    logger.info(f'推荐场景: {sort_score_data}')
    end_t = datetime.datetime.now()
    elapsed_sec = (end_t - start_t).total_seconds()
    logger.info("多进程计算 共消耗: " + "{:.2f}".format(elapsed_sec) + " 秒")


if __name__ == '__main__':
    concurrent()
