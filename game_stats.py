class GameStats():
    '''跟踪游戏的统计信息'''
    def __init__(self,ai_settings):
        self.ai_settings=ai_settings
        self.reset_stats()
        #让游戏一开始处于非活动状态
        self.game_active=False
        #在任何情况下都不应该重置最高分
        self.high_score=0
    def reset_stats(self):
        '''初始化游戏运行期间可能变化的统计信息'''
        self.ships_left=self.ai_settings.ship_limit
        self.score=0#为了每次开始游戏时都重置积分，我们在reset_stats()方法中将score设置为0