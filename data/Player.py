import pygame


class Player(object):
    def __init__(self, x, y, car_type, SCREEN):
        self.SCREEN = SCREEN

        self.width = car_type['width']
        self.height = car_type['height']
        self.x = x - (self.width / 2)
        self.y = y - (self.height / 2)
        self.name = car_type['name']
        self.vel = car_type['vel']
        self.zero = car_type['zero']
        self.color_1 = car_type['color_1']
        self.color_2 = car_type['color_2']

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        
        
        self.upper_border = self.SCREEN.get_height() / 2
        self.lower_border = self.SCREEN.get_height() - self.height * 1.5

        self.aim_x = 0
        self.aim_y = 0
        self.aim_color = (255, 255, 255)

        self.bullets = []

        # Defining movement as array of 4 items being 4 possible directions of movement
        # 0 = left, 1 = right, 2 = up, 3 = down 
        self.isMoving = [False, False, False, False]
    
        
        

    def handle_movement(self):
        if any(self.isMoving):
            if self.isMoving[0]:
                self.x -= self.vel
            if self.isMoving[1]:
                self.x += self.vel
            if self.isMoving[2]:
                self.y -= self.vel
            if self.isMoving[3]:
                self.y += self.vel

    def draw(self):
        # Draw base of the car
        pygame.draw.rect(
            self.SCREEN, 
            self.color_1, 
            (self.x, self.y, self.width, self.height))

        # Draw top of the car
        pygame.draw.rect(
            self.SCREEN, 
            self.color_2, 
            (self.x + self.width * 0.05, 
            self.y + self.height / 2, 
            self.width * 0.9, 
            self.height / 3))

        pygame.draw.circle(self.SCREEN, self.aim_color, (self.aim_x, self.aim_y), self.SCREEN.get_height() * 0.012, 1)
        pygame.draw.circle(self.SCREEN, self.aim_color, (self.aim_x, self.aim_y), self.SCREEN.get_height() * 0.002)