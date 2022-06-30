import pygame
from conf.config import *
from src.class_bird import Passaro
from src.class_barrel import Cano
from src.class_floor import Chao
from src.utils.draw_window import desenhar_tela

def pygame_event():
    for event in pygame.event.get():
        yield event

def pygame_quit(event):
    if event.type == pygame.QUIT:
        pygame.quit()
        quit()
        return False
    return True

def pygame_keys(event, birds):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
            # LIST FORMAT BECAUSE OF AI
            for bird in birds:
                bird.pular()

def create_birds(birds):
    for index, bird in enumerate(birds):
        yield (index, bird)

def create_barrels(barrels, add=False): 
    for barrel in barrels:
        yield barrel

def bird_colliding(**kwargs):
    if kwargs["barrel"].colidir(kwargs["bird"]):
        return True

def bird_not_colliding(**kwargs):
    passou = kwargs["barrel"].passou
    eixo_x_of_bird = kwargs["bird"].x
    eixo_x_of_barrel = kwargs["barrel"].x

    if not passou and eixo_x_of_bird > eixo_x_of_barrel:
        kwargs["barrel"].passou = True
        add_barrel = True

        return kwargs["barrel"].passou, add_barrel
    else:
        return False, False

def remove_barrel(barrel_position):
    if barrel_position < 0:
        return True

def reset_barrel_list_for_removing(remove_barrel_list):
    for item in remove_barrel_list:
        remove_barrel_list.remove(item)
    return remove_barrel_list

def pygame_fps(fps, Barrel, **kwargs):
    running = True
    while running:
        kwargs["watch"].tick(fps)

        # interação com o usuário
        for event in pygame_event():
            running = pygame_quit(event)

            pygame_keys(event, kwargs["birds"])

        # Move to things
        for bird in kwargs["birds"]:
            bird.mover()
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

                barrel.passou, add_barrel =bird_not_colliding(
                    barrel=barrel, bird=bird
                )

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

        for index, bird in birds:
            eixo_y = bird.eixo_y
            height = bird.img.get_height()
            bird_position = eixo_y + height
            area_limit = eixo_y < 0
            hit_on_floor = eixo_y < 0

        desenhar_tela(
            kwargs["window"], 
            kwargs["birds"], 
            kwargs["barrels"], 
            kwargs["floor"], 
            kwargs["points"]
        )

# Insert in main
def play(Bird, Floor, Barrel):
    # LIST FORMAT BECAUSE OF AI
    birds = [Bird(230, 350)]
    floor = Floor(730)

    barrels = [Barrel(700)]
    window = pygame.display.set_mode((width_window, height_window))
    # pontos = 0
    watch = pygame.time.Clock()

    pygame_fps(
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
    play(Passaro, Chao, Cano)

if __name__ == '__main__':
    main()
