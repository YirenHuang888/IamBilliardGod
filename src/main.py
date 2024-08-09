
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
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        #鼠标左键按下蓄力，松开击打
        elif event.type == pygame.MOUSEBUTTONDOWN:
            game.xuli = True
            t = 0
        elif event.type == pygame.MOUSEBUTTONUP:
            game.xuli = False
            game.fashe(t)
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:# 空格暂停
                game.paused = not game.paused
            elif event.key == pygame.K_RETURN:# 重启游戏
                game.startGame()
    # 暂停
    if game.paused:
        continue
    # 蓄力击打
    if game.xuli:      
        t += 0.04
        if t >= 3:
            t = 3
    # 刷新屏幕
    game.update()
    screen.fill(GREEN)
    fps = clock.get_fps()
    game.draw(fps)
    pygame.display.flip()
    
    # 控制帧率
    clock.tick(60)

