#!/usr/bin/env python
# coding: utf-8
# @Time     : 2021/5/14 22:21
# @Author   : toddler
# @FileName : event_config_bs.py
# @Project  : ShadowFightRobot


CLICK_CONTINUE_BUTTON = '''
/dev/input/event6: 0003 0035 000077a2
/dev/input/event6: 0003 0036 000073b3
/dev/input/event6: 0000 0002 00000000
/dev/input/event6: 0000 0000 00000000
/dev/input/event6: 0000 0002 00000000
/dev/input/event6: 0000 0000 00000000
'''


# 打开游戏
OPEN_GAME_EVENT = {
    'desc': '打开游戏',
    'value': '''
/dev/input/event6: 0003 0035 000035d6
/dev/input/event6: 0003 0036 000012ea
/dev/input/event6: 0000 0002 00000000
/dev/input/event6: 0000 0000 00000000
/dev/input/event6: 0000 0002 00000000
/dev/input/event6: 0000 0000 00000000
'''
}

# 关闭商店活动广告
CLOSE_SHOP_AD_EVENT = {
    'desc': '关闭商店活动广告',
    'value': '''
/dev/input/event6: 0003 0035 0000048f
/dev/input/event6: 0003 0036 00000509
/dev/input/event6: 0000 0002 00000000
/dev/input/event6: 0000 0000 00000000
/dev/input/event6: 0000 0002 00000000
/dev/input/event6: 0000 0000 00000000
'''
}

CLOSE_NEW_SEASON_DIALOG_EVENT = {
    'desc': '关闭新赛季提示弹窗',
    'value': '''
/dev/input/event6: 0003 0035 00005eaf
/dev/input/event6: 0003 0036 0000602e
/dev/input/event6: 0000 0002 00000000
/dev/input/event6: 0000 0000 00000000
/dev/input/event6: 0000 0002 00000000
/dev/input/event6: 0000 0000 00000000
'''
}


# 打开决斗
CLICK_DUEL_BUTTON_EVENT = {
    'desc': '打开决斗',
    'value': '''
/dev/input/event6: 0003 0035 00006de3
/dev/input/event6: 0003 0036 00007141
/dev/input/event6: 0000 0002 00000000
/dev/input/event6: 0000 0000 00000000
/dev/input/event6: 0000 0002 00000000
/dev/input/event6: 0000 0000 00000000
'''
}

# 开始战斗
CLICK_START_FIGHT_BUTTON_EVENT = {
    'desc': '开始战斗',
    'value': '''
/dev/input/event6: 0003 0035 00004022
/dev/input/event6: 0003 0036 000070a4
/dev/input/event6: 0000 0002 00000000
/dev/input/event6: 0000 0000 00000000
/dev/input/event6: 0000 0002 00000000
/dev/input/event6: 0000 0000 00000000
'''
}

# 打一套连招
COMBO_EVENT = {
    'desc': '开始连招攻击',
    'value': '''
/dev/input/event6: 0003 0035 00000cf7
/dev/input/event6: 0003 0036 0000664e
/dev/input/event6: 0000 0002 00000000
/dev/input/event6: 0000 0000 00000000
/dev/input/event6: 0003 0035 00001734
/dev/input/event6: 0003 0036 0000664e
/dev/input/event6: 0000 0002 00000000
/dev/input/event6: 0000 0000 00000000
/dev/input/event6: 0003 0035 00001975
/dev/input/event6: 0003 0036 0000664e
/dev/input/event6: 0000 0002 00000000
/dev/input/event6: 0000 0000 00000000
/dev/input/event6: 0003 0035 00001975
/dev/input/event6: 0003 0036 0000664e
/dev/input/event6: 0000 0002 00000000
/dev/input/event6: 0003 0035 000075ef
/dev/input/event6: 0003 0036 00005f02
/dev/input/event6: 0000 0002 00000000
/dev/input/event6: 0000 0000 00000000
/dev/input/event6: 0003 0035 00001975
/dev/input/event6: 0003 0036 0000664e
/dev/input/event6: 0000 0002 00000000
/dev/input/event6: 0000 0000 00000000
/dev/input/event6: 0003 0035 00001975
/dev/input/event6: 0003 0036 0000664e
/dev/input/event6: 0000 0002 00000000
/dev/input/event6: 0003 0035 000075ef
/dev/input/event6: 0003 0036 00005f02
/dev/input/event6: 0000 0002 00000000
/dev/input/event6: 0000 0000 00000000
/dev/input/event6: 0003 0035 00001975
/dev/input/event6: 0003 0036 0000664e
/dev/input/event6: 0000 0002 00000000
/dev/input/event6: 0000 0000 00000000
/dev/input/event6: 0000 0002 00000000
/dev/input/event6: 0000 0000 00000000
/dev/input/event6: 0003 0035 000075ef
/dev/input/event6: 0003 0036 00005f02
/dev/input/event6: 0000 0002 00000000
/dev/input/event6: 0000 0000 00000000
/dev/input/event6: 0000 0002 00000000
/dev/input/event6: 0000 0000 00000000
/dev/input/event6: 0003 0035 000075ef
/dev/input/event6: 0003 0036 00005f02
/dev/input/event6: 0000 0002 00000000
/dev/input/event6: 0000 0000 00000000
/dev/input/event6: 0000 0002 00000000
/dev/input/event6: 0000 0000 00000000
/dev/input/event6: 0003 0035 00000cf7
/dev/input/event6: 0003 0036 0000664e
/dev/input/event6: 0000 0002 00000000
/dev/input/event6: 0000 0000 00000000
/dev/input/event6: 0003 0035 00001734
/dev/input/event6: 0003 0036 0000664e
/dev/input/event6: 0000 0002 00000000
/dev/input/event6: 0000 0000 00000000
/dev/input/event6: 0003 0035 00001975
/dev/input/event6: 0003 0036 0000664e
/dev/input/event6: 0000 0002 00000000
/dev/input/event6: 0000 0000 00000000
/dev/input/event6: 0003 0035 00001975
/dev/input/event6: 0003 0036 0000664e
/dev/input/event6: 0000 0002 00000000
/dev/input/event6: 0003 0035 000075ef
/dev/input/event6: 0003 0036 00005f02
/dev/input/event6: 0000 0002 00000000
/dev/input/event6: 0000 0000 00000000
/dev/input/event6: 0003 0035 00001975
/dev/input/event6: 0003 0036 0000664e
/dev/input/event6: 0000 0002 00000000
/dev/input/event6: 0000 0000 00000000
/dev/input/event6: 0003 0035 00001975
/dev/input/event6: 0003 0036 0000664e
/dev/input/event6: 0000 0002 00000000
/dev/input/event6: 0003 0035 000075ef
/dev/input/event6: 0003 0036 00005f02
/dev/input/event6: 0000 0002 00000000
/dev/input/event6: 0000 0000 00000000
/dev/input/event6: 0003 0035 00001975
/dev/input/event6: 0003 0036 0000664e
/dev/input/event6: 0000 0002 00000000
/dev/input/event6: 0000 0000 00000000
/dev/input/event6: 0000 0002 00000000
/dev/input/event6: 0000 0000 00000000
/dev/input/event6: 0003 0035 00000cf7
/dev/input/event6: 0003 0036 0000664e
/dev/input/event6: 0000 0002 00000000
/dev/input/event6: 0000 0000 00000000
/dev/input/event6: 0003 0035 00001734
/dev/input/event6: 0003 0036 0000664e
/dev/input/event6: 0000 0002 00000000
/dev/input/event6: 0000 0000 00000000
/dev/input/event6: 0003 0035 00001975
/dev/input/event6: 0003 0036 0000664e
/dev/input/event6: 0000 0002 00000000
/dev/input/event6: 0000 0000 00000000
/dev/input/event6: 0003 0035 00001975
/dev/input/event6: 0003 0036 0000664e
/dev/input/event6: 0000 0002 00000000
/dev/input/event6: 0003 0035 000075ef
/dev/input/event6: 0003 0036 00005f02
/dev/input/event6: 0000 0002 00000000
/dev/input/event6: 0000 0000 00000000
/dev/input/event6: 0003 0035 00001975
/dev/input/event6: 0003 0036 0000664e
/dev/input/event6: 0000 0002 00000000
/dev/input/event6: 0000 0000 00000000
/dev/input/event6: 0003 0035 00001975
/dev/input/event6: 0003 0036 0000664e
/dev/input/event6: 0000 0002 00000000
/dev/input/event6: 0003 0035 000075ef
/dev/input/event6: 0003 0036 00005f02
/dev/input/event6: 0000 0002 00000000
/dev/input/event6: 0000 0000 00000000
/dev/input/event6: 0003 0035 00001975
/dev/input/event6: 0003 0036 0000664e
/dev/input/event6: 0000 0002 00000000
/dev/input/event6: 0000 0000 00000000
/dev/input/event6: 0003 0035 00001975
/dev/input/event6: 0003 0036 0000664e
/dev/input/event6: 0000 0002 00000000
/dev/input/event6: 0003 0035 000075ef
/dev/input/event6: 0003 0036 00005f02
/dev/input/event6: 0000 0002 00000000
/dev/input/event6: 0000 0000 00000000
/dev/input/event6: 0003 0035 00001975
/dev/input/event6: 0003 0036 0000664e
/dev/input/event6: 0000 0002 00000000
/dev/input/event6: 0000 0000 00000000
/dev/input/event6: 0003 0035 00001975
/dev/input/event6: 0003 0036 0000664e
/dev/input/event6: 0000 0002 00000000
/dev/input/event6: 0003 0035 000075ef
/dev/input/event6: 0003 0036 00005f02
/dev/input/event6: 0000 0002 00000000
/dev/input/event6: 0000 0000 00000000
/dev/input/event6: 0003 0035 00001975
/dev/input/event6: 0003 0036 0000664e
/dev/input/event6: 0000 0002 00000000
/dev/input/event6: 0000 0000 00000000
/dev/input/event6: 0003 0035 00001975
/dev/input/event6: 0003 0036 0000664e
/dev/input/event6: 0000 0002 00000000
/dev/input/event6: 0003 0035 000075ef
/dev/input/event6: 0003 0036 00005f02
/dev/input/event6: 0000 0002 00000000
/dev/input/event6: 0000 0000 00000000
/dev/input/event6: 0003 0035 00001975
/dev/input/event6: 0003 0036 0000664e
/dev/input/event6: 0000 0002 00000000
/dev/input/event6: 0000 0000 00000000
/dev/input/event6: 0000 0002 00000000
/dev/input/event6: 0000 0000 00000000
/dev/input/event6: 0003 0035 00000cf7
/dev/input/event6: 0003 0036 0000664e
/dev/input/event6: 0000 0002 00000000
/dev/input/event6: 0000 0000 00000000
/dev/input/event6: 0003 0035 00001734
/dev/input/event6: 0003 0036 0000664e
/dev/input/event6: 0000 0002 00000000
/dev/input/event6: 0000 0000 00000000
/dev/input/event6: 0003 0035 00001975
/dev/input/event6: 0003 0036 0000664e
/dev/input/event6: 0000 0002 00000000
/dev/input/event6: 0000 0000 00000000
/dev/input/event6: 0003 0035 00001975
/dev/input/event6: 0003 0036 0000664e
/dev/input/event6: 0000 0002 00000000
/dev/input/event6: 0003 0035 000075ef
/dev/input/event6: 0003 0036 00005f02
/dev/input/event6: 0000 0002 00000000
/dev/input/event6: 0000 0000 00000000
/dev/input/event6: 0003 0035 00001975
/dev/input/event6: 0003 0036 0000664e
/dev/input/event6: 0000 0002 00000000
/dev/input/event6: 0000 0000 00000000
/dev/input/event6: 0003 0035 00001975
/dev/input/event6: 0003 0036 0000664e
/dev/input/event6: 0000 0002 00000000
/dev/input/event6: 0003 0035 000075ef
/dev/input/event6: 0003 0036 00005f02
/dev/input/event6: 0000 0002 00000000
/dev/input/event6: 0000 0000 00000000
/dev/input/event6: 0003 0035 00001975
/dev/input/event6: 0003 0036 0000664e
/dev/input/event6: 0000 0002 00000000
/dev/input/event6: 0000 0000 00000000
/dev/input/event6: 0003 0035 00001975
/dev/input/event6: 0003 0036 0000664e
/dev/input/event6: 0000 0002 00000000
/dev/input/event6: 0003 0035 000075ef
/dev/input/event6: 0003 0036 00005f02
/dev/input/event6: 0000 0002 00000000
/dev/input/event6: 0000 0000 00000000
/dev/input/event6: 0003 0035 00001975
/dev/input/event6: 0003 0036 0000664e
/dev/input/event6: 0000 0002 00000000
/dev/input/event6: 0000 0000 00000000
/dev/input/event6: 0000 0002 00000000
/dev/input/event6: 0000 0000 00000000
/dev/input/event6: 0003 0035 00000cf7
/dev/input/event6: 0003 0036 0000664e
/dev/input/event6: 0000 0002 00000000
/dev/input/event6: 0000 0000 00000000
/dev/input/event6: 0003 0035 00001734
/dev/input/event6: 0003 0036 0000664e
/dev/input/event6: 0000 0002 00000000
/dev/input/event6: 0000 0000 00000000
/dev/input/event6: 0003 0035 00001734
/dev/input/event6: 0003 0036 0000664e
/dev/input/event6: 0000 0002 00000000
/dev/input/event6: 0003 0035 000075ef
/dev/input/event6: 0003 0036 00005f02
/dev/input/event6: 0000 0002 00000000
/dev/input/event6: 0000 0000 00000000
/dev/input/event6: 0003 0035 00001975
/dev/input/event6: 0003 0036 0000664e
/dev/input/event6: 0000 0002 00000000
/dev/input/event6: 0003 0035 000075ef
/dev/input/event6: 0003 0036 00005f02
/dev/input/event6: 0000 0002 00000000
/dev/input/event6: 0000 0000 00000000
/dev/input/event6: 0003 0035 00001975
/dev/input/event6: 0003 0036 0000664e
/dev/input/event6: 0000 0002 00000000
/dev/input/event6: 0000 0000 00000000
/dev/input/event6: 0003 0035 00001975
/dev/input/event6: 0003 0036 0000664e
/dev/input/event6: 0000 0002 00000000
/dev/input/event6: 0003 0035 000075ef
/dev/input/event6: 0003 0036 00005f02
/dev/input/event6: 0000 0002 00000000
/dev/input/event6: 0000 0000 00000000
/dev/input/event6: 0003 0035 00001975
/dev/input/event6: 0003 0036 0000664e
/dev/input/event6: 0000 0002 00000000
/dev/input/event6: 0000 0000 00000000
/dev/input/event6: 0000 0002 00000000
/dev/input/event6: 0000 0000 00000000
'''
}

END_FIGHT_CLICK_CONTINUE_EVENT = {
    'desc': '结束战斗',
    'value': CLICK_CONTINUE_BUTTON
}


GOLD_DETAILS_CONTINUE_EVENT = {
    'desc': '展示金币明细',
    'value': CLICK_CONTINUE_BUTTON
}


RECEIVE_AWARD_GOLD_CLICK_CONTINUE_EVENT = {
    'desc': '领取战斗金币奖励',
    'value': CLICK_CONTINUE_BUTTON
}


annotation_event_map = {
    'wait_open_game.png': OPEN_GAME_EVENT,
    'wait_close_shop_ad.png': CLOSE_SHOP_AD_EVENT,
    # 通过这里控制参加哪个活动==>game_home_page
    'game_home_page.png': CLICK_DUEL_BUTTON_EVENT,
    'wait_click_fight_button.png': CLICK_START_FIGHT_BUTTON_EVENT,
    'wait_close_new_season_dialog.png': CLOSE_NEW_SEASON_DIALOG_EVENT,
    'end_fight_click_continue.png': END_FIGHT_CLICK_CONTINUE_EVENT,
    'gold_detail_click_continue.png': GOLD_DETAILS_CONTINUE_EVENT,
    'receive_award_gold_click_continue.png': RECEIVE_AWARD_GOLD_CLICK_CONTINUE_EVENT
}
