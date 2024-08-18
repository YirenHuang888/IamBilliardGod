# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 15:50:36 2024

@author: Administrator
"""
import pygame
from const import GRAY

class Hole():
    def __init__(self,pos):
        self.pos = pygame.Vector2(pos)
        self.radius = 36
        
    def draw(self,sc):
        pygame.draw.circle(sc, GRAY, (self.pos.x,self.pos.y), self.radius)
 