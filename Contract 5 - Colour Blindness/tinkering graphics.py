'__Author__: JB229064'
'__Year__: 2019'


import pygame  # importing pygame library to get pygame functions
pygame.init()  # initialise pygame
pygame.display.set_caption("Tinkering Graphics")  # setting a caption

window = pygame.display.set_mode((500, 500))  # setting window resolution
img = pygame.image.load("carrot.jpg")  # loading an image

def draw():  # defining draw function
    window.blit(img, (0, 0))  # loading image onto the screen
    pixels = PixelArray(img)  # getting the array of pixels (not working)
    pixels.replace(Color(255,255,255,255), Color(0,0,0,0))  # replacing red with black (not working)
    pygame.display.update()  # updating frames in pygame


# function attempting to use PIL
'''def no_red():  # defining function for removing red
    for col in range(img.get_width()):  # iterating through the pixels of the width
        for row in range(img.get_height()):  # iterating through the pixels of the height
            p = img.getPixel(col,row)  # getting the induvidual pixel
            new_red = 0  # new value of red pixels
            new_green = p.get_green()  # new value of the green pixels
            new_blue = p.get_blue()  # new value of the blue pixels
            new_pixel = img.Pixel(newred,newgreen,newblue)  # setting the value of the new pixel
            new_img.setPixel(col,row,new_pixel)  # adding the new pixel to the image
'''


# main loop
run = True  # bool variable for game state
while run:  # looping while run true
    for event in pygame.event.get():  # looping through pygame events
        if event.type == pygame.QUIT:  # checking if the event is QUIT
            run = False  # changing the bool to false to stop the main loop
    draw()  # calling the draw function
    
