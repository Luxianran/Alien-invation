import pygame


class Ship():
    def __init__(self, sn, ai_settings) -> None:
        self.sn = sn

        self.image = pygame.image.load('images/kunkun.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.sn_rect = sn.get_rect()

        self.rect.centerx = self.sn_rect.centerx
        self.rect.bottom = self.sn_rect.bottom

        self.center = float(self.rect.centerx)

        self.ai_settings = ai_settings

        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        self.sn.blit(self.image, self.rect)
    
    def update(self):
        if self.moving_left and self.rect.left > self.sn_rect.left:
            self.center -= self.ai_settings.ship_speed_factor

        if self.moving_right and self.rect.right < self.sn_rect.right:
            self.center += self.ai_settings.ship_speed_factor

        self.rect.centerx = self.center