import pygame

pygame.init()

screenWidth = 800
screenHeight = 500

gameScreenHeight = 500
gameScreenWidth = 590

cellWidth = gameScreenWidth = 590 / 3
cellHeight = gameScreenHeight / 3

menuWidth = 200
menuHeight = 480

surface = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Tic-Tac-Toe")

running = True

color = "red"

imgX = pygame.image.load("D:\\France\\Programmation\\pyhton\\Images\\x-png-22.png")
imgO = pygame.image.load("D:\\France\\Programmation\\pyhton\\Images\\R.png")
imgStartClicked = pygame.image.load("D:\\France\\Programmation\\pyhton\\Images\\startClicked.png")
imgStartUnclicked = pygame.image.load("D:\\France\\Programmation\\pyhton\\Images\\start_Unclicked.png")
imgQuitUnclicked = pygame.image.load("D:\\France\\Programmation\\pyhton\\Images\\quitUnclicked.png")
imgRestartUnclicked = pygame.image.load("D:\\France\\Programmation\\pyhton\\Images\\restartUnclicked.png")

imgX = pygame.transform.scale(imgX, (150, 150))
imgO = pygame.transform.scale(imgO, (150, 150))
imgStartUnclicked = pygame.transform.scale(imgStartUnclicked, (130, 50))
imgQuitUnclicked = pygame.transform.scale(imgQuitUnclicked, (130, 50))
imgRestartUnclicked = pygame.transform.scale(imgRestartUnclicked, (130, 50))


def gameInitializing():
    global textStartDisplay, clickState, boxUsed, gameNotFinished, textRestartDisplay, textQuitDisplay
    pygame.draw.rect(surface, "white", pygame.Rect((screenWidth - 210, screenHeight - 490, menuWidth, menuHeight)))
    textStartDisplay = surface.blit(imgStartUnclicked, (625, 40))
    textRestartDisplay = surface.blit(imgRestartUnclicked, (625, 160))
    textQuitDisplay = surface.blit(imgQuitUnclicked, (625, 100))
    pygame.display.flip()
    gameNotFinished = True
    clickState = "X"
    boxUsed = [["", "", ""], ["", "", ""], ["", "", ""]]


gameInitializing()


def gameRestart():
    global rect, textQuitDisplay, textRestartDisplay, textStartDisplay, boxUsed, gameNotFinished, clickState
    pygame.display.update()
    surface.fill("black")
    gameInitializing()


def drawXorO(row, col):
    global clickState
    print(row, "-", col)
    if boxUsed[row][col] == "":
        if clickState == "X":
            surface.blit(imgX, (cellWidth * col, cellHeight * row))
            clickState = "O"
            boxUsed[row][col] = "X"
        else:
            surface.blit(imgO, (cellWidth * col, cellHeight * row))
            clickState = "X"
            boxUsed[row][col] = "O"
        checkWin(row, col)
        pygame.display.update()


def alertBoxWinLoose():
    global gameNotFinished
    pygame.draw.line(surface, color, (23, 45), (200, 43))
    pygame.display.update()

    gameNotFinished = False;


def checkWin(row, col):
    global running
    if boxUsed[row][0] == boxUsed[row][1] == boxUsed[row][2]:
        alertBoxWinLoose()
    elif boxUsed[0][col] == boxUsed[1][col] == boxUsed[2][col]:
        alertBoxWinLoose()
    elif boxUsed[0][0] == boxUsed[1][1] == boxUsed[2][2] == "X":
        alertBoxWinLoose()
    elif boxUsed[0][0] == boxUsed[1][1] == boxUsed[2][2] == "O":
        alertBoxWinLoose()
    elif boxUsed[2][0] == boxUsed[1][1] == boxUsed[0][2] == "X":
        alertBoxWinLoose()
    elif boxUsed[2][0] == boxUsed[1][1] == boxUsed[0][2] == "O":
        alertBoxWinLoose()


def findColAndRow(x, y):
    row, col = -1, -1
    if x < cellWidth:
        col = 0
    elif x < cellWidth * 2:
        col = 1

    elif cellWidth * 2 < x < cellWidth * 3:
        col = 2

    if y < cellHeight:
        row = 0
    elif y < cellHeight * 2:
        row = 1
    elif cellHeight * 2 < y < cellHeight * 3:
        row = 2

    if row > -1 and col > -1:
        drawXorO(row, col)


def mouseClickDetection():
    if event.type == pygame.MOUSEBUTTONDOWN:
        (x, y) = pygame.mouse.get_pos()
        findColAndRow(x, y)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if textQuitDisplay.collidepoint(pos):
                running = False
            if textRestartDisplay.collidepoint(pos):

                gameRestart()
        if gameNotFinished:
            mouseClickDetection()
