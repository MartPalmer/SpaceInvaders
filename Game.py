import pygame
import Enemy
import Player
import Bullet
import Constants

c = Constants.Constants()

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
p = Player.Player(window_width/2, window_height - 100)
all_sprites_list.add(p)

bullets = []
enemies = []
enemyMoveCounter = 0


def setUpAliens():
    global enemies
    x = 750
    y = 25

    for e_counter in range(1,41):
        enemies.append(Enemy.Enemy(x, y))
        all_sprites_list.add(enemies[-1])
        
        x-=60
        if e_counter % 10 == 0:
            x = 750
            y += 60

            

def gameLoop():
    global enemies
    global enemyMoveCounter
    gameExit = False
    counter = 0
    direction = "left"
    changeDirection = False
    moveDown = False
    bullets_cooldown = 15

    setUpAliens()

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
                

        #controls
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a and p.rect.left > 0:
                p.moveLeft()
            elif event.key == pygame.K_d and p.rect.right < window_width:
                p.moveRight()

            if event.key == pygame.K_SPACE and bullets_cooldown >= 15:
                bullets.append(Bullet.Bullet(p.rect.centerx, p.rect.centery))
                all_sprites_list.add(bullets[-1])
                bullets_cooldown = 0

            

        #Game Logic
        b_counter = 0

        if counter%(fps/2) == 0:
            enemyMoveCounter += 1
            if enemyMoveCounter <= 8:
                direction = "Left"
            if enemyMoveCounter == 9:
                direction = "Down"
            if enemyMoveCounter >= 10 and enemyMoveCounter <= 17:
                direction = "Right"
            if enemyMoveCounter == 18:
                direction = "Down"
                enemyMoveCounter = 0
            
            for e_counter in range(0, len(enemies)):
                    enemies[e_counter].move(direction)
            
        
        while len(bullets) > 0 and b_counter < len(bullets):
           
            if bullets[b_counter].rect.centery > 50:
                bullets[b_counter].moveUp()
            else:
                bullets[b_counter].kill()
                bullets.remove(bullets[b_counter])
                b_counter -= 1

            b_counter += 1

        counter += 1
        
        bullets_cooldown += 1
            

        #Draw stuff
        gameDisplay.blit(bg, (bg_x, bg_y))
        all_sprites_list.draw(gameDisplay)
        
        pygame.display.update()

        clock.tick(fps)
    
    

gameLoop()
