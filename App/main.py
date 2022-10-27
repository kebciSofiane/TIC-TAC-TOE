import pygame
import time

pygame.init()

screenWidth = 800
screenHeight = 500

gameScreenHeight = 500
gameScreenWidth = 590

cellWidth = gameScreenWidth / 3
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
imgStartOverview = pygame.image.load("D:\\France\\Programmation\\pyhton\\Images\\startOverview.png")

imgRestartClicked = pygame.image.load("D:\\France\\Programmation\\pyhton\\Images\\restartClicked.png")
imgRestartUnclicked = pygame.image.load("D:\\France\\Programmation\\pyhton\\Images\\restartUnclicked.png")
imgRestartOverview = pygame.image.load("D:\\France\\Programmation\\pyhton\\Images\\restartOverview.png")

imgQuitClicked = pygame.image.load("D:\\France\\Programmation\\pyhton\\Images\\quitClicked.png")
imgQuitOverview = pygame.image.load("D:\\France\\Programmation\\pyhton\\Images\\quitOverview.png")
imgQuitUnclicked = pygame.image.load("D:\\France\\Programmation\\pyhton\\Images\\quitUnclicked.png")

imgPlayerFrame = pygame.image.load("D:\\France\\Programmation\\pyhton\\Images\\PlayerFrame.png")

imgHorizentalLine = pygame.image.load("D:\\France\\Programmation\\pyhton\\Images\\horizentalLine.png")
imgVerticalLine= pygame.image.load("D:\\France\\Programmation\\pyhton\\Images\\verticalLine.png")
imgdiagonalLeftLine= pygame.image.load("D:\\France\\Programmation\\pyhton\\Images\\diagonalLineLeft.png")
imgdiagonalRightLine= pygame.image.load("D:\\France\\Programmation\\pyhton\\Images\\diagonalLineRight.png")



imgX = pygame.transform.scale(imgX, (150, 150))
imgO = pygame.transform.scale(imgO, (150, 150))
imgStartUnclicked = pygame.transform.scale(imgStartUnclicked, (130, 50))
imgStartClicked = pygame.transform.scale(imgStartClicked, (130, 50))
imgStartOverview = pygame.transform.scale(imgStartOverview, (130, 50))

imgQuitUnclicked = pygame.transform.scale(imgQuitUnclicked, (130, 50))
imgQuitClicked = pygame.transform.scale(imgQuitClicked, (130, 50))
imgQuitOverview = pygame.transform.scale(imgQuitOverview, (130, 50))

imgRestartUnclicked = pygame.transform.scale(imgRestartUnclicked, (130, 50))
imgRestartClicked = pygame.transform.scale(imgRestartClicked, (130, 50))
imgRestartOverview = pygame.transform.scale(imgRestartOverview, (130, 50))

imgPlayerFrame = pygame.transform.scale(imgPlayerFrame, (170, 50))
imgHorizentalLine = pygame.transform.scale(imgHorizentalLine, (540, 61))
imgVerticalLine = pygame.transform.scale(imgVerticalLine, (61, 480))


font1 = pygame.font.SysFont('freesanbold.ttf', 40)
text1 = font1.render('Player X', True, (255, 255, 255))
text2 = font1.render('Player O', True, (255, 255, 255))
text3 = font1.render('The winner is ', True, (255, 255, 255))



def gameInitializing():
    global textStartDisplay, clickState, boxUsed, gameNotFinished, textRestartDisplay, textQuitDisplay, winner
    pygame.draw.rect(surface, "white",
                     pygame.Rect((screenWidth - 210, screenHeight - 490, menuWidth, menuHeight)))
    textStartDisplay = surface.blit(imgStartUnclicked, (625, 40))
    textRestartDisplay = surface.blit(imgRestartUnclicked, (625, 160))
    textQuitDisplay = surface.blit(imgQuitUnclicked, (625, 100))
    surface.blit(imgPlayerFrame, (605, 300))
    player = text1
    surface.blit(player, (630, 315))

    pygame.display.flip()
    gameNotFinished = True
    clickState = "X"
    winner =""
    boxUsed = [["", "", ""], ["", "", ""], ["", "", ""]]


gameInitializing()


def gameRestart():
    global rect, textQuitDisplay, textRestartDisplay, textStartDisplay, boxUsed, gameNotFinished, clickState
    pygame.display.update()
    surface.fill("black")
    gameInitializing()


def drawXorO(row, col):
    global clickState, player
    print(row, "-", col)
    if boxUsed[row][col] == "":
        if clickState == "X":
            surface.blit(imgX, (cellWidth * col, cellHeight * row))
            clickState = "O"
            player = text2
            boxUsed[row][col] = "X"
        else:
            surface.blit(imgO, (cellWidth * col, cellHeight * row))
            clickState = "X"
            player = text1
            boxUsed[row][col] = "O"
        checkWin(row, col)
        playerDisplay = surface.blit(imgPlayerFrame, (605, 300))
        surface.blit(player, (630, 315))
        pygame.display.update()



def checkWin(row, col):
    global gameNotFinished,running,winner

    if boxUsed[row][0] == boxUsed[row][1] == boxUsed[row][2]:
        surface.blit(imgHorizentalLine, (20, row*cellHeight+ cellHeight/3))
        gameNotFinished = False
        winner = boxUsed[row][0]

    elif boxUsed[0][col] == boxUsed[1][col] == boxUsed[2][col]:
        surface.blit(imgVerticalLine, (col * cellWidth + cellHeight / 3,10))
        gameNotFinished = False
        winner=boxUsed[1][col]

    elif boxUsed[0][0] == boxUsed[1][1] == boxUsed[2][2] == "X":
        surface.blit(imgdiagonalLeftLine, (40,30))
        gameNotFinished = False
        winner="X"

    elif boxUsed[0][0] == boxUsed[1][1] == boxUsed[2][2] == "O":
        surface.blit(imgdiagonalLeftLine, (40,30))
        gameNotFinished = False
        winner="O"

    elif boxUsed[2][0] == boxUsed[1][1] == boxUsed[0][2] == "X":
        surface.blit(imgdiagonalRightLine, (40,30))
        gameNotFinished = False
        winner="X"


    elif boxUsed[2][0] == boxUsed[1][1] == boxUsed[0][2] == "O":
        surface.blit(imgdiagonalRightLine, (40, 30))
        gameNotFinished = False
        winner="O"

    if winner== "X" :
        surface.blit(text3, (100, 470))
        surface.blit(text1, (300, 470))
    elif winner=="O" :
        surface.blit(text3, (100, 470))
        surface.blit(text2, (300, 470))



    pygame.display.update()


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
        pos = pygame.mouse.get_pos()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if textQuitDisplay.collidepoint(pos):
                textQuitDisplay = surface.blit(imgQuitClicked, (625, 100))
                pygame.display.flip()
                time.sleep(0.1)
                running = False
            elif textRestartDisplay.collidepoint(pos):
                textRestartDisplay = surface.blit(imgRestartClicked, (625, 160))
                pygame.display.flip()
                time.sleep(0.2)
                gameRestart()
            elif textStartDisplay.collidepoint(pos):
                textStartDisplay = surface.blit(imgStartClicked, (625, 40))
                pygame.display.flip()

        elif textStartDisplay.collidepoint(pos):
            textStartDisplay = surface.blit(imgStartOverview, (625, 40))
        elif textRestartDisplay.collidepoint(pos):
            textRestartDisplay = surface.blit(imgRestartOverview, (625, 160))
        elif textQuitDisplay.collidepoint(pos):
            textQuitDisplay = surface.blit(imgQuitOverview, (625, 100))

        else:
            textStartDisplay = surface.blit(imgStartUnclicked, (625, 40))
            textRestartDisplay = surface.blit(imgRestartUnclicked, (625, 160))
            textQuitDisplay = surface.blit(imgQuitUnclicked, (625, 100))

        pygame.display.flip()

        if gameNotFinished:
            mouseClickDetection()
