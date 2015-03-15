import math
import pygame
import random

class Enemy(pygame.sprite.Sprite):
	def __init__(self, width, height, surface):
		pygame.sprite.Sprite.__init__(self)
		self.rect = pygame.Rect(0,0,0,0)
		self.rect.size = (20,20)
		'''Init random starting location on edge of screen'''
		if random.randint(0,2) == 0:		
			if random.randint(0,2) == 0:
				self.rect.centerx = 0
			else:
				self.rect.centerx = width - 1
			self.rect.centery = random.randint(0, height)
		else:
			if random.randint(0,2) == 0:
				self.rect.centery = 0
			else:
				self.rect.centery = height - 1
			self.rect.centerx = random.randint(0, width)

		self.move_speed = 4
		self.angle = 0
		self.x_vel, self.y_vel = 0, 0
		self.updates = 0
		self.life_span = random.randint(30, 150)
		self.color = 0

	def get_angle(self, player_loc):
		'''Return angle of line between player center and player_loc'''
		xdiff = player_loc[0] - self.rect.center[0]
		ydiff = player_loc[1] - self.rect.center[1]
		return math.atan2(ydiff, xdiff)		

	def get_movement(self, player_loc):
		'''Take reported mouse position as point, then calculate the next point 
		to move player along that line'''
		self.x_vel = math.cos(self.angle) * self.move_speed
		self.y_vel = math.sin(self.angle) * self.move_speed
		if math.fabs(self.x_vel) < self.move_speed or \
					math.fabs(self.y_vel) < self.move_speed:
			return (self.rect.centerx + self.x_vel, 
					self.rect.centery + self.y_vel)
		else:
			return player_loc		

	def update(self, player_loc):
		if self.updates % 15 == 0:
			self.angle = self.get_angle(player_loc)
			self.rect.center = self.get_movement(player_loc)
		else:
			self.rect.center = (self.rect.centerx + self.x_vel, 
								self.rect.centery + self.y_vel)
		self.color = int((float(self.updates) / float(self.life_span)) * 255)	
		self.updates += 1


	def render(self, surface):
		surface.fill((255, 0, self.color) , self.rect)
