import pygame
import sys
from bullet import Bullet

def update_sn(ai_settings, sn, ship, bullets):
    sn.fill(ai_settings.bg_color)

    ship.update()

    for bullet in bullets:
        bullet.draw_bullet()

    ship.blitme()

    pygame.display.flip()

def key_down(event, ai_settings, sn, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    
    if event.key == pygame.K_LEFT:
        ship.moving_left = True

    if event.key == pygame.K_SPACE and len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, sn, ship)
        bullets.add(new_bullet)

def key_up(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False

    if event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ai_settings, sn, ship, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN: 
            key_down(event, ai_settings, sn, ship, bullets)

        if event.type == pygame.KEYUP:
            key_up(event, ship)