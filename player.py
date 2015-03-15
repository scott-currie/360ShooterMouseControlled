import math
import pygame
from pygame.locals import *

class Player(pygame.sprite.Sprite):
	MOVE_SPEED = 7
	BULLET_SPEED = 9
	SHOT_DELAY = 7

	def __init__(self, width, height, surface):
		pygame.sprite.Sprite.__init__(self)
		'''Init rect'''
		self.rect = pygame.Rect((width / 2, height / 2), (20,20))
		self.rect.center = surface.get_rect().center
		'''Init image from rect'''
		self.image = pygame.Surface((self.rect.width, self.rect.height))
		self.image.fill((0,255,0))
		self.image.convert()
		self.bullets = []
		self.shot_timer = 0
		self.scr_width = surface.get_rect().width
		self.scr_height = surface.get_rect().height

	def get_angle(self, mouse_pos):
		'''Return angle of line between player center and mouse_pos'''
		xdiff = mouse_pos[0] - self.rect.center[0]
		ydiff = mouse_pos[1] - self.rect.center[1]
		return math.atan2(ydiff, xdiff)		

	def get_movement(self, mouse_pos, angle, mouse_moved):
		'''Take reported mouse position as point, then calculate the next point 
		to move player along that line'''
		dx = math.cos(angle) * Player.MOVE_SPEED
		dy = math.sin(angle) * Player.MOVE_SPEED
		if math.fabs(dx) < Player.MOVE_SPEED or \
											math.fabs(dy) < Player.MOVE_SPEED:
			return (self.rect.centerx + dx, self.rect.centery + dy)
		else:
			return mouse_pos

	def fire_bullet(self, angle):
		'''A bullet is a list of two tuples: [0] is the bulllet's current
		position, and [1] is the x and y velocities'''
		x_spd = math.cos(angle) * Player.BULLET_SPEED
		y_spd = math.sin(angle) * Player.BULLET_SPEED
		self.bullets.append([(self.rect.centerx, self.rect.centery),
					 			(x_spd, y_spd)])
		self.shot_timer = Player.SHOT_DELAY

	def update_bullets(self):
		'''If any live bullets exist'''
		if len(self.bullets) > 0:
			'''List to hold dead bullets'''
			dead_bullets = []
			'''Iterate all bullets'''
			for bullet in self.bullets:
				'''If bullets within screen boundaries'''
				if bullet[0][0] > 0 and bullet[0][0] < self.scr_width:
					if bullet[0][1] > 0 and bullet[0][1] < self.scr_height:
						'''Move bullet'''
						bullet[0] = (bullet[0][0] + bullet[1][0], bullet[0][1] +
									 bullet[1][1]) 			
				else:
					'''If outside screen boundaries, add to dead_bullets'''						
					dead_bullets.append(bullet)
			'''Remove dead bullets'''
			for bullet in dead_bullets:
				self.bullets.remove(bullet)

	def update(self, mouse_pos, fire, mouse_moved):
		self.shot_timer -= 1
		angle = self.get_angle(mouse_pos)
		self.rect.center = self.get_movement(mouse_pos, angle, mouse_moved)
		if fire and self.shot_timer <= 0:
			self.fire_bullet(angle)
		self.update_bullets()

	def render_bullets(self, surface):
		if len(self.bullets) > 0:
			for bullet in self.bullets:
				pygame.draw.rect(surface, (0,255,0), (bullet[0][0], 
					            bullet[0][1], 2, 2))

	def render(self, surface):
		self.render_bullets(surface)
		# surface.fill((0,255,0) , self.rect)
		surface.blit(self.image, self.rect)
