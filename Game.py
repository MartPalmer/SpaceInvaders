import pygame
import Enemy
import Player
import Bullet

pygame.init()

window_width = 800
window_height = 600
fps = 30
clock = pygame.time.Clock()

bg_x = 0
bg_y = 0

gameDisplay = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Space Invaders")

bg = pygame.image.load('bg.jpg')

all_sprites_list = pygame.sprite.Group()

#Set up game elements
p = Player.Player()
p.rect.centerx = window_width/2
p.rect.centery = window_height - 100
all_sprites_list.add(p)

bullets = []

enemies = []

def setUpAliens():
    global enemies
    start = 675
    y = 25

    for h in range(0,4):
        line = []    
        for i in range(0,9):
            a1 = Enemy.Enemy()
            a1.rect.x = start
            a1.rect.y = y
            line.append(a1)
            all_sprites_list.add(line[i])
            start -= 75
        y += 75
        start = 675
        enemies.append(line)

def gameLoop():
    gameExit = False
    counter = 0
    bullets_cooldown = 15

    setUpAliens()

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

        #controls
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a and p.rect.centerx > p.ship_width/2:
                p.moveLeft()
            elif event.key == pygame.K_d and p.rect.centerx < window_width - (p.ship_width/2):
                p.moveRight()

            if event.key == pygame.K_g and bullets_cooldown >= 15:
                bullets.append(Bullet.Bullet())
                bullets[-1].rect.centerx = p.rect.centerx
                bullets[-1].rect.centery = p.rect.centery

                all_sprites_list.add(bullets[-1])
                bullets_cooldown = 0

        
        

        #Game Logic
        b_counter = 0
        while len(bullets) > 0 and b_counter < len(bullets):
           
            if bullets[b_counter].rect.centery > 50:
                bullets[b_counter].moveUp()
            else:
                bullets[b_counter].kill()
                bullets.remove(bullets[b_counter])
                b_counter -= 1

            b_counter += 1



        #Draw stuff
        gameDisplay.blit(bg, (bg_x, bg_y))
        all_sprites_list.draw(gameDisplay)
        
        pygame.display.update()



        clock.tick(fps)
        counter += 1
        if len(bullets) > 0:
            bullets_cooldown += 1

        

    

gameLoop()
