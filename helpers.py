import numpy as np
import math


def vec_length(vec: np.array) -> float: 
  return math.sqrt(vec[0]**2 + vec[1]**2)

def unit_vector(vec: np.array) -> np.array:
  return vec / np.linalg.norm(vec)

def rotation(angle: float) -> np.matrix:
  return np.array([[np.cos(angle), -np.sin(angle)], [np.sin(angle), np.cos(angle)]])



def sheep_reached_goal(sheep, goal_position, goal_radius):
    """
    Check if the sheep has entered the goal area
    """
    return vec_length(sheep.position - goal_position) <= goal_radius


#* OK
def all_sheep_on_left_side(sheep_arr, dog, goal_position):
    """
    Check if all sheep are on the left side of the dog based on the goal position and dog position
    """

    for sheep in sheep_arr:
        # Use the vector from dog to sheep and dog to goal to determine if the sheep is on the left side
        # TODO check result
        #if np.cross(sheep.position - dog.position, goal_position - dog.position) < 0:
        if ((goal_position-dog.position)[0]*(sheep.position-dog.position)[1] - (goal_position-dog.position)[1]*(sheep.position-dog.position)[0]) < 0:
            return False
        
    return True

#* OK
def all_sheep_on_right_side(sheep_arr, dog, goal_position):
    """
    Check if all sheep are on the right side of the dog
    """

    for sheep in sheep_arr:
        # Use the vector from dog to sheep and dog to goal to determine if the sheep is on the right side
        #if np.cross(sheep.position - dog.position, goal_position - dog.position) > 0:
        if ((goal_position-dog.position)[0]*(sheep.position-dog.position)[1] - (goal_position-dog.position)[1]*(sheep.position-dog.position)[0]) > 0:
            return False
    return True

#* OK
def sheep_is_covered(sheep, sheep_arr, dog): #? 11, 12
    """
    Check if the sheep is covered by the other sheep
    """ 

    # Calculate unit vector from dog to sheep
    piq = unit_vector(sheep.position - dog.position)

    # Calculate distance from dog to sheep
    distance = vec_length(sheep.position - dog.position)
    """ 
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
    """

    for other_sheep in sheep_arr:
        if other_sheep == sheep: #ignore self
            continue
        piq_other = unit_vector(other_sheep.position - dog.position)
        angle = math.atan2(piq[0], piq[1]) - math.atan2(piq_other[0],piq_other[1])
        if angle == 0 and distance > vec_length(other_sheep.position - dog.position):
            return True
    return False


#? 11
#* OK
def sheep_is_in_visible_range(sheep, dog):
    # Check if distance from dog to sheep is less than the dog's vision radius

    return vec_length(sheep.position - dog.position) <= dog.radius

#* OK
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
    # assert len(visible_sheep) > 0, "No visible sheep found"
    # return visible_sheep


#* OK
def find_left_most_visible_from_dog(visible_sheep, dog):
    """
    Find the left most sheep that is visible to the dog
    """
    left_most = visible_sheep[0]
    left_most_vect = unit_vector(left_most.position - dog.position)

    init_vector = unit_vector(np.array([0, 0]) - dog.position)
    left_most_angle = angle_between_vectors(left_most_vect, init_vector)

    for sheep in visible_sheep:
        sheep_vect = unit_vector(sheep.position - dog.position)
        angle = angle_between_vectors(sheep_vect, init_vector)

        if angle < left_most_angle:
            left_most = sheep
            left_most_angle = angle

    return left_most



def find_right_most_visible_from_dog(sheep_arr, dog):
    """
    Find the right most sheep that is visible to the dog
    """
    right_most = sheep_arr[0]
    right_most_vect = unit_vector(right_most.position - dog.position)

    init_vector = unit_vector(np.array([0, 0]) - dog.position)
    right_most_angle = angle_between_vectors(right_most_vect, init_vector)

    for sheep in sheep_arr:
        sheep_vect = unit_vector(sheep.position - dog.position)
        angle = angle_between_vectors(sheep_vect, init_vector)

        if angle > right_most_angle:
            right_most = sheep
            right_most_angle = angle

    return right_most

#* OK
def calculate_sheep_herd_center(sheep_arr):
    """
    Calculate the center of the sheep herd
    """
    # Calculate the mean of the x and y coordinates of the sheep
    x_mean = np.mean([sheep.position[0] for sheep in sheep_arr])
    y_mean = np.mean([sheep.position[1] for sheep in sheep_arr])

    return np.array([x_mean, y_mean])

#* OK
def find_left_most_visible_sheep_from_sheepfold(visible_sheep, dog, goal_position):
    """
    Find the left most sheep that is visible to the dog from the sheepfold
    """

    left_most = visible_sheep[0]
    left_most_vect = unit_vector(left_most.position - goal_position)

    init_vector = unit_vector(np.array([0, 0]) - goal_position)
    left_most_angle = angle_between_vectors(left_most_vect, init_vector)

    dist = vec_length(left_most.position - goal_position)

    for sheep in visible_sheep:
        sheep_vect = unit_vector(sheep.position - goal_position)
        angle = angle_between_vectors(sheep_vect, init_vector)

        if (angle > left_most_angle or 
          (angle == left_most_angle and 
           vec_length(sheep.position - goal_position) > dist)
          ):
            left_most = sheep
            left_most_angle = angle
            dist = vec_length(sheep.position - goal_position)

    return left_most


#? 22
def find_right_most_visible_sheep_from_sheepfold(visible_sheep, dog, goal_position):
    """
    Find the right most sheep that is visible to the dog from the sheepfold
    """

    right_most = visible_sheep[0]
    right_most_vect = unit_vector(right_most.position - goal_position)

    init_vector = unit_vector(np.array([0, 0]) - goal_position)
    right_most_angle = angle_between_vectors(init_vector, right_most_vect)

    dist = vec_length(right_most.position - goal_position)
    for sheep in visible_sheep:
        sheep_vect = unit_vector(sheep.position - goal_position)
        angle = angle_between_vectors(init_vector, sheep_vect)

        if angle > right_most_angle:
            right_most = sheep
            right_most_angle = angle
            dist = vec_length(sheep.position - goal_position)
        elif angle == right_most_angle:
            if vec_length(sheep.position - goal_position) > dist:
                right_most = sheep
                right_most_angle = angle
                dist = vec_length(sheep.position - goal_position)

    return right_most



#? 26
#* OK
def calc_left_cosine(sheep_arr, dog, goal_position):
    # Left sheep from sheepfold pov

    visible_sheep = get_visible_sheep(dog, sheep_arr)
    left_most_sheep_from_fold = find_left_most_visible_sheep_from_sheepfold(visible_sheep, dog, goal_position) #? 20
    
    left_most_fold_sheep_vect = dog.position - left_most_sheep_from_fold.position #? 21

    sheep_herd_center = calculate_sheep_herd_center(visible_sheep) #? 19
    dcd = unit_vector(goal_position - sheep_herd_center) #? 22

    # TODO Check why the division is using a vector length of 1 in dcd
    #return np.inner(dcd, left_most_fold_sheep_vect) / (vec_length(dcd) * vec_length(left_most_fold_sheep_vect))
    # print(math.acos(np.dot(dcd, left_most_fold_sheep_vect) / (vec_length(dcd) * vec_length(left_most_fold_sheep_vect))))
    return math.acos(np.dot(dcd, left_most_fold_sheep_vect) / (vec_length(dcd) * vec_length(left_most_fold_sheep_vect)))


#? 25
def calc_right_cosine(sheep_arr, dog, goal_position):
    # Right sheep from sheepfold pov

    visible_sheep = get_visible_sheep(dog, sheep_arr)
    right_most_sheep_from_fold = find_right_most_visible_sheep_from_sheepfold(visible_sheep, dog, goal_position) #? 20
    
    right_most_fold_sheep_vect = dog.position - right_most_sheep_from_fold.position #? 21

    sheep_herd_center = calculate_sheep_herd_center(visible_sheep) #? 19
    dcd = unit_vector(goal_position - sheep_herd_center) #? 22

    # TODO Check why the division is using a vector length of 1 in dcd
    #return np.inner(dcd, right_most_fold_sheep_vect) / (vec_length(dcd) * vec_length(right_most_fold_sheep_vect))
    # print(math.acos(np.dot(dcd, right_most_fold_sheep_vect) / (vec_length(dcd) * vec_length(right_most_fold_sheep_vect))))
    return math.acos(np.dot(dcd, right_most_fold_sheep_vect) / (vec_length(dcd) * vec_length(right_most_fold_sheep_vect)))


#* OK
def angle_between_vectors(vec1, vec2):
    """
    Calculate the angle between two vectors
    """
    return math.atan2(vec1[0], vec1[1]) - math.atan2(vec2[0], vec2[1])




#* ------------------------------------------
#! methods when dog does not detect any sheep
def see_the_bound(pos_vec, radius, bound_width, bound_height):
  if pos_vec[0] + radius > bound_width or pos_vec[0] - radius < 0:
    return True
  elif pos_vec[1] + radius > bound_height or pos_vec[1] - radius < 0:
    return True
  else:
    return False






#* ------------------------------------------