import math
import numpy as np
from helpers import *

class ShepherdDog():
    """
    A class used to represent a ShepherdDog. 
    """

    param: dict[str, float]

    position: np.array(int) = [0, 0] # x,y coordinate vector
    velocity: np.array(int) = [0, 0] # Velocity for each axis

    lambd: int = 0 # Indicator of direction
    radius: int = 0 # Radius of the dog

    def __init__(self, x:int, y:int, parameters):
        self.position = np.array([int(x), int(y)])
        self.param = parameters
        self.velocity = np.array([0, 0])
        self.radius = parameters['pr']

    def calculate_velocity(self, sheep_arr: list):
        self.velocity = np.array([80, 160])

        # Check if all sheep have reached the goal
        goal_sheep = 0
        for sheep in sheep_arr:
            goal_sheep += int(sheep.goal_reached)

        if goal_sheep == len(sheep_arr):
            self.velocity = np.array([0, 0])
            print("Success")
            return
        
        # Calculate visible sheep 
        visible_sheep = get_visible_sheep(self, sheep_arr)
        # TODO, rotate sheep if needed when implementing the angle

        # Check if all sheep are on left side of the dog
        if all_sheep_on_left_side(sheep_arr, self): #? 26
            self.lambd= 1

            # Get left most visible sheep
            left_most_sheep = get_left_most_sheep(visible_sheep, dog)



        # Check if all sheep are on right side of the dog
        if all_sheep_on_right_side(sheep_arr, self): #? 25
            self.lambd = 0

            # Get 


    def move(self):
        self.position = self.position + self.velocity * self.param['t']