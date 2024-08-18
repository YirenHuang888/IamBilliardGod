# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 11:53:32 2024

@author: Administrator
"""
import pygame
from const import screen_size,BLACK,WHITE
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
        if self.speed:
            num_steps = 200  # 将每帧时间分解为100个小步长
        
            for _ in range(num_steps):# 将1帧的运动再细分100份
                delta_x = self.speed / num_steps
                self.pos += delta_x
                
                #边界碰撞
                side = self.collide_side(side_group)
                if side:
                    self.speed_exchange3(side)
                    self.fric(0.95)
                #球体间碰撞
                other_ball = self.collide_ball(ball_group)
                if other_ball:
                    self.speed_exchange2(other_ball)
                    self.fric(0.95)
                #进洞判定
                get = self.collide_hole(hole_group)
                if get:
                    return self
                
                    
            self.fric(0.99)
            if self.speed.length() <= 0.2:
                self.speed = pygame.Vector2(0, 0)
    
    def collide_ball(self, group):
        for other_ball in group:
            if other_ball != self and self.pos.distance_to(other_ball.pos) <= self.radius * 2 :
                # print('-----\n',
                #       self.id,'撞到了：',other_ball.id,
                #       '\n跟ta的距离是：',self.pos.distance_to(other_ball.pos),
                #       '\n-----\n'
                #       )
                return other_ball
                        
    def speed_exchange2(self, other):
        # 计算法线向量
        normal = other.pos - self.pos
        distance = normal.length()
        if distance == 0:
            return  # 防止除零错误和重合情况
        normal = normal.normalize()
    
        # 计算相对速度
        relative_velocity = self.speed - other.speed
    
        # 计算速度沿法线方向的分量
        velocity_along_normal = relative_velocity.dot(normal)
    
        # 如果速度分量小于0，说明球体在分离，不处理
        if velocity_along_normal < 0:
            return
        # 碰撞后速度的计算 (弹性碰撞)
        restitution = 1 # 弹性系数，为1表示完全弹性碰撞
        impulse_magnitude = -(1 + restitution) * velocity_along_normal / 2
        impulse_vector = normal * impulse_magnitude
    
        # 更新球体的速度
        self.speed += impulse_vector
        if isinstance(self,type(other)):#如果被撞对象是球体
            other.speed -= impulse_vector
    

    # 摩擦力
    def fric(self,f):
        if self.speed.length() > 0.2:  
            self.speed *= f  
     
    # 边界检测
    def collide_side(self,group):
        for side in group:
            if side.IFcollide:
                if side.distance2ball(self) <= self.radius + side.radius:
                    return side
            
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
        pygame.draw.circle(screen, self.color, (self.pos.x,self.pos.y), int(self.radius))
        if not self.controlable:
            ball_id = pygame.font.Font(None, 18)
            textImage = ball_id.render(str(self.id), True, BLACK)
            screen.blit(textImage, (self.pos.x-4,self.pos.y-1))
            textImage = ball_id.render(str(self.id), True, WHITE)
            screen.blit(textImage, (self.pos.x-4,self.pos.y-4))



    
