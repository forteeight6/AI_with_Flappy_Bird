import pygame
import os
import random

# config barrel_img
def barrel_img():
	directory = os.path.join('assets', 'pipe.png')
	barrel_img = pygame.image.load(directory)
	barrel_img = pygame.transform.scale2x(barrel_img)
	return barrel_img

# config floor_img
def floor_img():
	directory = os.path.join('assets', 'base.png')
	floor_img = pygame.image.load(directory)
	floor_img = pygame.transform.scale2x(floor_img)
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