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
    position: np.array(int) = [0, 0] # x,y coordinate vector
    velocity: np.array(int) = [0, 0] # Velocity for each axis

    goal_not_reached: bool = True


    #? parameters for constant values from .ini file
    def __init__(self, x: int, y: int, parameters: dict[str, float]):
        self.position = np.array([x, y])
        self.param = parameters
        self.velocity = np.array([0, 0])

    #? 4
    def calculate_next_position(self, dog, sheeps: list , step: int):
        self.calculate_next_velocity(dog, sheeps, step)
        self.position_next = self.position + self.param['t'] * self.velocity
        print(f"Currrent position: {self.position}, Next position: {self.position_next}, velocity: {self.velocity}")


    def calculate_velocity(self, dog, sheep_arr: list , step: int):
        piq  = np.abs(self.position - dog.position) #? 6 Distance from dog
        piq_vec_length = vec_length(piq)

        vdi = 0
        if piq_vec_length > 0 and piq_vec_length <= self.param['pn']: #? 10a Reaction to dog
            phi = self.param['alpha'] * (1/ piq_vec_length - 1/self.param['pn'])
            vdi = phi * unit_vector(piq) #? 9a

        vsi = 0
        for sheep in sheep_arr:
            if sheep == self:
                continue
            
            x = vec_length(self.position - sheep.position) #? 9b
            tmp = 0
            """
            if self.param['ps'] < x and x <= self.param['pr']:
                tmp = self.param['beta'] * (1/(x-self.param['ps']) - 1/(self.param['pr']-self.param['ps']))
            """
            if x < self.param['pr']:
                tmp = ((self.param['pr'] - x) / self.param['pr']) * self.param['zeta']
            elif self.param['pg'] < x and x <= self.param['pd']:
                tmp =  self.param['gamma'] * (x - self.param['pg'])

            vsi += tmp * unit_vector(self.position - sheep.position)

        theta = self.param['ai'] * math.pi/180 * math.sin(self.param['wi'] * step * self.param['t'])
        vect = rotation(theta).dot(vsi)

        self.velocity = vdi + vect #? 7

    #? 7
    def calculate_next_velocity(self, dog, sheeps: list, step: int):
        #piq_vec_length: float = vec_length(self.piq) #? 9a
        piq  = np.abs(self.position - dog.position) #? 6
        piq_vec_length = vec_length(piq)
        #print(f"Self position: {self.position}, Dog position: {dog.position}, piq: {self.piq}")
        pn = self.param['pn']
        pd = self.param['pd']
        pr = self.param['pr']
        pg = self.param['pg']
        ps = self.param['ps']
        beta = self.param['beta']
        gamma = self.param['gamma']
        t = self.param['t']
        ai = self.param['ai']
        wi = self.param['wi']

        vdi = 0 #* reaction to Dog
        if piq_vec_length > 0 and piq_vec_length <= pn: #? 10a, dog is in range of sheep
            phi = self.param['alpha'] * (1/piq_vec_length - 1/pn)
            vdi = phi * unit_vector(self.piq) #? 9a

        vsi = 0
        for sheep in sheeps:
            tmp = 0
            if sheep == self:
                continue
            x = vec_length(self.position - sheep.position) #? 9b
            if ps < x and x <= pr:
                tmp += beta * (1/(x-ps) - 1/(pr-ps))
            elif pg < x and x <= pd:
                tmp += gamma * (x - pg)
            vsi += tmp * unit_vector(self.position - sheep.position)

        vsi = vsi.dot(unit_vector(self.position)) #? 9b

        theta = ai * math.pi * math.sin(wi * step * t)
        vect = rotation(theta).dot(vsi)

        self.velocity_next = vdi + vect #? 7
        
        #print(self.velocity_next)

        
    def move(self):
        self.position = self.position + self.velocity * self.param['t']




