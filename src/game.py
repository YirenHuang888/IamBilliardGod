# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 11:06:15 2024

@author: Administrator
"""
import pygame
import math
from ballbase import Ball
from side import Side
from stick import Stick
from hole import Hole
from data_dic import ball_data,arcSide_data,lineSide_data
from const import BLACK,WHITE,GRAY,HOLE


class Game(object):
    def __init__(self, sc):
        self.sc = sc
        self.Balls = []
        self.Sides = []
        self.Holes = []
        self.Stick = None
        self.Balls_get = []
        self.white_text = pygame.font.Font(None, 30)
        self.paused = False
        self.charge = False #总共有False、True、'Restore'三种状态，分别对应平常、蓄力、释放三种状态
        self.static = True
        
    def draw(self,fps):        
        #球洞绘制
        for hole in self.Holes:
            hole.draw(self.sc)
        #边界绘制
        for side in self.Sides:
            side.draw(self.sc)
        #球体绘制
        for ball in self.Balls:
            ball.draw(self.sc)
        # 球杆绘制
        if self.static and not self.charge and self.whiteBall:
            self.Stick.draw(self.sc)
        # 文字信息显示
        self.renderFont(fps)
    
    def update(self,mousePos):
        count = 0
        # 球类移动
        for ball in self.Balls:
            if ball.controlable:
                self.whiteBall = ball
            if ball.speed:
                self.static = False
                b = ball.move(self.Balls,self.Sides,self.Holes)
                if b:
                    self.Balls.remove(b)
                    self.Balls_get.append(b)
                    b.speed = pygame.Vector2(0, 0)
                    if b == self.whiteBall:# 白球进洞
                        self.whiteBall = False
                        self.charge = False
                ball.fric(0.99)
                if ball.speed.length() <= 0.2:
                    ball.speed = pygame.Vector2(0, 0)
            else:
                count += 1
                if count == len(self.Balls):
                    self.static = True
    
        
        # 球杆旋转
        if self.whiteBall:# 如果白球在场
            self.Stick.rotate(self.whiteBall.pos, mousePos)
        else:# 如果白球不在场
            self.Stick.centerPos = (1,1)

        
    def startGame(self):
        # 删除现有对象
        for ball in self.Balls:
            del ball
        for side in self.Sides:
            del side
        for hole in self.Holes:
            del hole
        del self.Stick

        # 初始化球类
        for i in range(len(ball_data)):
            pos = ball_data[i]['LOCATION']
            if i == 0:
                self.awaypos = pos
            b = Ball(pos,i)
            self.Balls.append(b)
        # 初始化球杆子
        self.Stick = Stick("E:/Billiard God/IamBilliardGod/pic/stick.png")
        # 初始化球洞
        for holepos in HOLE:
            hole = Hole(holepos)
            self.Holes.append(hole)
        # 初始化曲线边界
        for arc in arcSide_data.values():
            arcside = Side(True, arc)
            self.Sides.append(arcside)
        # 初始化直线边界
        for line in lineSide_data.values():
            lineside = Side(False, line)
            self.Sides.append(lineside)
    
    def xuli(self,xuli_time, mousePos):
        if self.whiteBall:
            # 球杆向后退蓄力
            self.Stick.away(self.sc, xuli_time, mousePos)
            
            # 增加蓄力时间
            xuli_time += 0.04
            if xuli_time >= 3:
                xuli_time = 3
            return xuli_time
    
    def fashe(self, xuli_time, mousePos):
        if self.whiteBall:# 如果白球在场
            num_steps = 20 # 将每帧时间分解为20个小步长
            backSpeed = 50 # 出杆速度
            for _ in range(num_steps): # 将1帧的运动再细分20份
                # 释放球杆
                dv = backSpeed / num_steps # 每份的移动速度
                centerPos,angle = self.Stick.back(self.sc, dv, mousePos)
                
                # 击打白球
                if self.whiteBall.pos.distance_to(centerPos) <= 1:
                    rate = 10 * xuli_time
                    self.whiteBall.speed[0] = rate * math.cos(angle)
                    self.whiteBall.speed[1] = rate * math.sin(angle)
                    self.charge = False

    def renderFont(self,fps):
        # FPS显示
        textImage = self.white_text.render('FPS:{}'.format(int(fps)), True, BLACK)
        self.sc.blit(textImage, (1280, 23))
        textImage = self.white_text.render('FPS:{}'.format(int(fps)), True, WHITE)
        self.sc.blit(textImage, (1280, 20))
        
        # 计分板
        score = len(self.Balls_get) * 10
        textImage = self.white_text.render('SCORE:{}'.format(score), True, BLACK)
        self.sc.blit(textImage, (10, 23))
        textImage = self.white_text.render('SCORE:{}'.format(score), True, WHITE)
        self.sc.blit(textImage, (10, 20))

            
    def pause(self):
        self.paused = True

        
        

            