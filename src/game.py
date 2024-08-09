# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 11:06:15 2024

@author: Administrator
"""
import pygame
import math
from ballbase import Ball
from data_dic import ball_data,arcSide_data,lineSide_data
from const import BLACK,WHITE,GRAY,HOLE


class Game(object):
    def __init__(self, sc):
        self.sc = sc
        self.Balls = []
        self.Balls_get = []
        self.white_text = pygame.font.Font(None, 30)
        self.paused = False
        self.xuli = False
        
    def draw(self,fps):
        for ball in self.Balls:
            ball.draw(self.sc)
        # print(self.Balls)
        # for eachhole in HOLE:
        #     pygame.draw.circle(self.sc, GRAY, eachhole, 36)
        for i in range(len(arcSide_data)):
            color = arcSide_data[i+1]['COLOR']
            rect = arcSide_data[i+1]['RECT']
            start_angle = arcSide_data[i+1]['START_ANGLE']
            stop_angle = arcSide_data[i+1]['STOP_ANGLE']
            width = arcSide_data[i+1]['WIDTH']
            pygame.draw.arc(self.sc, 
                            color, 
                            rect, 
                            start_angle, 
                            stop_angle, 
                            width)
        
        for i in range(len(lineSide_data)):
            color = lineSide_data[i+1]['COLOR']
            start_point = lineSide_data[i+1]['START_POINT']
            stop_point = lineSide_data[i+1]['STOP_POINT']
            width = lineSide_data[i+1]['WIDTH']
            pygame.draw.line(self.sc, 
                            color, 
                            start_point, 
                            stop_point, 
                            width)

        self.renderFont(fps)
    
    def update(self):
        for ball in self.Balls:
             c = ball.move(self.Balls)
             if c:
                 continue
        
    def startGame(self):
        self.Balls.clear()
        # pygame.draw.arc(self.sc, 
        #                 (0,0,0), 
        #                 (128.8262,73.0531,18.8978,18.8978),
        #                 1.5707963267948966, 
        #                 2.356194490192345, 
        #                 2)

        for i in range(len(ball_data)):
            pos = ball_data[i]['LOCATION']
            b = Ball(pos,i)
            self.Balls.append(b)
            # if i >3:
            #     break

        # print(self.Balls)
        
    def fashe(self, xuli_time):
        mousePos = pygame.mouse.get_pos()
        for ball in self.Balls:
            if ball.controlable:
                pos = ball.pos
                angle = math.atan2(mousePos[1]-pos[1],mousePos[0]-pos[0])
                rate = 10 * xuli_time
                ball.speed[0] = rate * math.cos(angle)
                ball.speed[1] = rate * math.sin(angle)
        
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
    
    def pause(self):
        self.paused = True

        
        

            