import pygame

class Ship:

    def __init__(self, ai_game):
        # Initializing the ship and setting its starting position
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Loading the ship image and getting its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Starting every new ship at the bottom of the screen.
        self.rect.midbottom = self.screen_rect.midbottom


    def blitme(self):
        self.screen.blit(self.image, self.rect)





