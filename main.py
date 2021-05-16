from game import *

from pygame.locals import *
from pygame import transform
pygame.display.set_icon(ICONE)

pygame.display.set_caption(TITLE_WINDOW)

pygame.display.set_mode(SCREEN_SIZE)

SCORE = 0
MAIN_LOOP = True
while MAIN_LOOP:
    print("mainloop")
    window.blit(Grey_GROUND, (0, 0))
    window.blit(transform.scale(HOME, SCREEN_SIZE), (0, 0))
    FONT = font.Font(None, 50)
    TEXT_SCORE = FONT.render(
        f"SCORE is {SCORE}\n Press Enter To Play",
        True,
        (200, 200, 200))
    window.blit(TEXT_SCORE, (15, 370))
    pygame.display.flip()

    # try to remove HOME_LOOP
    HOME_LOOP = True
    while HOME_LOOP:
        print("homeloop")
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                MAIN_LOOP = False
                HOME_LOOP = False
                GAME_LOOP = False
                print(" BYE BUDDY")
                pygame.display.flip()

            if event.type == KEYDOWN and event.key == K_RETURN:
                window.blit(transform.scale(BACKGROUND, SCREEN_SIZE), (0, 0))
                window.blit(transform.scale(WELCOME, SCREEN_SIZE), (0, 0))
                pygame.display.flip()

                HOME_LOOP = False
                GAME_LOOP = True
                window.blit(transform.scale(BACKGROUND, SCREEN_SIZE), (0, 0))
                labyrinth = Map(FILE)
                labyrinth.generate()
                labyrinth.display(window)
                pygame.display.flip()
                Macgyver = Player(labyrinth)
                pygame.display.flip()
                while GAME_LOOP:
                    pygame.time.Clock().tick(30)
                    for event in pygame.event.get():
                        if event.type == QUIT:
                            print("Bye Bye Buddy")
                            MAIN_LOOP = False
                            GAME_LOOP = False
                        if event.type == KEYDOWN:
                            if event.key == K_RIGHT:
                                Macgyver.move('right')
                                print("move right")
                            if event.key == K_LEFT:
                                Macgyver.move('left')
                                print("move left")
                            if event.key == K_UP:
                                Macgyver.move('up')
                                print('move Up')
                            if event.key == K_DOWN:
                                Macgyver.move('bottom')
                                print('move down')
                                print(f"counter {Macgyver.counter}")
                            if labyrinth.grid[Macgyver.sprite_y][Macgyver.sprite_x] == 'G':
                                print("Face the boss")
                                print(Macgyver.counter)
                                if Macgyver.counter == labyrinth.position:
                                    window.blit(transform.scale(WIN, SCREEN_SIZE), (0, 0))
                                    FONT = font.Font(None, 50)
                                    TEXT_WIN = FONT.render(
                                        "Proud of you",
                                        True,
                                        (200, 200, 200))
                                    window.blit(TEXT_WIN, (15, 15))
                                    pygame.display.flip()
                                    print("You Win")
                                    SCORE += 1
                                    GAME_LOOP = False
                                    HOME_LOOP = False
                                    pygame.display.flip()

                                else:
                                    window.blit(transform.scale(GAMEOVER, SCREEN_SIZE), (0, 0))
                                    FONT = font.Font(None, 35)
                                    TEXT_LOOSE = FONT.render(
                                        "Try Again Buddy",
                                        True,
                                        (200, 200, 200))
                                    window.blit(TEXT_LOOSE, (15, 370))
                                    pygame.display.flip()
                                    print("You Loose")
                                    SCORE -= 1
                                    GAME_LOOP = False
                                    HOME_LOOP = False
                                    break
