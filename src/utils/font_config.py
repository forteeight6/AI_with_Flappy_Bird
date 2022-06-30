import pygame

# config font
def font():
	pygame.font.init()
	font_points = pygame.font.SysFont('arial', 50)
	return font_points