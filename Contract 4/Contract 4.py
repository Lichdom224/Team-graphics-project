import pygame

pygame.init()

display_width = 569
display_height = 688

import random
rn = random.randint(0,5)

please = ['black', 'white', 'red', 'green', 'blue']
randomcolor = please[rn]
print (randomcolor)

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)


gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Contract 4')
clock = pygame.time.Clock()

image = pygame.image.load('sonic.jpg').convert_alpha()

gameDisplay.blit(image, (0, 0))
print (image)


running = True

while running == True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.Surface = image
    pygame.PixelArray = image

    if event.type == pygame.MOUSEBUTTONDOWN:
        (X, Y) = pygame.mouse.get_pos()
        color = pygame.Surface.get_at_mapped((X, Y))
        pygame.PixelArray.replace(color, randomcolor, 0, (0.299, 0.587, 0.114))

    pygame.display.update()
    clock.tick(60)


pygame.quit()
quit()