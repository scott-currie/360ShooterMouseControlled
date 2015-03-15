import pygame
import random
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
enemies = [Enemy(width, height, screen), Enemy(width, height, screen), 
			Enemy(width, height, screen)]

prev_mouse_pos = pygame.mouse.get_pos()

while 1:
	'''***Check events***'''
	p_events = []	
	# fire = False
	for e in pygame.event.get():
		if e.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	'''***Update***'''
	'''Get mouse cursor position. compare to previous mouse position to 
	determine whether mouse moved this update. Allows player to do less
	 math if course has not changed.'''
	mouse_pos = pygame.mouse.get_pos()
	if mouse_pos != prev_mouse_pos:
		mouse_moved = True
		prev_mouse_pos = mouse_pos
	else:
		mouse_moved = False
	player.update(mouse_pos, pygame.mouse.get_pressed()[0], mouse_moved)
	
	if len(enemies) < 8:
		enemies.append(Enemy(width, height, screen))	

	for enemy in enemies:
		enemy.update(player.rect.center)
		if enemy.updates >= enemy.life_span:
			enemies.remove(enemy)

	'''***Render***'''
	background.fill((0,0,0))
	player.render(background)
	for enemy in enemies:
		enemy.render(background)
	screen.blit(background, (0,0))
	pygame.display.flip()
	fps_timer.tick(30)