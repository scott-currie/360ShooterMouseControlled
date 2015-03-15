import pygame
import sys
from player import Player 
from enemy import Enemy 

pygame.init()
fps_timer = pygame.time.Clock()

width, height = 640, 480
screen = pygame.display.set_mode((width, height))
background = pygame.Surface((width, height))
background.fill((0,0,0))
background.convert()


player = Player(width, height, screen)
enemies = [Enemy(width, height)]
prev_mouse_pos = pygame.mouse.get_pos()

while 1:
	p_events = []	
	fire = False
	for e in pygame.event.get():
		if e.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		elif e.type == pygame.MOUSEBUTTONDOWN:
			fire = True
	'''Update'''
	mouse_pos = pygame.mouse.get_pos()
	if mouse_pos != prev_mouse_pos:
		mouse_moved = True
		prev_mouse_pos = mouse_pos
	else:
		mouse_moved = False
	player.update(mouse_pos, fire, mouse_moved)

	'''Render'''
	background.fill((0,0,0))
	player.render(background)
	screen.blit(background, (0,0))
	pygame.display.flip()
	fps_timer.tick(30)