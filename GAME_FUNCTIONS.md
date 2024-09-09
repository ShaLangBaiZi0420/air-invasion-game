```PY
import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep
import random

def check_keydown_events(event, ship, ai_settings, screen, bullets):
    '''响应按键'''
    key_actions = {
        pygame.K_RIGHT: lambda: setattr(ship, 'moving_right', True),
        pygame.K_LEFT: lambda: setattr(ship, 'moving_left', True),
        pygame.K_UP: lambda: setattr(ship, 'moving_up', True),
        pygame.K_DOWN: lambda: setattr(ship, 'moving_down', True),
        pygame.K_w: lambda: fire_bullets(ship, ai_settings, screen, bullets, 'up'),
        pygame.K_a: lambda: fire_bullets(ship, ai_settings, screen, bullets, 'left'),
        pygame.K_s: lambda: fire_bullets(ship, ai_settings, screen, bullets, 'down'),
        pygame.K_d: lambda: fire_bullets(ship, ai_settings, screen, bullets, 'right'),
        pygame.K_p: lambda: sys.exit(),
        pygame.K_q: lambda: sys.exit()
    }
    
    action = key_actions.get(event.key)
    if action:
        action()

def check_keyup_events(event, ship):
    '''响应松开'''
    key_actions = {
        pygame.K_RIGHT: lambda: setattr(ship, 'moving_right', False),
        pygame.K_LEFT: lambda: setattr(ship, 'moving_left', False),
        pygame.K_UP: lambda: setattr(ship, 'moving_up', False),
        pygame.K_DOWN: lambda: setattr(ship, 'moving_down', False)
    }
    action = key_actions.get(event.key)
    if action:
        action()

def check_events(ai_settings, screen, ship, bullets, stats, play_button, aliens):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship, ai_settings, screen, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, aliens, bullets, ship, stats, play_button, mouse_x, mouse_y)

def check_play_button(ai_settings, screen, aliens, bullets, ship, stats, play_button, mouse_x, mouse_y):
    '''在玩家单击Play按钮时开始游戏'''
    if play_button.rect.collidepoint(mouse_x, mouse_y) and not stats.game_active:
        ai_settings.initialize_dynamic_settings()
        pygame.mouse.set_visible(False)
        stats.reset_stats()
        stats.game_active = True
        aliens.empty()
        bullets.empty()
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

def update_screen(ai_settings, screen, ship, stats, bullets, aliens, play_button, sb):
    screen.fill(ai_settings.bg_color)
    sb.show_score()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    if not stats.game_active:
        play_button.draw_button()
    pygame.display.flip()

def fire_bullets(ship, ai_settings, screen, bullets, direction):
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship, direction)
        bullets.add(new_bullet)

def update_bullets(aliens, bullets, ai_settings, screen, ship, stats, sb, alien_hurt_sound1, alien_hurt_sound2, alien_hurt_sound3):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0 or bullet.rect.top >= ai_settings.screen_height or bullet.rect.right <= 0 or bullet.rect.left >= ai_settings.screen_width:
            bullets.remove(bullet)
    check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets, stats, sb, alien_hurt_sound1, alien_hurt_sound2, alien_hurt_sound3)

def check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets, stats, sb, alien_hurt_sound1, alien_hurt_sound2, alien_hurt_sound3):
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if not aliens:
        ai_settings.increase_speed()
        create_fleet(ai_settings, screen, ship, aliens)
    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points * len(aliens)
            sb.prep_score()
            random.choice([alien_hurt_sound1, alien_hurt_sound2, alien_hurt_sound3]).play()
        check_high_score(stats, sb)

def get_number_rows(ai_settings, ship_height, alien_height):
    available_space_y = ai_settings.screen_height - ship_height - 3 * alien_height
    return int(available_space_y / (2 * alien_height))

def get_number_aliens_x(ai_settings, alien_width):
    available_space_x = ai_settings.screen_width - 2 * alien_width
    return int(available_space_x / (3 * alien_width))

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    alien = Alien(ai_settings, screen)
    alien.x = alien.rect.width + 2 * alien.rect.width * alien_number
    alien.rect.x = alien.x
    alien.y = alien.rect.height + 2 * alien.rect.height * row_number
    alien.rect.y = alien.y
    aliens.add(alien)

def create_fleet(ai_settings, screen, ship, aliens):
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)
    remove_random_aliens(aliens)

def remove_random_aliens(aliens):
    num_to_remove = random.randint(5, len(aliens))
    aliens_to_remove = random.sample(aliens.sprites(), num_to_remove)
    for alien in aliens_to_remove:
        aliens.remove(alien)

def update_aliens(ai_settings, aliens, ship, stats, screen, bullets, game_over_sound):
    check_fleet_edges(ai_settings, aliens)
    check_fleet_edges_y(ai_settings, aliens)
    aliens.update()
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets, game_over_sound)

def change_fleet_direction(ai_settings, aliens):
    ai_settings.fleet_direction *= -1

def change_fleet_direction_y(ai_settings, aliens):
    ai_settings.fleet_direction_y *= -1

def check_fleet_edges(ai_settings, aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break

def check_fleet_edges_y(ai_settings, aliens):
    for alien in aliens.sprites():
        if alien.check_edges_y():
            change_fleet_direction_y(ai_settings, aliens)
            break

def ship_hit(ai_settings, stats, screen, ship, aliens, bullets, game_over_sound):
    if stats.ships_left > 0:
        stats.ships_left -= 1
        aliens.empty()
        bullets.empty()
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()
        sleep(0.5)
        game_over_sound.play()
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

def check_high_score(stats, sb):
    """检查是否有新的最高分"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()

def save_high_score(stats):
    with open('high_score.txt', 'w') as file:
        file.write(str(stats.high_score))

def load_high_score(stats):
    try:
        with open('high_score.txt', 'r') as file:
            stats.high_score = int(file.read())
    except FileNotFoundError:
        stats.high_score = 0
```

