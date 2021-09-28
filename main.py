import pygame, math

from data.cars.carslib import cars

from data.Player import Player
from data.Turret import Turret
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


def handle_inputs(player, turret, clock):

    keys_pressed = pygame.key.get_pressed()

    if keys_pressed[pygame.K_ESCAPE]:
        pygame.event.post(pygame.event.Event(pygame.QUIT)) 

    if keys_pressed[pygame.K_a] and player.x - player.vel > 0: # LEFT
        player.isMoving[0] = True
    else:
        player.isMoving[0] = False

    if keys_pressed[pygame.K_d] and player.x + player.vel < SCREEN.get_width() - player.width: # RIGHT
        player.isMoving[1] = True
    else:
        player.isMoving[1] = False

    if keys_pressed[pygame.K_w] and player.y - 1 > player.upper_border: # UP
        player.isMoving[2] = True
    else:
        player.isMoving[2] = False

    if keys_pressed[pygame.K_s] and player.y + 1 < player.lower_border: # DOWN     
        player.isMoving[3] = True
    else:
        player.isMoving[3] = False

    mouse_press = pygame.mouse.get_pressed()
    player.aim_x, player.aim_y = pygame.mouse.get_pos()

    if mouse_press[0]:
        player.bullets.append(
            [pygame.Rect(
                (player.x + player.width / 2) - player.width / 2,
                (player.y + player.height / 2) - player.height / 2,
                player.SCREEN.get_width() * 0.004,
                player.SCREEN.get_height() * 0.004),
            player.aim_x, 
            player.aim_y])

    if mouse_press[1]:
        print('Mouse Middle Click')

    if mouse_press[2]:
        print('Mouse 2 Click')



    

def handle_movement(player, turret, cur_map, projectiles):
    
    player.handle_movement()
    turret.handle_movement()
    projectiles.handle_movement(player)
    cur_map.handle_movement(player)


    

def draw_window(player, turret, cur_map, clock, projectiles, FONT):   


    cur_map.draw(player, clock, FONT)
    player.draw()
    projectiles.draw(player)
    turret.draw()


    pygame.display.update()


def main():
    
    player = Player(
            SCREEN.get_width() / 2,
            SCREEN.get_height() - cars[0]['height'],
            cars[0],
            SCREEN)

    turret = Turret(SCREEN, player)

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
        
        handle_inputs(player, turret, clock)
        handle_movement(player, turret, cur_map, projectiles)
        
        
        draw_window(player, turret, cur_map, clock, projectiles, FONT)

if __name__ == "__main__":
    main()