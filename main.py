import pygame
from typing import Type
from conf.config import *
from src.class_bird import Bird
from src.class_barrel import Barrel
from src.class_floor import Floor
from src.utils.game_fps import fps


def play(Bird: Type[Bird], Floor: Type[Floor], Barrel: Type[Barrel]) -> None:
    # LIST FORMAT BECAUSE OF AI
    birds = [Bird(230, 350)]
    floor = Floor(730)

    barrels = [Barrel(700)]
    window = pygame.display.set_mode((width_window, height_window))
    # pontos = 0
    watch = pygame.time.Clock()

    fps(
        fps=30,
        Barrel=Barrel,
        points=0,
        birds=birds,
        floor=floor,
        barrels=barrels,
        window=window,
        watch=watch,
    )


def main():
    play(Bird, Floor, Barrel)

if __name__ == '__main__':
    main()
