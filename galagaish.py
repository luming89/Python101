import pygame
import math

pygame.init()
playerImg = pygame.image.load('ship.png')
enemy1Img = pygame.image.load('enemy_1.png')
enemy2Img = pygame.image.load('enemy_2.png')
bulletImg = pygame.image.load('bullet.png')
WIDTH = 1280
HEIGHT = 800
playerX = WIDTH / 2 - 50
playerY = HEIGHT / 2 + 150
screen = pygame.display.set_mode((WIDTH, HEIGHT))

running = True
bulletXOffset = 49
bulletYOffset = -20

# lists that hold bullet coordinates
bulletsX = []
bulletsY = []

# lists that hold enemy coordinates
enemiesX = []
enemiesY = []

# frame counter
counter = 0

# key status map
keysDown = {
    pygame.K_LEFT: False,
    pygame.K_RIGHT: False,
    pygame.K_UP: False,
    pygame.K_DOWN: False
}

# generate enemies
for i in range(6):
    enemiesX.append(200 + i * 150)
    enemiesY.append(100)

def calculateDistance(x1, y1, x2, y2):
    return math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2))

while running:  # game loop
    counter += 1
    screen.fill((0, 0, 0))
    if keysDown[pygame.K_LEFT]:
        playerX -= 1;
    if keysDown[pygame.K_RIGHT]:
        playerX += 1;
    if keysDown[pygame.K_UP]:
        playerY -= 1;
    if keysDown[pygame.K_DOWN]:
        playerY += 1;
    lengthOfBullet = len(bulletsX)
    lengthOfEnemies = len(enemiesX)
    newEnemiesX = []
    newEnemiesY = []
    newBulletsX = []
    newBulletsY = []
    bulletCollision = []
    enemyCollision = []
    for i in range(lengthOfBullet):
        bulletCollision.append(False)

    for i in range(lengthOfEnemies):
        enemyCollision.append(False)

    # remove any bullet or enemy if applicable
    for i in range(lengthOfEnemies):
        for j in range(lengthOfBullet):
            if calculateDistance(enemiesX[i]+40,enemiesY[i]+40,bulletsX[j],bulletsY[j]) < 45:
                enemyCollision[i] = True
                bulletCollision[j] = True
            if bulletsY[j] <= 0:
                bulletCollision[j] = True

    for i in range(lengthOfBullet):
        if not bulletCollision[i]:
            newBulletsX.append(bulletsX[i])
            newBulletsY.append(bulletsY[i])
    for i in range(lengthOfEnemies):
        if not enemyCollision[i]:
            newEnemiesX.append(enemiesX[i])
            newEnemiesY.append(enemiesY[i])

    bulletsX = newBulletsX
    bulletsY = newBulletsY
    enemiesX = newEnemiesX
    enemiesY = newEnemiesY
    lengthOfBullet = len(bulletsX)
    lengthOfEnemies = len(enemiesX)

    # draw bullets
    for i in range(lengthOfBullet):
        screen.blit(bulletImg, (bulletsX[i], bulletsY[i]))
        bulletsY[i] -= 1

    # draw enemies
    lengthOfEnemies = len(enemiesX)
    for i in range(lengthOfEnemies):
        if counter % 800 < 400:
            screen.blit(enemy1Img, (enemiesX[i], enemiesY[i]))
            if counter % 100 == 0:
                enemiesX[i] += 10
        else:
            screen.blit(enemy2Img, (enemiesX[i], enemiesY[i]))
            if counter % 100 == 0:
                enemiesX[i] -= 10

    # draw our spaceship
    screen.blit(playerImg, (playerX, playerY))

    # update display
    pygame.display.update()

    # handle keyboard input
    print("Running in game loop")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                keysDown[pygame.K_LEFT] = True
            if event.key == pygame.K_RIGHT:
                keysDown[pygame.K_RIGHT] = True
            if event.key == pygame.K_UP:
                keysDown[pygame.K_UP] = True
            if event.key == pygame.K_DOWN:
                keysDown[pygame.K_DOWN] = True
            if event.key == pygame.K_SPACE:
                bulletsX.append(playerX + bulletXOffset)
                bulletsY.append(playerY + bulletYOffset)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                keysDown[pygame.K_LEFT] = False
            if event.key == pygame.K_RIGHT:
                keysDown[pygame.K_RIGHT] = False
            if event.key == pygame.K_UP:
                keysDown[pygame.K_UP] = False
            if event.key == pygame.K_DOWN:
                keysDown[pygame.K_DOWN] = False
print("Completed game loop!")
