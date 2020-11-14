import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("pygames/spaceInvaders/assets/ovni.png")

#player
playerImg = pygame.image.load("pygames/spaceInvaders/assets/astronave.png")
playerX = 370
playerY = 480
def player():
    screen.blit(playerImg, (playerX, playerY))

pygame.display.set_icon(icon)

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
            playerX-=0.1
        if event.key == pygame.K_RIGHT:
            playerX+=0.1
        if event.key == pygame.K_UP:
            playerY-=0.1
        if event.key == pygame.K_DOWN:
            playerY+=0.1

    player()
    pygame.display.update()
