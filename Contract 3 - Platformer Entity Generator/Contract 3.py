"""
Contract 3 - Platformer Entity Generator
Coded by Cole Gilbert
A part of team 4's submission

This program requires the 'CharacterPieces' folder of files to be installed in the same directory as the py script
in order to function. In order to generate a new monster and save to a file, press 'e' whilst the program is running.

Artwork referenced in readme.md and is being used under the Creative Commons Attribution 3.0 License
Python tutorial used for os.walk referenced in readme.md
"""

import pygame
import os
import random

# Assigning Variables
arm_files_l = []
arm_files_r = []
body_files = []
head_files = []
legs_files = []

# Assigning Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400

MONSTER_SURFACE_WIDTH = 75
MONSTER_SURFACE_HEIGHT = 120

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (255, 0, 255)


def append_character_pieces():
    """
    This function appends the file path for each appendage of the characters
    to the appropriate list, using 'import os' to find navigate the directories.

    r, d and f stand for Root, Directory and File respectively

    The function checks for files that are specifically '.png' files
    to ensure that only images from the directories are collected

    :return:
    """

    # CharacterPieces is a folder found in the same directory as the py file, it contains images of pieces
    for r, d, f in os.walk("CharacterPieces\\CharacterArms\\Left"):
        for file in f:
            if '.png' in file:
                arm_files_l.append(os.path.join(r, file))

    for r, d, f in os.walk("CharacterPieces\\CharacterArms\\Right"):
        for file in f:
            if '.png' in file:
                arm_files_r.append(os.path.join(r, file))

    for r, d, f in os.walk("CharacterPieces\\CharacterBody"):
        for file in f:
            if '.png' in file:
                body_files.append(os.path.join(r, file))

    for r, d, f in os.walk("CharacterPieces\\CharacterHead"):
        for file in f:
            if '.png' in file:
                head_files.append(os.path.join(r, file))

    for r, d, f in os.walk("CharacterPieces\\CharacterLegs"):
        for file in f:
            if '.png' in file:
                legs_files.append(os.path.join(r, file))


def main():
    """
    The main function in this program initiates pygame and runs the main
    pygame event handling loop, most other functions are called from main.

    main() does not handle generating or loading monsters but calls for functions
    for these processes

    :return:
    """

    pygame.init()

    monster_file_i = 1  # This variable keeps track of the current monster iteration for use in naming/loading

    display_surface, monster_file_i = generate_monster(monster_file_i)
    load_monster(display_surface, monster_file_i)

    pygame.display.set_caption("Contract 3 - Platformer Entity Generator")  # Setting the pygame screen caption
    pygame.display.flip()

    while True:  # This is the main event handling loop, handling quit events and keyboard events
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            if event.type == pygame.QUIT:
                return
            if keys[pygame.K_e]:  # If the 'e' key is pressed, the program will generate a new monster and save it
                monster_file_i = generate_monster(monster_file_i)
                load_monster(display_surface, monster_file_i)

            pygame.display.flip()


def generate_monster(monster_file_i):
    """
    This function will create a new surface with a purple background, to be removed later,
    for transparency

    The body parts of the monster are randomly generated using 'random.randrange()'
    using 'len()' to determine the maximum elements in each list. This way there is room
    for more body parts to be added to the program without needing to adjust any code as long as the
    sprite follows the same pixel scale, otherwise adjustments such as the 'if' statements below will be necessary.

    The program then using '.blit()' arranges the body parts on the screen so that the monster
    can be created and saved for later use.

    :param monster_file_i:
    :return:
    """

    monster_surface = pygame.display.set_mode((MONSTER_SURFACE_WIDTH, MONSTER_SURFACE_HEIGHT))
    monster_surface.fill(PURPLE)  # Purple is used as the colorkey later on to remove this background

    # Selecting random body parts
    random_arm_l = random.randrange(0, len(arm_files_l))
    random_arm_r = random.randrange(0, len(arm_files_r))
    random_body = random.randrange(0, len(body_files))
    random_head = random.randrange(0, len(head_files))
    random_legs = random.randrange(0, len(legs_files))

    if legs_files[random_legs] != "CharacterPieces\\CharacterLegs\\RWizardLegs.png" \
            and legs_files[random_legs] != "CharacterPieces\\CharacterLegs\\MerchantLegs.png":
        # This statements is created to ensure that no extra  changes are required as some assets are larger than others
        monster_surface.blit(pygame.image.load(legs_files[random_legs]), (20, 73))
    elif legs_files[random_legs] == "CharacterPieces\\CharacterLegs\\RWizardLegs.png":
        # These sprites need some adjustments based on their size, therefore they are shifted along the x axis
        monster_surface.blit(pygame.image.load(legs_files[random_legs]), (5, 73))
    elif legs_files[random_legs] == "CharacterPieces\\CharacterLegs\\MerchantLegs.png":
        # These sprites need some adjustments based on their size, therefore they are shifted along the x axis
        monster_surface.blit(pygame.image.load(legs_files[random_legs]), (13, 73))
    monster_surface.blit(pygame.image.load(arm_files_l[random_arm_l]), (17, 40))
    monster_surface.blit(pygame.image.load(arm_files_r[random_arm_r]), (40, 40))
    monster_surface.blit(pygame.image.load(body_files[random_body]), (25, 40))
    monster_surface.blit(pygame.image.load(head_files[random_head]), (25, 17))

    pygame.image.save(monster_surface, ("monster"+str(monster_file_i)+".png"))
    # This will save the monster as a '.png' file with indexing based on which monster this is

    monster_file_i += 1

    # The display is reset here as it is affected by the monster creation when making a surface for the monster creation
    display_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    display_surface.fill(BLACK)  # This will reset the screen so that the previous monster is no longer on screen

    if monster_file_i == 2:  # The display is not needed to be returned after the first iteration of this function
        return display_surface, monster_file_i
    else:
        return monster_file_i


def load_monster(display, monster_file_i):
    """
    This function is used to blit the newly created monster to the main display
    using 'set_colorkey()' to remove the background from the monster

    :param display:
    :param monster_file_i:
    :return:
    """

    monster = pygame.image.load(("monster"+str(monster_file_i-1)+".png"))
    monster.set_colorkey(PURPLE)
    # The colorkey is used to remove any pixels that are of the colour purple, therefore creating transparency.
    # This is used to remove the background from the monster images
    display.blit(monster, (100, 100))


append_character_pieces()
main()


