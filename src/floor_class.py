import utils

class Floor:
	width = pygame_floor_img(True)
	image = pygame_floor_img()
	speed = 5

	def __init__(self, eixo_y):
		self.eixo_y = eixo_y
		
		# position floors
		self.pos_floor_one = 0
		self.pos_floor_two = self.width


	def move(self):
		# position floors
		self.pos_floor_one -= self.speed
		self.pos_floor_two -= self.speed

		# verify positions
		verify_one, verify_two = (
			self.pos_floor_one + self.width < 0,
			self.pos_floor_two + self.width < 0
		)
		if verify_one:
			self.pos_floor_one = self.pos_floor_two + self.width

		if verify_two:
			self.pos_floor_two = self.pos_floor_one + self.width

	def draw(self, window):
		window.blit(
			self.image, (
				self.pos_floor_one,
				self.eixo_y
			)
		)
		window.blit(
			self.image, (
				self.pos_floor_two,
				self.eixo_y
			)
		)