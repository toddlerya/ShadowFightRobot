#!/usr/bin/env python
# coding: utf-8
# @Time     : 2021/5/14 22:21
# @Author   : toddler
# @FileName : tap_config.py
# @Project  : ShadowFightRobot


button_points = {
    'open_fight': {
        'x': 2127,
        'y': 940
    },
    'fist': {
        'x': 2015,
        'y': 720
    },
    'start_fight': {
        'x': 1201,
        'y': 940
    },
    'end_fight_continue': {
        'x': 1980,
        'y': 960
    }
}


CLICK_DUEL_BUTTON_EVENT = {
    'desc': '打开决斗',
    'value': button_points['open_fight']
}


CLICK_START_FIGHT_BUTTON_EVENT = {
    'desc': '开始战斗',
    'value': button_points['start_fight']
}

COMBO_EVENT = {
    'desc': '开始攻击',
    'value': button_points['fist']
}

END_FIGHT_CLICK_CONTINUE_EVENT = {
    'desc': '结束战斗',
    'value': button_points['end_fight_continue']
}

GOLD_DETAILS_CONTINUE_EVENT = {
    'desc': '展示金币明细',
    'value': button_points['end_fight_continue']
}

RECEIVE_AWARD_GOLD_CLICK_CONTINUE_EVENT = {
    'desc': '领取战斗金币奖励',
    'value': button_points['end_fight_continue']
}


annotation_event_map = {
    # 'thunder_wait_open_game.png': OPEN_GAME_EVENT,
    # 'wait_close_shop_ad.png': CLOSE_SHOP_AD_EVENT,
    # 通过这里控制参加哪个活动==>game_home_page
    'game_home_page.png': CLICK_DUEL_BUTTON_EVENT,
    'wait_click_fight_button.png': CLICK_START_FIGHT_BUTTON_EVENT,
    # 'wait_close_new_season_dialog.png': CLOSE_NEW_SEASON_DIALOG_EVENT,
    'end_fight_click_continue_hero.png': END_FIGHT_CLICK_CONTINUE_EVENT,
    'end_fight_click_continue_champion.png': END_FIGHT_CLICK_CONTINUE_EVENT,
    'gold_detail_click_continue.png': GOLD_DETAILS_CONTINUE_EVENT,
    'receive_award_gold_click_continue.png': RECEIVE_AWARD_GOLD_CLICK_CONTINUE_EVENT,
    'fighting.png': COMBO_EVENT
}