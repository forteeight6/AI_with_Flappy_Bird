import pygame
import random
from src.utils.image_config import pygame_barrel_img
from src.class_bird import Bird
from typing import Type

"""
Objetc Barrel
"""
class Barrel:
    DISTANCIA = 200
    VELOCIDADE = 5

    def __init__(self, x):
        self.x = x
        self.altura = 0
        self.pos_topo = 0
        self.pos_base = 0
        self.CANO_TOPO = pygame.transform.flip(pygame_barrel_img(), False, True)
        self.CANO_BASE = pygame_barrel_img()
        self.passou = False
        self.definir_altura()

    def definir_altura(self) -> None:
        """
        Define height of barrel
        """
        self.altura = random.randrange(50, 450)
        self.pos_topo = self.altura - self.CANO_TOPO.get_height()
        self.pos_base = self.altura + self.DISTANCIA

    def mover(self) -> None:
        """
        Define moviment
        """
        self.x -= self.VELOCIDADE

    def desenhar(self, tela) -> None:
        """
        Draw in the window
        """
        tela.blit(self.CANO_TOPO, (self.x, self.pos_topo))
        tela.blit(self.CANO_BASE, (self.x, self.pos_base))

    def colidir(self, passaro: Type[Bird]) -> bool:
        """
        Define colision
        """
        passaro_mask = passaro.get_mask()
        topo_mask = pygame.mask.from_surface(self.CANO_TOPO)
        base_mask = pygame.mask.from_surface(self.CANO_BASE)

        distancia_topo = (self.x - passaro.x, self.pos_topo - round(passaro.y))
        distancia_base = (self.x - passaro.x, self.pos_base - round(passaro.y))

        topo_ponto = passaro_mask.overlap(topo_mask, distancia_topo)
        base_ponto = passaro_mask.overlap(base_mask, distancia_base)

        if base_ponto or topo_ponto:
            return True
        else:
            return False