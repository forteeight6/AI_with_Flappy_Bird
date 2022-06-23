from src.util import bird_pictures

class Bird:
	pictures = bird_pictures()
	# Animation of Rotation
	max_rotation = 25
	speed_rotation = 20
	animation_time = 5

	def __init__(self, eixo_x, eixo_y):
		self.eixo_x = eixo_x
		self.eixo_y = eixo_y
		self.height = self.eixo_y
		self.angle = 0
		self.speed = 0
		self.time = 0
		self.count_img = 0
		self.img = self.pictures[0]
		self.n = 1

	def spring(self):
		self.speed = -10.5
		self.time = 0
		self.height = self.eixo_y


	def _calculate_displacement(self):
		# Calculate Displacement
		self.time += 1
		displacement = 1.5 * (self.time**2) + self.speed * self.time

	def _constrain_displacement(self):
		# Constrain Displacement
		if displacement > 16:
			displacement = 16
		elif displacement < 0:
			displacement -= 2

		self.y  += displacement


	def _bird_angle(self):
		# Bird Angle
		if displacement < 0 or self.eixo_y < (self.height + 50):
			if self.angle < self.max_rotation:
				self.angle = self.max_rotation
		else:
			if self.angle > -90:
				self.angle -= self.speed_rotation

	def budge(self):
		_calculate_displacement()
		_calculate_displacement()
		_bird_angle()

	# define which bird image will use
	def _flying_bird(self):
		"""
			A movimentação do passaro vai ser a sequência das imagens 0, 1, 2, 1, 0;
			The movement of the bird  will be the sequence of the images 0, 1, 2, 1, 0.

		"""
		self.count_img += 1
		
		if self.count_img < self.animation_time * self.n:
			if self.n <= 3:
				img_index = n-1
				self.img = self.pictures[img_index]
				self.n += 1
			elif self.n == 4:
				img_index = 1
				self.img = self.pictures[img_index]
				self.n += 1
			else:
				img_index = 0
				self.img = self.pictures[img_index]
				self.count_img = 0
				self.n = 1
		
	def _bird_falling(self):
		if self.angle <= -80:
			self.img = self.pictures[1]
			self.n = 2
			self.count_img = self.animation_time*self.n

	def _use_image(self):
		if self.angle > -80:
			_flying_bird()
		elif self.angle <= -80:
			_bird_falling()

	def draw(self, window):
		_use_image()

		# Drawing Picture
		rotated_img = pygame.transform.rotate(self.img, self.angle)

		topleft = (self.eixo_x, self.eixo_y)
		position_img = self.img.get_rect(topleft=topleft).center

		rectangle = rotated_img.get_rect(center=position_img)

		window.blit(rotated_img, rectangle.topleft)
