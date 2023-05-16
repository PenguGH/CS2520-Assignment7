from .settings import *
from .game_object import GameObject

class Shell(GameObject):
    '''
    The ball class. Creates a ball, controls it's movement and implement it's rendering.
    '''  
    min_rad = 10  # the minimum radius length for the shell
    max_rad = 30  # the maximum radius length for the shell
    def __init__(self, coord, vel, rad=20, color=None):
        '''
        Constructor method. Initializes ball's parameters and initial values.
        '''
        self.coord = coord
        self.vel = vel
        if color == None:
            color = rand_color()
        self.color = color
        self.rad = rad
        self.is_alive = True
    	
        # implement various types of projectiles. (shell changes size each time it is shot)
        if rad is None:
            self.initial_rad = randint(self.min_rad, self.max_rad) # random radius length between min and max radius
            self.rad = self.initial_rad
        else:
            self.initial_rad = rad
            self.rad = rad

    def check_corners(self, refl_ort=0.8, refl_par=0.9):
        '''
        Reflects ball's velocity when ball bumps into the screen corners. Implemetns inelastic rebounce.
        '''
        for i in range(2):
            if self.coord[i] < self.rad:
                self.coord[i] = self.rad
                self.vel[i] = -int(self.vel[i] * refl_ort)
                self.vel[1-i] = int(self.vel[1-i] * refl_par)
            elif self.coord[i] > SCREEN_SIZE[i] - self.rad:
                self.coord[i] = SCREEN_SIZE[i] - self.rad
                self.vel[i] = -int(self.vel[i] * refl_ort)
                self.vel[1-i] = int(self.vel[1-i] * refl_par)

    def move(self, time=1, grav=0):
        '''
        Moves the ball according to it's velocity and time step.
        Changes the ball's velocity due to gravitational force.
        '''
        self.vel[1] += grav
        for i in range(2):
            self.coord[i] += time * self.vel[i]
        self.check_corners()
        if self.vel[0]**2 + self.vel[1]**2 < 2**2 and self.coord[1] > SCREEN_SIZE[1] - 2*self.rad:
            self.is_alive = False
    
    def draw(self, screen):
        '''
        Draws the ball on appropriate surface.
        '''
        if self.rad == self.initial_rad:
            self.change_size()  # Randomly change the size of the bullet before drawing it by using the change_size function
        pg.draw.circle(screen, self.color, self.coord, self.rad)
        pg.draw.rect(screen, self.color, pg.Rect(30, 30, 60, 60))

    def change_size(self):
        if self.rad == self.initial_rad:
            self.rad = randint(self.min_rad, self.max_rad)

class Cannon(GameObject):
    '''
    Cannon class. Manages it's renderring, movement and striking.
    '''
    def __init__(self, coord=[30, SCREEN_SIZE[1]//2], angle=0, max_pow=50, min_pow=10, color=RED):
        '''
        Constructor method. Sets coordinate, direction, minimum and maximum power and color of the gun.
        '''
        self.coord = coord
        self.angle = angle
        self.max_pow = max_pow
        self.min_pow = min_pow
        self.color = color
        self.active = False
        self.pow = min_pow
    
    def activate(self):
        '''
        Activates gun's charge.
        '''
        self.active = True

    def gain(self, inc=2):
        '''
        Increases current gun charge power.
        '''
        if self.active and self.pow < self.max_pow:
            self.pow += inc

    def strike(self):
        '''
        Creates ball, according to gun's direction and current charge power.
        '''
        vel = self.pow
        angle = self.angle
        ball = Shell(list(self.coord), [int(vel * np.cos(angle)), int(vel * np.sin(angle))])
        self.pow = self.min_pow
        self.active = False
        return ball
        
    def set_angle(self, target_pos):
        '''
        Sets gun's direction to target position.
        '''
        self.angle = np.arctan2(target_pos[1] - self.coord[1], target_pos[0] - self.coord[0])

    def move(self, x_coordinate, y_coordinate):
        '''
        Changes horizontal position of the gun. by increasing or decreasing the x coordinate.
        '''
        if (30 < self.coord[0] < SCREEN_SIZE[0] - 30) or x_coordinate * np.sign(SCREEN_SIZE[0] - self.coord[0]) > 0:
            self.coord[0] += x_coordinate

        '''
        Changes vertical position of the gun. by increasing or decreasing the y coordinate.
        '''
        if (30 < self.coord[1] < SCREEN_SIZE[1] - 30) or y_coordinate * np.sign(SCREEN_SIZE[1] - self.coord[1]) > 0:
            self.coord[1] += y_coordinate

    def draw(self, screen):
        '''
        Draws the gun on the screen.
        '''
        gun_shape = []
        vec_1 = np.array([int(5*np.cos(self.angle - np.pi/2)), int(5*np.sin(self.angle - np.pi/2))])
        vec_2 = np.array([int(self.pow*np.cos(self.angle)), int(self.pow*np.sin(self.angle))])
        gun_pos = np.array(self.coord)
        gun_shape.append((gun_pos + vec_1).tolist())
        gun_shape.append((gun_pos + vec_1 + vec_2).tolist())
        gun_shape.append((gun_pos + vec_2 - vec_1).tolist())
        gun_shape.append((gun_pos - vec_1).tolist())
        pg.draw.polygon(screen, self.color, gun_shape)