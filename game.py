# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 11:06:15 2024

@author: Administrator
"""
import pygame
import math
import time
import random 
from ballbase import Ball
from side import Side
from stick import Stick
from hole import Hole
from data_dic import ball_data,arcSide_data,lineSide_data
from const import BLACK,WHITE,HOLE,TRANSPARENT,START_LOCATION


class Game(object):
    def __init__(self, sc, tpsc):
        self.sc = sc
        self.tpsc = tpsc
        self.white_text = pygame.font.Font(None, 30)
        self.bg = pygame.image.load(r".\pic\side.png").convert()

    def startGame(self):
        # 状态重置
        self.Stick = None # 球杆对象
        self.paused = False #是否暂停
        self.static = True # 是否击球结束
        self.charge = False #总共有False、True、'Restore'三种状态，分别对应平常、蓄力、释放三种状态
        self.baiqiu = False # 是否要摆球
        self.mouseOutside = False # 是否鼠标位于界外
        self.aiming = 'left' # 处于左键、右键瞄准状态
        self.timing = [] # 计算点击间隔，判断双击
        self.Balls = [] # 球类
        self.Sides = [] # 边界
        self.Holes = [] # 球洞
        self.Balls_get = [] # 进洞的球，算分
        self.score = 0 # 分数
        self.cldPos = [] # 用于绘制右键瞄准线
        
        # 初始化球类
        self.testBall = None
        START_POS = self.allocateStartPos(START_LOCATION)
        for i in range(len(ball_data)):
            pos = START_POS[i]
            b = Ball(pos,i)
            self.Balls.append(b)
            if i == 0:
                self.whiteBall = b
        # 初始化球杆子
        self.Stick = Stick("./pic/stick.png")
        # 初始化球洞
        for holepos in HOLE:
            hole = Hole(holepos)
            self.Holes.append(hole)
        # 初始化直线边界
        for line in lineSide_data.values():
            lineside = Side(False, line)
            self.Sides.append(lineside)
        # 初始化曲线边界
        for arc in arcSide_data.values():
            arcside = Side(True, arc)
            self.Sides.append(arcside)
            
    def draw(self,fps,mousePos):                
        # 背景图
        self.sc.blit(self.bg,(0,0))
        self.tpsc.fill(TRANSPARENT)
        
        #球洞绘制
        for hole in self.Holes:
            hole.draw(self.sc)
        #边界绘制
        for side in self.Sides:
            side.draw(self.sc)
        #球体绘制
        for ball in self.Balls:
            ball.draw(self.sc)
        
        if self.static:
            if self.whiteBall:
                self.drawAimLine(mousePos)# 瞄准线绘制
                if not self.charge:
                    self.Stick.draw(self.sc)# 球杆绘制
            else:
                pygame.draw.circle(self.sc, WHITE, mousePos, 18)
        
        # 文字信息显示
        self.renderFont(fps)
    
    def update(self,mousePos):
        # 正常计算球体位置
        if not self.static:# 击球后才运行
            count = 0
            # 球类移动
            for ball in self.Balls:
                if ball.speed:# 只针对有速度的球
                    obj, typ = ball.move(self.Balls,self.Sides,self.Holes)# 让球动起来
                    if typ == 'self':# 有球进洞了
                        self.Balls.remove(obj)
                        self.Balls_get.append(obj)
                        obj.speed = pygame.Vector2(0, 0)
                        if obj == self.whiteBall:# 是白球进洞
                            self.whiteBall = None
                            self.charge = False
                            self.Balls_get.remove(obj)
                            self.baiqiu = True
                            self.aiming = 'left'
                        self.score = len(self.Balls_get) * 10
                    ball.fric(0.99)
                    if ball.speed.length() <= 0.2:
                        ball.speed = pygame.Vector2(0, 0)
                else:
                    count += 1
                    if count == len(self.Balls):
                        self.static = True
                        if self.aiming == 'right':
                            self.createTestBall(mousePos,1)
        # 计算瞄准线位置
        if self.aiming == 'right' and self.testBall:
            typ, obj, tbpos, tbspd, objspd = self.testBall.simulateShoot(self.Balls,self.Sides,self.Holes)
            if typ:
                self.cldPos.append([self.whiteBall.pos, tbpos, 1])
                self.testBall = None
                if typ == 'ball':
                    newTbPos = tbpos + 60 * tbspd.normalize()
                    newObjPos = obj.pos + 60 * objspd.normalize()
                    self.cldPos.append([tbpos, newTbPos, 0])
                    self.cldPos.append([obj.pos, newObjPos, 0])
                elif typ == 'side':
                    pass
                elif typ == 'self':
                    pass
        
        # 球杆旋转
        if self.whiteBall:# 如果白球在场
            self.Stick.rotate(self.whiteBall.pos, mousePos)
        else:# 如果白球不在场
            self.Stick.centerPos = (0,0)
    
    def xuli(self,xuli_time, mousePos):
        if self.whiteBall:
            # 球杆向后退蓄力
            self.Stick.away(self.sc, xuli_time, mousePos)
            # 增加蓄力时间
            xuli_time += 0.05
            max_time = 3
            if xuli_time >= max_time:
                xuli_time = max_time
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
                    self.static = False

    def renderFont(self,fps):
        # FPS显示
        textImage = self.white_text.render('FPS:{}'.format(int(fps)), True, BLACK)
        self.sc.blit(textImage, (1280, 13))
        textImage = self.white_text.render('FPS:{}'.format(int(fps)), True, WHITE)
        self.sc.blit(textImage, (1280, 10))
        
        # 计分板
        textImage = self.white_text.render('SCORE: {}'.format(int(self.score)), True, BLACK)
        self.sc.blit(textImage, (10, 13))
        textImage = self.white_text.render('SCORE: {}'.format(int(self.score)), True, WHITE)
        self.sc.blit(textImage, (10, 10))

            
    def pause(self):
        self.paused = True
     
    def createTestBall(self, aimPos, mode):
        self.cldPos.clear()
        if mode == 1:
            if self.whiteBall:
                angle = math.atan2(aimPos[1]-self.whiteBall.pos[1],aimPos[0]-self.whiteBall.pos[0])
                self.testBall = Ball(self.whiteBall.pos,0)
                self.testBall.speed[0] = 1000 * math.cos(angle)
                self.testBall.speed[1] = 1000 * math.sin(angle)
        elif mode == 2:
            pass
            
    def drawAimLine(self, mousePos):
        if self.aiming == 'right':# 右键瞄准
            for Pospair in self.cldPos: 
                if Pospair[2] == 1:
                    # 创建圆环
                    pygame.draw.circle(self.tpsc, WHITE, Pospair[1], 18)
                    pygame.draw.circle(self.tpsc, TRANSPARENT, Pospair[1], 18-2)
                    self.sc.blit(self.tpsc, (0, 0))
                # 连线
                pygame.draw.line(self.sc, WHITE, Pospair[0], Pospair[1], 2)

        elif self.aiming == 'left':# 左键瞄准
            # 创建圆环
            pygame.draw.circle(self.tpsc, WHITE, mousePos, 18)
            pygame.draw.circle(self.tpsc, TRANSPARENT, mousePos, 18-2)
            self.sc.blit(self.tpsc, (0, 0))
            # 连线
            pygame.draw.line(self.sc, WHITE, self.whiteBall.pos, mousePos, 2)
    
    def doubleclick(self):
        self.timing.append(time.time())
        if len(self.timing) >= 2 and self.timing[-1] - self.timing[-2] < 0.5:
            self.timing.clear()
            return True
        else:
            return False
        
    def placeWhiteBall(self,mousePos):
        whiteBall = Ball(mousePos,0)
        self.Balls.insert(0,whiteBall)
        self.whiteBall = whiteBall

    def inCourt(self,mode,mousePos):
        self.testBall = Ball(mousePos,0)
        
        side = self.testBall.collide_side(self.Sides)[0]
        other_ball = self.testBall.collide_ball(self.Balls)
        get = self.testBall.collide_hole(self.Holes)
        xoutrange = not bool(97.3835<self.testBall.pos.x<1269.9695)
        youtrange = not bool(91.9509<self.testBall.pos.y<676.1886)
        if mode == 1:# 瞄准环节用（不检测球体）
            # 如果边界、球洞任碰其一，并且在球台外边
            if side or get or xoutrange or youtrange:
                return False
            else:
                return True
        elif mode == 2:# 摆球环节用（检测球体）
            # 如果边界、球体、球洞任碰其一，并且在球台外边
            if side or other_ball or get or xoutrange or youtrange:
                return False
            else:
                return True
    
    def allocateStartPos(self,pos_list):
        OLD_POS = pos_list.copy()# 防止把源数据全删掉引发错误
        # 白球、黑八位置固定，右上右下不能同色
        posD, posU, pos8, pos0 = (OLD_POS.pop(15), 
                                  OLD_POS.pop(11), 
                                  OLD_POS.pop(5), 
                                  OLD_POS.pop(0))
        # 选取位于右上右下的球号
        indexD, indexU = random.sample([random.randint(1,7),random.randint(9,16)],2)
        NEW_POS = random.sample(OLD_POS,12)# 剩下的位置随机排列
        # 把拆出来的项组装回新列表
        NEW_POS.insert(0, pos0)
        NEW_POS.insert(indexD, posD)
        NEW_POS.insert(indexU, posU)
        NEW_POS.insert(8, pos8)
        return NEW_POS

    def weitiao(self,mousePos,mode):
        if self.whiteBall:
            delta = 0.002
            if mode == 1:# 顺时针转
                angle = math.atan2(mousePos[1]-self.whiteBall.pos[1],mousePos[0]-self.whiteBall.pos[0])
                angle += delta
                newPos = (self.whiteBall.pos[0] + 2 * math.cos(angle),
                          self.whiteBall.pos[1] + 2 * math.sin(angle))
                return newPos
            elif mode == 2:# 逆时针转
                angle = math.atan2(mousePos[1]-self.whiteBall.pos[1],mousePos[0]-self.whiteBall.pos[0])
                angle -= delta
                newPos = (self.whiteBall.pos[0] + 2 * math.cos(angle),
                          self.whiteBall.pos[1] + 2 * math.sin(angle))
                return newPos
        return None