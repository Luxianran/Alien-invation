import pygame
import sys
from settings import Settings
from ship import Ship
import game_function as gf
from pygame.sprite import Group


def run_game():
    pygame.init()
    ai_settings = Settings()
    sn = pygame.display.set_mode(
        (ai_settings.sn_wid, ai_settings.sn_hei))
    ship = Ship(sn, ai_settings)
    bullets = Group()


    while True:
        gf.check_events(ai_settings, sn, ship, bullets)
        
        bullets.update()

        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)

        gf.update_sn(ai_settings, sn, ship, bullets)


run_game()