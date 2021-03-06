import pygame
from src.utils.image_config import pygame_floor_img

"""
Object Floor
"""
class Floor:
    VELOCIDADE = 5
    LARGURA = pygame_floor_img(op=True)
    IMAGEM = pygame_floor_img()

    def __init__(self, y):
        self.y = y
        self.x1 = 0
        self.x2 = self.LARGURA

    def mover(self) -> None:
        """
        Movement of the Floor
        """
        self.x1 -= self.VELOCIDADE
        self.x2 -= self.VELOCIDADE

        if self.x1 + self.LARGURA < 0:
            self.x1 = self.x2 + self.LARGURA
        if self.x2 + self.LARGURA < 0:
            self.x2 = self.x1 + self.LARGURA

    def desenhar(self, tela) -> None:
        """
        Draw the floor
        """
        tela.blit(self.IMAGEM, (self.x1, self.y))
        tela.blit(self.IMAGEM, (self.x2, self.y))