import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    def __init__(self, ai_settings, sn, ship):
        super(Bullet, self).__init__()
    
        self.sn = sn

        self.image = pygame.image.load('images/lanqiu.png').convert_alpha()
        width,height = self.image.get_size()
        self.image = pygame.transform.smoothscale(self.image, (width//6, height//6))

        self.rect = self.image.get_rect()

        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        self.y = float(self.rect.y)

        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        self.y -= self.speed_factor

        self.rect.y = self.y

    def draw_bullet(self):
        self.sn.blit(self.image, self.rect)