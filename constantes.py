import pygame
from pygame import font

pygame.init()

MAIN_LOOP = True
HOME_LOOP = True
GAME_LOOP = True

NBR_SPRITE = 15
SPRITE_SIZE = 30
SCREEN_SIZE = ((NBR_SPRITE ) * SPRITE_SIZE, (NBR_SPRITE ) * SPRITE_SIZE)

window = pygame.display.set_mode(SCREEN_SIZE)
TITLE_WINDOW = "Help Mac To Escape"
ICONE = pygame.image.load("images/Gardien.png").convert_alpha()

HOME = pygame.image.load("images/acceuil.png").convert()

WELCOME = pygame.image.load("images/welkom.png")

PICKUP = pygame.image.load("images/pickup.png").convert_alpha()
GAMEOVER = pygame.image.load("images/youloose.jpg").convert()

WIN = pygame.image.load("images/youwin.jpg").convert()

Grey_GROUND = pygame.image.load("images/background.jpg").convert()
BACKGROUND = pygame.image.load("images/fond.jpg").convert()

WALL = pygame.image.load("images/mur.png").convert()
ARRIVAL = pygame.image.load("images/Gardien.png").convert_alpha()

TUBE = pygame.image.load("images/tube_plastique.png").convert_alpha()
ETHER = pygame.image.load("images/ether.png").convert_alpha()
SYRINGE = pygame.image.load("images/seringue.png").convert_alpha()
AIGUILLE = pygame.image.load("images/aiguille.png").convert_alpha()
FONT = font.Font(None, 35)
TEXT_ITEM = FONT.render(
        "GOT IT",
        True,
        (200, 200, 200))

MG = pygame.image.load("images/MacGyver.png").convert_alpha()

FILE = ""

"""soundtrack and jingle= pygame.mixer.sound("sound/soundtrack.wav)"""
JINGLE = pygame.mixer.Sound("sound/jinglemac.mp3")
