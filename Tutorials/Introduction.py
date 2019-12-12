# Once you execute your program, this will pop up every single time:
# "pygame 1.9.4 Hello from the pygame community.
#  https://www.pygame.org/contribute.html"
# To remove it, do the following two lines
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import pygame
# documents: https://www.pygame.org/docs/ref/event.html

# QUIT              none
# ACTIVEEVENT       gain, state
# KEYDOWN           key, mod, unicode, scancode
# KEYUP             key, mod
# MOUSEMOTION       pos, rel, buttons
# MOUSEBUTTONUP     pos, button
# MOUSEBUTTONDOWN   pos, button
# JOYAXISMOTION     joy, axis, value
# JOYBALLMOTION     joy, ball, rel
# JOYHATMOTION      joy, hat, value
# JOYBUTTONUP       joy, button
# JOYBUTTONDOWN     joy, button
# VIDEORESIZE       size, w, h
# VIDEOEXPOSE       none
# USEREVENT         code


x = pygame.init()       # Return a tuple

# gameDisplay is our surface
gameDisplay = pygame.display.set_mode((800, 600))     # Input is tuple, set the game screen size

pygame.display.set_caption('Introduction')   # set the title of the game

# display.flip() and display.update() are almost the same, most people use display.update()
# pygame.display.flip()
# pygame.display.update()
gameExit = False


# start a game loop, this is the main loop
while not gameExit:
    for event in pygame.event.get():
        # print(event)    # print any events (mouse pressed, key pressed, key released, etc.)

        # Here you can quit the game by clicking the 'x' button
        if event.type == pygame.QUIT:   # quit event
            gameExit = True

    gameDisplay.fill((255, 255, 255))      # fill some color! (255, 255, 255) is white, but this wipes out everything into that colour

    # if you want a background picture, objects, other stuff, do it here.
    # To draw a rectangle, the parameters are where to draw, what color to draw, and then the coordinates.
    # The coordinates are the top left corner, and its width and height.
    pygame.draw.rect(gameDisplay, (255, 0, 0), [400, 300, 10, 50])  # (255, 0, 0) is red, and remember width FIRST, and then height.
    pygame.draw.rect(gameDisplay, (0, 0, 0), [400, 300, 10, 40])    # The black rectangle covers the red one.

    # There is a better way to draw rectangle
    gameDisplay.fill((0, 255, 0), rect=[200, 200, 50, 50])


    # once you have done everything such as filling colour, motions, shape changing, etc. then you call display.update()
    pygame.display.update()


# Exit pygame, uninitializing the parameters
pygame.quit()
quit()  # you have to do that