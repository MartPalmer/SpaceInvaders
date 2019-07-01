import pygame

class Player(pygame.sprite.Sprite):
    ship_width = 0
    ship_height = 0
    speed = 0
    
    def __init__(self, x, y):
        super().__init__()
        self.ship_width = 128
        self.speed = 20

        self.image = pygame.image.load("goodFighter.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (int(self.ship_width/2), int(self.ship_width/2)))
        ship_height = self.image.get_height()
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y


    def moveRight(self):
        self.rect.centerx += self.speed

    def moveLeft(self):
        self.rect.centerx -= self.speed

    def boost(self, speed_multiplier):
        self.speed = self.speed * speed_multiplier

    
    

        
