import pygame
import http.client
import json
import time, random, copy

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

playerNameLength = 9

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
imgVerticalLine= pygame.image.load("D:\\France\\Programmation\\pyhton\\Images\\verticalLine.png")
imgdiagonalLeftLine= pygame.image.load("D:\\France\\Programmation\\pyhton\\Images\\diagonalLineLeft.png")
imgdiagonalRightLine= pygame.image.load("D:\\France\\Programmation\\pyhton\\Images\\diagonalLineRight.png")

imgWinRect= pygame.image.load("D:\\France\\Programmation\\pyhton\\Images\\rect.png")
imgInputBox = pygame.image.load("D:\\France\\Programmation\\pyhton\\Images\\inputBox.png")



imgX = pygame.transform.scale(imgX, (150, 150))
imgO = pygame.transform.scale(imgO, (150, 150))
imgTitle = pygame.transform.scale(imgTitle,(300,200))
imgSubTitle = pygame.transform.scale(imgSubTitle,(550,30))

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

imgInputBox = pygame.transform.scale(imgInputBox, (170, 50))




color_passive = pygame.Color('white')
color_active = pygame.Color('red')
base_font = pygame.font.Font(None, 32)
color = color_passive
user_text = ''
active = False;


gameNotFinished=False;
gameType ="twoPlayers"



def translation(toBeTranslated, gameLanguage) :
    if gameLanguage =="fr" :
        return toBeTranslated

    conn = http.client.HTTPSConnection("microsoft-translator-text.p.rapidapi.com")

    payload = "[\r\n    {\r\n        \"Text\": \""+toBeTranslated+"\"\r\n    }\r\n]"

    headers = {
        'content-type': "application/json",
        'X-RapidAPI-Key': "6abcd70b6emshc428c20a28bad0dp1e7404jsn07b33286d64c",
        'X-RapidAPI-Host': "microsoft-translator-text.p.rapidapi.com"
    }

    conn.request("POST", "/translate?to%5B0%5D="+gameLanguage+"&api-version=3.0&from=fr&profanityAction=NoAction&textType=plain",
                 payload, headers)

    res = conn.getresponse()
    json_obj = json.load(res)

    theTranslation = json_obj[0].get('translations')[0].get('text');
    return theTranslation

font1 = pygame.font.SysFont('freesanbold.ttf', 40)
font2 = pygame.font.SysFont('freesanbold.ttf', 30)

gameLanguage = 'fr';


text3 = font1.render(translation("Le gagnant est ",gameLanguage), True, (0, 0, 0))
text4 = font1.render(translation("2 Joueurs",gameLanguage), True, (0, 0, 0))
text5 = font1.render(translation("Robot",gameLanguage), True, (0, 0, 0))
text6 = font1.render(translation("c'est un match nul",gameLanguage), True, (0, 0, 0))

firstClick = True


#todo
#count the wins
#Le boutton Play ne brille pas
#Ajout du nom des joueur

chooseName = False
def input_box() :
    global  user_text

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_BACKSPACE:
            user_text = user_text[:-1]
        else:
            if len(user_text) < playerNameLength:
                user_text += event.unicode
        if event.key == pygame.K_RETURN:
            print(user_text);


def input_name():
    global inputBox
    if len(user_text) <= playerNameLength :
        gameMode()
        inputBox = surface.blit(imgInputBox, (gameScreenWidth/2-imgInputBox.get_width()/2, gameScreenHeight-100))
        text_surface = base_font.render(user_text, True, (255, 255, 255))
        surface.blit(text_surface, (gameScreenWidth/2-imgInputBox.get_width()/2+20, gameScreenHeight-100+15))

def gameMode():

    global  bot, Player2,textQuitDisplay, surface,textStartDisplay,textRestartDisplay,gameNotFinished
    gameNotFinished = False;

    surface.fill("black")
    firstClick = False

    pygame.draw.rect(surface, "white",
                     pygame.Rect((screenWidth - 210, screenHeight - 490, menuWidth, menuHeight)))
    textStartDisplay = surface.blit(imgStartUnclicked, (625, 40))
    titleDisplay = surface.blit(imgTitle, (gameScreenWidth/2-imgTitle.get_width()/2, 100))
    subTitleDisplay = surface.blit(imgSubTitle, (gameScreenWidth/2-imgSubTitle.get_width()/2,  350))


    textRestartDisplay = surface.blit(imgRestartUnclicked, (625, 160))
    textQuitDisplay = surface.blit(imgQuitUnclicked, (625, 100))
    #TODO
    #Réorganiser tout ça sans les chiffres
    Player2 = surface.blit(imgPlayerFrame, (gameScreenWidth+15 , 300))
    Player2Text = surface.blit(text4, (gameScreenWidth+40, 315))
    bot = surface.blit(imgPlayerFrame, (gameScreenWidth+15, 350))
    botText = surface.blit(text5, (gameScreenWidth+70, 365))
def gameInitializing(gameType):
    global  clickState, board, gameNotFinished, winner,surface,text1,text2
    Player2.update(1000,1000,1,1)
    bot.update(1000,1000,1,1)

    surface.fill("black")
    pygame.draw.rect(surface, "white",
                     pygame.Rect((screenWidth - 210, screenHeight - 490, menuWidth, menuHeight)))
    surface.blit(imgPlayerFrame, (605, 300))
    text1 = font1.render(translation(user_text, gameLanguage), True, (255, 0, 0))
    text2 = font1.render(translation("Joueur O", gameLanguage), True, (255, 0, 0))

    player = text1
    surface.blit(player, (630, 315))
    pygame.display.flip()
    clickState = "X"
    winner =""
    board = [["", "", ""],
             ["", "", ""],
             ["", "", ""]]
    list = "";

gameMode()


def gameRestart(gameType):
    global rect, textQuitDisplay, textRestartDisplay, textStartDisplay, board, gameNotFinished, clickState

    bot.update(1000, 1000, 400, 300);
    Player2.update(1000, 1000, 400, 300);
    pygame.display.update()
    surface.fill("black")
    gameInitializing(gameType)





def bestMove():
    (i,j) = (-1,-1);

    possibleMoves=[];
    for i in range(3):
        for j in range(3):
            if(board[i][j] == ""):
                possibleMoves.append((i,j))

    if len(possibleMoves) == 0 :
        return  (-1,-1)

    for let in ['O','X'] :
        for (i,j) in possibleMoves:
            boardCopy = copy.deepcopy(board)
            boardCopy[i][j]= let;
            if (checkWin(i,j,boardCopy,False) ) == let :
                return (i,j);

    cornersOpen =[];
    for (i,j) in possibleMoves :
        if (i,j) in [(0,0),(0,2),(2,0),(2,2)]:
            cornersOpen.append((i,j));
    if(len(cornersOpen)>0):
        return random.choice(cornersOpen);


    if (1,1) in possibleMoves :
        return (1,1);

    edgesOpen =[];
    for (i,j) in possibleMoves :
        if (i,j) in [(0,1),(1,0),(1,2),(2,1)]:
            edgesOpen.append((i,j));
    if(len(edgesOpen)>0):
        return random.choice(edgesOpen);

    return (i,j);
def drawXorO(row, col):
    global clickState, player
    if gameType == "twoPlayers":
         if board[row][col] == "":
            if clickState == "X":
                surface.blit(imgX, (cellWidth * col, cellHeight * row))
                clickState = "O"
                player = text1
                board[row][col] = "X"
            else :
                surface.blit(imgO, (cellWidth * col, cellHeight * row))
                clickState = "X"
                player = text2
                board[row][col] = "O"""
            displayWinner(checkWin(row, col, board,True));
            playerDisplay = surface.blit(imgPlayerFrame, (605, 300))
            surface.blit(player, (630, 315))
            pygame.display.update()

    else:
        if board[row][col] == "":
                surface.blit(imgX, (cellWidth * col, cellHeight * row))
                player = text2
                board[row][col] = "X"
                displayWinner(checkWin(row, col, board,True));

                (i,j) = bestMove();
                if (i,j) != (-1,-1) and not checkBoardFull() :
                    surface.blit(imgO, (cellWidth * j, cellHeight * i))
                    board[i][j] = "O"
                    displayWinner(checkWin(i, j, board,True));


                else:
                    gameNotFinished = False;

def checkBoardFull():
    full = True
    for raw in board :
        for col in raw :
             if col == "" :
                  full = False
    return  full
def displayWinner(winner):
    global gameNotFinished;
    if winner== "X" :
        gameNotFinished = False
        surface.blit(imgWinRect, (gameScreenWidth / 2 - 150, gameScreenHeight / 2 - 130))
        surface.blit(text3, (gameScreenWidth / 2 - 100, gameScreenHeight / 2 - 80))
        surface.blit(text1, (gameScreenWidth / 2 - 60, gameScreenHeight / 2 - 30))

    elif winner=="O" :
        gameNotFinished = False
        surface.blit(imgWinRect, (gameScreenWidth / 2 - 150, gameScreenHeight / 2 - 130))
        surface.blit(text3, (gameScreenWidth / 2 - 100, gameScreenHeight / 2 - 80))
        surface.blit(text2, (gameScreenWidth / 2 - 60, gameScreenHeight / 2 - 30))


    elif checkBoardFull() :
        surface.blit(imgWinRect, (gameScreenWidth / 2 - 150, gameScreenHeight / 2 - 130))
        surface.blit(text6, (gameScreenWidth / 2 - imgWinRect.get_width()/2+text6
                             .get_width()/3, gameScreenHeight / 2 -imgWinRect.get_height()/2 +text6.get_height()/2))


    pygame.display.update()
def checkWin(row, col,boxUsed, drawLine):
    global winner

    if boxUsed[row][0] == boxUsed[row][1] == boxUsed[row][2]:
        if drawLine:
         surface.blit(imgHorizentalLine, (20, row*cellHeight+ cellHeight/3))
        winner = boxUsed[row][0]

    elif boxUsed[0][col] == boxUsed[1][col] == boxUsed[2][col]:
        if drawLine:
         surface.blit(imgVerticalLine, (col * cellWidth + cellHeight / 3,10))
        winner=boxUsed[1][col]

    elif boxUsed[0][0] == boxUsed[1][1] == boxUsed[2][2] == "X":
        if drawLine:
         surface.blit(imgdiagonalLeftLine, (40,30))
        winner="X"

    elif boxUsed[0][0] == boxUsed[1][1] == boxUsed[2][2] == "O":
        if drawLine:
         surface.blit(imgdiagonalLeftLine, (40,30))
        winner="O"

    elif boxUsed[2][0] == boxUsed[1][1] == boxUsed[0][2] == "X":
        if drawLine:
         surface.blit(imgdiagonalRightLine, (40,30))
        winner="X"

    elif boxUsed[2][0] == boxUsed[1][1] == boxUsed[0][2] == "O":
        if drawLine:
         surface.blit(imgdiagonalRightLine, (40, 30))
        winner="O"

    else :
        winner = " ";

    return  winner;


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

NameButtonClicked = False
while running:
    if not (chooseName):
      input_name()


    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if inputBox.collidepoint(pos):
                NameButtonClicked = True

        if event.type == pygame.QUIT:
            running = False
        pos = pygame.mouse.get_pos()

        if not (chooseName) and NameButtonClicked :
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
                chooseName =True
                gameInitializing(gameType)
                gameNotFinished = True

            elif Player2.collidepoint(pos):
                textStartDisplay = surface.blit(imgStartClicked, (625, 40))
                pygame.display.flip()
                gameType = "twoPlayers"
                chooseName =True
                gameInitializing(gameType)
                gameNotFinished = True
            elif textStartDisplay.collidepoint(pos):
                gameMode()

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

