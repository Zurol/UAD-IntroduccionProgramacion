import pygame

class Unity():
    image = None
    x = 0
    y = 0
    changedX = 0
    changedY = 0
    type = ""

    def draw(self):
        screen.blit(self.image, (self.x, self.y))

class Enemy(Unity):
    def __init__(self, x=0, y=0):
        self.type = "Enemigo"
        self.image = pygame.image.load("pygames/spaceInvaders/assets/alien.png")
        self.x = x
        self.y = y


    # def draw(self, x, y):
    #    screen.blit(self.image, (x, y))


class EnemyLine(Enemy):
    line = []
    def __init__(self, unitsNumber=0, lineIndex=0):
        for enemyUnit in range(unitsNumber):
            self.line.append(Enemy( ((enemyUnit*66)), (lineIndex*66)))

        print(self.line)

    def drawLine(self):
        for enemyUnit in range(len(self.line)):
            self.line[enemyUnit].draw()

    def move(self, changedX, changedY):
        for enemyUnit in range(len(self.line)):
            self.line[enemyUnit].x = self.line[enemyUnit].x + changedX
            self.line[enemyUnit].y = self.line[enemyUnit].y + changedY

class Army(EnemyLine):
    army = []
    armyStatus = 0
    x = 0
    y = 0
    unitsNumber = 0
    linesNumber  = 0
    changedX = 0
    changedY = 0
    armyWidth = 0
    armyHeight = 0


    def __init__(self, unitsNumber=0, linesNumber=0):
        self.unitsNumber = unitsNumber
        self.linesNumber = linesNumber
        self.armyWidth = unitsNumber * 70 - 6
        self.armyHeight = linesNumber * 70

        for line in range(linesNumber):
            self.army.append(EnemyLine(unitsNumber, line))

    def drawArmy(self):
        for line in range(len(self.army)):
            self.army[line].drawLine()

    def move(self):
        if (self.armyStatus == 0):
            if ( (self.x + self.armyWidth) <= 800 ):
                self.changedX = 0.1
                self.changedY = 0
            else :
                self.armyStatus = 1
                self.changedX = 0
                self.changedY = 5

        elif (self.armyStatus == 1):
            if ( (self.x) >= 0 ):
                self.changedX = -0.1
                self.changedY = 0
            else :
                self.armyStatus = 0
                self.changedX = 0
                self.changedY = 5

        self.x += self.changedX
        self.y += self.changedY
        for fila in range(self.linesNumber):
            self.army[fila].move(self.changedX, self.changedY)

        #self.x = self.x + self.changedX



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

filas = 2
unidades = 11

#enemigos = EnemyLine(unidades, 0)
enemigos = Army(unidades, filas)

print(enemigos)

#print (enemigos)



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
            firstPlayer.changedX = -0.1
        if event.key == pygame.K_RIGHT:
            firstPlayer.changedX = 0.1
        if event.key == pygame.K_UP:
            firstPlayer.changedY = -0.1
        if event.key == pygame.K_DOWN:
            firstPlayer.changedY = 0.1

    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT :
            firstPlayer.changedX = 0
        if event.key == pygame.K_UP or event.key == pygame.K_DOWN :
            firstPlayer.changedY = 0

    firstPlayer.x += firstPlayer.changedX
    firstPlayer.y += firstPlayer.changedY

    if (firstPlayer.x <= 0):
        firstPlayer.x = 0
    if (firstPlayer.x > 736):
        firstPlayer.x = 736


    if (firstPlayer.y <= 0):
        firstPlayer.y = 0
    if (firstPlayer.y > 536):
        firstPlayer.y = 536



    #firstEnemy.draw((firstPlayer.x + 64), (firstPlayer.x - 64))

    #for fila in range(len(enemigos)):
    #    for unidad in range(len(enemigos[fila])):
    #        enemigos[fila][unidad].draw()



    firstPlayer.draw()
    enemigos.drawArmy()
    enemigos.move()
    pygame.display.update()
