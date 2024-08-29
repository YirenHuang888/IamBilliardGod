# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 22:48:35 2024

@author: Administrator
"""

import pygame
import sys
from game import Game
from const import screen_size,HOLE

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode(screen_size)
transparent_surface = pygame.Surface(screen_size, pygame.SRCALPHA).convert_alpha()
icon = pygame.image.load(r".\pic\icon.ico")
pygame.mixer.music.load(r".\snd\Beegie Adair - Black Orpheus (Carnival) (feat. Beegie Adair).flac")
game = Game(screen,transparent_surface)
game.startGame()
pygame.display.set_caption("台球游戏")
pygame.display.set_icon(icon)
clock = pygame.time.Clock()
mousePos = HOLE[0]
pygame.mixer.music.play(-1)

while True:
    # 实时检测鼠标是否出界
    if game.static and game.aiming == 'left' and not game.charge:
        # 全场静止且使用左键瞄准未蓄力时
        if game.inCourt(1,pygame.mouse.get_pos()):# 未出界
            mousePos = pygame.mouse.get_pos()  
            game.mouseOutside = False
        else:# 出界
            if not game.mouseOutside:# 第一次出界
                lastMousePos = mousePos# 记录出界位置
                game.mouseOutside = True
            else:# 第n次出界
                mousePos = lastMousePos
    
    # 事件检测
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            btn = event.button
            if btn == 1:# 鼠标左键按下
                # 蓄力
                t = 0
                if game.static and game.whiteBall:# 全场的球体都静止，且白球存在
                    game.charge = True
                # 摆球
                if game.baiqiu and game.inCourt(2,pygame.mouse.get_pos()):# 正在摆球且摆球没出界
                    game.placeWhiteBall(mousePos)
                    game.baiqiu = False
            if btn == 3:# 鼠标右键按下
                mousePos = pygame.mouse.get_pos()
                game.aiming = 'right'
                game.createTestBall(mousePos,1)
                if game.doubleclick():
                    game.aiming = 'left'
            if btn == 4:# 滚轮上滑
                mousePos = game.weitiao(mousePos,2)
                game.createTestBall(mousePos,1)
            if btn == 5:# 滚轮下滑
                mousePos = game.weitiao(mousePos,1)
                game.createTestBall(mousePos,1)
        elif event.type == pygame.MOUSEBUTTONUP:
                if game.charge:# 鼠标左键已被按下过
                    game.charge = 'Restore'
                    
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:# 空格暂停
                game.paused = not game.paused
            elif event.key == pygame.K_RETURN:# 回车重启游戏
                game.startGame()
            if event.key == pygame.K_1 and pygame.key.get_mods() & pygame.KMOD_LALT:# 同时按下Alt+1
                print('秘籍已启用！')
                pass
    
    # 暂停
    if game.paused:
        continue
    
    # 刷新屏幕part1
    game.update(mousePos)
    game.draw(clock.get_fps(),mousePos)

    # 蓄力击打
    if game.charge == True:# 蓄力情况时
        if game.aiming == 'left':
            mousePos = pygame.mouse.get_pos()
        t = game.xuli(t,mousePos)
    elif game.charge == 'Restore':# 释放情况时
        game.fashe(t,mousePos)

    # 刷新屏幕part2
    pygame.display.flip()
    
    # 控制帧率
    clock.tick(60)

