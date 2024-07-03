import pygame

CHANGE_STATE = pygame.event.custom_type()
LEAVE_STATE = pygame.event.custom_type()

_change_state_event = pygame.event.Event(CHANGE_STATE, state=None)
_leave_state_event = pygame.event.Event(LEAVE_STATE)


def change_state(state):
    _change_state_event.state = state
    pygame.event.post(_change_state_event)


def leave_state():
    pygame.event.post(_leave_state_event)
