import math
from shepherd import ShepherdDog
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
    piq: np.array(int) = [0, 0] # Distance from dog


    # Next step 
    position_next: np.array(int) = [0, 0]
    velocity_next: np.array(int) = [0, 0] 
    piq_next: np.array(int) = [0, 0]




    #? parameters for constant values from .ini file
    def __init__(self, x: int, y: int, parameters: dict[str, float]):
        self.position[0] = x
        self.position[1] = y
        self.param = parameters

    #? 4
    def calculate_next_position(self, dog: ShepherdDog, sheeps: list(Sheep) ):
        self.calculate_next_velocity(self, dog, sheeps)
        self.position_next = self.position + self.param['T'] * self.velocity

    #? 7
    def calculate_next_velocity(self, dog: ShepherdDog, sheeps: list(Sheep), step: int):
        piq_vec_length: float = vec_length(self.piq) #? 9a
        pn = self.param['pn']
        pd = self.param['pd']
        pr = self.param['pr']
        pg = self.param['pg']
        ps = self.param['ps']
        beta = self.param['beta']
        gamma = self.param['gamma']
        t = self.param['T']
        ai = self.param['ai']
        wi = self.param['wi']

        vdi = 0 #* reaction to Dog
        if piq_vec_length > 0 and piq_vec_length <= pn: #? 10a
            phi = self.param['alpha'] * (1/piq_vec_length - 1/pn)
            vdi = phi * o(self.piq) #? 9a

        vsi = 0
        for sheep in sheeps:
            if sheep == self:
                continue
            x = vec_length(self.position - sheep.position) #? 9b
            if ps < x and x <= pr:
                vsi += beta * (1/(x-ps) - 1/(pr-ps))
            elif pg < x and x <= pd:
                vsi += gamma * (x - pg)
        
        vsi = vsi.dot(o(self.position)) #? 9b

        theta = ai * math.pi * math.sin(wi * step * t)
        self.velocity_next = vdi + rotation(theta).dot(vsi) #? 7
        
    def move(self, dog: ShepherdDog):
        self.position = self.position_next
        self.velocity = self.velocity_next
        
        self.piq = self.calc_piq(self, dog)

    def calc_piq(self, dog: ShepherdDog):
        self.piq = self.position - dog.position
        
    def to_string(self):
        return f"Sheep X: {self.x}, Y: {self.y}"
    

    




