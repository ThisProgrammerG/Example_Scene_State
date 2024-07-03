import pygame

from source.scene import state_event
from source.scene.menu import Menu
from source.scene.state import State


class Intro(State):
    def __init__(self):
        self.surface = pygame.display.get_surface().copy()
        self.color = pygame.Color("orange")
        self.font = pygame.font.SysFont("Consolas", 34)
        self.text = self.font.render("Splash Scene", True, "white")
        self.text_rect = self.text.get_rect(center=self.surface.get_rect().center)

    def clean_up(self):
        pass

    def pause(self):
        pass

    def resume(self):
        pass

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    state_event.change_state(Menu())

    def update(self, delta_time):
        pass

    def draw(self, surface):
        self.surface.fill(self.color)
        self.surface.blit(self.text, self.text_rect)
        surface.blit(self.surface, (0, 0))
