```PY
class Settings:
    '''游戏设置类，包含所有游戏相关的设置'''
    def __init__(self):
        '''初始化游戏的静态与动态设置'''
        # 屏幕设置
        self.screen_width = 1600
        self.screen_height = 900
        self.bg_color = (240, 240, 240)

        # 飞船设置
        self.ship_limit = 3

        # 子弹设置
        self.bullet_width = 15
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 5

        # 外星人设置
        self.fleet_drop_speed = 25

        # 速度与得分更新设置
        self.speedup_scale = 1.1
        self.score_scale = 1.5

        # 初始化动态设置
        self.initialize_dynamic_settings()
    
    def initialize_dynamic_settings(self):
        '''初始化游戏的动态设置'''
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 0.25
        self.fleet_direction = 1
        self.fleet_direction_y = 1
        self.alien_points = 50

    def increase_speed(self):
        '''增加游戏速度和外星人点数，每次调用此方法增量增加'''
        try:
            self.ship_speed_factor *= self.speedup_scale
            self.bullet_speed_factor *= self.speedup_scale
            self.alien_speed_factor *= self.speedup_scale
            self.alien_points = int(self.alien_points * self.score_scale)
        except Exception as e:
            print(f"Error in increasing speed: {e}")

```

