# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 11:53:32 2024

@author: Administrator
"""
import pygame
from const import screen_size,BLACK,WHITE
from data_dic import data

class Ball():
    def __init__(self, pos, ID):
        self.id = ID
        self.radius = 18
        self.pos = pygame.Vector2(pos)  
        self.color = self.getData()['COLOR']
        self.speed = pygame.Vector2(0, 0)  
        self.controlable = self.getData()['CTRL']
    
    def move(self,group):
        if self.speed:
            # print('我是',self.id,'号')
            num_steps = 30  # 将每帧时间分解为20个小步长
        
            for _ in range(num_steps):
                # print('----\n这是第{}遍循环'.format(_))
                delta_x = self.speed / num_steps
                # print('这个循环，我{}走出去了{}像素\n----'.format(self.id, delta_x.length()))
                self.pos += delta_x
                
                self.collide_side()
                other_ball = self.collide_ball(group)
                if other_ball:
                    self.speed_exchange2(other_ball)
                    return True
            # print('这一帧，我{}总共走出去了{}像素'.format(self.id, self.speed.length()))
            self.fric()
            if self.speed.length() <= 0.2:
                self.speed = pygame.Vector2(0, 0)
    
    def collide_ball(self, group):
        for other_ball in group:
            if other_ball != self and self.pos.distance_to(other_ball.pos) < self.radius * 2 :
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
        impulse_magnitude = -(1 + restitution) * velocity_along_normal
        impulse_magnitude /= (1 / self.radius + 1 / other.radius)
    
        impulse_vector = normal * impulse_magnitude
    
        # 更新球体的速度
        self.speed += impulse_vector / self.radius
        other.speed -= impulse_vector / other.radius
    

    # 摩擦力
    def fric(self):
        if self.speed.length() > 0.2:  
            self.speed *= 0.99  
     
    def collide_side(self):
        # 边界检测
        if self.pos.x - self.radius < 0 or self.pos.x + self.radius > screen_size[0]:
            self.speed.x = -self.speed.x * 0.95
        if self.pos.y - self.radius < 0 or self.pos.y + self.radius > screen_size[1]:
            self.speed.y = -self.speed.y * 0.95
    
    def getData(self):
        return data[self.id]

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.pos.x,self.pos.y), int(self.radius))
        # print('211')
        if not self.controlable:
            ball_id = pygame.font.Font(None, 18)
            textImage = ball_id.render(str(self.id), True, BLACK)
            screen.blit(textImage, (self.pos.x-4,self.pos.y-1))
            textImage = ball_id.render(str(self.id), True, WHITE)
            screen.blit(textImage, (self.pos.x-4,self.pos.y-4))



    
