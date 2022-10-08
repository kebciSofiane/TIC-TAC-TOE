import pygame

pygame.init()

surface = pygame.display.set_mode((800, 500))
pygame.display.set_caption("Tic-Tac-Toe")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


