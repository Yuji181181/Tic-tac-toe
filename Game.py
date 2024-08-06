import pygame
pygame.init()

screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("Tic-tac-toe")

Black = (0,0,0)
White = (255,255,255)
Red = (255,0,0)
Green = (0,255,0)
Blue = (0,0,255)

board = [
    [0,0,0],
    [0,0,0],
    [0,0,0]]
# 0:空白、1:◯、-1:✕


def draw_board():
    for row_index,row in enumerate(board):
        for col_index,col in enumerate(row):
            if col == 1:
                pygame.draw.circle(screen,Red,(col_index*200+100,row_index*200+100),80,5)
            elif col == -1:
                pygame.draw.line(screen,Blue,(col_index*200+20,row_index*200+20),(col_index*200+180,row_index*200+180),5)
                pygame.draw.line(screen,Blue,(col_index*200+180,row_index*200+20),(col_index*200+20,row_index*200+180),5)






run = True
while run:

    screen.fill(White)
    for i in range(1,3):
        pygame.draw.line(screen,Black,(0,i*200),(600,i*200),5)
        pygame.draw.line(screen,Black,(i*200,0),(i*200,600),5)

    draw_board()
    
    mx,my = pygame.mouse.get_pos()
    x = mx//200
    y = my//200
    


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            


    pygame.display.update()






pygame.quit()

