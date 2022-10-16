import pygame

from pygame.locals import *

from tkinter import *
from tkinter import messagebox

from pygame.time import Clock

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
clickState = "X"

color = "red"

imgX = pygame.image.load("D:\\France\\Programmation\\pyhton\\Images\\x-png-22.png")
imgO = pygame.image.load("D:\\France\\Programmation\\pyhton\\Images\\R.png")

imgX = pygame.transform.scale(imgX, (150, 150))
imgO = pygame.transform.scale(imgO, (150, 150))

rect = pygame.draw.rect(surface, "white", pygame.Rect((screenWidth - 210, screenHeight - 490, menuWidth, menuHeight)))
font = pygame.font.Font('freesansbold.ttf', 20)

textStart = font.render('Start', True, "black", "red")
textRestart = font.render('Restart', True, "black", "red")
textQuit = font.render('Quit', True, "black", "red")

textStartDisplay = surface.blit(textStart, (654, 20))
textRestartDisplay = surface.blit(textRestart, (654, 50))
textQuitDisplay = surface.blit(textQuit, (654, 80))

pygame.display.flip()

boxUsed = [["", "", ""], ["", "", ""], ["", "", ""]]


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


def checkWin(row, col):
    global running
    if boxUsed[row][0] == boxUsed[row][1] == boxUsed[row][2]:
        if not messagebox.askretrycancel('Restart', 'Do you want to start again ?'):
            running = False
    elif boxUsed[0][col] == boxUsed[1][col] == boxUsed[2][col]:
        if not messagebox.askretrycancel('Restart', 'Do you want to start again ?'):
            running = False
    elif boxUsed[0][0] == boxUsed[1][1] == boxUsed[2][2] == "X":
        if not messagebox.askretrycancel('Restart', 'Do you want to start again ?'):
            running = False
    elif boxUsed[0][0] == boxUsed[1][1] == boxUsed[2][2] == "O":
        if not messagebox.askretrycancel('Restart', 'Do you want to start again ?'):
            running = False
    elif boxUsed[2][0] == boxUsed[1][1] == boxUsed[0][2] == "X":
        if not messagebox.askretrycancel('Restart', 'Do you want to start again ?'):
            running = False
    elif boxUsed[2][0] == boxUsed[1][1] == boxUsed[0][2] == "O":
        if not messagebox.askretrycancel('Restart', 'Do you want to start again ?'):
            running = False


def findColAndRow(x, y):
    if x < cellWidth:
        col = 0
    elif x < cellWidth * 2:
        col = 1
    else:
        col = 2

    if y < cellHeight:
        row = 0
    elif y < cellHeight * 2:
        row = 1
    else:
        row = 2

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
        mouseClickDetection()
    clock = Clock()
    clock.tick(25)
