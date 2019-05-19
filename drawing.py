# Author:   Max Martinez Ruts
# Creation: 2019

import numpy as np
import pygame

# Convert coordinates form cartesian to screen coordinates (used to draw in pygame screen)
def cartesian_to_screen(car_pos):
    factor = 1
    screen_pos = np.array([center[0]*factor+car_pos[0],center[1]*factor+car_pos[1]])/factor
    screen_pos = screen_pos.astype(int)
    return screen_pos

def draw(bd):
    pygame.event.get()
    screen.fill((0, 0, 0))
    for i in range(0, 8):
        for j in range(0, 8):

            if (i + j) % 2 == 0:
                pygame.draw.rect(screen, boards_squares[i, j][1], boards_squares[i, j][0])
            else:
                pygame.draw.rect(screen, boards_squares[i, j][1], boards_squares[i, j][0])
    for i in range(0, 8):
        for j in range(0, 8):
            piece = bd[i, j]
            if piece != None:
                screen.blit(pygame.transform.scale(pygame.image.load(piece.image), (80, 80)),
                            cartesian_to_screen(grid_distribution[(i, j)] - np.array([40, 40])))
    pygame.display.flip()

# Screen parameters
width = 800
height = 800
center = np.array([width/2, height/2])
screen = pygame.display.set_mode((width, height))

# Colors
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
yellow = (255,255, 0)
black = (0,0, 0)
black_soft = (181,136,96)
white_soft = (240,217,178)

pos_distribution = np.linspace(-350,350,8)
grid_distribution = np.zeros((8,8,2))
for i in range(0,8):
    for j in range(0,8):
        grid_distribution[j,i] = np.array([pos_distribution[i],pos_distribution[j]])

boards_squares = np.ndarray((8,8), dtype=np.object)
for i in range(0, 8):
    for j in range(0, 8):
        if (i + j) % 2 == 0:
            boards_squares[j, i] = (pygame.Rect(cartesian_to_screen(grid_distribution[j, i])[0] - 50,
                                                cartesian_to_screen(grid_distribution[j, i])[1] - 50, 100, 100),
                                    white_soft)
        else:
            boards_squares[j, i] = (pygame.Rect(cartesian_to_screen(grid_distribution[j, i])[0] - 50,
                                                cartesian_to_screen(grid_distribution[j, i])[1] - 50, 100, 100),
                                    black_soft)