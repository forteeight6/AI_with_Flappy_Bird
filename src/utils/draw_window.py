import pygame
from conf.config import *
from src.utils.font_config import font
from src.utils.image_config import background_img

def draw_window(window, birds, barrels, floor, points):
    window.blit(background_img(), (0, 0))
    for passaro in birds:
        passaro.draw(window)
    for cano in barrels:
        cano.desenhar(window)

    texto = font().render(f"Pontuação: {points}", 1, (255, 255, 255))
    window.blit(texto, (width_window - 10 - texto.get_width(), 10))
    floor.desenhar(window)
    pygame.display.update()