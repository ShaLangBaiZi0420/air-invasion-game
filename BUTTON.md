```PY
import pygame.font

class Button():
    def __init__(self, ai_settings, screen, msg):
        '''初始化按钮的属性'''

        # 直接获取屏幕的rect对象
        self.screen = screen
        self.screen_rect = screen.get_rect()  
        # 设置按钮尺寸和其他属性
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        # 创建按钮rect对象并使其居中
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        # 按钮的标签只创建一次,并使其居中
        self.msg_image, self.msg_image_rect = self.prep_msg(msg)  # 直接返回渲染后的图像和rect对象

    def prep_msg(self, msg):
        '''将msg渲染为图像,并使其在按钮上居中'''
        msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        msg_image_rect = msg_image.get_rect()
        msg_image_rect.center = self.rect.center
        return msg_image, msg_image_rect

    def draw_button(self):
        '''在屏幕上绘制按钮'''
        self.screen.fill(self.button_color, self.rect)  # 填充按钮颜色
        self.screen.blit(self.msg_image, self.msg_image_rect)  # 绘制按钮文本

```

