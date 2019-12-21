import pygame

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

gameDisplay = pygame.display.set_mode((800, 600))

gameDisplay.fill(BLUE)  # background color

Pix = pygame.PixelArray(gameDisplay)    # return a large array of pixels
Pix[10][10] = GREEN
pygame.draw.line(gameDisplay, RED, (200, 300), (500, 500), 5)   # draw a 5 pixel wide red line from (200, 300) to (500, 700)
pygame.draw.circle(gameDisplay, RED, (50, 50), 50)  # circle
pygame.draw.rect(gameDisplay, GREEN, (150, 150, 200, 100))      # draw a rectangle at (150, 150), 200 wide, 100 long
pygame.draw.polygon(gameDisplay, WHITE, ((140, 5), (200, 16), (88, 333), (600, 222), (555, 22)))    # polygon, connecting the nodes


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    pygame.display.update()
