import pygame

class Enemy(pygame.sprite.Sprite):
    x = 0
    y = 0
    alive = True
    width = 50

    def __init__(self):
        super().__init__()

        self.speed = 20

        self.image = pygame.image.load("evil1.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (int(self.width*1), int(self.width*1)))
        self.rect = self.image.get_rect()

        
