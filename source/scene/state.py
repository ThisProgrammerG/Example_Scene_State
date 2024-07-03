from abc import ABC
from abc import abstractmethod


class State(ABC):
    @abstractmethod
    def clean_up(self):
        pass

    @abstractmethod
    def pause(self):
        pass

    @abstractmethod
    def resume(self):
        pass

    @abstractmethod
    def handle_events(self, events):
        pass

    @abstractmethod
    def update(self, delta_time):
        pass

    @abstractmethod
    def draw(self, surface):
        pass
