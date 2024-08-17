# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 20:26:52 2024

@author: Administrator
"""
import pygame

class Side():
    def __init__(self,IFarc,dic):
        self.IFarc = IFarc
        self.toward = False
        if self.IFarc:# 曲线边界
            self.color = dic['COLOR']
            self.rect = [round(i) for i in dic['RECT']]
            self.pos = pygame.Vector2(dic['RECT'][0]+dic['RECT'][2],dic['RECT'][1]+dic['RECT'][3])
            self.start_angle = dic['START_ANGLE']
            self.stop_angle = dic['STOP_ANGLE']
            self.speed = pygame.Vector2(0,0)
        else:
            self.color = dic['COLOR']
            self.start_point = dic['START_POINT']
            self.stop_point = dic['STOP_POINT']
            # print(self.start_point,self.stop_point,sep=',')
            if self.start_point[0] == self.stop_point[0]:# 竖着的
                self.toward = 'shu'
                # print('shu')
            elif self.start_point[1] == self.stop_point[1]:# 横着的
                self.toward = 'heng'
                # print('heng')
        self.width = 1
        self.IFcollide = dic['COLLIDE']
    
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
    
    def distance2ball(self,ball):
        if self.IFarc:# 曲线边界
            print(f'我{ball.id}号球与这个曲线边界的距离是{self.pos.distance_to(ball.pos)}',end='\n -------\n')
            return self.pos.distance_to(ball.pos)
        
        else:# 直线边界
            # 竖着的，且在上下之间
            if (self.toward == 'shu' and
                min(self.start_point[1], self.start_point[1]) < ball.pos.y < max(self.start_point[1], self.start_point[1])
                ):
                print(f'我{ball.id}号球与这个竖直边界的距离是{abs(ball.pos.x - self.start_point[0])}',end='\n -------\n')
                return abs(ball.pos.x - self.start_point[0])
            # 横着的，且在左右之间
            elif (self.toward == 'heng' and
                  min(self.start_point[0], self.start_point[0]) < ball.pos.x < max(self.start_point[0], self.start_point[0])
                  ):
                print(f'我{ball.id}号球与这个水平边界的距离是{abs(ball.pos.y - self.start_point[1])}',end='\n -------\n')
                return abs(ball.pos.y - self.start_point[1])
        print(f'我的起始点是{self.start_point}，结束点是{self.stop_point}。现在是{ball.id}号球')

        return 100


 