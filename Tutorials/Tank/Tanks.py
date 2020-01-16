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
RED = (200, 0, 0)
LIGHT_RED = (255, 0, 0)
GREEN = (34, 177, 76)
LIGHT_GREEN = (0, 255, 0)
YELLOW = (200, 200, 0)
LIGHT_YELLOW = (255, 255, 0)


display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Tanks')

# icon = pygame.image.load('Apple.png')  # 32 * 32
# pygame.display.set_icon(icon)  # set the icon image for the program

# img = pygame.image.load('SnakeHead.png')
# appleimg = pygame.image.load('Apple.png')

clock = pygame.time.Clock()

tankWidth = 40
tankHeight = 20
turretWidth = 5
wheelWidth = 5

ground_height = 35

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
        message_to_screen("The more enemies you destroy, the harder they get. ", BLACK, y_displace=50)

        # Display some rectangles and words (buttons)
        button("Play", 150, 500, 100, 50, GREEN, LIGHT_GREEN, action="Play")
        button("Control", 350, 500, 100, 50, YELLOW, LIGHT_YELLOW, action="Control")
        button("Quit", 550, 500, 100, 50, RED, LIGHT_RED, action="Quit")

        pygame.display.update()
        clock.tick(15)


def game_over():
    game_over = True
    while game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(WHITE)
        message_to_screen("Game Over", GREEN, y_displace=-100, size="large")
        message_to_screen("You died. ", BLACK, y_displace=-30)

        # Display some rectangles and words (buttons)
        button("Play Again", 150, 500, 150, 50, GREEN, LIGHT_GREEN, action="Play")
        button("Control", 350, 500, 100, 50, YELLOW, LIGHT_YELLOW, action="Control")
        button("Quit", 550, 500, 100, 50, RED, LIGHT_RED, action="Quit")

        pygame.display.update()
        clock.tick(15)


def you_win():
    win = True
    while win:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(WHITE)
        message_to_screen("You won!", GREEN, y_displace=-100, size="large")
        message_to_screen("Congratulations! ", BLACK, y_displace=-30)

        # Display some rectangles and words (buttons)
        button("Play Again", 150, 500, 150, 50, GREEN, LIGHT_GREEN, action="Play")
        button("Control", 350, 500, 100, 50, YELLOW, LIGHT_YELLOW, action="Control")
        button("Quit", 550, 500, 100, 50, RED, LIGHT_RED, action="Quit")

        pygame.display.update()
        clock.tick(15)


def tank(x, y, turPos):
    x = int(x)
    y = int(y)

    possibleTurrets = [(x-27, y-2),
                       (x-26, y-5),
                       (x-25, y-8),
                       (x-23, y-12),
                       (x-20, y-14),
                       (x-18, y-15),
                       (x-15, y-17),
                       (x-13, y-19),
                       (x-11, y-21)]

    pygame.draw.circle(gameDisplay, BLACK, (x, y), int(tankHeight/2))
    pygame.draw.rect(gameDisplay, BLACK, (x-tankHeight, y, tankWidth, tankHeight))
    pygame.draw.line(gameDisplay, BLACK, (x, y), possibleTurrets[turPos], turretWidth)

    startX = 15
    for i in range(6):
        pygame.draw.circle(gameDisplay, BLACK, (x-startX, y+21), wheelWidth)
        startX -= 6

    return possibleTurrets[turPos]


def enemy_tank(x, y, turPos):
    x = int(x)
    y = int(y)

    possibleTurrets = [(x+27, y-2),
                       (x+26, y-5),
                       (x+25, y-8),
                       (x+23, y-12),
                       (x+20, y-14),
                       (x+18, y-15),
                       (x+15, y-17),
                       (x+13, y-19),
                       (x+11, y-21)]

    pygame.draw.circle(gameDisplay, BLACK, (x, y), int(tankHeight/2))
    pygame.draw.rect(gameDisplay, BLACK, (x-tankHeight, y, tankWidth, tankHeight))
    pygame.draw.line(gameDisplay, BLACK, (x, y), possibleTurrets[turPos], turretWidth)

    startX = 15
    for i in range(6):
        pygame.draw.circle(gameDisplay, BLACK, (x-startX, y+21), wheelWidth)
        startX -= 6

    return possibleTurrets[turPos]


def barrier(xlocation, randomHeight, barrier_width):

    pygame.draw.rect(gameDisplay, BLACK, [xlocation, display_height-randomHeight, barrier_width, randomHeight])


def game_control():
    gcont = True
    while gcont:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(WHITE)
        message_to_screen("Control", GREEN, y_displace=-100, size="large")
        message_to_screen("Fire: Spacebar", BLACK, y_displace=-30)
        message_to_screen("Move Turret: Up and Down arrows", BLACK, y_displace=10)
        message_to_screen("Move Tank: Left and Right arrows", BLACK, y_displace=50)
        message_to_screen("Pause: P", BLACK, y_displace=90)

        # Display some rectangles and words (buttons)
        button("Play", 150, 500, 100, 50, GREEN, LIGHT_GREEN, action="Play")
        button("Main", 350, 500, 100, 50, YELLOW, LIGHT_YELLOW, action="Main")
        button("Quit", 550, 500, 100, 50, RED, LIGHT_RED, action="Quit")

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


def button(text, x, y, width, height, inactive_color, active_color, action=None):
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + width > cur[0] > x and y + height > cur[1] > y:
        pygame.draw.rect(gameDisplay, active_color, (x, y, width, height))
        if click[0] == 1 and action is not None:
            if action == "Quit":
                pygame.quit()
                quit()
            if action == "Control":
                game_control()
            if action == "Play":
                gameLoop()
            if action == "Main":
                game_intro()

    else:
        pygame.draw.rect(gameDisplay, inactive_color, (x, y, width, height))

    text_to_button(text, BLACK, x, y, width, height)


def fireShell(xy, tankx, tanky, turPos, gun_power, xlocation, barrier_width, randomHeight, enemyTankX, enemyTankY):
    damage = 0
    fire = True
    startingShell = list(xy)

    while fire:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        pygame.draw.circle(gameDisplay, RED, (startingShell[0], startingShell[1]), 5)

        startingShell[0] -= (12 - turPos)*2

        # y = x**2
        startingShell[1] += int((((startingShell[0] - xy[0]) * 0.015/(gun_power/50))**2) - (turPos + turPos/(12-turPos)))

        if startingShell[1] > display_height - ground_height:
            hit_x = int((startingShell[0] * display_height - ground_height) / startingShell[1])
            hit_y = int(display_height - ground_height)

            if enemyTankX+10 > hit_x > enemyTankX-10:
                damage = 25
            elif enemyTankX+15 > hit_x > enemyTankX-15:
                damage = 18
            if enemyTankX+25 > hit_x > enemyTankX-25:
                damage = 10
            elif enemyTankX+35 > hit_x > enemyTankX-35:
                damage = 5

            explosion(hit_x, hit_y)
            fire = False

        check_x_1 = startingShell[0] <= xlocation + barrier_width
        check_x_2 = startingShell[0] >= xlocation
        check_y_1 = startingShell[1] <= display_height
        check_y_2 = startingShell[1] >= display_height - randomHeight

        if check_x_1 and check_x_2 and check_y_1 and check_y_2:
            hit_x = int((startingShell[0]))
            hit_y = int(startingShell[1])
            explosion(hit_x, hit_y)
            fire = False

        pygame.display.update()
        clock.tick(50)

    return damage


def enemy_fireShell(xy, tankx, tanky, turPos, gun_power, xlocation, barrier_width, randomHeight, playerTankX, playerTankY):
    damage = 0
    currentPower = 1
    power_found = False

    while not power_found:
        currentPower += 1
        if currentPower > 100:
            power_found = True

        fire = True
        startingShell = list(xy)

        while fire:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            startingShell[0] += (12 - turPos)*2

            # y = x**2
            startingShell[1] += int((((startingShell[0] - xy[0]) * 0.015/(currentPower/50))**2) - (turPos + turPos/(12-turPos)))

            if startingShell[1] > display_height - ground_height:
                hit_x = int((startingShell[0] * display_height - ground_height) / startingShell[1])
                hit_y = int(display_height - ground_height)

                if playerTankX+10 > hit_x > playerTankX-10:
                    damage = 25
                elif playerTankX+15 > hit_x > playerTankX-15:
                    damage = 18
                if playerTankX+25 > hit_x > playerTankX-25:
                    damage = 10
                elif playerTankX+35 > hit_x > playerTankX-35:
                    damage = 5

                fire = False

            check_x_1 = startingShell[0] <= xlocation + barrier_width
            check_x_2 = startingShell[0] >= xlocation
            check_y_1 = startingShell[1] <= display_height
            check_y_2 = startingShell[1] >= display_height - randomHeight

            if check_x_1 and check_x_2 and check_y_1 and check_y_2:
                hit_x = int((startingShell[0]))
                hit_y = int(startingShell[1])
                fire = False

    fire = True
    startingShell = list(xy)

    while fire:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        pygame.draw.circle(gameDisplay, RED, (startingShell[0], startingShell[1]), 5)

        startingShell[0] += (12 - turPos)*2

        # y = x**2
        gun_power = random.randrange(int(currentPower*0.9), int(currentPower*1.1))
        startingShell[1] += int((((startingShell[0] - xy[0]) * 0.015/(gun_power/50))**2) - (turPos + turPos/(12-turPos)))

        if startingShell[1] > display_height - ground_height:
            hit_x = int((startingShell[0] * display_height - ground_height) / startingShell[1])
            hit_y = int(display_height - ground_height)
            if playerTankX+15 > hit_x > playerTankX-15:
                damage = 25
            explosion(hit_x, hit_y)
            fire = False

        check_x_1 = startingShell[0] <= xlocation + barrier_width
        check_x_2 = startingShell[0] >= xlocation
        check_y_1 = startingShell[1] <= display_height
        check_y_2 = startingShell[1] >= display_height - randomHeight

        if check_x_1 and check_x_2 and check_y_1 and check_y_2:
            hit_x = int((startingShell[0]))
            hit_y = int(startingShell[1])
            explosion(hit_x, hit_y)
            fire = False

        pygame.display.update()
        clock.tick(50)

    return damage


def health_bars(player_health, enemy_health):
    if player_health > 70:
        player_health_color = GREEN
    elif player_health > 40:
        player_health_color = YELLOW
    else:
        player_health_color = RED

    if enemy_health > 70:
        enemy_health_color = GREEN
    elif enemy_health > 40:
        enemy_health_color = YELLOW
    else:
        enemy_health_color = RED

    pygame.draw.rect(gameDisplay, player_health_color, (680, 25, player_health, 25))
    pygame.draw.rect(gameDisplay, enemy_health_color, (20, 25, enemy_health, 25))


def explosion(x, y, size=50):
    explode = True
    while explode:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        startPoint = x, y
        colorChoices = [RED, LIGHT_RED, YELLOW, LIGHT_YELLOW]
        magnitude = 1

        while magnitude < size:
            exploding_bit_x = x + random.randrange(-1*magnitude, magnitude)
            exploding_bit_y = y + random.randrange(-1*magnitude, magnitude)
            pygame.draw.circle(gameDisplay, colorChoices[random.randrange(0, 4)], (exploding_bit_x, exploding_bit_y), random.randrange(1, 5))
            magnitude += 1
            pygame.display.update()
            clock.tick(100)
        explode = False


def power(level):
    text = smallfont.render("Power: " + str(level) + "%", True, BLACK)
    gameDisplay.blit(text, [int(display_width/2), 0])


def gameLoop():
    gameExit = False
    gameOver = False
    FPS = 15

    player_health = 100
    enemy_health = 100

    mainTankX = display_width * 0.9
    mainTankY = display_height * 0.9
    tankMove = 0
    currentTurPos = 0
    changeTur = 0

    enemyTankX = display_width * 0.1
    enemyTankY = display_height * 0.9

    fire_power = 50
    power_change = 0

    xlocation = (display_width / 2) + random.randint(-0.2*display_width, 0.2*display_width)
    randomHeight = random.randrange(display_height*0.1, display_height*0.6)
    barrier_width = 50

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
                    tankMove = -5

                elif event.key == pygame.K_RIGHT:  # If right arrow key is pressed
                    tankMove = 5

                elif event.key == pygame.K_UP:  # If up arrow key is pressed
                    changeTur = 1

                elif event.key == pygame.K_DOWN:  # If down arrow key is pressed
                    changeTur = -1

                elif event.key == pygame.K_p:
                    pause()

                elif event.key == pygame.K_SPACE:
                    enemy_damage = fireShell(gun, mainTankX, mainTankY, currentTurPos, fire_power, xlocation, barrier_width, randomHeight, enemyTankX, enemyTankY)
                    enemy_health -= enemy_damage

                    possibleMovement = ['f', 'r']
                    moveIndex = random.randrange(0, 2)
                    for x in range(random.randrange(0, 10)):
                        if display_width*0.3 > enemyTankX > display_width*0.03:
                            if possibleMovement[moveIndex] == 'f':
                                enemyTankX += 5
                            elif possibleMovement[moveIndex] == 'r':
                                enemyTankX -= 5

                            gameDisplay.fill(WHITE)
                            health_bars(player_health, enemy_health)

                            gun = tank(mainTankX, mainTankY, currentTurPos)
                            enemy_gun = enemy_tank(enemyTankX, enemyTankY, 8)

                            fire_power += power_change
                            power(fire_power)

                            barrier(int(xlocation), int(randomHeight), barrier_width)
                            gameDisplay.fill(GREEN, rect=[0, display_height-ground_height, display_width, ground_height])
                            pygame.display.update()
                            clock.tick(FPS)

                    player_damage = enemy_fireShell(enemy_gun, enemyTankX, enemyTankY, 8, 50, xlocation, barrier_width, randomHeight, mainTankX, mainTankY)
                    player_health -= player_damage

                elif event.key == pygame.K_a:
                    power_change = -1

                elif event.key == pygame.K_d:
                    power_change = 1

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    tankMove = 0

                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    changeTur = 0

                if event.key == pygame.K_a or event.key == pygame.K_d:
                    power_change = 0

        mainTankX += tankMove

        currentTurPos += changeTur
        # to avoid going out of range
        if currentTurPos > 8:
            currentTurPos = 8
        elif currentTurPos < 0:
            currentTurPos = 0

        if mainTankX - tankWidth/2 < xlocation + barrier_width:
            mainTankX += 5

        gameDisplay.fill(WHITE)
        health_bars(player_health, enemy_health)

        gun = tank(mainTankX, mainTankY, currentTurPos)
        enemy_gun = enemy_tank(enemyTankX, enemyTankY, 8)

        fire_power += power_change
        power(fire_power)

        barrier(int(xlocation), int(randomHeight), barrier_width)
        gameDisplay.fill(GREEN, rect=[0, display_height-ground_height, display_width, ground_height])
        pygame.display.update()

        if player_health < 1:
            game_over()
        elif enemy_health < 1:
            you_win()
        clock.tick(FPS)  # Specify frame per second, 30 is typical

    pygame.quit()
    quit()


game_intro()
gameLoop()
