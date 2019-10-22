import pygame
import random
pygame.init()

swidth = 500
sheight = 500
size = (swidth, sheight)

Background = pygame.image.load('Background.png')
Platform = pygame.image.load('Platform.png')
Shrine = pygame.image.load('Shrine.png')

tile = 64
backx = 0
backy = 0

first = 2

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Platform level generator")
platforms = []

def setupbackground():
    global backx
    global backy

    while backx <= swidth:
        screen.blit(Background, (backx, backy))
        pygame.display.update()
        backx = backx + tile
    if backy <= sheight:
        backy = backy + tile
        backx = 0
        setupbackground()
    else:
        pass


def setupplatform():
    global tile
    global swidth
    global sheight
    global backx
    global backy
    global first

    backx = 0
    while backx < swidth + 64:
        screen.blit(Platform, (backx, backy - tile))
        print(backx)
        backx = backx + tile

    randomplat()


def randomplat():
    global backx
    global backy
    global platforms

    backx = backx - 64
    backy = backy - 64

    platformx = random.randrange(0, backx, 64)
    platformy = random.randrange(0, backy, 64)
    screen.blit(Platform, (platformx, platformy))
    screen.blit(Platform, (platformx - 64, platformy))
    screen.blit(Platform, (platformx + 64, platformy))
    list = (platformx, platformy)
    platforms.append(list)


def randomshrine():
    global platforms

    choice = random.randint(0, 5, 1)
    if choice == 1:
        print(choice)
        screen.blit(Shrine, (platforms[1]))
    else:
        pass

##main loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    while first > 0:
        setupbackground()
        setupplatform()
        first = first - 1

pygame.quit()