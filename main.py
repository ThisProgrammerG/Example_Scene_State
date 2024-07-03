import pygame


from source.engine.engine import Engine
from source.scene.intro import Intro


def run(engine):
    display = pygame.display.get_surface()
    clock = pygame.Clock()
    delta_time = 0

    while engine.running():
        events = pygame.event.get()
        engine.handle_events(events)
        engine.update(delta_time)
        engine.draw(display)
        pygame.display.flip()
        delta_time = clock.tick() * 0.001

    engine.clean_up()
    pygame.quit()


def main():
    pygame.init()
    pygame.display.set_caption("Title Goes Here")
    pygame.display.set_mode((800, 800))

    engine = Engine()
    engine.push_state(Intro())

    run(engine)


if __name__ == "__main__":
    main()
