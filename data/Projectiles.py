import pygame, math

class Projectiles(object):
    def __init__(self, SCREEN):
        self.SCREEN = SCREEN

    def handle_movement(self, player):
        if len(player.bullets) > 0:
            for id, value in enumerate(player.bullets):
                bullet = player.bullets[id][0]
                direction_x, direction_y = value[1], value[2]
                vector_x = direction_x - player.x / player.width
                vector_y = direction_y - player.y / player.height

                distance = math.sqrt(vector_x * vector_x + vector_y * vector_y)

                print(distance, vector_x, vector_y)

                if vector_x > 0:
                    bullet.x += 1
                elif vector_x < 0:
                    bullet.x -= 1
                
                if vector_y > 0:
                    bullet.y += 1
                elif vector_y < 0:
                    bullet.y -= 1

                print(bullet.x, bullet.y)

                if (bullet.x > self.SCREEN.get_width() + 10 or 
                    bullet.x < self.SCREEN.get_width() - 10 or
                    bullet.y > self.SCREEN.get_height + 10 or
                    bullet.y < self.SCREEN.get_height() - 10):

                    player.bullets.pop(id)
                    print('Bullet Deleted')
        
    def draw(self, player):
        if len(player.bullets) > 0:
            for bullet in player.bullets:
                pygame.draw.rect(self.SCREEN, (255, 255, 255), (bullet[0].x, bullet[0].y, bullet[0].width, bullet[0].height))

