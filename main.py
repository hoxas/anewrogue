import pygame, math

from data.cars.carslib import cars

from data.Player import Player
from data.Projectiles import Projectiles
from data.Map import Map

pygame.init()

pygame.mouse.set_cursor((8,8),(0,0),(0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0))

# create surface on screen
SCREEN = pygame.display.set_mode((800, 600))

FONT = pygame.font.SysFont('Comic Sans MS', 15)

FPS = 60

# Speed that road moves at
SPEED = 3
# Speed that car moves sideways
VEL = 5


BLACK = (0, 0, 0)
GRAY = (102, 102, 102)
RED = (255, 8, 0)
WHITE = (255, 255, 255)
ORANGE = (237, 111, 0)



def centerer(x, y, width, height, centerY = True):
    """Positioning through center of object"""

    if centerY == True:
        return (x - (width / 2), y - (height / 2), width, height)
    else:
        return (x - width / 2, y, width, height)


def handle_inputs(player, clock):   
    player.handle_inputs()
    

    

def handle_movement(player, cur_map, projectiles):
    
    player.handle_movement()
    projectiles.handle_movement(player)
    cur_map.handle_movement(player)


    

def draw_window(player, cur_map, clock, projectiles, FONT):   


    cur_map.draw(player, clock, FONT)
    player.draw()
    projectiles.draw(player)


    pygame.display.update()


def main():
    
    player = Player(
            SCREEN.get_width() / 2,
            SCREEN.get_height() - cars[0]['height'],
            cars[0],
            SCREEN)

    projectiles = Projectiles(SCREEN)

    cur_map = Map(SCREEN)

    # setting logo img
    ''' 
    logo = pygame.image.load('path/to/logo.png')
    pygame.display.set_icon(logo) 
    '''
    pygame.display.set_caption('A New Rogue')

    clock = pygame.time.Clock()
    
    running = True

    while running:

        clock.tick(FPS)

        # event handling getting events from queue
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        handle_inputs(player, clock)
        handle_movement(player, cur_map, projectiles)
        
        
        draw_window(player, cur_map, clock, projectiles, FONT)

if __name__ == "__main__":
    main()