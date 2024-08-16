
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
t = 0

while True:
    # 常用变量
    fps = clock.get_fps()
    mousePos = pygame.mouse.get_pos()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        #鼠标左键按下蓄力，松开击打
        elif event.type == pygame.MOUSEBUTTONDOWN:
            t = 0
            if game.static:# 全场的球体都静止
                game.charge = True
        elif event.type == pygame.MOUSEBUTTONUP:
            if game.charge:
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
    game.update()
    game.draw(fps,mousePos)
    
    # 蓄力击打
    t = game.xuli(t,mousePos)
    game.fashe(t,mousePos)
    
    # 刷新屏幕2
    pygame.display.flip()
    
    # 控制帧率
    clock.tick(60)

