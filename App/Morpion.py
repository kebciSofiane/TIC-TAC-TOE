import pygame
import time, random, copy

# todo
# Parfois y'a un beug ou quand x gagne en mode bot le o jour directement et gagne aussi
# le prbleme du scroll


pygame.init()

screenWidth = 800
screenHeight = 550

gameScreenHeight = 500
gameScreenWidth = 590

cellWidth = gameScreenWidth / 3
cellHeight = gameScreenHeight / 3

menuWidth = 200
menuHeight = screenHeight

surface = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Tic-Tac-Toe")

running = True
color = "red"

imgX = pygame.image.load("D:\\France\\Programmation\\pyhton\\Images\\x-png-22.png")
imgO = pygame.image.load("D:\\France\\Programmation\\pyhton\\Images\\R.png")
imgTitle = pygame.image.load("D:\\France\\Programmation\\pyhton\\Images\\Title.png")
imgSubTitle = pygame.image.load("D:\\France\\Programmation\\pyhton\\Images\\SubTitle.png")

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
imgVerticalLine = pygame.image.load("D:\\France\\Programmation\\pyhton\\Images\\verticalLine.png")
imgdiagonalLeftLine = pygame.image.load("D:\\France\\Programmation\\pyhton\\Images\\diagonalLineLeft.png")
imgdiagonalRightLine = pygame.image.load("D:\\France\\Programmation\\pyhton\\Images\\diagonalLineRight.png")

imgWinRect = pygame.image.load("D:\\France\\Programmation\\pyhton\\Images\\rect.png")
imgInputFrame = pygame.image.load("D:\\France\\Programmation\\pyhton\\Images\\inputBox.png")

imgX = pygame.transform.scale(imgX, (150, 150))
imgO = pygame.transform.scale(imgO, (150, 150))
imgTitle = pygame.transform.scale(imgTitle, (300, 200))
imgSubTitle = pygame.transform.scale(imgSubTitle, (550, 30))

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

imgInputFrame = pygame.transform.scale(imgInputFrame, (170, 50))

imgInputBox2 = imgInputFrame.copy()

base_font = pygame.font.Font(None, 32)
userName = ''
player2Name = ''
player1Name = ''

playerOScore = 0
playerXScore = 0

nameButtonClicked = False
displayGameMode = False

gameNotFinished = False
gameType = "twoPlayers"
playerNameLength = 9
botStarts = False

font1 = pygame.font.SysFont('freesanbold.ttf', 40)
font2 = pygame.font.SysFont('freesanbold.ttf', 30)
font3 = pygame.font.SysFont('freesanbold.ttf', 20)

gameLanguage = 'fr'

announceWinnerText = font1.render("The winner is ", True, (0, 0, 0))
twoPlayersText = font1.render("2 Players", True, (0, 0, 0))
botText = font1.render("Bot", True, (0, 0, 0))
drawText = font1.render("It's a draw", True, (0, 0, 0))
currentPlayerText = font1.render("Player 1's name:", True, (255, 255, 255))
creditText = font3.render("Sofiane Kebci", True, (255, 255, 255))
yearText = font3.render("2023", True, (255, 255, 255))
versionText = font3.render("v1.0", True, (255, 255, 255))

firstClick = True

chooseName = False
enterClick = 0


def input_box():
    global userName, enterClick, player1Name, player2Name, currentPlayerText
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_BACKSPACE:
            userName = userName[:-1]
        else:
            if len(userName) < playerNameLength:
                userName += event.unicode
        if event.key == pygame.K_RETURN:
            enterClick += 1
            if enterClick == 1:
                player1Name = userName[:-1]
                currentPlayerText = font1.render("Player 2's name :", True, (255, 255, 255))

            elif enterClick == 2:
                player2Name = userName[:-1]

            userName = ''


def input_name():
    global inputFrameName
    if len(userName) <= playerNameLength:
        gameMode()
        inputFrameName = surface.blit(imgInputFrame, (gameScreenWidth / 2, gameScreenHeight - 100))
        textDisplayOnInputFrame = base_font.render(userName, True, (255, 255, 255))
        surface.blit(textDisplayOnInputFrame, (gameScreenWidth / 2 + 20, gameScreenHeight - 85))
        surface.blit(currentPlayerText, (gameScreenWidth / 2 - currentPlayerText.get_width(), gameScreenHeight - 85))


def gameMode():
    global bot, Player2, textQuitDisplay, surface, textStartDisplay, displayGameMode, textRestartDisplay, gameNotFinished, playerXScore, playerOScore
    gameNotFinished = False
    displayGameMode = True

    surface.fill("black")
    playerXScore = 0
    playerOScore = 0

    pygame.draw.rect(surface, "white",
                     pygame.Rect((screenWidth - 210, 0, menuWidth, menuHeight)))
    surface.blit(imgTitle, (gameScreenWidth / 2 - imgTitle.get_width() / 2, 100))
    surface.blit(imgSubTitle, (gameScreenWidth / 2 - imgSubTitle.get_width() / 2, 350))
    textStartDisplay = surface.blit(imgStartUnclicked, (1000, 40))
    textRestartDisplay = surface.blit(imgRestartUnclicked, (1000, 160))
    textQuitDisplay = surface.blit(imgQuitUnclicked, (625, 100))
    Player2 = surface.blit(imgPlayerFrame, (gameScreenWidth + 15, 300))
    surface.blit(twoPlayersText, (gameScreenWidth + 40, 315))
    bot = surface.blit(imgPlayerFrame, (gameScreenWidth + 15, 350))
    surface.blit(botText, (gameScreenWidth + 70, 365))
    surface.blit(creditText, (gameScreenWidth - creditText.get_width(), gameScreenHeight+5))
    surface.blit(yearText, (gameScreenWidth - 2*yearText.get_width(), gameScreenHeight+20))
    surface.blit(versionText, (0, 0))


def gameInitializing(gameType):
    global clickState, board, gameNotFinished, displayGameMode, winner, surface, text1, text2, player2Name, player1Name, currentPlayerText, playerXScore, playerXScore
    displayGameMode = False
    Player2.update(1000, 1000, 1, 1)
    bot.update(1000, 1000, 1, 1)
    surface.fill("black")
    pygame.draw.rect(surface, "white",
                     pygame.Rect((screenWidth - 210, 0, menuWidth, menuHeight)))
    surface.blit(imgPlayerFrame, (605, 300))
    if player2Name == "":
        player2Name = "Player O"
    if player1Name == "":
        player1Name = "Player X"

    text1 = font1.render(player1Name, True, (255, 0, 0))
    text2 = font1.render(player2Name, True, (255, 0, 0))
    textScorePlayerX = font1.render(player1Name + " : " + str(playerXScore), True, (255, 255, 255))
    textScorePlayerO = font1.render(player2Name + " : " + str(playerOScore), True, (255, 255, 255))

    textStartDisplay.update(625, 40, 20, 29)
    textRestartDisplay.update(625, 160, 20, 29)

    surface.blit(textScorePlayerX, (gameScreenWidth / 3 - text1.get_width() / 2, gameScreenHeight))
    surface.blit(textScorePlayerO, (gameScreenWidth * 2 / 3 - text2.get_width() / 2, gameScreenHeight))
    states = ["X", "O"]
    firstPlaying = random.choice(states)
    clickState = firstPlaying
    if firstPlaying == "X":
        player = text1
    else:
        player = text2

    surface.blit(player, (630, 315))
    pygame.display.flip()
    winner = ""
    board = [["", "", ""],
             ["", "", ""],
             ["", "", ""]]
    if firstPlaying == "O" and gameType == 'bot':
        botPlay()


gameMode()


def gameRestart(gameType):
    global rect, textQuitDisplay, textRestartDisplay, textStartDisplay, board, gameNotFinished, clickState

    bot.update(1000, 1000, 400, 300)
    Player2.update(1000, 1000, 400, 300)
    pygame.display.update()
    surface.fill("black")
    gameInitializing(gameType)


def bestMove():
    (i, j) = (-1, -1)

    possibleMoves = []
    for i in range(3):
        for j in range(3):
            if (board[i][j] == ""):
                possibleMoves.append((i, j))

    if len(possibleMoves) == 0:
        return (-1, -1)

    for let in ['O', 'X']:
        for (i, j) in possibleMoves:
            boardCopy = copy.deepcopy(board)
            boardCopy[i][j] = let
            if (checkWin(i, j, boardCopy, False)) == let:
                return (i, j)

    cornersOpen = []
    for (i, j) in possibleMoves:
        if (i, j) in [(0, 0), (0, 2), (2, 0), (2, 2)]:
            cornersOpen.append((i, j))
    if (len(cornersOpen) > 0):
        return random.choice(cornersOpen)

    if (1, 1) in possibleMoves:
        return (1, 1)

    edgesOpen = []
    for (i, j) in possibleMoves:
        if (i, j) in [(0, 1), (1, 0), (1, 2), (2, 1)]:
            edgesOpen.append((i, j))
    if (len(edgesOpen) > 0):
        return random.choice(edgesOpen)

    return (i, j)


def drawXorO(row, col):
    global clickState, player
    if gameType == "twoPlayers":
        if board[row][col] == "":
            if clickState == "X":
                surface.blit(imgX, (cellWidth * col, cellHeight * row))
                clickState = "O"
                player = text2
                board[row][col] = "X"
            else:
                surface.blit(imgO, (cellWidth * col, cellHeight * row))
                clickState = "X"
                player = text1
                board[row][col] = "O"""
            displayWinner(checkWin(row, col, board, True))
            playerDisplay = surface.blit(imgPlayerFrame, (605, 300))
            surface.blit(player, (630, 315))
            pygame.display.update()

    else:
        if board[row][col] == "":
            surface.blit(imgX, (cellWidth * col, cellHeight * row))
            player = text2
            board[row][col] = "X"
            displayWinner(checkWin(row, col, board, True))
            botPlay()


def botPlay():
    (i, j) = bestMove()
    if (i, j) != (-1, -1) and not checkBoardFull():
        surface.blit(imgO, (cellWidth * j, cellHeight * i))
        board[i][j] = "O"
        displayWinner(checkWin(i, j, board, True))


def checkBoardFull():
    full = True
    for raw in board:
        for col in raw:
            if col == "":
                full = False
    return full


def displayWinner(winner):
    global gameNotFinished, nbr, playerXScore, playerOScore
    if winner == "X":
        playerXScore += 1

        gameNotFinished = False
        surface.blit(imgWinRect, (
        gameScreenWidth / 2 - imgWinRect.get_width() / 2, gameScreenHeight / 2 - imgWinRect.get_height() / 2))
        surface.blit(announceWinnerText,
                     (gameScreenWidth / 2 - announceWinnerText.get_width() / 2, gameScreenHeight / 2 - 40))
        surface.blit(text1, (
        gameScreenWidth / 2 - text1.get_width() / 2, gameScreenHeight / 2 + announceWinnerText.get_height() / 2))

    elif winner == "O":
        playerOScore += 1
        gameNotFinished = False
        surface.blit(imgWinRect, (
        gameScreenWidth / 2 - imgWinRect.get_width() / 2, gameScreenHeight / 2 - imgWinRect.get_height() / 2))
        surface.blit(announceWinnerText, (gameScreenWidth / 2 - 100, gameScreenHeight / 2 - 40))
        surface.blit(text2, (gameScreenWidth / 2 - 60, gameScreenHeight / 2 + announceWinnerText.get_height() / 2))


    elif checkBoardFull():
        surface.blit(imgWinRect, (
        gameScreenWidth / 2 - imgWinRect.get_width() / 2, gameScreenHeight / 2 - imgWinRect.get_height() / 2))
        surface.blit(drawText, (gameScreenWidth / 2 - imgWinRect.get_width() / 2 + drawText
                                .get_width() / 2, gameScreenHeight / 2 - drawText.get_height() / 2))

    pygame.display.update()


def checkWin(row, col, boxUsed, drawLine):
    global winner

    if boxUsed[row][0] == boxUsed[row][1] == boxUsed[row][2]:
        if drawLine:
            surface.blit(imgHorizentalLine,
                         (20, row * cellHeight + cellHeight / 3 - imgHorizentalLine.get_height() / 3))
        winner = boxUsed[row][0]

    elif boxUsed[0][col] == boxUsed[1][col] == boxUsed[2][col]:
        if drawLine:
            surface.blit(imgVerticalLine, (col * cellWidth + cellHeight / 3 - imgVerticalLine.get_width() / 4, 10))
        winner = boxUsed[1][col]

    elif boxUsed[0][0] == boxUsed[1][1] == boxUsed[2][2] == "X":
        if drawLine:
            surface.blit(imgdiagonalLeftLine, (40, 30))
        winner = "X"

    elif boxUsed[0][0] == boxUsed[1][1] == boxUsed[2][2] == "O":
        if drawLine:
            surface.blit(imgdiagonalLeftLine, (40, 30))
        winner = "O"

    elif boxUsed[2][0] == boxUsed[1][1] == boxUsed[0][2] == "X":
        if drawLine:
            surface.blit(imgdiagonalRightLine, (40, 30))
        winner = "X"

    elif boxUsed[2][0] == boxUsed[1][1] == boxUsed[0][2] == "O":
        if drawLine:
            surface.blit(imgdiagonalRightLine, (40, 30))
        winner = "O"

    else:
        winner = " "

    return winner


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
    global firstClick
    if event.type == pygame.MOUSEBUTTONDOWN:
        (x, y) = pygame.mouse.get_pos()
        findColAndRow(x, y)


while running:
    if not (chooseName):
        input_name()

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if inputFrameName.collidepoint(pos):
                nameButtonClicked = True

        if event.type == pygame.QUIT:
            running = False
        pos = pygame.mouse.get_pos()

        if not (chooseName) and nameButtonClicked:
            input_box()

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
                gameNotFinished = True
                gameRestart(gameType)
            elif bot.collidepoint(pos):
                textStartDisplay = surface.blit(imgStartClicked, (625, 40))
                pygame.display.flip()
                gameType = "bot"
                chooseName = True
                gameInitializing(gameType)
                gameNotFinished = True

            elif Player2.collidepoint(pos):
                textStartDisplay = surface.blit(imgStartClicked, (625, 40))
                pygame.display.flip()
                gameType = "twoPlayers"
                chooseName = True
                gameInitializing(gameType)
                gameNotFinished = True
            elif textStartDisplay.collidepoint(pos):
                currentPlayerText = font1.render("Player 1's name:", True, (255, 255, 255))
                chooseName = False
                gameMode()

        elif textRestartDisplay.collidepoint(pos):
            textRestartDisplay = surface.blit(imgRestartOverview, (625, 160))

        elif textQuitDisplay.collidepoint(pos):
            textQuitDisplay = surface.blit(imgQuitOverview, (625, 100))

        elif textStartDisplay.collidepoint(pos):
            textStartDisplay = surface.blit(imgStartOverview, (625, 40))
        elif not displayGameMode:
            textStartDisplay = surface.blit(imgStartUnclicked, (625, 40))
            textRestartDisplay = surface.blit(imgRestartUnclicked, (625, 160))
            textQuitDisplay = surface.blit(imgQuitUnclicked, (625, 100))
        else:
            textQuitDisplay = surface.blit(imgQuitUnclicked, (625, 100))

        pygame.display.flip()

        if gameNotFinished:
            mouseClickDetection()
