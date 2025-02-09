import pygame

pygame.init()

## ウィンドウの設定
screen = pygame.display.set_mode((600, 600))

## タイトルの設定
pygame.display.set_caption("タイトル")

## 色の設定
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

## 盤面の設定
board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  # 0:空白、1:◯、-1:✕


# メインループ-------------------------------------------------------------------------
run = True
while run:

    # 画面の描画
    screen.fill(WHITE)
    for i in range(1, 3):
        pygame.draw.line(screen, BLACK, (0, i * 200), (600, i * 200), 5)
        pygame.draw.line(screen, BLACK, (i * 200, 0), (i * 200, 600), 5)

    # quitイベント
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # 画面の更新
    pygame.display.update()

# ------------------------------------------------------------------------------------

pygame.quit()
