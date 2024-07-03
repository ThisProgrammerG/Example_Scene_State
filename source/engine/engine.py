import pygame

from source.scene import state_event


class Engine:
    def __init__(self):
        self.states = []
        self._running = True

    @property
    def current_state(self):
        return self.states[-1]

    def running(self):
        return self._running

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                self._running = False
            elif event.type == state_event.CHANGE_STATE:
                self.push_state(event.state)
            elif event.type == state_event.LEAVE_STATE:
                self.pop_state()

        self.current_state.handle_events(events)

    def update(self, delta_time):
        self.current_state.update(delta_time)

    def draw(self, surface):
        surface.fill("black")
        self.current_state.draw(surface)

    def clean_up(self):
        while self.states:
            self.current_state.clean_up()
            self.states.pop()

    def push_state(self, state):
        if self.states:
            self.current_state.pause()

        self.states.append(state)

    def pop_state(self):
        if self.states:
            self.current_state.clean_up()
            self.states.pop()

        if self.states:
            self.current_state.resume()
