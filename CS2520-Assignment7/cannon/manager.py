from components.cannon import Cannon
from components.target import Target, MovingTargets, Bomb
from components.enemy_cannon import EnemyCannon
from components.score_table import ScoreTable
from components.settings import *



class Manager:
    '''
    Class that manages events' handling, ball's motion and collision, target creation, etc.
    '''
    def __init__(self, n_targets=1):
        self.balls = []
        self.gun = Cannon()
        self.targets = []
        self.score_t = ScoreTable()
        self.n_targets = n_targets
        self.bombs = []    

        #Defines EnemyCannon and balls
        self.EnemyCannon = [EnemyCannon(), EnemyCannon(), EnemyCannon()]
        self.enemyBalls = []

        self.new_mission()

    def new_mission(self):
        '''
        Adds new targets.
        '''
        for i in range(self.n_targets):
            self.targets.append(MovingTargets(rad=randint(max(1, 30 - 2*max(0, self.score_t.score())),
                30 - max(0, self.score_t.score()))))
            self.targets.append(Target(rad=randint(max(1, 30 - 2*max(0, self.score_t.score())),
                30 - max(0, self.score_t.score()))))

    def process(self, events, screen):
        '''
        Runs all necessary method for each iteration. Adds new targets, if previous are destroyed.
        '''
        done = self.handle_events(events)

        if pg.mouse.get_focused():
            mouse_pos = pg.mouse.get_pos()
            self.gun.set_angle(mouse_pos)
        
        self.move()
        self.collide()
        self.draw(screen)

        # Randomly shoots EnemyCannon balls
        for cannon in self.EnemyCannon:
            if (randint(0,100) < 1):
                self.enemyBalls.append(cannon.strike())

        # check if all targets are destroyed
        if len(self.targets) == 0:
            self.balls = []  # clear any remaining balls
            self.new_mission()

        # Once every bomb disappears, a new set of bombs will be dropped
        if len(self.bombs) == 0:
            for i, target in enumerate(self.targets): 
                self.bombs.append(Bomb(coord=target.coord.copy(), vel=None, rad=10))

        return done

    def handle_events(self, events):
        '''
        Handles events from keyboard, mouse, etc.
        '''
        done = False
        for event in events:
            if event.type == pg.QUIT:
                done = True
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_w: # Added handling for w key
                    self.gun.move(0, -5)  # Move up
                elif event.key == pg.K_s: # Added handling for s key
                    self.gun.move(0, 5)  # Move down
                elif event.key == pg.K_a: # Added handling for a key
                    self.gun.move(-5, 0)  # Move left
                elif event.key == pg.K_d: # Added handling for d key
                    self.gun.move(5, 0)  # Move right
            elif event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.gun.activate()
            elif event.type == pg.MOUSEBUTTONUP:
                if event.button == 1:
                    self.balls.append(self.gun.strike())
                    self.score_t.b_used += 1
        return done
    
    def draw(self, screen):
        '''
        Runs balls', gun's, targets' and score table's drawing method.
        '''
        for ball in self.balls:
            ball.draw(screen)
        for ball in self.enemyBalls:
            ball.draw(screen)
        for target in self.targets:
            target.draw(screen)
        self.gun.draw(screen)
        self.score_t.draw(screen)
        for bomb in self.bombs:
            bomb.draw(screen)
        
        #justin added
        for cannon in self.EnemyCannon:
            cannon.draw(screen)

    def move(self):
        '''
        Runs balls' and gun's movement method, removes dead balls.
        '''
        dead_balls = []
        for i, ball in enumerate(self.balls):
            ball.move(grav=2)
            if not ball.is_alive:
                dead_balls.append(i)
        for i, ball in enumerate(self.enemyBalls):
            ball.move(grav=2)
            if not ball.is_alive:
                self.enemyBalls.pop(i)
        for i in reversed(dead_balls):
            self.balls.pop(i)
        for i, target in enumerate(self.targets):
            target.move()
        
        # Manages of the movement of each bomb and checks if it is still active
        for i, bomb in enumerate(self.bombs):
            bomb.move()
            if not bomb.is_alive:
                self.bombs.pop(i)
        # Moves the EnemyCannon randomly on screen
        for cannon in self.EnemyCannon:
            cannon.move()
        self.gun.gain()

    def collide(self):
        '''
        Checks whether balls bump into targets, sets balls' alive trigger.
        '''
        collisions = []
        targets_c = []
        for i, ball in enumerate(self.balls):
            for j, target in enumerate(self.targets):
                if target.check_collision(ball):
                    collisions.append([i, j])
                    targets_c.append(j)
        targets_c.sort()
        for j in reversed(targets_c):
            self.score_t.t_destr += 1
            self.targets.pop(j)