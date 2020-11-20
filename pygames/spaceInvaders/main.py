import pygame

class Unity():
    image = None
    x = 0
    y = 0
    changed = 0
    type = ""

    def draw(self):
        screen.blit(self.image, (self.x, self.y))

class Enemy(Unity):
    def __init__(self, x=0, y=0):
        self.type = "Enemigo"
        self.image = pygame.image.load("pygames/spaceInvaders/assets/alien.png")
        self.x = x
        self.y = y

    def draw(self, x, y):
        screen.blit(self.image, (x, y))


class Player(Unity):
    def __init__(self, x=0, y=0):
        self.type = "Jugador"
        self.image = pygame.image.load("pygames/spaceInvaders/assets/astronave.png")
        self.x = x
        self.y = y


pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("pygames/spaceInvaders/assets/ovni.png")
pygame.display.set_icon(icon)

firstPlayer = Player(370, 480)
firstEnemy  = Enemy(370, 480)


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
            firstPlayer.changed = -0.1
        if event.key == pygame.K_RIGHT:
            firstPlayer.changed = 0.1

    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT :
            firstPlayer.changed = 0

    firstPlayer.x += firstPlayer.changed

    if (firstPlayer.x <= 0):
        firstPlayer.x = 0
    if (firstPlayer.x > 736):
        firstPlayer.x = 736

    firstEnemy.draw((firstPlayer.x + 64), (firstPlayer.x - 64))
    firstPlayer.draw()
    pygame.display.update()
