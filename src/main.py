# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 22:48:35 2024

@author: Administrator
"""

import pygame
import sys
from game import Game
from const import screen_size,GREEN

pygame.init()
screen = pygame.display.set_mode(screen_size)
game = Game(screen)
pygame.display.set_caption("台球游戏")
clock = pygame.time.Clock()
game.startGame()

while True:
    # 常用变量
    fps = clock.get_fps()
    if not game.aiming or not game.mouseOutside:
        mousePos = pygame.mouse.get_pos()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            btn = event.button
            if btn == 1:# 鼠标左键按下
                if game.baiqiu:
                    print(not 97.3835+18 < mousePos[0] < 1269.9695-18,
                          not 91.9509+18 < mousePos[1] < 676.1886-18,
                          game.intheHole(mousePos),sep='\n')
                    # 如果不在范围
                    if (not 97.3835+18 < mousePos[0] < 1269.9695-18 or
                        not 91.9509+18 < mousePos[1] < 676.1886-18 or
                        game.intheHole(mousePos)):
                        game.mouseOutside = True
                        continue
                    game.placeWhiteBall(mousePos)
                    game.baiqiu = False
                t = 0
                if game.static and game.whiteBall:# 全场的球体都静止，且白球存在
                    game.charge = True
            if btn == 3:# 鼠标右键按下
                mousePos = pygame.mouse.get_pos()
                game.aiming = True
                if game.doubleclick():
                    game.aiming = False
            if btn == 2:# 鼠标中键取消瞄准
                game.aiming = False
        elif event.type == pygame.MOUSEBUTTONUP:
                if game.charge:# 鼠标左键已被按下过
                    game.charge = 'Restore'
                    
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:# 空格暂停
                game.paused = not game.paused
            elif event.key == pygame.K_RETURN:# 回车重启游戏
                game.startGame()
    # 暂停
    if game.paused:
        continue
    
    # 刷新屏幕1
    screen.fill(GREEN)
    game.update(mousePos)
    game.draw(fps,mousePos)
    
    # 蓄力击打
    if game.charge == True:# 蓄力情况时
        t = game.xuli(t,mousePos)
    elif game.charge == 'Restore':# 反弹情况时
        game.fashe(t,mousePos)
    
    # 刷新屏幕2
    pygame.display.flip()
    
    # 控制帧率
    clock.tick(60)

