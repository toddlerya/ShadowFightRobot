#!/usr/bin/env python
# coding: utf-8
# @Time     : 2021/5/14 22:30
# @Author   : toddler
# @FileName : image.py
# @Project  : ShadowFightRobot


"""计算图片相似度，推算符合哪个图片事件，执行相应的事件动作"""

import cv2
import numpy
from PIL import Image
from skimage import metrics
from loguru import logger


@logger.catch(reraise=True)
def verify_image(image_path):
    """
    校验图片是否完整
    """
    status = False
    try:
        Image.open(image_path).verify()
        status = True
    except Exception as err:
        logger.error(f'图片完整性验证失败: {err}')
    return status


@logger.catch(reraise=True)
def read_image(image_path):
    return cv2.imread(image_path)


@logger.catch(reraise=True)
def mean_hash(img: numpy.ndarray) -> str:
    """
    均值哈希，值越小，相似度越高
    """
    # 均值哈希算法
    # 缩放为8*8
    img = cv2.resize(img, (8, 8))
    # 转换为灰度图
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # s为像素和初值为0，hash_str为hash值初值为''
    s = 0
    hash_str = ''
    # 遍历累加求像素和
    for i in range(8):
        for j in range(8):
            s = s+gray[i, j]
    # 求平均灰度
    avg = s/64
    # 灰度大于平均值为1相反为0生成图片的hash值
    for i in range(8):
        for j in range(8):
            if gray[i, j] > avg:
                hash_str = hash_str+'1'
            else:
                hash_str = hash_str+'0'
    return hash_str


@logger.catch(reraise=True)
def different_hash(img: numpy.ndarray) -> str:
    """
    差值哈希算法，值越小，相似度越高
    """
    # 差值哈希算法
    # 缩放8*8
    img = cv2.resize(img, (9, 8))
    # 转换灰度图
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    hash_str = ''
    # 每行前一个像素大于后一个像素为1，相反为0，生成哈希
    for i in range(8):
        for j in range(8):
            if gray[i, j] > gray[i, j+1]:
                hash_str = hash_str+'1'
            else:
                hash_str = hash_str+'0'
    return hash_str


@logger.catch(reraise=True)
def perceptual_hash(img: numpy.ndarray) -> str:
    """
    感知哈希算法，值越小，相似度越高
    """
    img = cv2.resize(img, (32, 32))  # , interpolation=cv2.INTER_CUBIC

    # 转换为灰度图
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 将灰度图转为浮点型，再进行dct变换
    dct = cv2.dct(numpy.float32(gray))
    # opencv实现的掩码操作
    dct_roi = dct[0:8, 0:8]
    __hash = list()
    average = numpy.mean(dct_roi)
    for i in range(dct_roi.shape[0]):
        for j in range(dct_roi.shape[1]):
            if dct_roi[i, j] > average:
                __hash.append(1)
            else:
                __hash.append(0)
    return ''.join([str(ele) for ele in __hash])


@logger.catch(reraise=True)
def perceptual_hash_similarity_score(img_1: numpy.ndarray, img_2: numpy.ndarray):
    """
    感知hash相似度
    """


@logger.catch(reraise=True)
def ssim_score(img_1: numpy.ndarray, img_2: numpy.ndarray):
    """
    结构相似度量
    SSIM是一种全参考的图像质量评价指标，分别从亮度、对比度、结构三个方面度量图像相似性。
    SSIM取值范围[0, 1]，值越大，表示图像失真越小。在实际应用中，可以利用滑动窗将图像分块，令分块总数为N，
    考虑到窗口形状对分块的影响，采用高斯加权计算每一窗口的均值、方差以及协方差，然后计算对应块的结构相似度SSIM，
    最后将平均值作为两图像的结构相似性度量，即平均结构相似性SSIM。
    """
    score = metrics.structural_similarity(im1=img_1, im2=img_2, multichannel=True)
    return score


@logger.catch(reraise=True)
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
