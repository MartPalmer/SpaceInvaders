import pygame

class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.ship_width = 128
        self.speed = 20

        self.image = pygame.image.load("goodFighter.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (int(self.ship_width/2), int(self.ship_width/2)))
        self.rect = self.image.get_rect()
            
        
        


    def moveRight(self):
        self.rect.centerx += self.speed

    def moveLeft(self):
        self.rect.centerx -= self.speed
    

        
