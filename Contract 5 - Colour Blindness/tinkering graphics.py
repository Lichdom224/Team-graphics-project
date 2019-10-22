'__Author__ JB229064'


import pygame  # importing pygame to use pygame libraries
pygame.init()  # initialise pygame
pygame.display.set_caption("Tinkering Graphics")  # setting a caption
window = pygame.display.set_mode((717, 177))  # setting window resolution
img = pygame.image.load("blind_scale.jpg")  # loading an image

def draw():  # defining draw function
    window.blit(img, (0, 0))  # loading image onto the screen
    #pixels = PixelArray(img)  # getting the array of pixels (not working)
    #pixels.replace(Color(255,255,255,255), Color(0,0,0,0))  # replacing red with black (not working)
    pygame.display.update()  # updating frames in pygame


def select_option():  # defining a function to allow user to select an option
    choice = input("[a] = remove red\n[b] = remove green\n[c] = remove blue\nInput Choice: ")  # allowing user to enter choice
    if choice == "a":  # for if the selection is "a"
        remove_red(img)  # calling the remove red function
    if choice == "g":  # for if the selection is "g"
        remove_green(img)  # calling the remove green function
    if choice == "b":  # for if the selection is "b"
        remove_blue(img)  # calling the remove blue function


def remove_red(image):  # defining the fucntion for removing red
    pixel = pygame.Color(0, 0, 0)  # sets a local variable for white
    for x in range(image.get_width()):  # iterating through the width of the image
        for y in range(image.get_height()):  # iterating through the height of the image
            pixel = image.get_at((x, y))  # getting the pixel colour value at each position
            image.set_at((x, y), pygame.Color(pixel.b, pixel.g, 0))  # setting the pixel colour value at each position


def remove_green(image):  # defining the function for removing green
    pixel = pygame.Color(0, 0, 0)  # sets a local variable for white
    for x in range(image.get_width()):  # iterating through the width of the image
        for y in range(image.get_height()):  # iterating through the height of the image
            pixel = image.get_at((x, y))  # getting the pixel colour value at each position
            image.set_at((x, y), pygame.Color(pixel.b, 0, pixel.r))  # setting the pixel colour value at each position          


def remove_blue(image):  # defining the function for removing blue
    pixel = pygame.Color(0, 0, 0)  # sets a local variable for white
    for x in range(image.get_width()):  # iterating through the width of the image
        for y in range(image.get_height()):  # iterating through the height of the image
            pixel = image.get_at((x, y))  # getting the pixel colour value at each position
            image.set_at((x, y), pygame.Color(0, pixel.g, pixel.r))  # setting the pixel colour value at each position         


# main loop
run = True  # bool variable for game state
while run:  # looping while run true
    for event in pygame.event.get():  # looping through pygame events
        if event.type == pygame.QUIT:  # checking if the event is QUIT
            run = False  # changing the bool to false to stop the main loop
    draw()  # calling the draw function
    select_option()  # calling the select colour function
