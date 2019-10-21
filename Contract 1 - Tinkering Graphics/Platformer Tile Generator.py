#generate textures
#various different types of tile
#soil- dry, wet
#foliage- spring, autumn, summer, winter

import pygame, sys
from pygame.locals import *

pygame.init()

WINDOWWIDTH = 700
WINDOWHEIGHT = 600

DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))
pygame.display.set_caption('Tile Generator')

WHITE = (255,255,255)

def main():
    global DISPLAYSURF, soil_dict, foliage_dict, xcoord, ycoord

    xcoord = 150
    ycoord = 150
    
    DISPLAYSURF.fill(WHITE)

    soil_dict = {'dry':pygame.image.load('dry_soil.jpg').convert(),
                 'wet':pygame.image.load('wet_soil.jpg').convert()}

    foliage_dict = {'spring':pygame.image.load('spring_texture.jpg').convert(),
                    'autumn':pygame.image.load('autumn_texture.jpg').convert(),
                    'summer':pygame.image.load('summer_texture.jpg').convert(),
                    'winter':pygame.image.load('snow_texture.jpg').convert()}

    soil_arae = [soil_dict['dry'],soil_dict['wet']]

    foliage_arae = [foliage_dict['spring'],foliage_dict['autumn'],foliage_dict['summer'],
                    foliage_dict['winter']]

    soil_length = len(soil_arae)
    foliage_length = len(foliage_arae)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            pygame.display.update()
            
        for i in range(soil_length):
            soil_scale = pygame.transform.scale(soil_arae[i], (xcoord,ycoord))
            soil_rect = soil_arae[i].get_rect()
            DISPLAYSURF.blit(soil_scale, soil_rect)
            i += 1
            
       
            

        for k in range(foliage_length):
            xcoord = 150
            ycoord = 150
            foliage_scale = pygame.transform.scale(foliage_arae[k], (xcoord,ycoord))
            foliage_rect = foliage_arae[i].get_rect()
            DISPLAYSURF.blit(foliage_scale, foliage_rect)
            k += 1
            xcoord += 150
           

        
        

        pygame.display.flip()


if __name__ == '__main__':
    main()
