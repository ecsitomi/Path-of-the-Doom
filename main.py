import pygame, sys
from settings import *
from map import *
from player import *
from raycasting import *
from object_renderer import *

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(RES)
        self.clock = pygame.time.Clock()
        self.delta_time = 1
        self.victory = False
        self.new_game()
        
    def new_game(self):
        self.map = Map(self)
        self.player = Player(self)
        self.object_renderer = ObjectRenderer(self)
        self.ray_casting = RayCasting(self)

    def update(self):
        self.player.update()
        self.ray_casting.update()
        pygame.display.flip()
        self.delta_time = self.clock.tick(FPS)
        #pygame.display.set_caption(f"{int(self.clock.get_fps())}")
        pygame.display.set_caption("Path of the Doom")
        
    def draw(self):
        self.screen.fill('black')
        self.object_renderer.draw()
        if self.victory:
            self.draw_victory_message()

    def draw_victory_message(self):
        self.screen.fill('black')
        self.player.move = False
        font = pygame.font.Font(None, 240)
        text = font.render('GYŐZELEM!', True, pygame.Color('green'))
        rect = text.get_rect(center=(HALF_WIDTH, HALF_HEIGHT))
        self.screen.blit(text, rect)

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()
    
    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()


if __name__ == "__main__":
    game = Game()
    game.run()