import pygame
import math

# 初始化Pygame
pygame.init()

# 设定屏幕尺寸
screen_width = 1366
screen_height = 768
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("台球开局摆球")

# 颜色定义
WHITE = (255, 255, 255)
GREEN = (0, 128, 0)
RED = (255, 0, 0)

# 台球半径
radius = 18

# 首球位置
first_ball_x = 977.4488
first_ball_y = 385.6364

# 球与球之间的间距，可以修改
spacing = 1

# 球的间距实际计算
distance = 2 * radius + spacing

# 设置模式：0为正常模式，1为整数精度模式，2为两位小数模式
integer_mode = 2

# 计算球的坐标
def generate_ball_positions(first_x, first_y, distance, integer_mode):
    positions = [(first_x, first_y)]
    rows = 5  # 一共需要摆5行球
    for row in range(1, rows):
        for col in range(row + 1):
            x = first_x + row * distance * math.cos(math.radians(30))
            y = first_y + 2*(col - row / 2) * distance * math.sin(math.radians(30))
            if integer_mode == 1:
                x = int(round(x))
                y = int(round(y))
            if integer_mode == 2:
                x = round(x,2)
                y = round(y,2)
            positions.append((x, y))
    return positions

# 生成球的坐标
ball_positions = generate_ball_positions(first_ball_x, first_ball_y, distance, integer_mode)
for each in ball_positions:
    print(each,',',sep='')

# 绘制函数
def draw_balls(screen, positions, radius):
    for pos in positions:
        pygame.draw.circle(screen, RED, (int(pos[0]), int(pos[1])), int(radius))

# 主循环
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill(GREEN)  # 填充背景
    draw_balls(screen, ball_positions, radius)  # 绘制球
    pygame.display.flip()  # 更新屏幕

pygame.quit()
