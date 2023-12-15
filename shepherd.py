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

    src_direction_right: bool =  True #direction of search
    src_next_x: int = 0 
    src_moving_x: bool = False # ali se premikamo po širini za naslednje preiskovanje
    src_direction_up: bool = True # in which direction the search is going


    def __init__(self, x:int, y:int, goal, parameters):
        self.position = np.array([int(x), int(y)])
        self.param = parameters
        self.velocity = np.array([0, 0])
        self.radius = parameters['ra']

        self.goal_position = np.array([int(goal[0]), int(goal[1])])
        self.goal_radius = int(goal[2])

        self.lambd = 0

    def calculate_velocity(self, sheep_arr: list):
        self.velocity = np.array([80, 160])

        # Check if all sheep have reached the goal
        goal_sheep = 0
        for sheep in sheep_arr:
            goal_sheep += int(sheep.goal_reached)

        if goal_sheep == len(sheep_arr):
            self.velocity = np.array([0, 0])
            return True
        
        # Calculate visible sheep 
        visible_sheep = get_visible_sheep(self, sheep_arr)
        # TODO, rotate sheep if needed when implementing the angle

        if(visible_sheep == []):
          print("No visible sheep")


          if(self.velocity[1] < 0): 
              self.src_direction_up = False #we are searching down
          
          #poglej ali je vektor oblike [0,y] če ni ga nastavi
          #nastavimo vektor da gre prečeše gor dol (pomeni x komponenta == 0)
          if(not self.src_moving_x and self.velocity[0] != 0): #only if not moving in x direction
            self.velocity[0] = 0
            #TODO maybe do something for Y speed
          
          if(self.src_moving_x): #* we are moving in x direction while searching
            print("search moving x")
            #first check bounds
            next_step_out_of_bounds = (self.position[0] + self.velocity[0] >= self.param['b_width'] or self.position[0] - self.velocity[0] <= 0)
            
            if((self.src_direction_right and (self.position[0]) >= self.src_next_x) #we reached the next x moving right
               or (not self.src_direction_right and (self.position[0]) <= self.src_next_x) #we reached the next x moving left
               or next_step_out_of_bounds): # next step would be out of bounds
              self.src_moving_x = False
              if(self.src_direction_up):
                self.velocity = [0, -abs(self.velocity[0])]
                self.src_direction_up = False
              else:
                self.velocity = [0, abs(self.velocity[0])]
                self.src_direction_up = True
              self.src_moving_x = False
              if(next_step_out_of_bounds):
                self.src_direction_right = not self.src_direction_right #flip the search direction
          else: #* we are moving in y direction while searching
            # # if(see_the_bound(self.position, self.radius, self.param['b_width'], self.param['b_height'])): # we encountered the boudn
            reachedTop = ((self.position[1] + self.radius) <= self.param['b_height'])
            reachedBottom = (self.position[1] - self.radius <= 0)
            if( reachedTop #* dog reached the top -> move to self.src_direction
                or reachedBottom): #* dog reached the bottom -> move to self.src_direction
              diameter = 2*self.radius
              if(self.src_direction_right):
                self.velocity = [abs(self.velocity[1]),0]
                self.src_next_x = self.position[0] + diameter
              else:
                self.velocity = [-abs(self.velocity[1]),0]
                self.src_next_x = self.position[0] - diameter
              if(reachedTop):
                self.src_direction_up = False
              elif(reachedBottom): 
                self.src_direction_up = True
                 
            
        else: #? dog sees at least one sheep
          # Check if all sheep are on right side of the dog
          if all_sheep_on_right_side(sheep_arr, self, self.goal_position) and calc_left_cosine(sheep_arr, self, self.goal_position) > float(self.param['theta_t']): #? 24
              # print("All sheep on right side")
              self.lambd= 0

              # Get right most visible sheep
              right_most_sheep = find_right_most_visible_from_dog(visible_sheep, self)

              # Get the vector from dog to sheep
              piq = right_most_sheep.position - self.position

              # Check if sheep is far away to justify a chase
              if vec_length(piq) >= float(self.param['ra']):
                  self.velocity = int(self.param['gamma_a']) * unit_vector(piq)
              else:
                  self.velocity =int(self.param['gamma_b']) * rotation(float(self.param['theta_r'])).dot(unit_vector(piq))

          # Check if all sheep are on left side of the dog
          elif all_sheep_on_left_side(sheep_arr, self, self.goal_position) and calc_right_cosine(sheep_arr, self, self.goal_position) > float(self.param['theta_t']): #? 25
              # print("All sheep on left side")
              self.lambd = 1

              # Get left most visible sheep
              left_most_sheep = find_left_most_visible_from_dog(visible_sheep, self)

              # Get the vector from dog to sheep
              piq = left_most_sheep.position - self.position

              # Check if sheep is far away to justify a chase
              if vec_length(piq) >= float(self.param['ra']):
                  self.velocity = int(self.param['gamma_a']) * unit_vector(piq)
              else:
                  self.velocity = int(self.param['gamma_b']) * rotation(float(self.param['theta_l'])).dot(unit_vector(piq))
          
          elif self.lambd == 1:
              # print("Lambda = 1")
              # Get left most visible sheep
              left_most_sheep = find_left_most_visible_from_dog(visible_sheep, self)

              # Get the vector from dog to sheep
              piq = left_most_sheep.position - self.position

              # Check if sheep is far away to justify a chase
              if vec_length(piq) >= float(self.param['ra']):
                  self.velocity = int(self.param['gamma_a']) * unit_vector(piq)
              else:
                  self.velocity =int(self.param['gamma_b']) * rotation(float(self.param['theta_l'])).dot(piq)
          else:
              # print("Lambda = 0")
              # Get right most visible sheep
              right_most_sheep = find_right_most_visible_from_dog(visible_sheep, self)

              # Get the vector from dog to sheep
              piq = right_most_sheep.position - self.position

              # Check if sheep is far away to justify a chase
              if vec_length(piq) >= float(self.param['ra']):
                  self.velocity = int(self.param['gamma_a']) * unit_vector(piq)
              else:
                  self.velocity = int(self.param['gamma_b']) * rotation(float(self.param['theta_r'])).dot(piq)



    def move(self):
        self.position = self.position + self.velocity * self.param['t']