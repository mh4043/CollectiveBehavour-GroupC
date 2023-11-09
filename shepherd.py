import math
import numpy as np
from helpers import *
from sheep import Sheep

class ShepherdDog():
    """
    A class used to represent a ShepherdDog. It has following attributes:

    """
    position: np.array(int) = [0, 0] # x,y coordinate vector
    velocity: np.array(int) = [0, 0] # Velocity for each axis


    # Next step 
    position_next: np.array(int) = [0, 0]
    velocity_next: np.array(int) = [0, 0] 

    #? 5
    def calculate_next_position(self, sheeps: list(Sheep)):
        self.calculate_next_velocity(self, sheeps)
        self.position_next = self.position + self.param['T'] * self.velocity

    # def calculate_next_velocity(self, sheeps: list(Sheep)):
        



    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)
