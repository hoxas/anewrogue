import pygame, math

class Turret(object):
    def __init__(self, SCREEN, player):
        self.SCREEN = SCREEN
        self.turret_color = (0, 0, 255)
        self.player = player
        self.width = player.width / 3
        self.height = player.height / 3
        self.x = self.player.rect.centerx
        self.y = self.player.rect.centery

        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(self.turret_color)
        self.rect = self.image.get_rect(center=(self.x, self.y))
        
    def handle_movement(self):
        if any(self.player.isMoving):
            if self.player.isMoving[0]:
                self.rect.x -= self.player.vel
            if self.player.isMoving[1]:
                self.rect.x += self.player.vel
            if self.player.isMoving[2]:
                self.rect.y -= self.player.vel
            if self.player.isMoving[3]:
                self.rect.y += self.player.vel

    def draw(self):
        self.SCREEN.blit(self.image, (self.rect.x, self.rect.y))