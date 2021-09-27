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
        
        
        self.upper_border = self.SCREEN.get_height() / 2
        self.lower_border = self.SCREEN.get_height() - self.height * 1.5

        self.aim_x = 0
        self.aim_y = 0
        self.aim_color = (255, 255, 255)

        self.bullets = []

        # Defining movement as array of 4 items being 4 possible directions of movement
        # 0 = left, 1 = right, 2 = up, 3 = down 
        self.isMoving = [False, False, False, False]
    
    def handle_inputs(self):
        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[pygame.K_ESCAPE]:
            pygame.event.post(pygame.event.Event(pygame.QUIT)) 

        if keys_pressed[pygame.K_a] and self.x - self.vel > 0: # LEFT
            self.isMoving[0] = True
        else:
            self.isMoving[0] = False

        if keys_pressed[pygame.K_d] and self.x + self.vel < self.SCREEN.get_width() - self.width: # RIGHT
            self.isMoving[1] = True
        else:
            self.isMoving[1] = False

        if keys_pressed[pygame.K_w] and self.y - 1 > self.upper_border: # UP
            self.isMoving[2] = True
        else:
            self.isMoving[2] = False

        if keys_pressed[pygame.K_s] and self.y + 1 < self.lower_border: # DOWN     
            self.isMoving[3] = True
        else:
            self.isMoving[3] = False

        mouse_press = pygame.mouse.get_pressed()
        self.aim_x, self.aim_y = pygame.mouse.get_pos()

        if mouse_press[0]:
            self.bullets.append(
                [pygame.Rect(
                    (self.x + self.width / 2) - self.width / 2,
                    (self.y + self.height / 2) - self.height / 2,
                    self.SCREEN.get_width() * 0.004,
                    self.SCREEN.get_height() * 0.004),
                self.aim_x, 
                self.aim_y])

        if mouse_press[1]:
            print('Mouse Middle Click')

        if mouse_press[2]:
            print('Mouse 2 Click')

        

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