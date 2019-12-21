
import pygame
import random

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


pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 155, 0)
YELLOW = (200, 200, 0)

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Tanks')

#icon = pygame.image.load('Apple.png')  # 32 * 32
#pygame.display.set_icon(icon)  # set the icon image for the program

# img = pygame.image.load('SnakeHead.png')
# appleimg = pygame.image.load('Apple.png')

clock = pygame.time.Clock()

AppleThickness = 30
block_size = 20
FPS = 15

smallfont = pygame.font.SysFont("comicsansms", 25)  # set up a font for the game, or use font.Font to define your own font
medfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms", 80)


def pause():
    paused = True

    message_to_screen("Paused", BLACK, -100, size="large")
    message_to_screen("Press C to continue or Q to quit. ", BLACK, 25)
    pygame.display.update()

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()
        # gameDisplay.fill(WHITE)

        clock.tick(5)


def score(score):
    text = smallfont.render('Score: ' + str(score), True, BLACK)
    gameDisplay.blit(text, [0, 0])


def randAppleGen():
    randAppleX = round(random.randrange(0, display_width - AppleThickness))  # / 10.0) * 10.0
    randAppleY = round(random.randrange(0, display_height - AppleThickness))  # / 10.0) * 10.0

    return randAppleX, randAppleY


# start menu
def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        gameDisplay.fill(WHITE)
        message_to_screen("Welcome to Tanks", GREEN, y_displace=-100, size="large")
        message_to_screen("The objective is to shoot and destroy!", BLACK, y_displace=-30)
        message_to_screen("the enemy tank before they destory you. ", BLACK, y_displace=10)
        message_to_screen("The enemies you destroy, the harder they get. ", BLACK, y_displace=50)
        # message_to_screen("Press C to play, P to pause or Q to quit. ", BLACK, y_displace=180)

        # Display some rectangles and buttons
        pygame.draw.rect(gameDisplay, GREEN, (150, 500, 100, 50))
        pygame.draw.rect(gameDisplay, YELLOW, (350, 500, 100, 50))
        pygame.draw.rect(gameDisplay, RED, (550, 500, 100, 50))

        text_to_button("Play", BLACK, 150, 500, 100, 50)
        text_to_button("Control", BLACK, 350, 500, 100, 50)
        text_to_button("Quit", BLACK, 550, 500, 100, 50)


        pygame.display.update()
        clock.tick(15)



def text_objects(text, color, size):
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    elif size == "medium":
        textSurface = medfont.render(text, True, color)
    elif size == "large":
        textSurface = largefont.render(text, True, color)
    return textSurface, textSurface.get_rect()

def text_to_button(msg, color, buttonx, buttony, buttonwidth, butttonheight, size = "small"):
    textSurf, textRect = text_objects(msg, color, size)
    textRect.center = (int(buttonx + (buttonwidth/2)), buttony + int(butttonheight/2))
    gameDisplay.blit(textSurf, textRect)


def message_to_screen(msg, color, y_displace=0, size="small"):  # center the text
    textSurf, textRect = text_objects(msg, color, size)
    textRect.center = int(display_width / 2), int(display_height / 2) + y_displace
    gameDisplay.blit(textSurf, textRect)


def gameLoop():
    gameExit = False
    gameOver = False
    FPS = 15

    while not gameExit:
        if gameOver:
            message_to_screen("Game Over", RED, y_displace=-50, size="large")
            message_to_screen("Press C to play again or Q to quit", BLACK, y_displace=50, size="medium")
            pygame.display.update()

        while gameOver:
            # gameDisplay.fill(WHITE)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                    gameOver = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                gameExit = True

            if event.type == pygame.KEYDOWN:  # If any key on the keyboard is pressed
                # when lead_x_change or lead_y_change has value, the other variable has to set to 0, otherwise the snake will
                # move diagonally and never changes back.
                if event.key == pygame.K_LEFT:  # If left arrow key is pressed
                    pass

                elif event.key == pygame.K_RIGHT:  # If right arrow key is pressed
                    pass

                elif event.key == pygame.K_UP:  # If up arrow key is pressed
                    pass

                elif event.key == pygame.K_DOWN:  # If down arrow key is pressed
                    pass

                elif event.key == pygame.K_p:
                    pause()


        gameDisplay.fill(WHITE)

        pygame.display.update()

        clock.tick(FPS)  # Specify frame per second, 30 is typical

    pygame.quit()
    quit()


game_intro()
gameLoop()
