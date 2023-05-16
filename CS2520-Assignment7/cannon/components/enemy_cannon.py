from .cannon import *

class EnemyCannon(Cannon):
    '''
    EnemyCannon class. Manages it's renderring, movement and striking.
    '''
    def __init__(self, coord=[SCREEN_SIZE[0]//2, SCREEN_SIZE[1]//2], angle=0, max_pow=50, min_pow=10, color=BLUE):
        super().__init__(coord=[SCREEN_SIZE[0]//2, SCREEN_SIZE[1]//2], angle=0, max_pow=50, min_pow=10, color=BLUE)
        self.vx = randint(-2, +2)
        self.vy = randint(-2, +2)
    
    def activate(self):
        pass

    def gain(self, inc=2):
        pass

    def strike(self):
        '''
        Creates ball, according to a random direction and charge power.
        '''
        vel = randint(10,50)
        angle = randint(10,90)
        ball = Shell(list(self.coord), [int(vel * np.cos(angle)), int(vel * np.sin(angle))])
        self.pow = self.min_pow
        #self.active = False
        return ball
        
    def set_angle(self, target_pos):
        pass

    def move(self):
        '''
        Moves EnemyCannon randomly on screen
        '''
        # change direction randomly
        if randint(0, 100) < 5:
            self.vx = randint(-2, 2)
            self.vy = randint(-2, 2)

        # check for collision with edges of the screen
        if self.coord[0] > SCREEN_SIZE[0]:
            self.coord[0] = SCREEN_SIZE[0] 
            self.vx = -abs(self.vx)  # change direction in x-axis
        else:
            self.coord[0] += self.vx
        
        if self.coord[1] > SCREEN_SIZE[1]:
            self.coord[1] = SCREEN_SIZE[1]
            self.vy = -abs(self.vy)  # change direction in y-axis
        else:
            self.coord[1] += self.vy

    def draw(self, screen):
        '''
        Draws the EnemyCannon on the screen.
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