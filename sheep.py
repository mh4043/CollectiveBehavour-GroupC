import math
import numpy as np
from helpers import *


class Sheep():
    """
    A class used to represent a Sheep. Every sheep has following attributes:
    x: x-coordinate
    y: y-coordinate
    velocity: velocity of the sheep
    vector: vector of the sheep
    """
    param: dict[str, float]
    # Current parameters
    position: np.array(int) = [0, 0]  # x,y coordinate vector
    velocity: np.array(int) = [0, 0]  # Velocity for each axis
    color: str = 'blue'

    goal_reached: bool = False

    # ? parameters for constant values from .ini file

    def __init__(self, x: int, y: int, goal, parameters: dict[str, float],):
        self.position = np.array([x, y])
        self.param = parameters
        self.velocity = np.array([0, 0])

        self.goal_position = np.array([int(goal[0]), int(goal[1])])
        self.goal_radius = int(goal[2])

    # ? 4
    def calculate_velocity(self, dog, sheep_arr: list, step: int):
        # ? 6 Distance from dog
        piq: np.array(int) = self.position - dog.position
        piq_vec_length: float = vec_length(piq)

        vdi = 0
        # ? 10a Reaction to dog
        if piq_vec_length > 0 and piq_vec_length <= dog.radius:
            phi = self.param['alpha'] * \
                (1 / piq_vec_length - 1/dog.radius)
            vdi = phi * unit_vector(piq)  # ? 9a

        vsi = 0
        for sheep in sheep_arr:
            if sheep == self:
                continue

            x = vec_length(self.position - sheep.position)  # ? 9b
            tmp = 0
            """
            if self.param['ps'] < x and x <= self.param['pr']:
                tmp = self.param['beta'] * (1/(x-self.param['ps']) - 1/(self.param['pr']-self.param['ps']))
            """
            if x < self.param['pr']:
                tmp = ((self.param['pr'] - x) / self.param['pr']) * self.param['zeta']
            elif self.param['pg'] < x and x <= self.param['pd']:
                tmp = self.param['gamma'] * (x - self.param['pg'])

            vsi += tmp * unit_vector(self.position - sheep.position)

        theta = self.param['ai'] * (math.pi/180) * \
            math.sin(self.param['wi'] * step * self.param['t'])
        vect = rotation(theta).dot(vsi)

        self.velocity = vdi + vect  # ? 7
        if self.goal_reached:
            self.velocity = 0.2 * self.velocity
            return

    def move(self):
        self.position = self.position + self.velocity * self.param['t']

        # Check goal entry
        self.goal_reached = sheep_reached_goal(self,
                                                  self.goal_position,
                                                    self.goal_radius)