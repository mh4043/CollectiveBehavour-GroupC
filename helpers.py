import numpy as np


def vec_length(vec: np.array) -> float: 
  return np.sqrt(vec[0]**2 + vec[1]**2)

def unit_vector(vec: np.array) -> np.array:
  return vec / np.linalg.norm(vec)

def rotation(angle: float) -> np.matrix:
  return np.array([[np.cos(angle), -np.sin(angle)], [np.sin(angle), np.cos(angle)]])



