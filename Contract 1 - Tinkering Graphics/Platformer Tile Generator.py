
import pygame, sys
from pygame.locals import *

pygame.init()

WINDOWWIDTH = 300
WINDOWHEIGHT = 600

DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))
pygame.display.set_caption('Tile Generator')

WHITE = (255,255,255)

#the main function where the images are displayed on screen
def main():
    global DISPLAYSURF, soil_dict, foliage_dict, xcoord, ycoord

    #coordinates for the for loops 
    xcoord = 0
    ycoord = 0

    #making the screen white
    DISPLAYSURF.fill(WHITE)

    #loading the images(tiles) into dictionaries
    soil_dict = {'dry':pygame.image.load('dry_soil.jpg').convert(),
                 'wet':pygame.image.load('wet_soil.jpg').convert()}

    foliage_dict = {'spring':pygame.image.load('spring_texture.jpg').convert(),
                    'autumn':pygame.image.load('autumn_texture.jpg').convert(),
                    'summer':pygame.image.load('summer_texture.jpg').convert(),
                    'winter':pygame.image.load('snow_texture.jpg').convert()}

    #calling the loaded images from dictionary into an arae
    soil_arae = [soil_dict['dry'],soil_dict['wet']]

    foliage_arae = [foliage_dict['spring'],foliage_dict['autumn'],foliage_dict['summer'],
                    foliage_dict['winter']]

    #length for the for loops 
    soil_length = len(soil_arae)
    foliage_length = len(foliage_arae)

    #main loop
    while True:
        #for quiting
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            pygame.display.update()

        #displaying the soil images
        for i in range(soil_length):
            soil_scale = pygame.transform.scale(soil_arae[i], (150,150))
            DISPLAYSURF.blit(soil_scale,(xcoord,ycoord))
            i += 1
            ycoord += 150

        #setting cooardinates for the next loop
        xcoord = 150
        ycoord = 0 

        #displaying the foliage images
        for k in range(foliage_length):
            foliage_scale = pygame.transform.scale(foliage_arae[k], (150,150))
            DISPLAYSURF.blit(foliage_scale, (xcoord,ycoord))
            k += 1
            ycoord += 150

        pygame.display.flip()
        #breaking the while loop
        pass


#making sure the main function runs
if __name__ == '__main__':
    main()
