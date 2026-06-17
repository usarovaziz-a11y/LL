import pygame
import random

pygame.init()

#СОЗДАНИЕ ОКНА
width, height = 600, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Угадай цвет")

COLOR = {
    "RED": (255, 0, 0),
    "BLUE": (0, 0, 255),
    "GREEN": (0, 255, 0),
    "YELLOW": (255, 255, 0),
    "BLACK": (0, 0, 0),
    "SDF": (255,255,255),
    "TYI": (255,0,0),
    "DCD": (0,255,0),
    "HGF": (0,0,255),
    "NBV": (255,255,0),
    "YH": (255,0,255),
    "KJN": (0,255,255),

}

color_keys = list(COLOR.keys())
current_color = random.choice(color_keys)
while True:
    for event in pygame.event.get():
        if event. type == pygame.QUIT:
            pygame.quit ()
            quit()
        if event. type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                current_color = "RED"
            elif event. key == pygame.K_g:
                current_color = "GREEN"
            elif event.key == pygame.K_b:
                current_color = "BLUE"
            elif event.key == pygame.K_y:
                current_color = "YELLOW"
            elif event. key == pygame.K_q:
                current_color = "BLACK"
            elif event. key == pygame.K_z:
                current_color = "SDF"
            elif event.key == pygame.K_x:
                current_color = "TYI"
            elif event.key == pygame.K_c:
                current_color = "DCD"
            elif event.key == pygame.K_v:
                current_color = "HGF"
            elif event.key == pygame.K_b:
                current_color = "NBV"
            elif event.key == pygame.K_n:
                current_color = "YH"
            elif event.key == pygame.K_m:
                current_color = "KJN"



    screen.fill(COLOR[current_color])
    pygame.display.flip()



