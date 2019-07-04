import pygame

WHITE = (255, 255, 255)

class Bullet(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        
        self.speed = 10

        self.image = pygame.image.load("b.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
            
        
    def moveUp(self):
        self.rect.centery -= self.speed
    

        
