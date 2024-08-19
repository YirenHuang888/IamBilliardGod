# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 15:50:36 2024

@author: Administrator
"""
import pygame
import math
from const import WHITE

class Stick():
    def __init__(self,path):
        self.image = pygame.image.load(path).convert_alpha()
        self.centerPos = (1,1)
    
    def rotate(self,ballPos,mousePos):
        self.centerPos = ballPos
        # 计算白球球心与鼠标的角度
        angle = math.atan2(mousePos[1]-self.centerPos[1],mousePos[0]-self.centerPos[0])
        # 旋转球杆子贴图
        self.rotated_stick = pygame.transform.rotate(self.image, -math.degrees(angle))
        self.rotated_stick.set_colorkey(WHITE)# 使底色变透明
        self.stick_rect = self.rotated_stick.get_rect(center=self.centerPos)
    
    def draw(self,screen):
        # 绘制旋转后的球杆子
        screen.blit(self.rotated_stick, self.stick_rect.topleft)
    
    def away(self,screen,t,mousePos):
        # 计算后退距离
        angle = math.atan2(mousePos[1]-self.centerPos[1],mousePos[0]-self.centerPos[0])
        awayDistance = 50 * t
        self.awaypos = (self.stick_rect.centerx + awayDistance * -math.cos(angle),
                        self.stick_rect.centery + awayDistance * -math.sin(angle))
        
        # 绘制蓄力后退的球杆子
        screen.blit(self.rotated_stick, 
                     (self.awaypos[0]-self.stick_rect.width/2,
                      self.awaypos[1]-self.stick_rect.height/2)
                     )
    
    def back(self,screen,dv,mousePos):
        angle = math.atan2(mousePos[1]-self.centerPos[1],mousePos[0]-self.centerPos[0])
        self.awaypos = (self.awaypos[0] + dv * math.cos(angle),
                        self.awaypos[1] + dv * math.sin(angle))
        screen.blit(self.rotated_stick,
                     (self.awaypos[0]-self.stick_rect.width/2,
                      self.awaypos[1]-self.stick_rect.height/2)
                     )
        
        return self.centerPos,angle
            

 