import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("pygames/spaceInvaders/assets/ovni.png")
pygame.display.set_icon(icon)

#Enemy
enemyImg = pygame.image.load("pygames/spaceInvaders/assets/alien.png")
enemyX = 370
enemyY = 480
enemyX_Changed = 0

#Player
playerImg = pygame.image.load("pygames/spaceInvaders/assets/astronave.png")
playerX = 370
playerY = 480
playerX_Changed = 0

def player(x, y):
    screen.blit(playerImg, (x, y))

def enemy(x, y):
    screen.blit(enemyImg, (x, x))


#Game loop
running = True
while running:
    #RGB = limpieza de screen
    screen.fill((15,15,15))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            playerX_Changed = -0.1
        if event.key == pygame.K_RIGHT:
            playerX_Changed = 0.1

    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT :
            playerX_Changed = 0

    playerX += playerX_Changed
    if (playerX <= 0):
        playerX = 0
    if (playerX > 736):
        playerX = 736


    enemy(playerX+64, playerY-64)
    player(playerX, playerY)
    pygame.display.update()
