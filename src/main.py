
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
        elif event.type == pygame.MOUSEBUTTONDOWN:
            game.mouseClickHandler(event.button)
    
    # 刷新屏幕
    game.update()
    screen.fill(GREEN)
    fps = clock.get_fps()
    game.draw(fps)
    pygame.display.flip()
    
    # 控制帧率
    clock.tick(60)

