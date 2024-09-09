import pygame
from pygame.sprite import Sprite
 
class Alien(Sprite):
    """表示单个外星人的类"""
    def __init__(self, ai_settings, screen):
        """初始化外星人并设置其起始位置"""
        super().__init__()
         
        # 存储screen和setting以便后续使用
        self.ai_settings = ai_settings
        self.screen = screen
         
        try:
            self.image = pygame.image.load(r'images\alien.bmp')
        except pygame.error as e:
            print(f"无法加载图像: {e}")
            raise
 
        # 加载外星人图像，并设置其rect属性
        self.rect = self.image.get_rect()
         
        # 每个外星人最初都在屏幕左上角附近
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
         
        # 存储外星人的准确位置
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
         
    def blitme(self):
        """在指定位置绘制外星人"""
        self.screen.blit(self.image, self.rect)
         
    def check_edges(self):
        """检查外星人是否到达屏幕左右边缘"""
        screen_rect = self.screen.get_rect()
        return self.rect.right >= screen_rect.right or self.rect.left <= screen_rect.left
     
    def check_edges_y(self):
        """检查外星人是否到达屏幕上下边缘"""
        screen_rect = self.screen.get_rect()
        return self.rect.bottom >= screen_rect.bottom or self.rect.top <= screen_rect.top
     
    def update(self):
        """更新外星人的位置"""
        
        '''向右移动外星人'''
        self.x += self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction
        self.rect.x = int(self.x)
         
        '''向下移动外星人'''
        self.y += self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction_y
        self.rect.y = int(self.y)