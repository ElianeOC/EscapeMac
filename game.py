from pygame import transform
from constantes import*
from random import *


class Map:
    """define the labyritnh with my file.txt wich contains the maze.
    i will generate the structure and then display it """

    def __init__(self, file):
        self.file = file
        self.grid = []
        self.position = set()

    def generate(self):
        """generate the structure from the file.txt"""
        frame = []
        with open("my_map", "r") as file:
            for line in file:
                line = line.strip()
                frame.append(list(line))
                self.grid = frame

    def display(self, window):
        """display  wall as w and guardien as a"""
        ELMENT = {'e', 's', 't'}
        print(ELMENT)
        num_line = 0
        for line in self.grid:
            num_sprite = 0
            for sprite in line:
                x = num_sprite * SPRITE_SIZE
                y = num_line * SPRITE_SIZE
                if sprite == "w":
                    window.blit(WALL, (x, y))
                elif sprite == "a":
                    window.blit(transform.scale(ARRIVAL, (SPRITE_SIZE, SPRITE_SIZE)), (x, y))
                else:
                    if ELMENT != set():
                        N = randint(1, 12)
                        print(N)
                        my_list = list(ELMENT)
                        first_element = my_list[0]
                        if N == 1:
                            if first_element == "e":
                                window.blit(transform.scale(ETHER, (SPRITE_SIZE, SPRITE_SIZE)), (x, y))
                            if first_element == "s":
                                window.blit(transform.scale(SYRINGE, (SPRITE_SIZE, SPRITE_SIZE)), (x, y))
                            if first_element == "t":
                                window.blit(transform.scale(TUBE, (SPRITE_SIZE, SPRITE_SIZE)), (x, y))
                            self.position.add((num_line, num_sprite))
                            ELMENT.remove(first_element)
                            print(f"self.position is {self.position}")
                pygame.display.flip()
                num_sprite += 1
            num_line += 1
            pygame.display.flip()
        ELMENT = {"e", "s", "t"}


class Player:
    def __init__(self, labyrinth):
        self.x = 0
        self.y = 0
        self.sprite_x = 0
        self.sprite_y = 0
        self.counter = set()
        self.labyrinth = labyrinth
        window.blit(transform.scale(MG, (SPRITE_SIZE, SPRITE_SIZE)), (self.x, self.y))
        pygame.display.flip()

    def move(self, direction):
        if direction == "right":
            print(self.sprite_y, self.sprite_x + 1)
            if self.sprite_x < NBR_SPRITE:
                if self.labyrinth.grid[self.sprite_y][self.sprite_x+1] != "w":
                    if(self.sprite_y, self.sprite_x + 1) in self.labyrinth.position:
                        self.counter.add((self.sprite_y, self.sprite_x + 1))
                    window.blit(transform.scale(BACKGROUND, (SPRITE_SIZE, SPRITE_SIZE)), (self.x, self.y))
                    self.sprite_x += 1
                    self.x = self.sprite_x * SPRITE_SIZE
                    window.blit(transform.scale(MG, (SPRITE_SIZE, SPRITE_SIZE)), (self.x, self.y))
                    pygame.display.flip()
        if direction == "left":
            if self.sprite_x > 0:
                if self.labyrinth.grid[self.sprite_y][self.sprite_x-1] != "w":
                    if (self.sprite_y, self.sprite_x - 1) in self.labyrinth.position:
                        print("_______________")
                        self.counter.add((self.sprite_y, self.sprite_x - 1))

                    window.blit(transform.scale(BACKGROUND, (SPRITE_SIZE, SPRITE_SIZE)), (self.x, self.y))
                    self.sprite_x -= 1
                    self.x = self.sprite_x * SPRITE_SIZE
                    window.blit(transform.scale(MG, (SPRITE_SIZE, SPRITE_SIZE)), (self.x, self.y))
                    pygame.display.flip()

        if direction == "bottom":
            if self.sprite_y < NBR_SPRITE:
                if self.labyrinth.grid[self.sprite_y+1][self.sprite_x] != "w":
                    if (self.sprite_y + 1, self.sprite_x) in self.labyrinth.position:
                        print("+++++++++++++")
                        self.counter.add((self.sprite_y + 1, self.sprite_x))
                    window.blit(transform.scale(BACKGROUND, (SPRITE_SIZE, SPRITE_SIZE)), (self.x, self.y))
                    self.sprite_y += 1
                    self.y = self.sprite_y * SPRITE_SIZE
                    window.blit(transform.scale(MG, (SPRITE_SIZE, SPRITE_SIZE)), (self.x, self.y))
                    pygame.display.flip()
        if direction == "up":
            if self.sprite_y > 0:
                if self.labyrinth.grid[self.sprite_y-1][self.sprite_x] != "w":
                    if (self.sprite_y - 1, self.sprite_x) in self.labyrinth.position:
                        print("========")
                        self.counter.add((self.sprite_y - 1, self.sprite_x))
                    window.blit(transform.scale(BACKGROUND, (SPRITE_SIZE, SPRITE_SIZE)), (self.x, self.y))
                    self.sprite_y -= 1
                    self.y = self.sprite_y * SPRITE_SIZE
                    window.blit(transform.scale(MG, (SPRITE_SIZE, SPRITE_SIZE)), (self.x, self.y))
                    pygame.display.flip()
