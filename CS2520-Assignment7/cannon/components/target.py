from .settings import *
from .game_object import GameObject

class Target(GameObject):
    '''
    Target class. Creates target, manages it's rendering and collision with a ball event.
    '''
    def __init__(self, coord=None, color=None, rad=30):
        '''
        Constructor method. Sets coordinate, color and radius of the target.
        '''
        if coord == None:
            coord = [randint(rad, SCREEN_SIZE[0] - rad), randint(rad, SCREEN_SIZE[1] - rad)]
        self.coord = coord
        self.rad = rad

        if color is None:
            color = (WHITE)

    def check_collision(self, ball):
        '''
        Checks whether the ball bumps into target.
        '''
        dist = sum([(self.coord[i] - ball.coord[i])**2 for i in range(2)])**0.5
        min_dist = self.rad + ball.rad
        return dist <= min_dist

    def draw(self, screen):
        '''
        Draws the target on the screen
        '''
        pg.draw.circle(screen, RED, self.coord, self.rad) # red outer circle
        pg.draw.circle(screen, WHITE, self.coord, self.rad-5) # white 2nd inner circle
        pg.draw.circle(screen, RED, self.coord, self.rad-10) # red 3rd inner circle
        pg.draw.circle(screen, WHITE, self.coord, self.rad-15) # white 4th inner circle
        pg.draw.circle(screen, RED, self.coord, self.rad-20) # red center circle

    def move(self):
        """
        This type of target can't move at all.
        :return: None
        """
        pass


class MovingTargets(Target):
    def __init__(self, coord=None, color=None, rad=30):
        super().__init__(coord, color, rad)
        self.vx = randint(-2, +2)
        self.vy = randint(-2, +2)
    
    def move(self):
        # update position based on velocity
        self.coord[0] += self.vx
        self.coord[1] += self.vy

        # change direction randomly
        if randint(0, 100) < 5:
            self.vx = randint(-2, 2)
            self.vy = randint(-2, 2)
        
        # check for collision with edges of the screen
        if self.coord[0] < self.rad:
            self.coord[0] = self.rad
            self.vx = abs(self.vx)  # change direction in x-axis
        elif self.coord[0] > SCREEN_SIZE[0] - self.rad:
            self.coord[0] = SCREEN_SIZE[0] - self.rad
            self.vx = -abs(self.vx)  # change direction in x-axis
        
        if self.coord[1] < self.rad:
            self.coord[1] = self.rad
            self.vy = abs(self.vy)  # change direction in y-axis
        elif self.coord[1] > SCREEN_SIZE[1] - self.rad:
            self.coord[1] = SCREEN_SIZE[1] - self.rad
            self.vy = -abs(self.vy)  # change direction in y-axis


class Bomb(GameObject):
    '''
    The Bomb class. Creates a Bomb, controls it's movement and implement it's rendering.
    '''
    def __init__(self, coord, vel=None, rad=10, color=None):
        '''
        Constructor method. Initializes bomb's parameters and initial values.
        '''
        if coord == None:
            coord = [randint(rad, SCREEN_SIZE[0] - rad), randint(rad, SCREEN_SIZE[1] - rad)]
        self.coord = coord
        if vel == None:
            vel = [0,2]
        self.vel = vel
        if color == None:
            color = rand_color()
        self.color = color
        self.rad = rad
        self.is_alive = True

    def move(self, time=1, grav=0.25):
        '''
        Moves the bomb according to it's velocity and time step.
        Changes the bomb's velocity due to gravitational force.
        '''
        # increases the y-velocity by gravity every iteration
        self.vel[1] += grav

        #changes y coordinate
        self.coord[1] += time * self.vel[1]

        #checks collision with ground
        if self.coord[1] > SCREEN_SIZE[1] - 2*self.rad:
            self.is_alive = False

    def draw(self, screen):
        '''
        Draws the bomb on appropriate surface.
        '''
        pg.draw.circle(screen, self.color, self.coord, self.rad)