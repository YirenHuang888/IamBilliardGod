# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 11:53:32 2024

@author: Administrator
"""
import pygame
from const import BLACK,WHITE
from data_dic import ball_data

class Ball():
    def __init__(self, pos, ID):
        self.id = ID
        self.radius = 18
        self.pos = pygame.Vector2(pos)  
        self.color = self.getBallData('COLOR')
        self.speed = pygame.Vector2(0, 0)  
        self.controlable = self.getBallData('CTRL')
    
    def move(self,ball_group,side_group,hole_group):
        num_steps = 40  # 将每帧时间分解为40个小步长
        for _ in range(num_steps):# 将1帧的运动再细分40份
            delta_x = self.speed / num_steps
            self.pos += delta_x
            
            #边界碰撞
            side,overlap = self.collide_side(side_group)
            if side:
                self.speed_exchange3(side)
                self.getawayfromSide(overlap,side)# 防重叠
                self.fric(0.95)
                return side, 'side'
            #球体间碰撞
            other_ball,overlap = self.collide_ball(ball_group)
            if other_ball:
                self.speed_exchange2(other_ball)
                self.getawayfromBall(overlap,other_ball)# 防重叠
                self.fric(0.95)
                return other_ball, 'ball'
            #进洞判定,进洞则返回要被删除的球
            get = self.collide_hole(hole_group)
            if get:
                return self, 'self'
        return None, None
                
    def collide_ball(self, group):
        for other_ball in group:
            if other_ball.id != self.id and self.pos.distance_to(other_ball.pos) <= self.radius * 2 :
                overlap = self.radius * 2 - self.pos.distance_to(other_ball.pos)
                return other_ball,overlap
        return None,0
    
    def getawayfromBall(self,overlap,other_ball):
            normal = self.pos - other_ball.pos
            normal = normal.normalize()
            self.pos += overlap * normal
    
    def getawayfromSide(self,overlap,side):
        if side.IFarc:
            normal = self.pos - side.pos
            normal = normal.normalize()
            self.pos += overlap * normal
        else:
            if side.toward == 'shu':
                normal = pygame.Vector2(self.pos.x - side.xory,0)
                normal = normal.normalize()
                self.pos += overlap * normal
            elif side.toward == 'heng':
                normal = pygame.Vector2(0,self.pos.y - side.xory)
                normal = normal.normalize()
                self.pos += overlap * normal

    def speed_exchange2(self, other):
        # 计算法线向量
        normal = other.pos - self.pos
        distance = normal.length()
        if distance == 0:
            return  # 防止除零错误和重合情况
        normal = normal.normalize()
    
        relative_velocity = self.speed - other.speed# 计算相对速度
        velocity_along_normal = relative_velocity.dot(normal)# 速度沿法线方向的分量
        if velocity_along_normal < 0:# 如果速度分量小于0，说明球体在分离，不处理
            return
        
        # 碰撞后速度的计算 (弹性碰撞)
        impulse_magnitude = -velocity_along_normal
    
        # 更新球体的速度
        self.speed += normal * impulse_magnitude
        if isinstance(self,type(other)):#如果被撞对象是球体
            other.speed -= normal * impulse_magnitude

    def fric(self,f):
        if self.speed.length() > 0.2:  
            self.speed *= f  
     
    def collide_side(self,group):
        for side in group:
            if side.IFcollide:
                distance = side.distance2ball(self)
                if distance <= self.radius + side.radius:
                    overlap = self.radius + side.radius - distance
                    return side,overlap
        return None,0
            
    def speed_exchange3(self,side):
        if side.IFarc:
            self.speed_exchange2(side)
        else:
            if side.toward == 'shu':# 竖着的
                self.speed.x = -self.speed.x
            elif side.toward == 'heng':# 横着的
                self.speed.y = -self.speed.y
    
    def collide_hole(self, group):
        for hole in group:
            if self.pos.distance_to(hole.pos) <= hole.radius :
                return True

    def getBallData(self,key):
        return ball_data[self.id][key]

    def draw(self, screen):
        # 绘制球体
        pygame.draw.circle(screen, self.color, (self.pos.x,self.pos.y), int(self.radius))
        # 绘制序号
        if not self.controlable:
            ball_id = pygame.font.Font(None, 25)
            textImage = ball_id.render(str(self.id), True, BLACK)
            screen.blit(textImage, (self.pos.x-8,self.pos.y-4))
            textImage = ball_id.render(str(self.id), True, WHITE)
            screen.blit(textImage, (self.pos.x-8,self.pos.y-8))
    
    def simulateShoot(self,ball_group,side_group,hole_group):
        num_steps = 80  # 将每帧时间分解为40个小步长
        for _ in range(num_steps):# 将1帧的运动再细分40份
            delta_x = self.speed / num_steps
            self.pos += delta_x
            
            #边界碰撞
            side,overlap = self.collide_side(side_group)
            if side:
                self.getawayfromSide(overlap,side)# 防重叠
                self.speed = pygame.Vector2(0, 0)
                return side, 'side'
            #球体间碰撞
            other_ball,overlap = self.collide_ball(ball_group)
            if other_ball:
                self.getawayfromBall(overlap,other_ball)# 防重叠
                self.speed = pygame.Vector2(0, 0)
                return other_ball, 'ball'
            #进洞判定,进洞则返回要被删除的球
            get = self.collide_hole(hole_group)
            if get:
                self.speed = pygame.Vector2(0, 0)
                return self, 'self'
        return None, None



    
