#!/usr/bin/env python
# coding: utf-8
# @Time     : 3/20/21 11:03 PM
# @Author   : toddlerya 
# @FileName : setting.py
# @Project  : ShadowFightRobot


# ========= 令牌活动 ========
# 点击进入活动按钮
WEEK_JOB_POINT = {'x': 1765, 'y': 300}
# 注册活动按钮
REGISTERED_JOB = {'x': 1945, 'y': 935}
# 活动付款按钮
PAY_JOB = {'x': 730, 'y': 940}
# 战斗按钮
FIGHT = {'x': 1915, 'y': 940}

# ======== 格斗手柄 ========
# 方向
UP = {'x': 435, 'y': 630}
DOWN = {'x': 435, 'y': 930}
RIGHT = {'x': 600, 'y': 770}
LEFT = {'x': 280, 'y': 770}
# 动作
FIST = {'x': 2050, 'y': 730}
FOOT = {'x': 1970, 'y': 880}
DARTS = {'x': 1970, 'y': 570}
SHADOW_SKILL = {'x': 1900, 'y': 730}

# ======== 连招 ========
# 前+拳+拳
FRONT_FIST_FIST = 'input swipe {FRONT_X} {FRONT_Y} {FRONT_X} {FRONT_Y} {TIME} && ' \
                  'input swipe {FIST_X} {FIST_Y} {FIST_X} {FIST_Y} {TIME} && ' \
                  'input swipe {FIST_X} {FIST_Y} {FIST_X} {FIST_Y} {TIME}'.format(
                        FRONT_X=RIGHT.get('x'),
                        FRONT_Y=RIGHT.get('y'),
                        FIST_X=FIST.get('x'),
                        FIST_Y=FIST.get('y'),
                        TIME=10
                        )
