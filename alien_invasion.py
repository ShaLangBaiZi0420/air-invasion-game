import pygame
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
 
# 运行游戏的函数
def run_game():
    
        pygame.init()
        ai_settings = Settings()
        screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
        pygame.display.set_caption('Alien Invasion')
 
        # 创建play按钮
        play_button = Button(ai_settings, screen, "Play")
 
        # 创建游戏统计信息实例和记分牌
        stats = GameStats(ai_settings)
        sb = Scoreboard(ai_settings, screen, stats)
 
        # 创建飞船、子弹和外星人编组
        ship = Ship(screen, ai_settings)
        bullets = Group()
        aliens = Group()
 
        # 创建外星人群
        gf.create_fleet(ai_settings, screen, ship, aliens)
 
        # 初始化音效
        pygame.mixer.init()
        pygame.mixer.music.load(r'music/game_music.mp3')
        pygame.mixer.music.play(-1)
 
        alien_hurt_sounds = [
            pygame.mixer.Sound(r'music/alien_hurt.wav'),
            pygame.mixer.Sound(r'music/alien_hurt2.wav'),
            pygame.mixer.Sound(r'music/alien_hurt3.wav')
        ]
        game_over_sound = pygame.mixer.Sound(r'music/game_over.wav')
 
        # 读取最高分
        gf.load_high_score(stats)
        sb.prep_high_score()
 
        while True:
            gf.check_events(ai_settings, screen, ship, bullets, stats, play_button, aliens)
            if stats.game_active:
                ship.update()
                gf.update_bullets(aliens, bullets, ai_settings, screen, ship, stats, sb, *alien_hurt_sounds)
                gf.update_aliens(ai_settings, aliens, ship, stats, screen, bullets, game_over_sound)
            gf.update_screen(ai_settings, screen, ship, stats, bullets, aliens, play_button, sb)
 
            if not stats.game_active and stats.high_score < stats.score:
                stats.high_score = stats.score
                gf.save_high_score(stats)
 
  
    
 
run_game()