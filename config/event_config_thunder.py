#!/usr/bin/env python
# coding: utf-8
# @Time     : 2021/5/14 22:21
# @Author   : toddler
# @FileName : event_config_bs.py
# @Project  : ShadowFightRobot


CLICK_CONTINUE_BUTTON = '''
/dev/input/event3: 0003 0039 00000005
/dev/input/event3: 0001 014a 00000001
/dev/input/event3: 0003 0035 000006dd
/dev/input/event3: 0003 0036 000003c2
/dev/input/event3: 0000 0000 00000000
/dev/input/event3: 0003 0039 ffffffff
/dev/input/event3: 0001 014a 00000000
/dev/input/event3: 0000 0000 00000000
'''


# 打开游戏
OPEN_GAME_EVENT = {
    'desc': '打开游戏',
    'value': '''
/dev/input/event3: 0003 0039 0000004d
/dev/input/event3: 0001 014a 00000001
/dev/input/event3: 0003 0035 00000689
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

# 打一套连招
COMBO_EVENT = {
    'desc': '开始连招攻击',
    'value': '''
/dev/input/event3: 0003 0039 00000008
/dev/input/event3: 0001 014a 00000001
/dev/input/event3: 0003 003a 00000002
/dev/input/event3: 0003 0035 000000b3
/dev/input/event3: 0003 0036 00000371
/dev/input/event3: 0000 0000 00000000
/dev/input/event3: 0003 002f 00000001
/dev/input/event3: 0003 0039 00000009
/dev/input/event3: 0003 003a 00000002
/dev/input/event3: 0003 0035 000006ee
/dev/input/event3: 0003 0036 00000338
/dev/input/event3: 0000 0000 00000000
/dev/input/event3: 0003 002f 00000000
/dev/input/event3: 0003 0035 000000b8
/dev/input/event3: 0003 0036 00000372
/dev/input/event3: 0000 0000 00000000
/dev/input/event3: 0003 0035 000000bc
/dev/input/event3: 0003 0036 00000373
/dev/input/event3: 0000 0000 00000000
/dev/input/event3: 0003 0035 000000e7
/dev/input/event3: 0003 0036 00000372
/dev/input/event3: 0000 0000 00000000
/dev/input/event3: 0003 0035 00000101
/dev/input/event3: 0000 0000 00000000
/dev/input/event3: 0003 0035 0000011a
/dev/input/event3: 0003 0036 00000371
/dev/input/event3: 0000 0000 00000000
/dev/input/event3: 0003 0035 00000134
/dev/input/event3: 0000 0000 00000000
/dev/input/event3: 0003 002f 00000001
/dev/input/event3: 0003 0039 ffffffff
/dev/input/event3: 0000 0000 00000000
/dev/input/event3: 0003 002f 00000000
/dev/input/event3: 0003 0036 00000372
/dev/input/event3: 0000 0000 00000000
/dev/input/event3: 0003 0035 00000135
/dev/input/event3: 0003 0036 00000371
/dev/input/event3: 0000 0000 00000000
/dev/input/event3: 0003 0036 00000372
/dev/input/event3: 0000 0000 00000000
/dev/input/event3: 0003 002f 00000001
/dev/input/event3: 0003 0039 0000000a
/dev/input/event3: 0003 0035 000006ed
/dev/input/event3: 0003 0036 00000339
/dev/input/event3: 0000 0000 00000000
/dev/input/event3: 0003 002f 00000000
/dev/input/event3: 0003 0035 00000134
/dev/input/event3: 0003 0036 00000371
/dev/input/event3: 0000 0000 00000000
/dev/input/event3: 0003 002f 00000001
/dev/input/event3: 0003 0039 ffffffff
/dev/input/event3: 0000 0000 00000000
/dev/input/event3: 0003 0039 0000000b
/dev/input/event3: 0003 0035 000006ee
/dev/input/event3: 0000 0000 00000000
/dev/input/event3: 0003 0039 ffffffff
/dev/input/event3: 0000 0000 00000000
/dev/input/event3: 0003 0039 0000000c
/dev/input/event3: 0000 0000 00000000
/dev/input/event3: 0003 0039 ffffffff
/dev/input/event3: 0000 0000 00000000
/dev/input/event3: 0003 0039 0000000d
/dev/input/event3: 0003 0036 00000338
/dev/input/event3: 0000 0000 00000000
/dev/input/event3: 0003 0039 ffffffff
/dev/input/event3: 0000 0000 00000000
/dev/input/event3: 0003 0039 0000000e
/dev/input/event3: 0003 0036 00000339
/dev/input/event3: 0000 0000 00000000
/dev/input/event3: 0003 0039 ffffffff
/dev/input/event3: 0000 0000 00000000
/dev/input/event3: 0003 0039 0000000f
/dev/input/event3: 0000 0000 00000000
/dev/input/event3: 0003 0039 ffffffff
/dev/input/event3: 0000 0000 00000000
/dev/input/event3: 0003 002f 00000000
/dev/input/event3: 0003 0039 ffffffff
/dev/input/event3: 0001 014a 00000000
/dev/input/event3: 0000 0000 00000000
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
