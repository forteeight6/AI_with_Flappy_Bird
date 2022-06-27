import src.utils as util

class Barrel:
	distance = 200
	speed = 5

	def __init__(self, eixo_x):
		self.eixo_x = eixo_x
		self.height = 0
		self.roof_pos = 0
		self.floor_pos = 0

		barrel_img = util.pygame_barrel_img()
		self.roof_barrel = util.pygame_flip_image(barrel_img)
		self.barrel_floor = barrel_img

		self.go = False
		self.height, self.roof_pos, self.floor_pos = util.pygame_define_height(
			self.roof_pos, self.distance
		)

	def move(self):
		self.eixo_x -= self.speed

	def draw(self, window):
		config_window = (self.eixo_x, self.roof_pos)
		window.blit(self.roof_barrel, config_window)

		config_window = (self.eixo_x, self.floor_pos)
		window.blit(self.barrel_floor, config_window)


	def clash(self, bird):
		mask_bird = bird.get_mask()

		roof_barrel_mask = util.pygame_mask(self.roof_barrel)
		barrel_floor_mask = util.pygame_mask(self.barrel_floor)

		roof_distance = (
			self.eixo_x - bird.eixo_x,
			self.roof_pos - round(bird.eixo_y)
		)

		floor_distance = (
			self.eixo_x - bird.eixo_x,
			self.floor_pos - round(bird.eixo_y)
		)

		point_roof = util.pygame_overlap(
			mask_bird, args=(
				'roof_barrel_mask', 
				'roof_distance'
			)
		)

		point_floor = util.pygame_overlap(
			mask_bird, args=(
				'barrel_floor_mask', 
				'floor_distance'
			)
		)

		if point_roof or point_floor:
			return True
		else:
			return False