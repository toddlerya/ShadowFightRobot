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

IMAGE_NAME = 'home_page.png'

# 打开决斗
CLICK_DUEL_BUTTON_EVENT = '''
/dev/input/event3: 0003 0039 000007c5
/dev/input/event3: 0001 014a 00000001
/dev/input/event3: 0003 0035 00000624
/dev/input/event3: 0003 0036 000003c8
/dev/input/event3: 0000 0000 00000000
/dev/input/event3: 0003 0039 ffffffff
/dev/input/event3: 0001 014a 00000000
/dev/input/event3: 0000 0000 00000000
'''

# 开始战斗
START_FIGHT_EVENT = '''
/dev/input/event3: 0003 0039 000007c6
/dev/input/event3: 0001 014a 00000001
/dev/input/event3: 0003 0035 0000048c
/dev/input/event3: 0003 0036 000003db
/dev/input/event3: 0000 0000 00000000
/dev/input/event3: 0003 0039 ffffffff
/dev/input/event3: 0001 014a 00000000
/dev/input/event3: 0000 0000 00000000
'''

# 打一套连招
COMBO_EVENT = '''

'''


def get_screen_size():
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
