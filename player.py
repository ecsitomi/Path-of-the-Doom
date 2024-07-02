import pygame, math
from settings import *

class Player:
    def __init__(self, game):
        self.game = game
        self.x, self.y = PLAYER_POS
        self.angle = PLAYER_ANGLE
        self.move = True

    def movement(self):
        # Mozgás szögek számolása
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        dx, dy = 0, 0
        speed = PLAYER_SPEED * self.game.delta_time 
        speed_sin = speed * sin_a
        speed_cos = speed * cos_a

        # Mozgás szögek alapján
        keys = pygame.key.get_pressed()
        if self.move:
            if keys[pygame.K_w]:
                dx += speed_cos
                dy += speed_sin
            if keys[pygame.K_s]:
                dx -= speed_cos
                dy -= speed_sin
            if keys[pygame.K_a]:
                dx += speed_sin
                dy -= speed_cos
            if keys[pygame.K_d]:
                dx -= speed_sin
                dy += speed_cos

        # Ütközés a fallal
        self.check_wall_collision(dx, dy)

        if keys[pygame.K_LEFT]:
            self.angle -= PLAYER_ROT_SPEED * self.game.delta_time
        if keys[pygame.K_RIGHT]:
            self.angle += PLAYER_ROT_SPEED * self.game.delta_time
        self.angle %= math.tau
    
    def check_wall(self, x, y):
        if (x, y) in self.game.map.world_map:
            if self.game.map.world_map[(x, y)] == 5:
                self.game.victory = True
            return False
        return True
    
    def check_wall_collision(self, dx, dy):
        if self.check_wall(int(self.x + dx), int(self.y)):
            self.x += dx
        if self.check_wall(int(self.x), int(self.y + dy)):
            self.y += dy
    
    def draw(self):
        pygame.draw.circle(self.game.screen, 'green', (self.x * 100, self.y * 100), 15)
    
    def update(self):
        self.movement()
        #self.check_victory()

    def check_victory(self):
        if self.game.victory:
            print("Győzelem!")  # Itt jelenítsd meg a győzelmi üzenetet a képernyőn

    @property
    def pos(self):
        return (self.x, self.y)

    @property
    def map_pos(self):
        return int(self.x), int(self.y)
