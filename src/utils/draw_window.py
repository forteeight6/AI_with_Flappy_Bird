import pygame
from conf.config import *
from src.utils.font_config import font
from src.utils.image_config import background_img

def desenhar_tela(tela, passaros, canos, chao, pontos):
    tela.blit(background_img(), (0, 0))
    for passaro in passaros:
        passaro.desenhar(tela)
    for cano in canos:
        cano.desenhar(tela)

    texto = font().render(f"Pontuação: {pontos}", 1, (255, 255, 255))
    tela.blit(texto, (width_window - 10 - texto.get_width(), 10))
    chao.desenhar(tela)
    pygame.display.update()