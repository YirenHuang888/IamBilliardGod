# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 11:06:15 2024

@author: Administrator
"""
import pygame
import math
from ballbase import Ball
from data_dic import data
from const import BLACK,WHITE


class Game(object):
    def __init__(self, sc):
        self.sc = sc
        self.Balls = pygame.sprite.Group()
        self.Balls_get = []
        self.white_text = pygame.font.Font(None, 30)

        
    def draw(self,fps):
        for ball in self.Balls:
            ball.draw(self.sc)
        # print(self.Balls)
        self.renderFont(fps)
        # for eachhole in HOLE:
        #     pygame.draw.circle(self.sc, GRAY, eachhole, 20)

    
    def update(self):
        for ball in self.Balls:
            ball.move(self.Balls)

        
    def startGame(self):
        for i in range(len(data)):
            pos = data[i]['LOCATION']
            b = Ball(pos,i)
            self.Balls.add(b)
            if i >0:
                break
        
    
    def mouseClickHandler(self, btn):
        mousePos = pygame.mouse.get_pos()
        for ball in self.Balls:
            if ball.controlable:
                pos = ball.pos
                angle = math.atan2(mousePos[1]-pos[1],mousePos[0]-pos[0])
                rate = 0
                if btn == 1:
                    rate = 18
                elif btn == 3:
                    rate = -18
                ball.speed[0] = rate * math.cos(angle)
                ball.speed[1] = rate * math.sin(angle)
        
    def renderFont(self,fps):
        textImage = self.white_text.render('FPS:{}'.format(int(fps)), True, BLACK)
        self.sc.blit(textImage, (13, 63))
        textImage = self.white_text.render('FPS:{}'.format(int(fps)), True, WHITE)
        self.sc.blit(textImage, (10, 60))

        for ball in self.Balls:
            if ball.controlable:
                wt_speed = ball.speed
                wt_pos = ball.pos
                wt_rect = ball.rect.center
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
                #rect坐标表
                textImage = self.white_text.render(str(wt_rect), True, BLACK)
                self.sc.blit(textImage, (223, 43))
                textImage = self.white_text.render(str(wt_rect), True, WHITE)
                self.sc.blit(textImage, (220, 40))

        
        

            