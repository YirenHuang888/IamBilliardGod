# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 20:26:52 2024

@author: Administrator
"""
import pygame

class Side():
    def __init__(self,IFarc,dic):
        self.IFarc = IFarc
        if self.IFarc:# 曲线边界
            self.color = dic['COLOR']
            self.rect = [round(i) for i in dic['RECT']]
            self.start_angle = dic['START_ANGLE']
            self.stop_angle = dic['STOP_ANGLE']
        else:
            self.color = dic['COLOR']
            self.start_point = dic['START_POINT']
            self.stop_point = dic['STOP_POINT']
        
        self.width = 1
        self.IFcollide = dic['COLLIDE']

        pass
    
    def draw(self,screen):
        if self.IFarc:# 曲线边界
            pygame.draw.arc(screen, 
                            self.color, 
                            self.rect, 
                            self.start_angle, 
                            self.stop_angle, 
                            self.width)
        else:# 直线边界
            pygame.draw.line(screen, 
                            self.color, 
                            self.start_point, 
                            self.stop_point, 
                            self.width)



 