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
        self.Balls_get = []
        self.white_text = pygame.font.Font(None, 30)
        self.paused = False
        self.charge = False #总共有False、True、'Restore'三种状态，分别对应平常、蓄力、释放三种状态
        self.static = True
        
        self.stick_image = pygame.image.load("E:/Billiard God/IamBilliardGod/pic/stick.png").convert_alpha()
        self.awaypos = (0,0)

        
    def draw(self,fps,mousePos):
        count = 0
        pos = False
        
        #球洞绘制
        for hole in self.Holes:
            hole.draw(self.sc)
        #边界绘制
        for side in self.Sides:
            side.draw(self.sc)
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

        
        
        
        # 文字信息显示
        self.renderFont(fps)
        if pos:
            # 计算白球球心与鼠标的角度
            angle = math.atan2(mousePos[1]-pos[1],mousePos[0]-pos[0])
            # 旋转球杆子贴图
            self.rotated_stick = pygame.transform.rotate(self.stick_image, -math.degrees(angle))
            self.rotated_stick.set_colorkey(WHITE)
            self.stick_rect = self.rotated_stick.get_rect(center=pos)
            # 绘制旋转后的球杆子
            if self.static and not self.charge:# 所有球静止，且没有蓄力没有发射
                self.sc.blit(self.rotated_stick, self.stick_rect.topleft)
                # pygame.draw.rect(self.sc, (255,0,0), self.stick_rect, 2)
                # pygame.draw.circle(self.sc, GRAY, pos, 3)

    
    def update(self):
        for ball in self.Balls:
             b = ball.move(self.Balls,self.Sides,self.Holes)
             if b:
                 self.Balls.remove(b)
                 self.Balls_get.append(b)
        
    def startGame(self):
        self.Balls.clear()
        self.Sides.clear()
        self.Holes.clear()

        for i in range(len(ball_data)):
            pos = ball_data[i]['LOCATION']
            if i == 0:
                self.awaypos = pos
            b = Ball(pos,i)
            self.Balls.append(b)
            # if type(b) == Ball:
            #     print(type(b))
            # if i >3:
            #     break
        for holepos in HOLE:
            hole = Hole(holepos)
            self.Holes.append(hole)
        for arc in arcSide_data.values():
            arcside = Side(True, arc)
            self.Sides.append(arcside)
        for line in lineSide_data.values():
            lineside = Side(False, line)
            self.Sides.append(lineside)

        # print(self.Balls)
    
    def xuli(self,xuli_time, mousePos):
        for ball in self.Balls:
            if ball.controlable:
                pos = ball.pos
                angle = math.atan2(mousePos[1]-pos[1],mousePos[0]-pos[0])
                awayDistance = 50 * xuli_time
                # print(f'白球坐标为：{pos}，贴图中心坐标为：{self.stick_rect.center}')
                self.awaypos = (self.stick_rect.centerx + awayDistance * -math.cos(angle),
                                self.stick_rect.centery + awayDistance * -math.sin(angle))
                
                self.sc.blit(self.rotated_stick, 
                             (self.awaypos[0]-self.stick_rect.width/2,
                              self.awaypos[1]-self.stick_rect.height/2)
                             )
                # pygame.draw.rect(self.sc,
                #                  (255,0,0),
                #                  (self.awaypos[0]-self.stick_rect.width/2,
                #                   self.awaypos[1]-self.stick_rect.height/2,
                #                   self.stick_rect.width,
                #                   self.stick_rect.height),
                #                  2)
                # pygame.draw.circle(self.sc, GRAY, self.awaypos, 3)

                break
        xuli_time += 0.04
        if xuli_time >= 3:
            xuli_time = 3
        return xuli_time
    
    def fashe(self, xuli_time, mousePos):
        for ball in self.Balls:
            if ball.controlable:
                pos = ball.pos
                angle = math.atan2(mousePos[1]-pos[1],mousePos[0]-pos[0])
                backDistance = 50
                num_steps = 20  # 将每帧时间分解为100个小步长
            
                for _ in range(num_steps):# 将1帧的运动再细分100份
                    delta_d = backDistance / num_steps
                    self.awaypos = (self.awaypos[0] + delta_d * math.cos(angle),
                                    self.awaypos[1] + delta_d * math.sin(angle))
                    self.sc.blit(self.rotated_stick,
                                 (self.awaypos[0]-self.stick_rect.width/2,
                                  self.awaypos[1]-self.stick_rect.height/2)
                                 )
                    # pygame.draw.rect(self.sc,
                    #                  (255,0,0),
                    #                  (self.awaypos[0]-self.stick_rect.width/2,
                    #                   self.awaypos[1]-self.stick_rect.height/2,
                    #                   self.stick_rect.width,
                    #                   self.stick_rect.height),
                    #                  2)
                    # pygame.draw.circle(self.sc, GRAY, self.awaypos, 3)
    
                    if pos.distance_to(self.awaypos) <= ball.radius:
                        rate = 10 * xuli_time
                        ball.speed[0] = rate * math.cos(angle)
                        ball.speed[1] = rate * math.sin(angle)
                        self.charge = False
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

        
        

            