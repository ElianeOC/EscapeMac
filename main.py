from Game import *

from pygame.locals import *
from pygame import transform
pygame.display.set_icon(ICONE)

pygame.display.set_caption(TITLE_WINDOW)

pygame.display.set_mode(SCREEN_SIZE)

MAIN_LOOP = True
while MAIN_LOOP:
    window.blit(Grey_GROUND, (0, 0))
    window.blit(transform.scale(HOME, SCREEN_SIZE), (0, 0))
    pygame.display.flip()

    # try to remove HOME_LOOP
    HOME_LOOP = True
    while HOME_LOOP:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                MAIN_LOOP = False
                HOME_LOOP = False
                GAME_LOOP = False
                print(" BYE BUDDY")
                pygame.display.flip()

            if event.type == KEYDOWN and event.key == K_RETURN:
                # JINGLE.stop()
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
                        pygame.display.flip()
