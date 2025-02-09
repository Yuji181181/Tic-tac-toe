import pygame

pygame.init()

## ウィンドウの設定
screen = pygame.display.set_mode((600, 600))

pygame.display.set_caption("タイトル")

## 色の設定
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# メインループ-------------------------------------
run = True
while run:

    # 画面の背景色
    screen.fill(WHITE)

    # イベント処理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # 画面の更新
    pygame.display.update()

# -------------------------------------------------

pygame.quit()
