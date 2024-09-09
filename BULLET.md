bullet.py

```py
import pygame
from pygame.sprite import Sprite
# 不要把sprite里的group想象成任何一种数据结构或者形状。它只是一种“容器”。

class Bullet(Sprite):
    
    def __init__(self, ai_settings, screen, ship, direction):
        """在飞船所处的位置创建一个子弹对象"""
        
        super().__init__()  # 初始化父类
        self.screen = screen  # 记录屏幕对象
        self.direction = direction  # 子弹的运动方向

        # 在(0,0)处创建一个表示子弹的矩形
        # 不负责设置位置
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)

        # 移动到正确位置 - 使用ship的rect来定位
        self.rect.centerx = ship.rect.centerx  # 子弹水平居中在飞船顶部
        self.rect.centery = ship.rect.top  # 子弹顶部与飞船顶部对齐
         
        # 存储用小数表示的子弹位置，以便精确控制子弹的速度
        self.x = float(self.rect.x) 
        self.y = float(self.rect.y) 

        # 记录子弹的颜色和速度
        self.color = ai_settings.bullet_color 
        self.speed_factor = ai_settings.bullet_speed_factor
        
    def update(self):
        # 根据方向更新子弹的位置
        if self.direction == 'up':  # 如果方向是向上
            self.y -= self.speed_factor  # 子弹向上移动
        elif self.direction == 'down':  # 如果方向是向下
            self.y += self.speed_factor  # 子弹向下移动
        elif self.direction == 'left':  # 如果方向是向左
            self.x -= self.speed_factor  # 子弹向左移动
        elif self.direction == 'right':  # 如果方向是向右
            self.x += self.speed_factor  # 子弹向右移动
        
        # 更新子弹rect的位置，以匹配y和x的新位置
        self.rect.y = self.y
        self.rect.x = self.x

    def draw_bullet(self):
        # 在屏幕上绘制子弹
        pygame.draw.rect(self.screen, self.color, self.rect)
    

```

