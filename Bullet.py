import pygame

WHITE = (255, 255, 255)

class Bullet(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        
        self.speed = 10

        self.image = pygame.image.load("b.png").convert()
        self.image.set_colorkey(WHITE)
        self.bullet_width = self.image.get_width()
        #self.image = pygame.transform.scale(self.image, (int(self.ship_width/2), int(self.ship_width/2)))
        self.rect = self.image.get_rect()
            
        
    def moveUp(self):
        self.rect.centery -= self.speed
    

        
