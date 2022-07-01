import pygame

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
                bird.spring()

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

def remove_barrel(barrel_position):
    if barrel_position < 0:
        return True

def reset_barrel_list_for_removing(remove_barrel_list):
    for item in remove_barrel_list:
        remove_barrel_list.remove(item)
    return remove_barrel_list