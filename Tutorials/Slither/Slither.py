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

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Slither')

icon = pygame.image.load('Apple.png')  # 32 * 32
pygame.display.set_icon(icon)  # set the icon image for the program

img = pygame.image.load('SnakeHead.png')
appleimg = pygame.image.load('Apple.png')

clock = pygame.time.Clock()

AppleThickness = 30
block_size = 20
FPS = 15
direction = "right"  # snake's head direction
smallfont = pygame.font.SysFont("comicsansms",
                                25)  # set up a font for the game, or use font.Font to define your own font
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
        message_to_screen("Welcome to Slither", GREEN, y_displace=-100, size="large")
        message_to_screen("The objective of the game is to eat red apples", BLACK, y_displace=-30)
        message_to_screen("The more apples you eat, the longer you get", BLACK, y_displace=10)
        message_to_screen("If you run into yourself, or the edges, you die!", BLACK, y_displace=50)
        message_to_screen("Press C to play, P to pause or Q to quit. ", BLACK, y_displace=180)

        pygame.display.update()
        clock.tick(15)


def snake(block_size, snakelist):
    if direction == "right":
        head = pygame.transform.rotate(img, 270)  # it's rotating counterclockwise
    if direction == "left":
        head = pygame.transform.rotate(img, 90)
    if direction == "up":
        head = img
    if direction == "down":
        head = pygame.transform.rotate(img, 180)

    gameDisplay.blit(head, (snakelist[-1][0], snakelist[-1][1]))
    for XnY in snakelist[:-1]:  # snakelist is a list of lists
        pygame.draw.rect(gameDisplay, GREEN, [XnY[0], XnY[1], block_size, block_size])


def text_objects(text, color, size):
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    elif size == "medium":
        textSurface = medfont.render(text, True, color)
    elif size == "large":
        textSurface = largefont.render(text, True, color)
    return textSurface, textSurface.get_rect()


def message_to_screen(msg, color, y_displace=0, size="small"):  # center the text
    textSurf, textRect = text_objects(msg, color, size)
    textRect.center = (display_width / 2), (display_height / 2) + y_displace
    gameDisplay.blit(textSurf, textRect)


def gameLoop():
    global direction

    direction = 'right'
    gameExit = False
    gameOver = False

    # those are the first block of the snake
    lead_x = display_width / 2
    lead_y = display_height / 2
    lead_x_change = 10
    lead_y_change = 0

    snakeList = []
    snakeLength = 1

    # Right now the center of the apple is at top left corner,
    # If the apple appears at the edge, it will go out of the frame
    randAppleX, randAppleY = randAppleGen()

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
                    direction = "left"
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:  # If right arrow key is pressed
                    direction = "right"
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP:  # If up arrow key is pressed
                    direction = "up"
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:  # If down arrow key is pressed
                    direction = "down"
                    lead_y_change = block_size
                    lead_x_change = 0
                elif event.key == pygame.K_p:
                    pause()

            # if event.type == pygame.KEYUP:      # if the player release the key
            #     if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:   # to prevent players accidentally hit some keys, we ask
            #                                                                     # if the key is left arrow of right arrow
            #         lead_x_change = 0       # if the palyer release it, then the snake stop moving

        if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:  # set up the boundaries
            gameOver = True

        lead_x += lead_x_change
        lead_y += lead_y_change

        gameDisplay.fill(WHITE)

        # pygame.draw.rect(gameDisplay, RED, [randAppleX, randAppleY, AppleThickness, AppleThickness])    # drawing an apple
        gameDisplay.blit(appleimg, (randAppleX, randAppleY))  # drawing an apple image

        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)

        if len(snakeList) > snakeLength:
            del snakeList[0]

        for eachSegment in snakeList[:-1]:
            if eachSegment == snakeHead:
                gameOver = True

        snake(block_size, snakeList)  # drawing a snake (call a function)

        score(snakeLength - 1)

        pygame.display.update()

        # Old Cross Over Code
        # This is when the apple has the exact same size as the snake
        # if lead_x == randAppleX and lead_y == randAppleY:
        #     # recreate an apple
        #     randAppleX = round(random.randrange(0, display_width - block_size) / 10.0) * 10.0
        #     randAppleY = round(random.randrange(0, display_height - block_size) / 10.0) * 10.0
        #     snakeLength += 1

        # if the apple size is bigger than the snake, then we have to check the range
        # if lead_x >= randAppleX and lead_x <=randAppleX+AppleThickness:
        #     if lead_y >= randAppleY and lead_y <= randAppleY + AppleThickness:
        #         # recreate an apple
        #         randAppleX = round(random.randrange(0, display_width - block_size))         # / 10.0) * 10.0
        #         randAppleY = round(random.randrange(0, display_height - block_size))       # / 10.0) * 10.0
        #         snakeLength += 1

        if randAppleX < lead_x < randAppleX + AppleThickness or randAppleX < lead_x + block_size < randAppleX + AppleThickness:
            if randAppleY < lead_y < randAppleY + AppleThickness or randAppleY < lead_y + block_size < randAppleY + AppleThickness:
                randAppleX, randAppleY = randAppleGen()
                snakeLength += 1

        clock.tick(FPS)  # Specify frame per second, 30 is typical
        # For a snack game, 10-15 is good

    pygame.quit()
    quit()


game_intro()
gameLoop()
