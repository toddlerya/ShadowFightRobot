#!/usr/bin/env python
# coding: utf-8
# @Time     : 2021/5/14 22:14
# @Author   : toddler
# @FileName : trans.py
# @Project  : ShadowFightRobot


def hex2dec(line):
    """
    将事件中的16进制数字转为10进制
    :params line: 示例: /dev/input/event3 0003 0039 000007c5
    """
    __sp_line = line.split(' ')
    temp = list()
    temp.append(__sp_line[0])
    for each in __sp_line[1:]:
        dec = int(each, 16)
        temp.append(str(dec))
    return ' '.join(temp)
