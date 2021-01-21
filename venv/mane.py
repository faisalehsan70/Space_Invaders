import pygame
import random

#initializing pygame
pygame.init()

#setting up the screen
screen = pygame.display.set_mode((800, 600))

#changing the window name
pygame.display.set_caption("Space Invaders")

#changin window icon
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

#setting player image
playerImg = pygame.image.load('spaceship.png')
playerX = 370
playerY = 480
playerX_change = 0
#defining player function
def player(x,y):
    screen.blit(playerImg, (playerX, playerY))

#setting enemy image
enemyImg = pygame.image.load('alien.png')
enemyX = random.randint(0, 800)
enemyY = random.randint(0, 100)
enemyX_change = 0.3
enemyY_change = 40
#defining enemy function
def enemy(x,y):
    screen.blit(enemyImg, (enemyX, enemyY))

#setting background image
backgroundImg = pygame.image.load('blackhole.jpg')
def background(x,y):
    screen.blit(backgroundImg, (0, 0))

#setting bullet image
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 20
bullet_state = 'ready'

#defining player function
def bullet_fire(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x+16, y+10))

#setting game loop
running = True
while running:
    # setting screen color
    screen.fill((0, 255, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.3
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.3
            if event.key == pygame.K_SPACE:
                bullet_fire(playerX, bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    playerX += playerX_change
    enemyX += enemyX_change
    if playerX <= 0:
        playerX = 736
    elif playerX >= 736:
        playerX = 0
    if enemyX <= 0:
        enemyX_change = 0.3
        enemyY += enemyY_change
    elif enemyX >= 736:
        enemyX_change = -0.3
        enemyY += enemyY_change

    if bullet_state == 'fire':
        bullet_fire (playerX, bulletY)
        bulletY -= bulletY_change

    #showing player image
    background(0,0)
    player(playerX,playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()

