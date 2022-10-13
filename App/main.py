import pygame

from pygame.locals import *
from pygame.time import Clock

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

rect = pygame.draw.rect(surface, "white", pygame.Rect((screenWidth - 210, screenHeight - 490, 200, 480)))
font = pygame.font.Font('freesansbold.ttf', 20)

textStart = font.render('Start', True, "black", "red")
textRestart = font.render('Restart', True, "black", "red")
textQuit = font.render('Quit', True, "black", "red")

textStartDisplay = surface.blit(textStart, (654, 20))
textRestartDisplay = surface.blit(textRestart, (654, 50))
textQuitDisplay = surface.blit(textQuit, (654, 80))

pygame.display.flip()




def XorO(cellY, cellX):
    global clickState
    if not clickState:
        surface.blit(imgX, (cellX, cellY))
        clickState = True
    else:
        surface.blit(imgO, (cellX, cellY))
        clickState = False

    pygame.display.update()

clickState = False

def start():
    global clickState

    if event.type == pygame.MOUSEBUTTONDOWN:
        (x, y) = pygame.mouse.get_pos()
        if cell1_1X + cellWidth > x > cell1_1X and cell1_1Y + cellHeight > y > cell1_1Y:
            XorO(cell1_1Y, cell1_1X)
        elif cell1_2X + cellWidth > x > cell1_2X and cell1_2Y + cellHeight > y > cell1_2Y:
            XorO(cell1_2Y, cell1_2X)
        if cell1_3X + cellWidth > x > cell1_3X and cell1_3Y + cellHeight > y > cell1_3Y:
            XorO(cell1_3Y, cell1_3X)
        if cell2_1X + cellWidth > x > cell2_1X and cell2_1Y + cellHeight > y > cell2_1Y:
            XorO(cell2_1Y, cell2_1X)
        if cell2_2X + cellWidth > x > cell2_2X and cell2_2Y + cellHeight > y > cell2_2Y:
            XorO(cell2_2Y, cell2_2X)
        if cell2_3X + cellWidth > x > cell2_3X and cell2_3Y + cellHeight > y > cell2_3Y:
            XorO(cell2_3Y, cell2_3X)
        if cell3_1X + cellWidth > x > cell3_1X and cell3_1Y + cellHeight > y > cell3_1Y:
            XorO(cell3_1Y, cell3_1X)
        if cell3_2X + cellWidth > x > cell3_2X and cell3_2Y + cellHeight > y > cell3_2Y:
            XorO(cell3_2Y, cell3_2X)
        if cell3_3X + cellWidth > x > cell3_3X and cell3_3Y + cellHeight > y > cell3_3Y:
            XorO(cell3_3Y, cell3_3X)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if textQuitDisplay.collidepoint(pos):
               running = False
        start()
    clock = Clock()
    clock.tick(25)

