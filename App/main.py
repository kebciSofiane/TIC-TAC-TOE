import pygame

pygame.init()

surface = pygame.display.set_mode((800, 500))
pygame.display.set_caption("Tic-Tac-Toe")

running = True

color = "red"
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    rect = pygame.draw.rect(surface, "white", pygame.Rect((590, 10, 200, 480)))
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
