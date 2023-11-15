import math
import numpy as np
from helpers import *

class ShepherdDog():
    """
    A class used to represent a ShepherdDog. It has following attributes:

    """

    param: dict[str, float]

    position: np.array(int) = [0, 0] # x,y coordinate vector
    velocity: np.array(int) = [0, 0] # Velocity for each axis

    def __init__(self, x:int, y:int, parameters):
        self.position = np.array([int(x), int(y)])
        self.param = parameters
        self.velocity = np.array([0, 0])

    def calculate_velocity(self, sheeps: list):
        self.velocity = np.array([80, 160])

    def move(self):
        self.position = self.position + self.velocity * self.param['t']
        print(self.position)



