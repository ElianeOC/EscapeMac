from game import Player, Map
from constantes import ICONE, TITLE_WINDOW, SCREEN_SIZE, HOME,\
    Grey_GROUND, window, BACKGROUND, WELCOME, FILE, WIN, GAMEOVER

from pygame.locals import K_ESCAPE, K_RETURN, K_RIGHT, K_LEFT, K_UP, K_DOWN
from pygame import transform, display, event, font, QUIT, KEYDOWN, time
display.set_icon(ICONE)

display.set_caption(TITLE_WINDOW)

display.set_mode(SCREEN_SIZE)

SCORE = 0
MAIN_LOOP = True
while MAIN_LOOP:
    window.blit(Grey_GROUND, (0, 0))
    window.blit(transform.scale(HOME, SCREEN_SIZE), (0, 0))
    FONT = font.Font(None, 30)
    TEXT_SCORE = FONT.render(
        f"SCORE is {SCORE}\n Press Enter To Play",
        True,
        (200, 200, 200))
    window.blit(TEXT_SCORE, (15, 370))
    display.flip()

    HOME_LOOP = True
    while HOME_LOOP:
        for e in event.get():
            if e.type == QUIT or (e.type == KEYDOWN and e.key == K_ESCAPE):
                MAIN_LOOP = False
                HOME_LOOP = False
                GAME_LOOP = False
                display.flip()

            if e.type == KEYDOWN and e.key == K_RETURN:
                window.blit(transform.scale(BACKGROUND, SCREEN_SIZE), (0, 0))
                window.blit(transform.scale(WELCOME, SCREEN_SIZE), (0, 0))
                display.flip()

                HOME_LOOP = False
                GAME_LOOP = True
                window.blit(transform.scale(BACKGROUND, SCREEN_SIZE), (0, 0))
                labyrinth = Map(FILE)
                labyrinth.generate()
                labyrinth.display(window)
                display.flip()
                Macgyver = Player(labyrinth)
                display.flip()
                while GAME_LOOP:
                    time.Clock().tick(30)
                    for e in event.get():
                        if e.type == QUIT:
                            MAIN_LOOP = False
                            GAME_LOOP = False
                        if e.type == KEYDOWN:
                            if e.key == K_RIGHT:
                                Macgyver.move('right')
                            if e.key == K_LEFT:
                                Macgyver.move('left')
                            if e.key == K_UP:
                                Macgyver.move('up')
                            if e.key == K_DOWN:
                                Macgyver.move('bottom')
                            if labyrinth.grid[Macgyver.sprite_y][Macgyver.sprite_x] == 'G':
                                if Macgyver.counter == labyrinth.position:
                                    window.blit(transform.scale(WIN, SCREEN_SIZE), (0, 0))
                                    FONT = font.Font(None, 50)
                                    TEXT_WIN = FONT.render(
                                        "Proud of you",
                                        True,
                                        (200, 200, 200))
                                    window.blit(TEXT_WIN, (15, 15))
                                    display.flip()
                                    SCORE += 1
                                    GAME_LOOP = False
                                    HOME_LOOP = False
                                    display.flip()

                                else:
                                    window.blit(transform.scale(GAMEOVER, SCREEN_SIZE), (0, 0))
                                    FONT = font.Font(None, 50)
                                    TEXT_LOOSE = FONT.render(
                                        "Try Again Buddy",
                                        True,
                                        (200, 200, 200))
                                    window.blit(TEXT_LOOSE, (15, 370))
                                    display.flip()
                                    SCORE -= 1
                                    GAME_LOOP = False
                                    HOME_LOOP = False
                                    break
