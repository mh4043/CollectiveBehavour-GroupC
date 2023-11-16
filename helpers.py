import numpy as np
import math


def vec_length(vec: np.array) -> float: 
  return np.sqrt(vec[0]**2 + vec[1]**2)

def unit_vector(vec: np.array) -> np.array:
  return vec / np.linalg.norm(vec)

def rotation(angle: float) -> np.matrix:
  return np.array([[np.cos(angle), -np.sin(angle)], [np.sin(angle), np.cos(angle)]])



def sheep_reached_goal(sheep, goal_position, goal_radius):
    """
    Check if the sheep has entered the goal area
    """
    return vec_length(sheep.position - goal_position) <= goal_radius



def all_sheep_on_left_side(sheep_arr, dog):
    """
    Check if all sheep are on the left side of the dog
    """

    for sheep in sheep_arr:
        if sheep.position[0] > dog.position[0]:
            return False

    return True


def all_sheep_on_right_side(sheep_arr, dog):
    """
    Check if all sheep are on the right side of the dog
    """

    for sheep in sheep_arr:
        if sheep.position[0] < dog.position[0]:
            return False

    return True


def sheep_is_covered(sheep, sheep_arr, dog): #? 11, 12
    """
    Check if the sheep is covered by the other sheep
    """ 

    # Calculate unit vector from dog to sheep
    piq = unit_vector(sheep.position - dog.position)

    # Calculate distance from dog to sheep
    distance = vec_length(sheep.position - dog.position)

    for other_sheep in sheep_arr:
      if other_sheep == sheep:
          continue

      # Calculate unit vector from dog to other_sheep
      dog_curr_sheep_vect = unit_vector(other_sheep.position - dog.position)
      
      # TODO Check if correct - might need arctan2
      # Calculate if the sheep is covered by the other sheep by subtracting one unit vector from the other
      if vec_length(piq - dog_curr_sheep_vect) == 0 and vec_length(other_sheep.position - dog.position) < distance:
          return True
    return False


def sheep_is_in_visible_range(sheep, dog):
    # Check if distance from dog to sheep is less than the dog's vision radius
    return vec_length(sheep.position - dog.position) <= dog.radius


def sheep_is_visible(sheep, sheep_arr, dog):
    """
    Check if the sheep is visible to the dog. Consider positions of other sheep, and dog's vision angle
    """

    # Check if sheep is in visible range
    if not sheep_is_in_visible_range(sheep, dog):
        return False

    # Check if sheep is covered by other sheep
    if sheep_is_covered(sheep, sheep_arr, dog):
        return False
    
    # TODO Check if sheep is in dog's vision angle by using its position and velocity

    return True



def get_visible_sheep(dog, sheep_arr):
    """
    Get the sheep that are visible to the dog. Consider positions of other sheep, and dog's vision angle
    """
    visible_sheep = [sheep for sheep in sheep_arr if sheep_is_visible(sheep, sheep_arr, dog)]
    
    # TODO, remove when adding angle and handle it
    assert len(visible_sheep) > 0, "No visible sheep found"
    return visible_sheep



def find_left_most_visible_sheep(visible_sheep, dog):
    """
    Find the left most sheep that is visible to the dog
    """

    # Return the sheep with the smallest x value
    return min(visible_sheep, key=lambda sheep: sheep.position[0])


def find_right_most_visible(sheep_arr, dog):
    """
    Find the right most sheep that is visible to the dog
    """
    
    # Return the sheep with the largest x value
    return max(sheep_arr, key=lambda sheep: sheep.position[0])



def angle_between_vectors(vec1, vec2):
    """
    Calculate the angle between two vectors
    """
    un_v1 = unit_vector(vec1)
    un_v2 = unit_vector(vec2)
    return math.degrees(np.arccos(np.dot(un_v1, un_v2) / (np.linalg.norm(un_v1) * np.linalg.norm(un_v2))))