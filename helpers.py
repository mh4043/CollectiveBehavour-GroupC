import numpy as np


def vec_length(vec: np.array) -> float: 
  return np.sqrt(vec.dot(vec))

def o(vec: np.array) -> np.array:
  return vec / vec_length(vec)

def rotation(angle: float) -> np.matrix:
  return [[np.cos(angle), -np.sin(angle)], [np.sin(angle), np.cos(angle)]]



