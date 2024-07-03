import pygame

from source.scene import state_event
from source.scene.state import State


class Menu(State):
    def __init__(self):
        self.surface = pygame.display.get_surface().copy()
        self.color = pygame.Color("dodgerblue")
        self.font = pygame.font.SysFont("Consolas", 34)
        self.menu_text = self.font.render("Menu Scene", True, "white")
        self.menu_rect = self.menu_text.get_rect(center=self.surface.get_rect().center)

    def clean_up(self):
        pass

    def pause(self):
        pass

    def resume(self):
        pass

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    state_event.leave_state()

    def update(self, delta_time):
        pass

    def draw(self, surface):
        self.surface.fill(self.color)
        self.surface.blit(self.menu_text, self.menu_rect)
        surface.blit(self.surface, (0, 0))
