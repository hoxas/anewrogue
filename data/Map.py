import pygame, random

class Map(object):
    def __init__(self, SCREEN):
        self.SCREEN = SCREEN
        self.background = (237, 111, 0)
        self.road_color = (102, 102, 102)
        self.road_width = (self.SCREEN.get_width() / 3) * 1.5
        self.road_height = self.SCREEN.get_height()
        self.road_x = SCREEN.get_width() / 2 - self.road_width / 2
        self.road_y = 0

        self.speed = 3

        self.white, self.yellow = (255, 255, 255), (251, 255, 0)

        self.road_lines_width = 6
        self.road_lines_height = 40
        self.road_lines_space = 25
        self.road_lines_quantity = range(round(self.SCREEN.get_height() / 65) + 1)
        self.road_lines_ypositions = [i * 65 for i in self.road_lines_quantity]
        self.road_line_color = random.choice([self.white, self.yellow])

    def handle_movement(self, player):
        for i, _val in enumerate(self.road_lines_ypositions):
            self.road_lines_ypositions[i] += self.speed
            self.road_lines_ypositions[i] = self.road_lines_ypositions[i] % self.SCREEN.get_height()

        speed_percentage = (
            (player.y - player.lower_border) / (player.upper_border - player.lower_border) * 100)
        
        self.speed = speed_percentage * 0.1 + player.zero

    def draw(self, player, clock, FONT):
        self.SCREEN.fill(self.background)
    
        player_coordinates = FONT.render(
            f'X: {player.x} Y: {player.y} FPS: {round(clock.get_fps())}', 
            False, 
            self.white)
        player_speed = FONT.render(
            f'Speed: {round(self.speed)}', 
            False, 
            self.white)
        player_aim = FONT.render(
            f'AimX: {player.aim_x} AimY: {player.aim_y}',
            False,
            self.white
        )

        self.SCREEN.blit(player_coordinates, (0, 0))
        self.SCREEN.blit(player_speed, (0, 15))
        self.SCREEN.blit(player_aim, (0, 30))

        pygame.draw.rect(
            self.SCREEN, 
            self.road_color,
            (self.road_x,
            self.road_y,
            self.road_width,
            self.road_height))

        for i in self.road_lines_quantity:
            pygame.draw.rect(
                self.SCREEN, 
                self.road_line_color, 
                (self.SCREEN.get_width() / 2 - self.road_lines_width / 2, 
                self.road_lines_ypositions[i - 1], 
                self.road_lines_width, 
                self.road_lines_height))


