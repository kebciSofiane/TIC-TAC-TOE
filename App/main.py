import pygame

pygame.init()

screenWidth = 800
screenHeight = 500

gameScreenHeight = 500
gameScreenWidth = 590
cellWidth = 590 / 3
cellHeight = 500 / 3

cell1_1X = 0
cell1_1Y = 0

cell1_2X = cell1_1X + cellWidth
cell1_2Y = cell1_1Y

cell1_3X = cell1_2X + cellWidth
cell1_3Y = cell1_2Y

cell2_1X = cell1_1X
cell2_1Y = cell1_1Y + cellHeight

cell2_2X = cell1_1X + cellWidth
cell2_2Y = cell2_1Y

cell2_3X = cell1_2X + cellWidth
cell2_3Y = cell2_1Y

cell3_1X = cell1_1X
cell3_1Y = cell2_1Y + cellHeight

cell3_2X = cell1_2X
cell3_2Y = cell3_1Y

cell3_3X = cell1_3X
cell3_3Y = cell3_1Y

surface = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Tic-Tac-Toe")

running = True
color = "red"

imgX = pygame.image.load("D:\\France\\Programmation\\pyhton\\Images\\x-png-22.png")
imgO = pygame.image.load("D:\\France\\Programmation\\pyhton\\Images\\R.png")

imgX = pygame.transform.scale(imgX, (150, 150))
imgO = pygame.transform.scale(imgO, (150, 150))

clickState = False


def oddOrEven(cellY, cellX):
    if not clickState:
        surface.blit(imgX, (cellX, cellY))
    else:
        surface.blit(imgO, (cellX, cellY))
    pygame.display.flip()


def start():
    global clickState
    if clickState:
        clickState = False
    else:
        clickState = True

    if event.type == pygame.MOUSEBUTTONUP:

        mouse_presses = pygame.mouse.get_pressed()
        (x, y) = pygame.mouse.get_pos()
        while mouse_presses[0]:
            mouse_presses = pygame.mouse.get_pressed()

        if cell1_1X + cellWidth > x > cell1_1X and cell1_1Y + cellHeight > y > cell1_1Y:
            oddOrEven(cell1_1Y, cell1_1X)
        elif cell1_2X + cellWidth > x > cell1_2X and cell1_2Y + cellHeight > y > cell1_2Y:
            oddOrEven(cell1_2Y, cell1_2X)
        if cell1_3X + cellWidth > x > cell1_3X and cell1_3Y + cellHeight > y > cell1_3Y:
            oddOrEven(cell1_3Y, cell1_3X)
        if cell2_1X + cellWidth > x > cell2_1X and cell2_1Y + cellHeight > y > cell2_1Y:
            surface.blit(imgX, (cell2_1X, cell2_1Y))
        if cell2_2X + cellWidth > x > cell2_2X and cell2_2Y + cellHeight > y > cell2_2Y:
            surface.blit(imgX, (cell2_2X, cell2_2Y))
        if cell2_3X + cellWidth > x > cell2_3X and cell2_3Y + cellHeight > y > cell2_3Y:
            surface.blit(imgX, (cell2_3X, cell2_3Y))
        if cell3_1X + cellWidth > x > cell3_1X and cell3_1Y + cellHeight > y > cell3_1Y:
            surface.blit(imgX, (cell3_1X, cell3_1Y))
        if cell3_2X + cellWidth > x > cell3_2X and cell3_2Y + cellHeight > y > cell3_2Y:
            surface.blit(imgX, (cell3_2X, cell3_2Y))
        if cell3_3X + cellWidth > x > cell3_3X and cell3_3Y + cellHeight > y > cell3_3Y:
            surface.blit(imgX, (cell3_3X, cell3_3Y))


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    rect = pygame.draw.rect(surface, "white", pygame.Rect((screenWidth - 210, screenHeight - 490, 200, 480)))
    font = pygame.font.Font('freesansbold.ttf', 20)

    textStart = font.render('Start', True, "black", "red")
    textRestart = font.render('Restart', True, "black", "red")
    textQuit = font.render('Quit', True, "black", "red")

    textStartDisplay = surface.blit(textStart, (654, 20))
    textRestartDisplay = surface.blit(textRestart, (654, 50))
    textQuitDisplay = surface.blit(textQuit, (654, 80))

    pygame.display.flip()

    if event.type == pygame.MOUSEBUTTONDOWN:
        pos = pygame.mouse.get_pos()
        if textQuitDisplay.collidepoint(pos):
            running = False
    start()
