import pygame.font

class Button():
    def __init__(self,ai_settings,screen,msg):
        '''初始化按钮的属性'''
        self.screen=screen
        self.screen_rect=self.screen.get_rect()
        #设置按钮尺寸和其他属性
        self.width,self.height=200,50
        self.button_color=(0,255,0)
        self.text_color=(255,255,255)
        self.font=pygame.font.SysFont(None,48)
        #创建按钮rect对象并使其剧中
        self.rect=pygame.Rect(0,0,self.width,self.height)
        self.rect.center=self.screen_rect.center
        #按钮的标签只创建一次
        self.prep_msg(msg)#pygame要将字符串渲染为图像
        
    def prep_msg(self,msg):
        '''将msg渲染为图像,并使其在按钮上居中'''
        self.msg_image=self.font.render(msg,True,self.text_color,self.button_color)
        self.msg_image_rect=self.msg_image.get_rect()
        self.msg_image_rect.center=self.rect.center#这个self.rect是谁--忘了这是在类里面了。。。
    def draw_button(self):
        self.screen.fill(self.button_color,self.rect)#surface->color
        self.screen.blit(self.msg_image,self.msg_image_rect)#surface->surface
        
        