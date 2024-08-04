# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 19:39:50 2024

@author: Administrator
"""
import pygame

class Ball(pygame.sprite.Sprite):
    def __init__(self, pos, ID):
        super().__init__()
        self.id = ID
        self.radius = 10.5
        self.pos = pygame.Vector2(pos)
        self.speed = pygame.Vector2(0, 0)
        self.createSurface(pos)
    
    def createSurface(self, pos):
        self.image = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (255, 0, 0), (int(self.radius), int(self.radius)), int(self.radius))
        self.rect = self.image.get_rect(center=pos)
    
    def move(self, group, dt):
        num_steps = 10
        step_size = dt / num_steps

        for _ in range(num_steps):
            self.pos += self.speed * step_size
            self.rect.center = (int(self.pos.x), int(self.pos.y))

            collision = self.check_collision(group)
            if collision:
                self.handle_collision(collision)

            self.fric()
            self.collide_side()
    
    def check_collision(self, group):
        for sprite in group:
            if sprite != self and pygame.sprite.collide_circle(self, sprite):
                if isinstance(sprite, Ball):
                    return sprite
        return None
    
    def handle_collision(self, other):
        if isinstance(other, Ball):
            normal = self.pos - other.pos
            distance = normal.length()
            combined_radius = self.radius + other.radius

            if distance < combined_radius:
                overlap = combined_radius - distance
                normal.normalize_ip()
                self.pos += normal * (overlap / 2)
                other.pos -= normal * (overlap / 2)

                self.speed_exchange(other)

    def speed_exchange(self, other):
        normal = pygame.Vector2(other.pos.x - self.pos.x, other.pos.y - self.pos.y)
        if normal.length() == 0:
            return
        normal.normalize()

        relative_velocity = self.speed - other.speed
        velocity_along_normal = relative_velocity.dot(normal)

        if velocity_along_normal > 0:
            return

        self.speed -= normal * velocity_along_normal
        other.speed += normal * velocity_along_normal

    def fric(self):
        if self.speed.length() > 0.2:
            self.speed *= 1

    def collide_side(self):
        # 边界检测
        if self.rect.left < 0 or self.rect.right > screen_size[0]:
            self.speed.x = -self.speed.x * 0.95
        if self.rect.top < 0 or self.rect.bottom > screen_size[1]:
            self.speed.y = -self.speed.y * 0.95

# 初始化 Pygame
pygame.init()
screen_size = (800, 600)
screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()

# 创建球体
ball1 = Ball((100, 100), 1)
ball2 = Ball((150, 150), 2)

# 创建精灵组
all_sprites = pygame.sprite.Group()
all_sprites.add(ball1)
all_sprites.add(ball2)

# 游戏主循环
running = True
while running:
    dt = clock.tick(60) / 1000.0  # 计算时间步长（以秒为单位）

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Keyboard controls for ball1
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                ball1.speed.x = -10
            elif event.key == pygame.K_RIGHT:
                ball1.speed.x = 10
            elif event.key == pygame.K_UP:
                ball1.speed.y = -10
            elif event.key == pygame.K_DOWN:
                ball1.speed.y = 10
        
        # Stop movement on key release
        # if event.type == pygame.KEYUP:
        #     if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
        #         ball1.speed.x = 0
        #     if event.key in [pygame.K_UP, pygame.K_DOWN]:
        #         ball1.speed.y = 0


    # 更新游戏状态
    for ball in all_sprites:
        ball.move(all_sprites, dt)

    # 绘制
    screen.fill((0, 0, 0))
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()


