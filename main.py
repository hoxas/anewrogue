import pygame

pygame.init()

# create surface on screen
SCREEN = pygame.display.set_mode((800, 600))

FONT = pygame.font.SysFont('Comic Sans MS', 15)

FPS = 60

# Speed that road moves at
SPEED = 0
# Speed that car moves atSS
VEL = 5
ACCELERATION = 0

BLACK = (0, 0, 0)
GRAY = (102, 102, 102)
RED = (255, 8, 0)
WHITE = (255, 255, 255)

whitelines_width = 8
whitelines_height = 40
whitelines_space = 25

whitelines_quantity = range(round(SCREEN.get_height() / 65) + 1)
whitelines_ypositions = [i * 65 for i in whitelines_quantity]
print(whitelines_ypositions)

def centerer(x, y, width, height, centerY = True):
    """Positioning through center of object"""

    if centerY == True:
        return (x - (width / 2), y - (height / 2), width, height)
    else:
        return (x - width / 2, y, width, height)


def draw_window(player):
    global ACCELERATION
    global SPEED

    SCREEN.fill(BLACK)
    
    player_coordinates = FONT.render(f'X: {player.x} Y: {player.y}', False, WHITE)
    player_speed = FONT.render(f'Acceleration: {ACCELERATION} Speed: {SPEED}', False, WHITE)

    SCREEN.blit(player_coordinates, (0, 0))
    SCREEN.blit(player_speed, (0, 30))

    pygame.draw.rect(SCREEN, GRAY, (centerer(SCREEN.get_width() / 2, 0, (SCREEN.get_width() / 3) * 1.5, SCREEN.get_height(), False)))


    global whitelines_quantity, whitelines_ypositions, whitelines_height, whitelines_width, whitelines_space

    for i in whitelines_quantity:
        pygame.draw.rect(SCREEN, WHITE, (centerer(SCREEN.get_width() / 2, whitelines_ypositions[i - 1], whitelines_width, whitelines_height, False)))


    pygame.draw.rect(SCREEN, RED, (player.x, player.y, player.width, player.height))


    pygame.display.update()

def handle_input(keys_pressed, player):
    global ACCELERATION
    if keys_pressed[pygame.K_a] and player.x - VEL > 0: # LEFT
        player.x -= VEL
    if keys_pressed[pygame.K_d] and player.x + VEL < SCREEN.get_width() - player.width: # RIGHT
        player.x += VEL
    if keys_pressed[pygame.K_w] and ACCELERATION + 1 < 11: # UP
        ACCELERATION += 1
    if keys_pressed[pygame.K_s] and ACCELERATION - 1 > -11: # DOWN     
        ACCELERATION -= 1
    if not keys_pressed[pygame.K_w] and not keys_pressed[pygame.K_s]:
        if ACCELERATION > 0 and not ACCELERATION < 10:
            ACCELERATION -= 10
        elif ACCELERATION < 0 and not ACCELERATION > -10:
            ACCELERATION += 10
        else:
            ACCELERATION = 0

    if keys_pressed[pygame.K_ESCAPE]:
        pygame.event.post(pygame.event.Event(pygame.QUIT))
    
def handle_movement():
    global ACCELERATION, SPEED, whitelines_ypositions

    if SPEED > 150:
        SPEED = 150

    if ACCELERATION > 0:
        if SPEED + ACCELERATION > 150:
            SPEED = 150
        else:
            SPEED += ACCELERATION
    elif ACCELERATION < 0:
        if SPEED - -ACCELERATION < 0:
            SPEED = 0
        else:
            SPEED -= -ACCELERATION

    if SPEED > 0:
        for i, value in enumerate(whitelines_ypositions):
            whitelines_ypositions[i] += SPEED 
            whitelines_ypositions[i] = whitelines_ypositions[i] % SCREEN.get_height()



def main():
    
    player = pygame.Rect(centerer(SCREEN.get_width() / 2, SCREEN.get_height() / 2, 40, 40))

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
        
        keys_pressed = pygame.key.get_pressed()
        handle_input(keys_pressed, player)
        handle_movement()
        
        draw_window(player)

if __name__ == "__main__":
    main()