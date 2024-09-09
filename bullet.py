import pygame
from pygame.sprite import Sprite
class Bullet(Sprite):
    """一个对飞船发射的子弹进行管理的类"""
    def __init__(self,ai_settings,screen,ship,direction):
        """在飞船所处的位置创建一个子弹对象"""
        #继承的例行公事
        super().__init__()
        self.screen = screen
        self.direction = direction
        # 在(0,0)处创建一个表示子弹的矩形，再设置正确的位置
        self.rect = pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)
        #移动到正确位置-使用rect
        self.rect.centerx = ship.rect.centerx
        self.rect.centery = ship.rect.top
         
        #存储用小数表示的子弹位置
        self.x = float(self.rect.x) 
        self.y = float(self.rect.y) 

        #颜色和速度
        self.color = ai_settings.bullet_color 
        self.speed_factor = ai_settings.bullet_speed_factor
        
    def update(self):
        if self.direction == 'up': 
            self.y -= self.speed_factor
        elif self.direction == 'down':
            self.y += self.speed_factor
        elif self.direction == 'left':
            self.x -= self.speed_factor
        elif self.direction == 'right':
            self.x += self.speed_factor
        
        #更新子弹位置
        self.rect.y=self.y
        self.rect.x=self.x

    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)
    
        

        