import pygame
pygame.init()

screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("Tic-tac-toe")

Black = (0,0,0)
White = (255,255,255)
Red = (255,0,0)
Green = (0,255,0)
Blue = (0,0,255)



run = True
while run:

    screen.fill(White)





    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            



    pygame.display.update()






pygame.quit()