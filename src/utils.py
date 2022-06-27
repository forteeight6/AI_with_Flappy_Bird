import pygame
import os
import random


def pygame_overlap(obj_pygame, args=(a, b)):
	return obj_pygame.overlap(eval(a), eval(b))

def pygame_mask(obj_pygame):
	return pygame.mask.from_surface(obj_pygame)

def pygame_define_height(**kwargs):
	height = random.randrange(50, 450)
	roof_position = height - kwargs['roof_position'].get_height()
	floor_position = height + kwargs['distance']
	return height, roof_position, floor_position


def pygame_flip_image(img):
	return pygame.transform.flip(img, False, True)

# config barrel_img
def pygame_barrel_img():
	directory = os.path.join('assets', 'pipe.png')
	barrel_img = pygame.image.load(directory)
	barrel_img = pygame.transform.scale2x(barrel_img)
	return barrel_img

# config floor_img
def pygame_floor_img(op=False):
	directory = os.path.join('assets', 'base.png')
	floor_img = pygame.image.load(directory)
	floor_img = pygame.transform.scale2x(floor_img)
	if op:
		return floor_img.get_width()
	else:
		return floor_img
		
# config backgrounf_img
def background_img():
	directory = os.path.join('assets', 'bg.png')
	background_img = pygame.image.load(directory)
	background_img = pygame.image.transform.scale2x(background_img)
	return background_img


# config bird_img_one
def bird_img_one():
	directory = os.path.join('assets', 'bird1.png')
	bird_img_one = pygame.image.load(directory)
	bird_img_one = pygame.transform.scale2x(bird_img_one)
	return bird_img_one

# config bird_img_two
def bird_img_two():
	directory = os.path.join('assets', 'bird2.png')
	bird_img_two = pygame.image.load(directory)
	bird_img_two = pygame.transform.scale2x(bird_img_two)
	return bird_img_two

# config bird_img_three
def bird_img_three():
	directory = os.path.join('assets', 'bird3.png')
	bird_img_three = pygame.image.load(directory)
	bird_img_three = pygame.transform.scale2x(bird_img_three)
	return bird_img_three

def bird_pictures():
	pictures = [
		bird_img_one(), 
		bird_img_two(), 
		bird_img_three()
	]
	return pictures

# config font
def font():
	pygame.font.init()
	font_points = pygame.font.SysFont('arial', 50)
	return font_points

def width_of_window():
	windows_width = 500
	return windows_width

def height_of_window():
	windows_height = 800
	return windows_height

def draw_window(**kwargs):
	"""
		Entries: window
				 birds
				 barrels
				 floor
				 points
	"""
	kwargs["window"].blit(background_img(), (0, 0))
	for bird in kwargs["birds"]:
		bird.draw(kwargs["window"])
	for barrel in kwargs["barrels"]:
		barrel.draw(kwargs["window"])

	text = f"Points: {kwargs['points']}"
	text = font().render(
		text, 1, (255, 255, 255)
	)

	text_width = text.get_width()
	config_blit = windows_width() - 10 - text_width
	kwargs["window"].blit(
		text, config_blit, 10
	)
	kwargs["floor"].draw(kwargs["window"])
	pygame.display.update()


def pygame_set_mode(width_of_window, height_of_window):
	return pygame.display.set_mode((width_of_window, height_of_window))

def pygame_o_clock():
	return pygame.time.Clock()


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
	if kwargs["barrel"].clash(kwargs["bird"]):
		return True

def bird_not_colliding(**kwargs):
	go = kwargs["barrel"].go
	eixo_x_of_bird = kwargs["bird"].eixo_x
	eixo_x_of_barrel = kwargs["barrel"].eixo_x

	if not go and eixo_x_of_bird > eixo_x_of_barrel:
		kwargs["barrel"].go = True
		add_barrel = True

		return kwargs["barrel"].go, add_barrel
	else:
		return False, False

def remove_barrel(barrel_position):
	if barrel_position < 0:
		return True

def reset_barrel_list_for_removing(remove_barrel_list):
	for item in remove_barrel_list:
		remove_barrel_list.remove(item)
	return remove_barrel_list

def remove_bird(area_limit, hit_on_floor):
	if area_limit | hit_on_floor:
		return True

def pygame_fps(fps, **kwargs):
	"""
	watch = pygame_o_clock()
	"""
	running = True
	while running:

		kwargs["watch"].tick(fps)
		for event in pygame_event():
			running = pygame_quit()

			# Pode haver um erro aqui pois não esta
			# retornando os passaros modificados
			# apenas enviando o comando de pular.
			pygame_keys(event, kwargs["birds"])

		# Move to things
		for bird in kwargs["birds"]:
			bird.move()
		floor.move()

		remove_barrel_list = []
		add_barrel = False
		barrels = create_barrels(
			kwargs["barrels"], 
			add_barrel
		)

		for barrel in barrels:
			birds = create_birds(
				kwargs["birds"]
			)
			for index, bird in birds:
				if bird_colliding(barrel, bird):
					kwargs["birds"].pop(index)

				
				kwargs["barrel"].go, add_barrel = bird_not_colliding(
					barrel, bird
				)

			barrel.move()
			barrel_position = barrel.eixo_x + barrel.roof_barrel
			if remove_barrel(barrel_position):
				remove_barrel.append(barrel)

			if add_barrel:
				kwargs["points"] += 1
				barrels.append(Barrel(600))

			# Reset remove_barrel_list
			remove_barrel_list = reset_barrel_list_for_removing(remove_barrel_list)

			for index, bird in birds:
				bird_position = bird.eixo_y + bird.img.get_height()
				area_limit = bird.eixo_y < 0
				hit_on_floor = bird.eixo_y < 0

				if remove_bird(area_limit, hit_on_floor):
					birds.pop(index)

			draw_window(
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
	window = pygame_set_mode(
		width_of_window(), height_of_window()
	)
	watch =  pygame_o_clock()

	pygame_fps(
		fps=30,
		points=0,
		birds=birds,
		floor=floor,
		barrels=barrels,
		window=window,
		watch=watch,
		barrel=Barrel
	)
