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
from data_dic import ball_data,arcSide_data,lineSide_data
from const import BLACK,WHITE,GRAY,HOLE


class Game(object):
    def __init__(self, sc):
        self.sc = sc
        self.Balls = []
        self.Sides = []
        self.Balls_get = []
        self.white_text = pygame.font.Font(None, 30)
        self.paused = False
        self.charge = False #总共有False、True、'Restore'三种状态，分别对应平常、蓄力、释放三种状态
        self.static = True
        self.stick_image = pygame.image.load("E:/Billiard God/IamBilliardGod/pic/stick.png").convert_alpha()
        self.awaypos = (0,0)

        
    def draw(self,fps,mousePos):
        count = 0
        #球体绘制
        for ball in self.Balls:
            ball.draw(self.sc)
            
            if ball.speed:
                self.static = False
            else:
                count += 1
                if count == len(self.Balls):
                    self.static = True
                        
            if ball.controlable:
                pos = ball.pos
        #边界绘制
        for side in self.Sides:
            side.draw(self.sc)

        
        # print(self.Balls)
        # for eachhole in HOLE:
        #     pygame.draw.circle(self.sc, GRAY, eachhole, 36)
        
        
        # 文字信息显示
        self.renderFont(fps)
        
        if not self.charge:# 只有处在False时,即平常时
            # 计算白球球心与鼠标的角度
            angle = math.atan2(mousePos[1]-pos[1],mousePos[0]-pos[0])
            # 旋转球杆子贴图
            self.rotated_stick = pygame.transform.rotate(self.stick_image, -math.degrees(angle))
            self.rotated_stick.set_colorkey(WHITE)
            self.stick_rect = self.rotated_stick.get_rect(center=pos)
            # 绘制旋转后的球杆子
            if self.static:
                self.sc.blit(self.rotated_stick, self.stick_rect.topleft)
                pygame.draw.circle(self.sc, GRAY, pos, 3)


    
    def update(self):
        for ball in self.Balls:
             c = ball.move(self.Balls)
             if c:
                 continue
        
    def startGame(self):
        self.Balls.clear()
        self.Sides.clear()

        for i in range(len(ball_data)):
            pos = ball_data[i]['LOCATION']
            if i == 0:
                self.awaypos = pos
            b = Ball(pos,i)
            self.Balls.append(b)
            # if i >3:
            #     break
        
        for arc in arcSide_data.values():
            arcside = Side(True, arc)
            self.Sides.append(arcside)
        for line in lineSide_data.values():
            lineside = Side(False, line)
            self.Sides.append(lineside)

        # print(self.Balls)
    
    def xuli(self,xuli_time, mousePos):
        if self.charge == True:# 蓄力情况时
            for ball in self.Balls:
                if ball.controlable:
                    pos = ball.pos
                    angle = math.atan2(mousePos[1]-pos[1],mousePos[0]-pos[0])
                    awayspeed = 50 * xuli_time
                    # print(f'白球坐标为：{pos}，贴图中心坐标为：{self.stick_rect.center}')
                    self.awaypos = (self.stick_rect.x + awayspeed * -math.cos(angle),
                                    self.stick_rect.y + awayspeed * -math.sin(angle))
                    
                    self.sc.blit(self.rotated_stick, self.awaypos)
                    break
            xuli_time += 0.04
            if xuli_time >= 3:
                xuli_time = 3
            return xuli_time
    
    def fashe(self, xuli_time, mousePos):
        if self.charge == 'Restore':
            for ball in self.Balls:
                if ball.controlable:
                    pos = ball.pos
                    angle = math.atan2(mousePos[1]-pos[1],mousePos[0]-pos[0])
                    backspeed = 10
                    self.awaypos = (self.awaypos[0] + backspeed * math.cos(angle),
                                    self.awaypos[1] + backspeed * math.sin(angle))
                    self.sc.blit(self.rotated_stick, self.awaypos)
                    if pos.distance_to(self.awaypos) <= ball.radius:
                        rate = 10 * xuli_time
                        ball.speed[0] = rate * math.cos(angle)
                        ball.speed[1] = rate * math.sin(angle)
                    break
        
    def renderFont(self,fps):
        # FPS显示
        textImage = self.white_text.render('FPS:{}'.format(int(fps)), True, BLACK)
        self.sc.blit(textImage, (1280, 23))
        textImage = self.white_text.render('FPS:{}'.format(int(fps)), True, WHITE)
        self.sc.blit(textImage, (1280, 20))
        
        for ball in self.Balls:
            if ball.controlable:
                wt_speed = ball.speed
                wt_pos = ball.pos
                #速度表
                textImage = self.white_text.render("vx: " + str(round(wt_speed[0],2)) + "  vy: " + str(round(wt_speed[1],2)) + ' v: ' + str(round(wt_speed.length(),2)), True, BLACK)
                self.sc.blit(textImage, (13, 23))
                textImage = self.white_text.render("vx: " + str(round(wt_speed[0],2)) + "  vy: " + str(round(wt_speed[1],2)) + ' v: ' + str(round(wt_speed.length(),2)), True, WHITE)
                self.sc.blit(textImage, (10, 20))
                #pos坐标表
                textImage = self.white_text.render("x: " + str(round(wt_pos[0],1)) + "  y: " + str(round(wt_pos[1],1)), True, BLACK)
                self.sc.blit(textImage, (13, 43))
                textImage = self.white_text.render("x: " + str(round(wt_pos[0],1)) + "  y: " + str(round(wt_pos[1],1)), True, WHITE)
                self.sc.blit(textImage, (10, 40))
                break
    
    def pause(self):
        self.paused = True

        
        

            