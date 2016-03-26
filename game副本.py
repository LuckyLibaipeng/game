# -*- coding: utf-8 -*-
#encoding:utf-8
"""
Created on Fri Mar 25 13:39:56 2016

@author: Lucky
"""
import random
print "游戏现在开!"
print "请您出0：石头,\n1:剪刀,\n2:布\n按Q退出游戏："
List =["石头","剪刀","布"]
WinDict = [("石头","剪刀"),("剪刀","布"),("布","石头")]
while True :
    user=raw_input("input (0,1,2):")
    if user not in ["0","1","2","Q"]:
        print '你的输入有误请重新输,按Q退出游戏'
        continue
    elif user=="Q":
        print '游戏已退出，再见！'
        break
    else :
        print '你出:', List[int(user)]
    C=random.choice(['石头','剪刀','布'])
    print "电脑出：",C
    if (List[int(user)],C) in WinDict :
        print "恭喜你！你赢了"
    elif List[int(user)]==C :
        print "平局"
    else :
        print "很遗憾！你输了"
    print "..........按Q退出游戏............."

       
     


