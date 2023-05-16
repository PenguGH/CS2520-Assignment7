from manager import *

if __name__ == '__main__':
    pg.init()
    pg.font.init()

    screen = pg.display.set_mode(SCREEN_SIZE)
    pg.display.set_caption("Cannon Fodder")

    done = False
    clock = pg.time.Clock()

    mgr = Manager(n_targets=3)

    while not done:
        clock.tick(15)
        screen.fill(BLACK)

        done = mgr.process(pg.event.get(), screen)

        pg.display.flip()

    pg.quit()