# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 11:53:32 2024

@author: Administrator
"""
import pygame
from const import screen_size
from data_dic import data

class Ball(pygame.sprite.Sprite):
    def __init__(self, pos, ID):
        super().__init__()
        self.id = ID
        self.radius = 18
        self.pos = pygame.Vector2(pos)  
        self.color = self.getData()['COLOR']
        self.speed = pygame.Vector2(0, 0)  
        self.controlable = self.getData()['CTRL']
        self.createSurface(pos)
    
    def createSurface(self, pos):
        self.image = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, self.color, (int(self.radius), int(self.radius)), int(self.radius))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(center=pos)
    
    def move(self,group):
        if self.speed:
            dt = pygame.time.Clock().tick(60) / 1000.0  # 计算时间步长（以秒为单位）
            num_steps = 10  # 将每帧时间分解为10个小步长
            step_size = dt / num_steps  # 每个小步长的时间
            # print(dt,num_steps,step_size)
        
            # for _ in range(num_steps):
                # 计算每个小步长的速度
                # print('第{}次循环'.format(_))
            self.pos += self.speed #* step_size
            # self.rect.center = (self.pos.x,self.pos.y)
            
            self.fric()
            self.collide_side()
            self.collide_ball(group)

            if self.speed.length() <= 0.2:
                self.speed = pygame.Vector2(0, 0)
    
    def collide_ball(self, group):
        for sprite in group:
            if sprite != self and pygame.sprite.collide_circle(self, sprite):
                print('-----\n',
                      self.id,'撞到了：',sprite.id,
                      '\n跟ta的rect距离是：',pygame.Vector2(self.rect.center).distance_to(pygame.Vector2(sprite.rect.center)),
                      '\n跟ta的pos距离是：',self.pos.distance_to(sprite.pos),
                      '\n-----\n'
                      )
                # 防止球体重叠，调整位置
                normal = sprite.pos - self.pos
                distance = normal.length()
                overlap = self.radius + sprite.radius - distance
                if overlap > 0:
                    correction = normal * (overlap / 2)
                    self.pos -= correction
                    sprite.pos += correction

                self.speed_exchange2(sprite)
                        
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
        restitution = 1  # 弹性系数，为1表示完全弹性碰撞
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
        # print('211')
        pygame.draw.circle(screen, self.color, (self.pos.x,self.pos.y), int(self.radius))

    
