#!/usr/bin/env python
# coding: utf-8
# @Time     : 2021/5/14 22:21
# @Author   : toddler
# @FileName : event_config.py
# @Project  : ShadowFightRobot


# 打开游戏
OPEN_GAME_EVENT = {
    'desc': '打开游戏',
    'value': '''
/dev/input/event3: 0003 0039 00000017
/dev/input/event3: 0001 014a 00000001
/dev/input/event3: 0003 0035 00000669
/dev/input/event3: 0003 0036 000000e0
/dev/input/event3: 0000 0000 00000000
/dev/input/event3: 0003 0039 ffffffff
/dev/input/event3: 0001 014a 00000000
/dev/input/event3: 0000 0000 00000000
'''
}

# 关闭商店活动广告
CLOSE_SHOP_AD_EVENT = {
    'desc': '关闭商店活动广告',
    'value': '''
/dev/input/event3: 0003 0039 00000018
/dev/input/event3: 0001 014a 00000001
/dev/input/event3: 0003 0035 0000004e
/dev/input/event3: 0003 0036 00000032
/dev/input/event3: 0000 0000 00000000
/dev/input/event3: 0003 0039 ffffffff
/dev/input/event3: 0001 014a 00000000
/dev/input/event3: 0000 0000 00000000
'''
}

CLOSE_NEW_SEASON_DIALOG_EVENT = {
    'desc': '关闭新赛季提示弹窗',
    'value': '''
/dev/input/event3: 0003 0039 0000002d
/dev/input/event3: 0001 014a 00000001
/dev/input/event3: 0003 0035 0000058c
/dev/input/event3: 0003 0036 0000032d
/dev/input/event3: 0000 0000 00000000
/dev/input/event3: 0003 0039 ffffffff
/dev/input/event3: 0001 014a 00000000
/dev/input/event3: 0000 0000 00000000
'''
}


# 打开决斗
CLICK_DUEL_BUTTON_EVENT = {
    'desc': '打开决斗',
    'value': '''
/dev/input/event3: 0003 0039 000007c5
/dev/input/event3: 0001 014a 00000001
/dev/input/event3: 0003 0035 00000624
/dev/input/event3: 0003 0036 000003c8
/dev/input/event3: 0000 0000 00000000
/dev/input/event3: 0003 0039 ffffffff
/dev/input/event3: 0001 014a 00000000
/dev/input/event3: 0000 0000 00000000
'''
}

# 开始战斗
CLICK_START_FIGHT_BUTTON_EVENT = {
    'desc': '开始战斗',
    'value': '''
/dev/input/event3: 0003 0039 000007c6
/dev/input/event3: 0001 014a 00000001
/dev/input/event3: 0003 0035 0000048c
/dev/input/event3: 0003 0036 000003db
/dev/input/event3: 0000 0000 00000000
/dev/input/event3: 0003 0039 ffffffff
/dev/input/event3: 0001 014a 00000000
/dev/input/event3: 0000 0000 00000000
'''
}

# # 打一套连招
# COMBO_EVENT = '''
#
# '''

annotation_event_map = {
    'wait_open_game.png': OPEN_GAME_EVENT,
    'wait_close_shop_ad.png': CLOSE_SHOP_AD_EVENT,
    # 通过这里控制参加哪个活动==>game_home_page
    'game_home_page.png': CLICK_DUEL_BUTTON_EVENT,
    'wait_click_fight_button.png': CLICK_START_FIGHT_BUTTON_EVENT,
    'wait_close_new_season_dialog.png': CLOSE_NEW_SEASON_DIALOG_EVENT,
}
