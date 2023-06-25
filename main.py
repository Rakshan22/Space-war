import pygame
import random
import math
from pygame import mixer


pygame.init()
screen = pygame.display.set_mode((1000, 1500))



# title and game icon
pygame.display.set_caption('Space War')
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

# background music
mixer.music.load('backround.wav')
mixer.music.play(-1)

# tank
theplayer = pygame.image.load('spaceship.png')
playerX = 480
playerY = 784
playerX_change = 0
playerY_change = 0

# enemy planet
enemy_planet = pygame.image.load('enemy planet.png')
enemy_planetX = 450
enemy_planetY = 0

# enemy station
enemy_station = pygame.image.load('enemy station.png')
enemy_stationX = 260
enemy_stationY = 0

# enemy station 2
enemy_station2 = pygame.image.load('enemy station.png')
enemy_station2X = 70
enemy_station2Y = 0

# enemy station 3
enemy_station3 = pygame.image.load('enemy station.png')
enemy_station3X = 640
enemy_station3Y = 0

# enemy station 3
enemy_station4 = pygame.image.load('enemy station.png')
enemy_station4X = 830
enemy_station4Y = 0


# Alien 1
obstacle_image = pygame.image.load('alien invader.png')
obstacleX = random.randint(0, 800)
obstacleY = random.randint(128, 136)
obstacleX_change = 9


# Alien 2
obstacle2_image = pygame.image.load('alien invader.png')
obstacle2X = random.randint(0, 800)
obstacle2Y = random.randint(200, 250)
obstacle2X_change = 8


# bullet
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 0
bulletX_change = 0
bulletY_change = 15
bullet_state = "ready"


# landmine
landmine_image = pygame.image.load('landmine.png')
landmineX = random.randint(500, 550)
landmineY = random.randint(580, 680)

# landmine 2
landmine2_image = pygame.image.load('landmine.png')
landmine2X = random.randint(600, 650)
landmine2Y = random.randint(580, 680)

# landmine 3
landmine3_image = pygame.image.load('landmine.png')
landmine3X = random.randint(700, 750)
landmine3Y = random.randint(580, 680)

# landmine 4
landmine4_image = pygame.image.load('landmine.png')
landmine4X = random.randint(100, 150)
landmine4Y = random.randint(580, 680)

# landmine 5
landmine5_image = pygame.image.load('landmine.png')
landmine5X = random.randint(200, 250)
landmine5Y = random.randint(580, 680)

# landmine 6
landmine6_image = pygame.image.load('landmine.png')
landmine6X = random.randint(300, 350)
landmine6Y = random.randint(580, 680)

# landmine 7
landmine7_image = pygame.image.load('landmine.png')
landmine7X = random.randint(400, 450)
landmine7Y = random.randint(580, 680)

# landmine 8
landmine8_image = pygame.image.load('landmine.png')
landmine8X = random.randint(800, 850)
landmine8Y = random.randint(580, 680)

# landmine 9
landmine9_image = pygame.image.load('landmine.png')
landmine9X = random.randint(900, 950)
landmine9Y = random.randint(580, 680)

# landmine 10
landmine10_image = pygame.image.load('landmine.png')
landmine10X = random.randint(75, 100)
landmine10Y = random.randint(580, 680)

# landmine 12
landmine12_image = pygame.image.load('landmine.png')
landmine12X = random.randint(0, 50)
landmine12Y = random.randint(436, 536)

# landmine 13
landmine13_image = pygame.image.load('landmine.png')
landmine13X = random.randint(100, 150)
landmine13Y = random.randint(436, 536)

# landmine 14
landmine14_image = pygame.image.load('landmine.png')
landmine14X = random.randint(200, 250)
landmine14Y = random.randint(436, 536)

# landmine 15
landmine15_image = pygame.image.load('landmine.png')
landmine15X = random.randint(300, 350)
landmine15Y = random.randint(436, 536)

# landmine 16
landmine16_image = pygame.image.load('landmine.png')
landmine16X = random.randint(400, 450)
landmine16Y = random.randint(436, 536)

# landmine 17
landmine17_image = pygame.image.load('landmine.png')
landmine17X = random.randint(500, 550)
landmine17Y = random.randint(436, 536)

# landmine 18
landmine18_image = pygame.image.load('landmine.png')
landmine18X = random.randint(600, 650)
landmine18Y = random.randint(436, 536)

# landmine 19
landmine19_image = pygame.image.load('landmine.png')
landmine19X = random.randint(700, 750)
landmine19Y = random.randint(436, 536)

# landmine 20
landmine20_image = pygame.image.load('landmine.png')
landmine20X = random.randint(800, 850)
landmine20Y = random.randint(436, 536)

# landmine 21
landmine21_image = pygame.image.load('landmine.png')
landmine21X = random.randint(900, 950)
landmine21Y = random.randint(436, 536)

# score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 16)
textX = 10
textY = 0

# time
time_left = 2400
font2 = pygame.font.Font('freesansbold.ttf', 16)
timetextX = 10
timetextY = 20

# Game Over
over_font = pygame.font.Font('freesansbold.ttf', 64)





def player(x, y):
    screen.blit(theplayer, (x, y))

def enemyplanet(x, y):
    screen.blit(enemy_planet, (x, y))

def enemystation(x, y):
    screen.blit(enemy_station, (x, y))

def enemystation2(x, y):
    screen.blit(enemy_station2, (x, y))

def enemystation3(x, y):
    screen.blit(enemy_station3, (x, y))

def enemystation4(x, y):
    screen.blit(enemy_station4, (x, y))

def enemybase(x, y):
    screen.blit(obstacle_image, (x, y))

def enemybase2(x, y):
    screen.blit(obstacle2_image, (x, y))

def landmine(x, y):
    screen.blit(landmine_image, (x, y))

def landmine2(x, y):
    screen.blit(landmine2_image, (x, y))

def landmine3(x, y):
    screen.blit(landmine3_image, (x, y))

def landmine4(x, y):
    screen.blit(landmine4_image, (x, y))

def landmine5(x, y):
    screen.blit(landmine5_image, (x, y))

def landmine6(x, y):
    screen.blit(landmine6_image, (x, y))

def landmine7(x, y):
    screen.blit(landmine7_image, (x, y))

def landmine8(x, y):
    screen.blit(landmine8_image, (x, y))

def landmine9(x, y):
    screen.blit(landmine9_image, (x, y))

def landmine10(x, y):
    screen.blit(landmine10_image, (x, y))

def landmine12(x, y):
    screen.blit(landmine12_image, (x, y))

def landmine13(x, y):
    screen.blit(landmine13_image, (x, y))

def landmine14(x, y):
    screen.blit(landmine14_image, (x, y))

def landmine15(x, y):
    screen.blit(landmine15_image, (x, y))

def landmine16(x, y):
    screen.blit(landmine16_image, (x, y))

def landmine17(x, y):
    screen.blit(landmine17_image, (x, y))

def landmine18(x, y):
    screen.blit(landmine18_image, (x, y))

def landmine19(x, y):
    screen.blit(landmine19_image, (x, y))

def landmine20(x, y):
    screen.blit(landmine20_image, (x, y))

def landmine21(x, y):
    screen.blit(landmine21_image, (x, y))


def show_score(x, y):
    score = font.render('Score: ' + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def show_time(x, y):
    time = font.render('Time: ' + str(time_left), True, (255, 255, 255))
    screen.blit(time, (x, y))

def game_won_text():
    over_text = over_font.render("The Game is Won", True, (255, 0, 0))
    screen.blit(over_text, (200, 250))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 30, y + 5))


def isCollision(obstacleX, obstacleY, bulletX, bulletY):
    distance = math.sqrt((math.pow(obstacleX - bulletX, 2)) + (math.pow(obstacleY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False

def isCollision2(obstacle2X, obstacle2Y, bulletX, bulletY):
    distance23 = math.sqrt((math.pow(obstacle2X - bulletX, 2)) + (math.pow(obstacle2Y - bulletY, 2)))
    if distance23 < 27:
        return True
    else:
        return False


def isCollisionlandmine(playerX, playerY, landmineX, landmineY):
    distance2 = math.sqrt((math.pow(playerX - landmineX, 2)) + (math.pow(playerY - landmineY, 2)))
    if distance2 < 27:
        return True
    else:
        return False

def isCollisionlandmine2(playerX, playerY, landmine2X, landmine2Y):
    distance3 = math.sqrt((math.pow(playerX - landmine2X, 2)) + ((math.pow(playerY - landmine2Y, 2))))
    if distance3 < 27:
        return True
    else:
        return False

def isCollisionlandmine3(playerX, playerY, landmine3X, landmine3Y):
    distance4 = math.sqrt((math.pow(playerX - landmine3X, 2)) + ((math.pow(playerY - landmine3Y, 2))))
    if distance4 < 27:
        return True
    else:
        return False

def isCollisionlandmine4(playerX, playerY, landmine4X, landmine4Y):
    distance5 = math.sqrt((math.pow(playerX - landmine4X, 2)) + ((math.pow(playerY - landmine4Y, 2))))
    if distance5 < 27:
        return True
    else:
        return False

def isCollisionlandmine5(playerX, playerY, landmine5X, landmine5Y):
    distance6 = math.sqrt((math.pow(playerX - landmine5X, 2)) + ((math.pow(playerY - landmine5Y, 2))))
    if distance6 < 27:
        return True
    else:
        return False

def isCollisionlandmine6(playerX, playerY, landmine6X, landmine6Y):
    distance7 = math.sqrt((math.pow(playerX - landmine6X, 2)) + ((math.pow(playerY - landmine6Y, 2))))
    if distance7 < 27:
        return True
    else:
        return False

def isCollisionlandmine7(playerX, playerY, landmine7X, landmine7Y):
    distance8 = math.sqrt((math.pow(playerX - landmine7X, 2)) + ((math.pow(playerY - landmine7Y, 2))))
    if distance8 < 27:
        return True
    else:
        return False

def isCollisionlandmine8(playerX, playerY, landmine8X, landmine8Y):
    distance9 = math.sqrt((math.pow(playerX - landmine8X, 2)) + ((math.pow(playerY - landmine8Y, 2))))
    if distance9 < 27:
        return True
    else:
        return False

def isCollisionlandmine9(playerX, playerY, landmine9X, landmine9Y):
    distance10 = math.sqrt((math.pow(playerX - landmine9X, 2)) + ((math.pow(playerY - landmine9Y, 2))))
    if distance10 < 27:
        return True
    else:
        return False

def isCollisionlandmine10(playerX, playerY, landmine10X, landmine10Y):
    distance11 = math.sqrt((math.pow(playerX - landmine10X, 2)) + ((math.pow(playerY - landmine10Y, 2))))
    if distance11 < 27:
        return True
    else:
        return False


def isCollisionlandmine12(playerX, playerY, landmine12X, landmine12Y):
    distance13 = math.sqrt((math.pow(playerX - landmine12X, 2)) + ((math.pow(playerY - landmine12Y, 2))))
    if distance13 < 27:
        return True
    else:
        return False


def isCollisionlandmine13(playerX, playerY, landmine13X, landmine13Y):
    distance14 = math.sqrt((math.pow(playerX - landmine13X, 2)) + ((math.pow(playerY - landmine13Y, 2))))
    if distance14 < 27:
        return True
    else:
        return False


def isCollisionlandmine14(playerX, playerY, landmine14X, landmine14Y):
    distance15 = math.sqrt((math.pow(playerX - landmine14X, 2)) + ((math.pow(playerY - landmine14Y, 2))))
    if distance15 < 27:
        return True
    else:
        return False

def isCollisionlandmine15(playerX, playerY, landmine15X, landmine15Y):
    distance16 = math.sqrt((math.pow(playerX - landmine15X, 2)) + ((math.pow(playerY - landmine15Y, 2))))
    if distance16 < 27:
        return True
    else:
        return False


def isCollisionlandmine16(playerX, playerY, landmine16X, landmine16Y):
    distance17 = math.sqrt((math.pow(playerX - landmine16X, 2)) + ((math.pow(playerY - landmine16Y, 2))))
    if distance17 < 27:
        return True
    else:
        return False


def isCollisionlandmine17(playerX, playerY, landmine17X, landmine17Y):
    distance18 = math.sqrt((math.pow(playerX - landmine17X, 2)) + ((math.pow(playerY - landmine17Y, 2))))
    if distance18 < 27:
        return True
    else:
        return False

def isCollisionlandmine18(playerX, playerY, landmine18X, landmine18Y):
    distance19 = math.sqrt((math.pow(playerX - landmine18X, 2)) + ((math.pow(playerY - landmine18Y, 2))))
    if distance19 < 27:
        return True
    else:
        return False

def isCollisionlandmine19(playerX, playerY, landmine19X, landmine19Y):
    distance20 = math.sqrt((math.pow(playerX - landmine19X, 2)) + ((math.pow(playerY - landmine19Y, 2))))
    if distance20 < 27:
        return True
    else:
        return False


def isCollisionlandmine20(playerX, playerY, landmine20X, landmine20Y):
    distance21 = math.sqrt((math.pow(playerX - landmine20X, 2)) + ((math.pow(playerY - landmine20Y, 2))))
    if distance21 < 27:
        return True
    else:
        return False


def isCollisionlandmine21(playerX, playerY, landmine21X, landmine21Y):
    distance22 = math.sqrt((math.pow(playerX - landmine21X, 2)) + ((math.pow(playerY - landmine21Y, 2))))
    if distance22 < 27:
        return True
    else:
        return False

running = True
while running:
    screen.fill((0, 0, 225))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                playerY_change = -5
            if event.key == pygame.K_s:
                playerY_change = 5
            if event.key == pygame.K_a:
                playerX_change = -5
            if event.key == pygame.K_d:
                playerX_change = 5
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bullet_sound = mixer.Sound('Flash-laser.wav')
                    bullet_sound.play()
                    bulletX = playerX
                    bulletY = playerY
                    fire_bullet(bulletX, bulletY)
        if event.type == pygame.KEYUP:
            playerY_change = 0
            playerX_change = 0

    if score_value == 15:
        obstacleY = 3000
        obstacle2Y = 3100
    if playerY == 130 and score_value == 15:
        break


    time_left -= 1

    if time_left == 0:
        break


    obstacleX += obstacleX_change
    if obstacleX <= 0:
        obstacleX_change = 9
    elif obstacleX >= 936:
        obstacleX_change = -9

    obstacle2X += obstacle2X_change
    if obstacle2X <= 0:
        obstacle2X_change = 8
    elif obstacle2X >= 936:
        obstacle2X_change = -8

    if bulletY <= 0:
        bulletY = playerY
        bullet_state = "ready"
    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 936:
        playerX = 936

    playerY += playerY_change
    if playerY <= 0:
        playerY = 0
    elif playerY >= 720:
        playerY = 720

    collision = isCollision(obstacleX, obstacleY, bulletX, bulletY)
    if collision:
        explosion_sound = mixer.Sound('explosion.wav')
        explosion_sound.play()
        bulletY = playerY
        bullet_state = 'ready'
        obstacleX = random.randint(0, 800)
        obstacleY = random.randint(128, 136)
        score_value += 1

    collision2 = isCollisionlandmine(playerX, playerY, landmineX, landmineY)
    if collision2:
        break

    collision3 = isCollisionlandmine2(playerX, playerY, landmine2X, landmine2Y)
    if collision3:
        break

    collision4 = isCollisionlandmine3(playerX, playerY, landmine3X, landmine3Y)
    if collision4:
        break

    collision5 = isCollisionlandmine4(playerX, playerY, landmine4X, landmine4Y)
    if collision5:
        break

    collision6 = isCollisionlandmine5(playerX, playerY, landmine5X, landmine5Y)
    if collision6:
        break

    collision7 = isCollisionlandmine6(playerX, playerY, landmine6X, landmine6Y)
    if collision7:
        break

    collision8 = isCollisionlandmine7(playerX, playerY, landmine7X, landmine7Y)
    if collision8:
        break

    collision9 = isCollisionlandmine8(playerX, playerY, landmine8X, landmine8Y)
    if collision9:
        break

    collision10 = isCollisionlandmine9(playerX, playerY, landmine9X, landmine9Y)
    if collision10:
        break

    collision11 = isCollisionlandmine10(playerX, playerY, landmine10X, landmine10Y)
    if collision11:
        break

    collision13 = isCollisionlandmine12(playerX, playerY, landmine12X, landmine12Y)
    if collision13:
        break

    collision14 = isCollisionlandmine13(playerX, playerY, landmine13X, landmine13Y)
    if collision14:
        break

    collision15 = isCollisionlandmine14(playerX, playerY, landmine14X, landmine14Y)
    if collision15:
        break

    collision16 = isCollisionlandmine15(playerX, playerY, landmine15X, landmine15Y)
    if collision16:
        break

    collision17 = isCollisionlandmine16(playerX, playerY, landmine16X, landmine16Y)
    if collision17:
        break

    collision18 = isCollisionlandmine17(playerX, playerY, landmine17X, landmine17Y)
    if collision18:
        break

    collision19 = isCollisionlandmine18(playerX, playerY, landmine18X, landmine18Y)
    if collision19:
        break

    collision20 = isCollisionlandmine19(playerX, playerY, landmine19X, landmine19Y)
    if collision20:
        break

    collision21 = isCollisionlandmine20(playerX, playerY, landmine20X, landmine20Y)
    if collision21:
        break

    collision22 = isCollisionlandmine21(playerX, playerY, landmine21X, landmine21Y)
    if collision22:
        break

    collision23 = isCollision2(obstacle2X, obstacle2Y, bulletX, bulletY)
    if collision23:
        explosion_sound = mixer.Sound('explosion.wav')
        explosion_sound.play()
        bulletY = playerY
        bullet_state = 'ready'
        obstacle2X = random.randint(0, 800)
        obstacle2y = random.randint(200, 250)
        score_value += 1


    player(playerX, playerY)
    enemyplanet(enemy_planetX, enemy_planetY)
    enemystation(enemy_stationX, enemy_stationY)
    enemystation2(enemy_station2X, enemy_station2Y)
    enemystation3(enemy_station3X, enemy_station3Y)
    enemystation4(enemy_station4X, enemy_station4Y)
    show_score(textX, textY)
    show_time(timetextX, timetextY)
    enemybase(obstacleX, obstacleY)
    enemybase2(obstacle2X, obstacle2Y)
    landmine(landmineX, landmineY)
    landmine2(landmine2X, landmine2Y)
    landmine3(landmine3X, landmine3Y)
    landmine4(landmine4X, landmine4Y)
    landmine5(landmine5X, landmine5Y)
    landmine6(landmine6X, landmine6Y)
    landmine7(landmine7X, landmine7Y)
    landmine8(landmine8X, landmine8Y)
    landmine9(landmine9X, landmine9Y)
    landmine10(landmine10X, landmine10Y)
    landmine12(landmine12X, landmine12Y)
    landmine13(landmine13X, landmine13Y)
    landmine14(landmine14X, landmine14Y)
    landmine15(landmine15X, landmine15Y)
    landmine16(landmine16X, landmine16Y)
    landmine17(landmine17X, landmine17Y)
    landmine18(landmine18X, landmine18Y)
    landmine19(landmine19X, landmine19Y)
    landmine20(landmine20X, landmine20Y)
    landmine21(landmine21X, landmine21Y)
    pygame.display.update()

