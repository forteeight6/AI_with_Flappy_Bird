import pygame
from src.utils.utils_for_game_fps import (
    pygame_event, pygame_quit, pygame_keys, create_birds,
    create_barrels, bird_colliding, bird_not_colliding,
    remove_barrel, reset_barrel_list_for_removing
)
from src.utils.draw_window import draw_window

def fps(fps, Barrel, **kwargs):
    running = True
    while running:
        kwargs["watch"].tick(fps)

        # interação com o usuário
        for event in pygame_event():
            running = pygame_quit(event)

            pygame_keys(event, kwargs["birds"])

        # Move to things
        for bird in kwargs["birds"]:
            bird.move()
        kwargs["floor"].mover()

        remove_barrel_list = []
        add_barrel = False
        barrels = create_barrels(
            kwargs["barrels"],
            add_barrel
        )

        for barrel in kwargs["barrels"]:
            birds = create_birds(
                kwargs["birds"]
            )
            for index, bird in birds:

                if bird_colliding(barrel=barrel, bird=bird):
                    kwargs["birds"].pop(index)

                try:
                    barrel.passou, add_barrel = bird_not_colliding(
                        barrel=barrel, bird=bird
                    )
                except:
                    pass

            barrel.mover()
            eixo_x = barrel.x
            roof_barrel = barrel.CANO_TOPO.get_height() #
            barrel_position = eixo_x + roof_barrel
            if remove_barrel(barrel_position):
                remove_barrel_list.append(barrel)

        if add_barrel:
            kwargs["points"] += 1
            kwargs["barrels"].append(Barrel(600))

        # Reset remove_barrel_list
        remove_barrel_list = reset_barrel_list_for_removing(remove_barrel_list)

        # ADICIONAR COLISÃO COM O CHAO E COM O CEU AQUI
        birds = create_birds(
            kwargs["birds"]
        )
        for index, bird in birds:
            print(kwargs["floor"].y)
            
            bird_height = bird.y + bird.imagem.get_height()
            hit_the_floor = True if bird_height > kwargs["floor"].y else False
            limit_area = True if bird.y < 0 else False

            if limit_area | hit_the_floor:
                kwargs["birds"].pop(index)


        draw_window(
            kwargs["window"], 
            kwargs["birds"], 
            kwargs["barrels"], 
            kwargs["floor"], 
            kwargs["points"]
        )