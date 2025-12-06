import numpy as np
from dataclasses import dataclass
import sys
from typing import Union, List, Any


#Function to get probability numbers
def Probability(value):
    if value == 0:
        return 0
    if value == 2:
        return 1/36
    if value == 3:
        return 2/36
    if value == 4:
        return 3/36
    if value == 5:
        return 4/36
    if value == 6:
        return 5/36
    if value == 7:
        return 6/36
    if value == 8:
        return 5/36
    if value == 9:
        return 4/36
    if value == 10:
        return 3/36
    if value == 11:
        return 2/36
    if value == 12:
        return 1/36


#Adjacency Matrix
Adj = np.array([
    [0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0]
])
#Add zero column and row so index matches vertex number
Adj = np.insert(Adj, 0, 0, axis=1)
Adj = np.insert(Adj, 0, 0, axis=0)
#Availablility List, index matches vertex number
Available = [None] + [-1] * 54

#Settlement and City building requirements:
Settlement = np.array([2, 2, 1, 1, 0], dtype=float) #overestimate?? maybe do need to do 2, 2 b/c SHORT GAME, tested w/ trial 1: gave Settlement when made sense w/ all 1's, should change to this??
#settlement not being chosen, if change these weights then have very different things happening . . . DR BROUSSARD
City = np.array([0, 0, 2, 0, 3], dtype=float)

#Ideal vectors for each strategy
Max_Cards = np.array([1, 1, 1, 1, 1])
Settlement_Pack = np.array([3, 3, 1, 1, 0.5])
City_Pack = np.array([0.5, 0.5, 2, 0.5, 3])
Self_Sufficient = np.array([1, 1, 1, 1, 1]) #Think about removing, lots of probs
Max_Lumber = np.array([3, 0.5, 0.5, 0.5, 0.5])
Max_Brick = np.array([0.5, 3, 0.5, 0.5, 0.5])
Max_Wheat = np.array([0.5, 0.5, 3, 0.5, 0.5])
Max_Sheep = np.array([0.5, 0.5, 0.5, 3, 0.5])
Max_Ore = np.array([0.5, 0.5, 0.5, 0.5, 3])

#Get data from file, number of players and the board
filename = sys.argv[1]
file = open(filename,"r")
Players = int(file.readline().strip())
@dataclass
class Hex:
    index: str
    prob: float
    resource: str

Hexes = {}
for i in range(19):
    line = file.readline().strip().split()
    Hexes[line[0]] = Hex(line[0], Probability(int(line[1])), line[2])


file.close()

#Define value of each vertex, matches availability list
Tile = Union[Hex, str]
@dataclass
class Vertex:
    index: int
    adjacent: list[Tile]
    available_index: int  
Vertices = [
    None,
    Vertex(1, [Hexes['A'], 'Water', 'Water'], 1), Vertex(2, [Hexes['A'], 'Water', 'Water'], 2), Vertex(3, [Hexes['A'], Hexes['B'], 'Water'], 3), Vertex(4, [Hexes['B'], 'Water', 'Wheat'], 4), Vertex(5, [Hexes['B'], Hexes['C'], 'Wheat'], 5),
    Vertex(6, [Hexes['C'], 'Water', 'Water'], 6), Vertex(7, [Hexes['C'], 'Water', 'Water'], 7), Vertex(8, [Hexes['D'], 'Water', 'Lumber'], 8), Vertex(9, [Hexes['A'], Hexes['D'], 'Water'], 9), Vertex(10, [Hexes['A'], Hexes['D'], Hexes['E']], 10),
    Vertex(11, [Hexes['A'], Hexes['B'], Hexes['E']], 11), Vertex(12, [Hexes['B'], Hexes['E'], Hexes['F']], 12), Vertex(13, [Hexes['B'], Hexes['C'], Hexes['F']], 13), Vertex(14, [Hexes['C'], Hexes['F'], Hexes['G']], 14), Vertex(15, [Hexes['C'], Hexes['G'], 'Ore'], 15),
    Vertex(16, [Hexes['G'], 'Water', 'Ore'], 16), Vertex(17, [Hexes['H'], 'Water', 'Water'], 17), Vertex(18, [Hexes['D'], Hexes['H'], 'Lumber'], 18), Vertex(19, [Hexes['D'], Hexes['H'], Hexes['I']], 19), Vertex(20, [Hexes['D'], Hexes['E'], Hexes['I']], 20),  
    Vertex(21, [Hexes['E'], Hexes['I'], Hexes['J']], 21), Vertex(22, [Hexes['E'], Hexes['F'], Hexes['J']], 22), Vertex(23, [Hexes['F'], Hexes['J'], Hexes['K']], 23), Vertex(24, [Hexes['F'], Hexes['G'], Hexes['K']], 24), Vertex(25, [Hexes['G'], Hexes['K'], Hexes['L']], 25),
    Vertex(26, [Hexes['G'], Hexes['L'], 'Water'], 26), Vertex(27, [Hexes['L'], 'Water', 'Water'], 27), Vertex(28, [Hexes['H'], 'Water', 'Water'], 28), Vertex(29, [Hexes['H'], Hexes['M'], 'Brick'], 29), Vertex(30, [Hexes['H'], Hexes['I'], Hexes['M']], 30),  
    Vertex(31, [Hexes['I'], Hexes['M'], Hexes['N']], 31), Vertex(32, [Hexes['I'], Hexes['J'], Hexes['N']], 32), Vertex(33, [Hexes['J'], Hexes['N'], Hexes['O']], 33), Vertex(34, [Hexes['J'], Hexes['K'], Hexes['O']], 34), Vertex(35, [Hexes['K'], Hexes['O'], Hexes['P']], 35),
    Vertex(36, [Hexes['K'], Hexes['L'], Hexes['P']], 36), Vertex(37, [Hexes['L'], Hexes['P'], 'Water'], 37), Vertex(38, [Hexes['L'], 'Water', 'Water'], 38), Vertex(39, [Hexes['M'], 'Water', 'Brick'], 39), Vertex(40, [Hexes['M'], Hexes['Q'], 'Water'], 40), 
    Vertex(41, [Hexes['M'], Hexes['N'], Hexes['Q']], 41), Vertex(42, [Hexes['N'], Hexes['Q'], Hexes['R']], 42), Vertex(43, [Hexes['N'], Hexes['O'], Hexes['R']], 43), Vertex(44, [Hexes['O'], Hexes['R'], Hexes['S']], 44), Vertex(45, [Hexes['O'], Hexes['P'], Hexes['S']], 45),
    Vertex(46, [Hexes['P'], Hexes['S'], 'Sheep'], 46), Vertex(47, [Hexes['P'], 'Water', 'Sheep'], 47), Vertex(48, [Hexes['Q'], 'Water', 'Water'], 48), Vertex(49, [Hexes['Q'], 'Water', 'Water'], 49), Vertex(50, [Hexes['Q'], Hexes['R'], 'Water'], 50),
    Vertex(51, [Hexes['R'], 'Water', 'Water'], 51), Vertex(52, [Hexes['R'], Hexes['S'], 'Water'], 52), Vertex(53, [Hexes['S'], 'Water', 'Water'], 53), Vertex(54, [Hexes['S'], 'Water', 'Water'], 54)
]

#Create expected value vectors for each vertex 
vert = [None]
for i in range(1, 55):
    get_vert = np.array([0.0, 0.0, 0.0, 0.0, 0.0])
    for tile in Vertices[i].adjacent:
        if isinstance(tile, Hex):
            if tile.resource == 'lumber':
                get_vert[0] += tile.prob
            elif tile.resource == 'brick':
                get_vert[1] += tile.prob
            elif tile.resource == 'wheat':
                get_vert[2] += tile.prob
            elif tile.resource == 'sheep':
                get_vert[3] += tile.prob
            elif tile.resource == 'ore':
                get_vert[4] += tile.prob    
    vert.append(get_vert)

#sanity check for expected value vectors:
#print("\nExpected Value Vectors for Each Vertex")
#print("Vertex |  Lumber   Brick   Wheat   Sheep   Ore")
#print("-----------------------------------------------")
#for i in range(1, 55):
    # Extract the vector for this vertex
    #v = vert[i]
    # Print neatly formatted values (3 decimal places)
    #print(f"{i:>6} | {v[0]:7.3f} {v[1]:7.3f} {v[2]:7.3f} {v[3]:7.3f} {v[4]:7.3f}")

#Function to determine VertexEV
def VertexEV(i, Ideal, already_have):
    if Available[i] != -1:
        return float('-inf')
    
    only_vert = Ideal.dot(vert[i] + already_have)
    two_away = set()

    for j in range(1, 55):
        if Adj[i][j] == 1:
            for k in range(1, 55):
                if Adj[j][k] == 1 and k != i and Adj[i][k] == 0:
                    two_away.add(k)

    expansion_values = []
    for p in two_away:
        if Available[p] == -1:
            expansion_values.append(Ideal.dot(vert[p]))
        
    expansion_values.sort(reverse=True)
    best_expansions = expansion_values[:3]

    return (only_vert + (1/12) * sum(best_expansions))

#Function for any player except last one in first settlement placement to determine best candidates, need to include 1st settlement when considering 2nd
def BestAvailable(Ideal, already_have, candidates=None):
    best_index = None
    max_value = float('-inf')

    if candidates is None:
        candidates = range(1, 55)

    for i in candidates:
        value = VertexEV(i, Ideal, already_have)
        if value > max_value:
            max_value = value
            best_index = i

    return best_index


#Functions for player who places two settlements at once to determine best candidates, add two vectors together to get candidate
#throw out placements adjacent to port
def BestforTwo_Lumber(Ideal):
    lumber_ports = [8, 18]
    best_combo = (None, None)
    max_value = float('-inf')

    for port in lumber_ports:
        if Available[port] != -1:
            continue

        #same temporary change logic as in BestforTwo
        Available[port] = -3
        for i in range(1, 55):
            if Adj[port][i] == 1 and Available[i] == -1:
                Available[i] = -2

        best_second = BestAvailable(Ideal, vert[port])
        if best_second is None:
            Available[port] = -1
            continue

        total_value = Ideal.dot(vert[port] + vert[best_second])

        if total_value > max_value:
            max_value = total_value
            best_combo = (port, best_second)

        Available[port] = -1
        for i in range(1, 55):
            if Adj[port][i] == 1 and Available[i] == -2:
                Available[i] = -1

    return best_combo

def BestforTwo_Brick(Ideal):
    brick_ports = [29, 39]
    best_combo = (None, None)
    max_value = float('-inf')

    for port in brick_ports:
        if Available[port] != -1:
            continue

        #same temporary change logic as in BestforTwo
        Available[port] = -3
        for i in range(1, 55):
            if Adj[port][i] == 1 and Available[i] == -1:
                Available[i] = -2

        best_second = BestAvailable(Ideal, vert[port])
        if best_second is None:
            Available[port] = -1
            continue

        total_value = Ideal.dot(vert[port] + vert[best_second])

        if total_value > max_value:
            max_value = total_value
            best_combo = (port, best_second)

        Available[port] = -1
        for i in range(1, 55):
            if Adj[port][i] == 1 and Available[i] == -2:
                Available[i] = -1

    return best_combo

def BestforTwo_Wheat(Ideal):
    wheat_ports = [4, 5]
    best_combo = (None, None)
    max_value = float('-inf')
    
    for port in wheat_ports:
        if Available[port] != -1:
            continue
             
        #same temporary change logic as in BestforTwo
        Available[port] = -3
        for i in range(1, 55):
            if Adj[port][i] == 1 and Available[i] == -1:
                Available[i] = -2

        best_second = BestAvailable(Ideal, vert[port])
        if best_second is None:
            Available[port] = -1
            continue

        total_value = Ideal.dot(vert[port] + vert[best_second])

        if total_value > max_value:
            max_value = total_value
            best_combo = (port, best_second)

        Available[port] = -1
        for i in range(1, 55):
            if Adj[port][i] == 1 and Available[i] == -2:
                Available[i] = -1

    return best_combo

def BestforTwo_Sheep(Ideal):
    sheep_ports = [46, 47]
    best_combo = (None, None)
    max_value = float('-inf')

    for port in sheep_ports:
        if Available[port] != -1:
            continue

        #same temporary change logic as in BestforTwo
        Available[port] = -3
        for i in range(1, 55):
            if Adj[port][i] == 1 and Available[i] == -1:
                Available[i] = -2


        best_second = BestAvailable(Ideal, vert[port])
        if best_second is None:
            Available[port] = -1
            continue

        total_value = Ideal.dot(vert[port] + vert[best_second])

        if total_value > max_value:
            max_value = total_value
            best_combo = (port, best_second)

        Available[port] = -1
        for i in range(1, 55):
            if Adj[port][i] == 1 and Available[i] == -2:
                Available[i] = -1

    return best_combo

def BestforTwo_Ore(Ideal):
    ore_ports = [15, 16]
    best_combo = (None, None)
    max_value = float('-inf')

    for port in ore_ports:
        if Available[port] != -1:
            continue

        Available[port] = -3
        for i in range(1, 55):
            if Adj[port][i] == 1 and Available[i] == -1:
                Available[i] = -2

        best_second = BestAvailable(Ideal, vert[port])
        if best_second is None:
            Available[port] = -1
            continue

        total_value = Ideal.dot(vert[port] + vert[best_second])

        if total_value > max_value:
            max_value = total_value
            best_combo = (port, best_second)

        Available[port] = -1
        for i in range(1, 55):
            if Adj[port][i] == 1 and Available[i] == -2:
                Available[i] = -1

    return best_combo

#With self-sucfficient strategy, need to change ideal vector each time 
def BestforTwo(Ideal):
    best_combo = (None, None)
    max_value = float('-inf')

    for i in range (1, 55):
        if Available[i] != -1:
            continue

        for j in range(i + 1, 55):
            if Available[j] != -1 or Adj[i][j] == 1:
                continue

            # -3 and -2 are temporary adjustments to keep track of what is being tested, don't want to change what Availability already has
            #-3 is temporary i and j, -2 is temporary adjacencies
            Available[i] = -3
            Available[j] = -3
            for next_to_i in range (1, 55):
                if Adj[i][next_to_i] == 1 and Available[next_to_i] == -1:
                    Available[next_to_i] = -2
            for next_to_j in range (1, 55):
                if Adj[j][next_to_j] == 1 and Available[next_to_j] == -1:
                    Available[next_to_j] = -2

            combined_vector = vert[i] + vert[j]
            only_verts = Ideal.dot(combined_vector)

            two_away_i = set()
            for c in range(1, 55):
                if Adj[i][c] == 1:
                    for k in range(1, 55):
                        if Adj[c][k] == 1 and k != i and Adj[i][k] == 0:
                            two_away_i.add(k)

            two_away_j = set()
            for a in range(1, 55):
                if Adj[j][a] == 1:
                    for b in range(1, 55):
                        if Adj[a][b] == 1 and b != j and Adj[j][b] == 0 and b not in two_away_i:
                            two_away_j.add(b)

            # for a in (i, j):
            #     for b in range(1, 55):
            #         if Adj[a][b] == 1:
            #             for c in range(1, 55):
            #                 if Adj[b][c] == 1 and c not in (i,j) and Adj[a][c] == 0:
            #                     two_away.add(c)

            expansion_values_i = []
            for p in two_away_i:
                if Available[p] == -1:
                    expansion_values_i.append(Ideal.dot(vert[p]))
            
            expansion_values_j = []       
            for p in two_away_j:
                if Available[p] == -1:
                    expansion_values_j.append(Ideal.dot(vert[p]))

            expansion_values_i.sort(reverse=True)
            best_expansions_i = expansion_values_i[:3]
            
            expansion_values_j.sort(reverse=True)
            best_expansions_j = expansion_values_j[:3]

            total_value = only_verts + (1/12) * sum(best_expansions_i) + (1/12) * sum(best_expansions_j) 

            if total_value > max_value:
                max_value = total_value
                best_combo = (i, j)
        
            #undo temporary values
            Available[i] = -1
            Available[j] = -1
            for next_to_i in range (1, 55):
                if Adj[i][next_to_i] == 1 and Available[next_to_i] == -2:
                    Available[next_to_i] = -1
            for next_to_j in range (1, 55):
                if Adj[j][next_to_j] == 1 and Available[next_to_j] == -2:
                    Available[next_to_j] = -1

    return best_combo

def BestforTwo_SelfSufficient(Ideal):
    best_combo = (None, None)
    max_value = float('-inf')

    for i in range(1, 55):
        if Available[i] != -1:
            continue

        covered_resources = vert[i] > 0
        Ideal_after_i = np.where(covered_resources, 0.5, 1.0)

        for j in range(1, 55):
            if Available[j] != -1 or Adj[i][j] == 1 or j == i:
                continue

            Available[i] = 0
            Available[j] = 0

            combined_vector = vert[i] + vert[j]
            only_verts = Ideal_after_i.dot(combined_vector)

            two_away = set()
            for a in (i, j):
                for b in range(1, 55):
                    if Adj[a][b] == 1:
                        for c in range(1, 55):
                            if Adj[b][c] == 1 and c not in (i, j) and Adj[a][c] == 0:
                                two_away.add(c)
            
            expansion_values = []
            for p in two_away:
                if Available[p] == -1:
                    expansion_values.append(Ideal.dot(vert[p]))
            
            expansion_values.sort(reverse=True)
            best_expansions = expansion_values[:3]
            total_value = only_verts + (1/12) * sum(best_expansions)

            if total_value > max_value:
                max_value = total_value
                best_combo = (i, j)

            Available[i] = -1
            Available[j] = -1
    return best_combo


#Function for testing which candidate is shortest to build city/settlement, gives where to build and which to build first

def TimeRequired_Packs(Placement_vector, turn): #works for packs and self-sufficient
    #Different for 2nd time because should have everything you are going to need
    if turn == 2:
        for i in range(0, 5):
            if(Placement_vector[i]) == 0:
                Placement_vector[i] = 1e-10
    mask_S = Settlement != 0 #to ignore resources not requried
    if not np.any(Placement_vector[mask_S] > 0):
        time_worst_S = None
    else:    
        time_resources_S = np.divide(
            Settlement,
            Placement_vector,
            out=np.full_like(Settlement, 0, dtype=float),
            where=Placement_vector != 0
        )
        time_worst_S = np.max(time_resources_S[mask_S])

    mask_C = City != 0 #to ignore resources not requried
    if not np.any(Placement_vector[mask_C] > 0):
        time_worst_C = None
    else:   
        time_resources_C = np.divide(
            City,
            Placement_vector,
            out=np.full_like(City, 0, dtype=float),
            where=Placement_vector != 0
        )
        time_worst_C = np.max(time_resources_C[mask_C])

    if time_worst_C is None and time_worst_S is None:
        return None, None
    if time_worst_C is None:
        return time_worst_S, "Settlement"
    elif time_worst_S is None:
        return time_worst_C, "City"
    else:
        if time_worst_C <= time_worst_S:
            return time_worst_C, "City"
        else:
            return time_worst_S, "Settlement"

def TimeRequired_Lumber(Placement_vector):
    L, B, W, S, O = np.copy(Placement_vector)

    if L == 0:
        return 0, None

    L_new = 3*(L/13)
    B_new = B + 6*(L/13)
    W_new = W + 2*(L/13)
    S_new = S + 2*(L/13)
    O_new = O

    Settlement_vector_Redistributed = np.array([L_new, B_new, W_new, S_new, O_new])
    mask_S = Settlement != 0
    if not np.any(Settlement_vector_Redistributed[mask_S] > 0):
        time_worst_S = None
    else:
        time_resources_S = np.divide(
            Settlement,
            Settlement_vector_Redistributed,
            out=np.full_like(Settlement, 0, dtype=float),
            where=Settlement_vector_Redistributed != 0
        )
        time_worst_S = np.max(time_resources_S[mask_S])

    L_new = 0
    B_new = B 
    W_new = W + 4*(L/10)
    S_new = S 
    O_new = O + 6*(L/10)

    City_vector_Redistributed = np.array([L_new, B_new, W_new, S_new, O_new])
    mask_C = City != 0
    if not np.any(City_vector_Redistributed[mask_C] > 0):
        time_worst_C = None
    else:
        time_resources_C = np.divide(
            City,
            City_vector_Redistributed,
            out=np.full_like(City, 0, dtype=float),
            where=City_vector_Redistributed != 0
        )
        time_worst_C = np.max(time_resources_C[mask_C])

    if time_worst_C is None and time_worst_S is None:
        return None, None
    if time_worst_C is None:
        return time_worst_S, "Settlement"
    elif time_worst_S is None:
        return time_worst_C, "City"
    else:
        if time_worst_C < time_worst_S:
            return time_worst_C, "City"
        else:
            return time_worst_S, "Settlement"

def TimeRequired_Brick(Placement_vector):
    L, B, W, S, O = np.copy(Placement_vector)

    if B == 0:
        return 0, None

    L_new = L + 6*(B/13)
    B_new = 3*(B/13)
    W_new = W + 2*(B/13)
    S_new = S + 2*(B/13)
    O_new = O

    Settlement_vector_Redistributed = np.array([L_new, B_new, W_new, S_new, O_new])
    mask_S = Settlement != 0
    if not np.any(Settlement_vector_Redistributed[mask_S] > 0):
        time_worst_S = None
    else:
        time_resources_S = np.divide(
            Settlement,
            Settlement_vector_Redistributed,
            out=np.full_like(Settlement, 0, dtype=float),
            where=Settlement_vector_Redistributed != 0
        )
        time_worst_S = np.max(time_resources_S[mask_S])

    L_new = L
    B_new = 0
    W_new = W + 4*(B/10)
    S_new = S 
    O_new = O + 6*(B/10)

    City_vector_Redistributed = np.array([L_new, B_new, W_new, S_new, O_new])
    mask_C = City != 0
    if not np.any(City_vector_Redistributed[mask_C] > 0):
        time_worst_C = None
    else:
        time_resources_C = np.divide(
            City,
            City_vector_Redistributed,
            out=np.full_like(City, 0, dtype=float),
            where=City_vector_Redistributed != 0
        )
        time_worst_C = np.max(time_resources_C[mask_C])

    if time_worst_C is None and time_worst_S is None:
        return None, None
    if time_worst_C is None:
        return time_worst_S, "Settlement"
    elif time_worst_S is None:
        return time_worst_C, "City"
    else:
        if time_worst_C < time_worst_S:
            return time_worst_C, "City"
        else:
            return time_worst_S, "Settlement"

def TimeRequired_Wheat(Placement_vector):
    L, B, W, S, O = np.copy(Placement_vector)

    if W == 0:
        return 0, None

    L_new = L + 6*(W/15)
    B_new = B + 6*(W/15)
    W_new = W/15
    S_new = S + 2*(W/15)
    O_new = O

    Settlement_vector_Redistributed = np.array([L_new, B_new, W_new, S_new, O_new])
    mask_S = Settlement != 0
    if not np.any(Settlement_vector_Redistributed[mask_S] > 0):
        time_worst_S = None
    else:
        time_resources_S = np.divide(
            Settlement,
            Settlement_vector_Redistributed,
            out=np.full_like(Settlement, 0, dtype=float),
            where=Settlement_vector_Redistributed != 0
        )
        time_worst_S = np.max(time_resources_S[mask_S])

    L_new = L
    B_new = B
    W_new = W + 2*(W/8)
    S_new = S 
    O_new = O + 6*(W/8)

    City_vector_Redistributed = np.array([L_new, B_new, W_new, S_new, O_new])
    mask_C = City != 0
    if not np.any(City_vector_Redistributed[mask_C] > 0):
        time_worst_C = None
    else:
        time_resources_C = np.divide(
            City,
            City_vector_Redistributed,
            out=np.full_like(City, 0, dtype=float),
            where=City_vector_Redistributed != 0
        )
        time_worst_C = np.max(time_resources_C[mask_C])

    if time_worst_C is None and time_worst_S is None:
        return None, None
    if time_worst_C is None:
        return time_worst_S, "Settlement"
    elif time_worst_S is None:
        return time_worst_C, "City"
    else:
        if time_worst_C < time_worst_S:
            return time_worst_C, "City"
        else:
            return time_worst_S, "Settlement"

def TimeRequired_Sheep(Placement_vector):
    L, B, W, S, O = np.copy(Placement_vector)

    if S == 0:
        return 0, None

    L_new = L + 6*(S/15)
    B_new = B + 6*(S/15)
    W_new = W + 2*(S/15)
    S_new = S/15
    O_new = O

    Settlement_vector_Redistributed = np.array([L_new, B_new, W_new, S_new, O_new])
    mask_S = Settlement != 0
    if not np.any(Settlement_vector_Redistributed[mask_S] > 0):
        time_worst_S = None
    else:
        time_resources_S = np.divide(
            Settlement,
            Settlement_vector_Redistributed,
            out=np.full_like(Settlement, 0, dtype=float),
            where=Settlement_vector_Redistributed != 0
        )
        time_worst_S = np.max(time_resources_S[mask_S])

    L_new = L
    B_new = B
    W_new = W + 4*(S/10)
    S_new = 0 
    O_new = O + 6*(S/10)

    City_vector_Redistributed = np.array([L_new, B_new, W_new, S_new, O_new])
    mask_C = City != 0
    if not np.any(City_vector_Redistributed[mask_C] > 0):
        time_worst_C = None
    else:
        time_resources_C = np.divide(
            City,
            City_vector_Redistributed,
            out=np.full_like(City, 0, dtype=float),
            where=City_vector_Redistributed != 0
        )
        time_worst_C = np.max(time_resources_C[mask_C])

    if time_worst_C is None and time_worst_S is None:
        return None, None
    if time_worst_C is None:
        return time_worst_S, "Settlement"
    elif time_worst_S is None:
        return time_worst_C, "City"
    else:
        if time_worst_C < time_worst_S:
            return time_worst_C, "City"
        else:
            return time_worst_S, "Settlement"

def TimeRequired_Ore(Placement_vector):
    L, B, W, S, O = np.copy(Placement_vector)

    if O == 0:
        return 0, None

    L_new = L + 6*(O/16)
    B_new = B + 6*(O/16)
    W_new = W + 2*(O/16)
    S_new = S + 2*(O/16)
    O_new = 0

    Settlement_vector_Redistributed = np.array([L_new, B_new, W_new, S_new, O_new])
    mask_S = Settlement != 0
    if not np.any(Settlement_vector_Redistributed[mask_S] > 0):
        time_worst_S = None
    else:
        time_resources_S = np.divide(
            Settlement,
            Settlement_vector_Redistributed,
            out=np.full_like(Settlement, 0, dtype=float),
            where=Settlement_vector_Redistributed != 0
        )
        time_worst_S = np.max(time_resources_S[mask_S])

    L_new = L
    B_new = B
    W_new = W + 4*(O/7)
    S_new = S 
    O_new = O + 3*(O/7)

    City_vector_Redistributed = np.array([L_new, B_new, W_new, S_new, O_new])
    mask_C = City != 0
    if not np.any(City_vector_Redistributed[mask_C] > 0):
        time_worst_C = None
    else:
        time_resources_C = np.divide(
            City,
            City_vector_Redistributed,
            out=np.full_like(City, 0, dtype=float),
            where=City_vector_Redistributed != 0
        )
        time_worst_C = np.max(time_resources_C[mask_C])

    if time_worst_C is None and time_worst_S is None:
        return None, None
    if time_worst_C is None:
        return time_worst_S, "Settlement"
    elif time_worst_S is None:
        return time_worst_C, "City"
    else:
        if time_worst_C < time_worst_S:
            return time_worst_C, "City"
        else:
            return time_worst_S, "Settlement"

def TimeRequired_MC(Placement_vector):
    L, B, W, S, O = np.copy(Placement_vector)
    most_index = int(np.argmax(Placement_vector))

    if most_index == 0: #redistribute lumber
        L_new = 3*(L/23)
        B_new = B + 12*(L/23)
        W_new = W + 4*(L/23)
        S_new = S + 4*(L/23)
        O_new = O

        Settlement_vector_Redistributed = np.array([L_new, B_new, W_new, S_new, O_new])
        mask_S = Settlement != 0
        if not np.any(Settlement_vector_Redistributed[mask_S] > 0):
            time_worst_S = None
        else:
            time_resources_S = np.divide(
                Settlement,
                Settlement_vector_Redistributed,
                out=np.full_like(Settlement, 0, dtype=float),
                where=Settlement_vector_Redistributed != 0
            )
            time_worst_S = np.max(time_resources_S[mask_S])

        L_new = 0
        B_new = B 
        W_new = W + 8*(L/20)
        S_new = S 
        O_new = O + 12*(L/20)

        City_vector_Redistributed = np.array([L_new, B_new, W_new, S_new, O_new])
        mask_C = City != 0
        if not np.any(City_vector_Redistributed[mask_C] > 0):
            time_worst_C = None
        else:
            time_resources_C = np.divide(
                City,
                City_vector_Redistributed,
                out=np.full_like(City, 0, dtype=float),
                where=City_vector_Redistributed != 0
            )
            time_worst_C = np.max(time_resources_C[mask_C])

    elif most_index == 1: #redistribute brick
        L_new = L + 12*(B/23)
        B_new = 3*(B/23)
        W_new = W + 4*(B/23)
        S_new = S + 4*(B/23)
        O_new = O

        Settlement_vector_Redistributed = np.array([L_new, B_new, W_new, S_new, O_new])
        mask_S = Settlement != 0
        if not np.any(Settlement_vector_Redistributed[mask_S] > 0):
            time_worst_S = None
        else:
            time_resources_S = np.divide(
                Settlement,
                Settlement_vector_Redistributed,
                out=np.full_like(Settlement, 0, dtype=float),
                where=Settlement_vector_Redistributed != 0
            )
            time_worst_S = np.max(time_resources_S[mask_S])

        L_new = L
        B_new = 0
        W_new = W + 8*(B/20)
        S_new = S 
        O_new = O + 12*(B/20)

        City_vector_Redistributed = np.array([L_new, B_new, W_new, S_new, O_new])
        mask_C = City != 0
        if not np.any(City_vector_Redistributed[mask_C] > 0):
            time_worst_C = None
        else:
            time_resources_C = np.divide(
                City,
                City_vector_Redistributed,
                out=np.full_like(City, 0, dtype=float),
                where=City_vector_Redistributed != 0
            )
            time_worst_C = np.max(time_resources_C[mask_C])

    elif most_index == 2: #redistribute wheat
        L_new = L + 12*(W/29)
        B_new = B + 12*(W/29)
        W_new = W/29
        S_new = S + 4*(W/29)
        O_new = O

        Settlement_vector_Redistributed = np.array([L_new, B_new, W_new, S_new, O_new])
        mask_S = Settlement != 0
        if not np.any(Settlement_vector_Redistributed[mask_S] > 0):
            time_worst_S = None
        else:
            time_resources_S = np.divide(
                Settlement,
                Settlement_vector_Redistributed,
                out=np.full_like(Settlement, 0, dtype=float),
                where=Settlement_vector_Redistributed != 0
            )
            time_worst_S = np.max(time_resources_S[mask_S])

        L_new = L
        B_new = B
        W_new = W + 2*(W/14)
        S_new = S 
        O_new = O + 12*(W/14)

        City_vector_Redistributed = np.array([L_new, B_new, W_new, S_new, O_new])
        mask_C = City != 0
        if not np.any(City_vector_Redistributed[mask_C] > 0):
            time_worst_C = None
        else:
            time_resources_C = np.divide(
                City,
                City_vector_Redistributed,
                out=np.full_like(City, 0, dtype=float),
                where=City_vector_Redistributed != 0
            )
            time_worst_C = np.max(time_resources_C[mask_C])

    elif most_index == 3: #redistribute sheep
        L_new = L + 12*(S/29)
        B_new = B + 12*(S/29)
        W_new = W + 4*(S/29)
        S_new = S/29
        O_new = O

        Settlement_vector_Redistributed = np.array([L_new, B_new, W_new, S_new, O_new])
        mask_S = Settlement != 0
        if not np.any(Settlement_vector_Redistributed[mask_S] > 0):
            time_worst_S = None
        else:
            time_resources_S = np.divide(
                Settlement,
                Settlement_vector_Redistributed,
                out=np.full_like(Settlement, 0, dtype=float),
                where=Settlement_vector_Redistributed != 0
            )
            time_worst_S = np.max(time_resources_S[mask_S])

        L_new = L
        B_new = B
        W_new = W + 8*(S/20)
        S_new = 0 
        O_new = O + 12*(S/20)

        City_vector_Redistributed = np.array([L_new, B_new, W_new, S_new, O_new])
        mask_C = City != 0
        if not np.any(City_vector_Redistributed[mask_C] > 0):
            time_worst_C = None
        else:
            time_resources_C = np.divide(
                City,
                City_vector_Redistributed,
                out=np.full_like(City, 0, dtype=float),
                where=City_vector_Redistributed != 0
            )
            time_worst_C = np.max(time_resources_C[mask_C])

    else: #redistribute ore
        L_new = L + 12*(O/32)
        B_new = B + 12*(O/32)
        W_new = W + 4*(O/32)
        S_new = S + 4*(O/32)
        O_new = 0

        Settlement_vector_Redistributed = np.array([L_new, B_new, W_new, S_new, O_new])
        mask_S = Settlement != 0
        if not np.any(Settlement_vector_Redistributed[mask_S] > 0):
            time_worst_S = None
        else:
            time_resources_S = np.divide(
                Settlement,
                Settlement_vector_Redistributed,
                out=np.full_like(Settlement, 0, dtype=float),
                where=Settlement_vector_Redistributed != 0
            )
            time_worst_S = np.max(time_resources_S[mask_S])

        L_new = L
        B_new = B
        W_new = W + 8*(O/11)
        S_new = S 
        O_new = O + 3*(O/11)

        City_vector_Redistributed = np.array([L_new, B_new, W_new, S_new, O_new])
        mask_C = City != 0
        if not np.any(City_vector_Redistributed[mask_C] > 0):
            time_worst_C = None
        else:
            time_resources_C = np.divide(
                City,
                City_vector_Redistributed,
                out=np.full_like(City, 0, dtype=float),
                where=City_vector_Redistributed != 0
            )
            time_worst_C = np.max(time_resources_C[mask_C])

    if time_worst_C is None and time_worst_S is None:
        return None, None
    if time_worst_C is None:
        return time_worst_S, "Settlement"
    elif time_worst_S is None:
        return time_worst_C, "City"
    else:
        if time_worst_C < time_worst_S:
            return time_worst_C, "City"
        else:
            return time_worst_S, "Settlement"

#Update Availability List
def update_Availability(Available, Adj, player_index, placements):

    if isinstance(placements, int):
        placements = [placements]
    
    for v in placements:
        
        if Available[v] > 0:
            print(f"Warning: Vertex {v} already occupied by player {Available[v]}")
            continue

        elif Available[v] == 0:
            print(f"Warning: Vertex {v} unavailable to build at")
            continue

        Available[v] = player_index

        for j in range(1, len(Available)):
            if Adj[v][j] == 1 and Available[j] == -1:
                Available[j] = 0
              
def safe_time_required(resource, vert_array, current_production, time_function):
    if resource is not None:
        return time_function(vert_array[resource] + current_production)
    else:
        return 0, None


# Check for working correctly
# print("\n=== Best Single Placements ===")
# MC = BestAvailable(Max_Cards)
# print(f"Max Cards: Vertex {MC}")

# SP = BestAvailable(Settlement_Pack)
# print(f"Settlement Pack: Vertex {SP}")

# CP = BestAvailable(City_Pack)
# print(f"City Pack: Vertex {CP}")

# SS = BestAvailable(Self_Sufficient_Initial)
# print(f"Self-Sufficient: Vertex {SS}")

# ML = BestAvailable(Max_Lumber)
# print(f"Max Lumber: Vertex {ML}")

# MB = BestAvailable(Max_Brick)
# print(f"Max Brick: Vertex {MB}")

# MW = BestAvailable(Max_Wheat)
# print(f"Max Wheat: Vertex {MW}")

# MS = BestAvailable(Max_Sheep)
# print(f"Max Sheep: Vertex {MS}")

# MO = BestAvailable(Max_Ore)
# print(f"Max Ore: Vertex {MO}")

# print("\n=== Best Two-Settlement Placements ===")
# MC2 = BestforTwo(Max_Cards)
# print(f"Max Cards (2): Vertices {MC2[0]} & {MC2[1]}")

# SP2 = BestforTwo(Settlement_Pack)
# print(f"Settlement Pack (2): Vertices {SP2[0]} & {SP2[1]}")

# CP2 = BestforTwo(City_Pack)
# print(f"City Pack (2): Vertices {CP2[0]} & {CP2[1]}")

# SS2 = BestforTwo_SelfSufficient(Self_Sufficient_Initial)
# print(f"Self-Sufficient (2): Vertices {SS2[0]} & {SS2[1]}")

# ML2 = BestforTwo_Lumber(Max_Lumber)
# print(f"Max Lumber (2): Vertices {ML2[0]} & {ML2[1]}")

# MB2 = BestforTwo_Brick(Max_Brick)
# print(f"Max Brick (2): Vertices {MB2[0]} & {MB2[1]}")

# MW2 = BestforTwo_Wheat(Max_Wheat)
# print(f"Max Wheat (2): Vertices {MW2[0]} & {MW2[1]}")

# MS2 = BestforTwo_Sheep(Max_Sheep)
# print(f"Max Sheep (2): Vertices {MS2[0]} & {MS2[1]}")

# MO2 = BestforTwo_Ore(Max_Ore)
# print(f"Max Ore (2): Vertices {MO2[0]} & {MO2[1]}")

# print("\n========== PACK STRATEGIES ==========")

# placement_vector = vert[SP2[0]] + vert[SP2[1]]
# time, next_build = TimeRequired_Packs(placement_vector)
# print(f"[SP2] Next build: {next_build:<10} | Estimated time: {time:.2f}")

# placement_vector = vert[CP2[0]] + vert[CP2[1]]
# time, next_build = TimeRequired_Packs(placement_vector)
# print(f"[CP2] Next build: {next_build:<10} | Estimated time: {time:.2f}")

# placement_vector = vert[SS2[0]] + vert[SS2[1]]
# time, next_build = TimeRequired_Packs(placement_vector)
# print(f"[SS2] Next build: {next_build:<10} | Estimated time: {time:.2f}")

# print("\n========== 2:1 PORT STRATEGIES ==========")

# placement = vert[ML2[0]] + vert[ML2[1]]
# time, next_build = TimeRequired_Lumber(placement)
# print(f"[Lumber Port] Next build: {next_build:<10} | Expected turns: {time:.2f}")

# placement = vert[MB2[0]] + vert[MB2[1]]
# time, next_build = TimeRequired_Brick(placement)
# print(f"[Brick Port]  Next build: {next_build:<10} | Expected turns: {time:.2f}")

# placement = vert[MW2[0]] + vert[MW2[1]]
# time, next_build = TimeRequired_Wheat(placement)
# print(f"[Wheat Port]  Next build: {next_build:<10} | Expected turns: {time:.2f}")

# placement = vert[MS2[0]] + vert[MS2[1]]
# time, next_build = TimeRequired_Sheep(placement)
# print(f"[Sheep Port]  Next build: {next_build:<10} | Expected turns: {time:.2f}")

# placement = vert[MO2[0]] + vert[MO2[1]]
# time, next_build = TimeRequired_Ore(placement)
# print(f"[Ore Port]    Next build: {next_build:<10} | Expected turns: {time:.2f}")

# print("\n========== MAX CARDS (4:1 PORT) STRATEGY ==========")

# placement = vert[MC2[0]] + vert[MC2[1]]
# time, next_build = TimeRequired_MC(placement)
# print(f"[MC2] Next build: {next_build:<10} | Expected turns: {time:.2f}")

player_results = []
if Players == 3:
    for i in range(1, 6):
        player_index = i
        current_production = np.array([0, 0, 0, 0, 0])

        if i == 3:
            player_index = 3

            MC = BestforTwo(Max_Cards)
            SP = BestforTwo(Settlement_Pack)
            CP = BestforTwo(City_Pack)
            SS = BestforTwo_SelfSufficient(Self_Sufficient)
            ML = BestforTwo_Lumber(Max_Lumber)
            MB = BestforTwo_Brick(Max_Brick)
            MW = BestforTwo_Wheat(Max_Wheat)
            MS = BestforTwo_Sheep(Max_Sheep)
            MO = BestforTwo_Ore(Max_Ore)

            MC_time, MC_next_build = TimeRequired_MC(vert[MC[0]] + vert[MC[1]])
            SP_time, SP_next_build = TimeRequired_Packs(vert[SP[0]] + vert[SP[1]], 2)
            CP_time, CP_next_build = TimeRequired_Packs(vert[CP[0]] + vert[CP[1]], 2)
            SS_time, SS_next_build = TimeRequired_Packs(vert[SS[0]] + vert[SS[1]], 2)
            ML_time, ML_next_build = TimeRequired_Lumber(vert[ML[0]] + vert[ML[1]])
            MB_time, MB_next_build = TimeRequired_Brick(vert[MB[0]] + vert[MB[1]])
            MW_time, MW_next_build = TimeRequired_Wheat(vert[MW[0]] + vert[MW[1]])
            MS_time, MS_next_build = TimeRequired_Sheep(vert[MS[0]] + vert[MS[1]])
            MO_time, MO_next_build = TimeRequired_Ore(vert[MO[0]] + vert[MO[1]])

            options = {
            "MC": (MC_time, MC_next_build, MC),
            "SP": (SP_time, SP_next_build, SP),
            "CP": (CP_time, CP_next_build, CP),
            "SS": (SS_time, SS_next_build, SS),
            "ML": (ML_time, ML_next_build, ML),
            "MB": (MB_time, MB_next_build, MB),
            "MW": (MW_time, MW_next_build, MW),
            "MS": (MS_time, MS_next_build, MS),
            "MO": (MO_time, MO_next_build, MO)
            }

        else:
            if i == 6:
                player_index = 1
                player1_vertex = Available.index(1)
                current_production = vert[player1_vertex].copy()
                Self_Sufficient = np.where(current_production > 0, 0.5, 1.0)

            elif i == 5:
                player_index = 2
                player2_vertex = Available.index(2)
                current_production = vert[player2_vertex].copy()
                Self_Sufficient = np.where(current_production > 0, 0.5, 1.0)

            MC = BestAvailable(Max_Cards, current_production)
            SP = BestAvailable(Settlement_Pack, current_production)
            CP = BestAvailable(City_Pack, current_production)
            SS = BestAvailable(Self_Sufficient, current_production)
            if i > 3:
                ML = BestAvailable(Max_Lumber, current_production, candidates=[8, 18])
                MB = BestAvailable(Max_Brick, current_production, candidates=[29, 39])
                MW = BestAvailable(Max_Wheat, current_production, candidates=[4, 5])
                MS = BestAvailable(Max_Sheep, current_production, candidates=[46, 47])
                MO = BestAvailable(Max_Ore, current_production, candidates=[15, 16])
            elif i > 1:
                ML = BestAvailable(Max_Lumber, current_production)
                MB = BestAvailable(Max_Brick, current_production)
                MW = BestAvailable(Max_Wheat, current_production)
                MS = BestAvailable(Max_Sheep, current_production)
                MO = BestAvailable(Max_Ore, current_production)
            else:
                ML = None
                MB = None
                MW = None
                MS = None
                MO = None

            MC_time, MC_next_build = TimeRequired_MC(vert[MC] + current_production)
            if i > 3:
                SP_time, SP_next_build = TimeRequired_Packs(vert[SP] + current_production, 2)
                CP_time, CP_next_build = TimeRequired_Packs(vert[CP] + current_production, 2)
                SS_time, SS_next_build = TimeRequired_Packs(vert[SS] + current_production, 2)
            else:
                SP_time, SP_next_build = TimeRequired_Packs(vert[SP] + current_production, 1)
                CP_time, CP_next_build = TimeRequired_Packs(vert[CP] + current_production, 1)
                SS_time, SS_next_build = TimeRequired_Packs(vert[SS] + current_production, 1)

            if i > 1:
                ML_time, ML_next_build = safe_time_required(ML, vert, current_production, TimeRequired_Lumber)
                MB_time, MB_next_build = safe_time_required(MB, vert, current_production, TimeRequired_Brick)
                MW_time, MW_next_build = safe_time_required(MW, vert, current_production, TimeRequired_Wheat)
                MS_time, MS_next_build = safe_time_required(MS, vert, current_production, TimeRequired_Sheep)
                MO_time, MO_next_build = safe_time_required(MO, vert, current_production, TimeRequired_Ore)
            else:
                ML_time = 0
                ML_next_build = None
                MB_time = 0
                MB_next_build = None
                MW_time = 0
                MW_next_build = None
                MS_time = 0
                MS_next_build = None
                MO_time = 0
                MO_next_build = None

            options = {
            "MC": (MC_time, MC_next_build, MC),
            "SP": (SP_time, SP_next_build, SP),
            "CP": (CP_time, CP_next_build, CP),
            "SS": (SS_time, SS_next_build, SS),
            "ML": (ML_time, ML_next_build, ML),
            "MB": (MB_time, MB_next_build, MB),
            "MW": (MW_time, MW_next_build, MW),
            "MS": (MS_time, MS_next_build, MS),
            "MO": (MO_time, MO_next_build, MO)
            }

        valid_options = [k for k in options if options[k][0] > 0]
        best_key = min(valid_options, key=lambda k: options[k][0])
        best_time, best_next_build, best_placement = options[best_key]

        player_results.append({
        "player": player_index,
        "strategy": best_key,
        "time": best_time,
        "next_build": best_next_build,
        "placement": best_placement
        })

        update_Availability(Available, Adj, player_index, best_placement)

else:
    for i in range(1, 8):
        player_index = i
        current_production = np.array([0, 0, 0, 0, 0])

        if i == 4:
            player_index = 4

            MC = BestforTwo(Max_Cards)
            SP = BestforTwo(Settlement_Pack)
            CP = BestforTwo(City_Pack)
            SS = BestforTwo_SelfSufficient(Self_Sufficient)
            ML = BestforTwo_Lumber(Max_Lumber)
            MB = BestforTwo_Brick(Max_Brick)
            MW = BestforTwo_Wheat(Max_Wheat)
            MS = BestforTwo_Sheep(Max_Sheep)
            MO = BestforTwo_Ore(Max_Ore)

            MC_time, MC_next_build = TimeRequired_MC(vert[MC[0]] + vert[MC[1]])
            SP_time, SP_next_build = TimeRequired_Packs(vert[SP[0]] + vert[SP[1]], 2)
            CP_time, CP_next_build = TimeRequired_Packs(vert[CP[0]] + vert[CP[1]], 2)
            SS_time, SS_next_build = TimeRequired_Packs(vert[SS[0]] + vert[SS[1]], 2)
            ML_time, ML_next_build = TimeRequired_Lumber(vert[ML[0]] + vert[ML[1]])
            MB_time, MB_next_build = TimeRequired_Brick(vert[MB[0]] + vert[MB[1]])
            MW_time, MW_next_build = TimeRequired_Wheat(vert[MW[0]] + vert[MW[1]])
            MS_time, MS_next_build = TimeRequired_Sheep(vert[MS[0]] + vert[MS[1]])
            MO_time, MO_next_build = TimeRequired_Ore(vert[MO[0]] + vert[MO[1]])

            options = {
            "MC": (MC_time, MC_next_build, MC),
            "SP": (SP_time, SP_next_build, SP),
            "CP": (CP_time, CP_next_build, CP),
            "SS": (SS_time, SS_next_build, SS),
            "ML": (ML_time, ML_next_build, ML),
            "MB": (MB_time, MB_next_build, MB),
            "MW": (MW_time, MW_next_build, MW),
            "MS": (MS_time, MS_next_build, MS),
            "MO": (MO_time, MO_next_build, MO)
            }

        else:
            if i == 7:
                player_index = 1
                player1_vertex = Available.index(1)
                current_production = vert[player1_vertex].copy()
                Self_Sufficient = np.where(current_production > 0, 0.5, 1.0)

            elif i == 6:
                player_index = 2
                player2_vertex = Available.index(2)
                current_production = vert[player2_vertex].copy()
                Self_Sufficient = np.where(current_production > 0, 0.5, 1.0)

            elif i == 5:
                player_index = 3
                player3_vertex = Available.index(3)
                current_production = vert[player3_vertex].copy()
                Self_Sufficient = np.where(current_production > 0, 0.5, 1.0)

            MC = BestAvailable(Max_Cards, current_production)
            SP = BestAvailable(Settlement_Pack, current_production)
            CP = BestAvailable(City_Pack, current_production)
            SS = BestAvailable(Self_Sufficient, current_production)
            if i > 4:
                ML = BestAvailable(Max_Lumber, current_production, candidates=[8, 18])
                MB = BestAvailable(Max_Brick, current_production, candidates=[29, 39])
                MW = BestAvailable(Max_Wheat, current_production, candidates=[4, 5])
                MS = BestAvailable(Max_Sheep, current_production, candidates=[46, 47])
                MO = BestAvailable(Max_Ore, current_production, candidates=[15, 16])
            elif i > 2:
                ML = BestAvailable(Max_Lumber, current_production)
                MB = BestAvailable(Max_Brick, current_production)
                MW = BestAvailable(Max_Wheat, current_production)
                MS = BestAvailable(Max_Sheep, current_production)
                MO = BestAvailable(Max_Ore, current_production)
            else:
                ML = None
                MB = None
                MW = None
                MS = None
                MO = None

            MC_time, MC_next_build = TimeRequired_MC(vert[MC] + current_production)
            if i > 4:
                SP_time, SP_next_build = TimeRequired_Packs(vert[SP] + current_production, 2)
                CP_time, CP_next_build = TimeRequired_Packs(vert[CP] + current_production, 2)
                SS_time, SS_next_build = TimeRequired_Packs(vert[SS] + current_production, 2)
            else:
                SP_time, SP_next_build = TimeRequired_Packs(vert[SP] + current_production, 1)
                CP_time, CP_next_build = TimeRequired_Packs(vert[CP] + current_production, 1)
                SS_time, SS_next_build = TimeRequired_Packs(vert[SS] + current_production, 1)

            if i > 2:
                ML_time, ML_next_build = safe_time_required(ML, vert, current_production, TimeRequired_Lumber)
                MB_time, MB_next_build = safe_time_required(MB, vert, current_production, TimeRequired_Brick)
                MW_time, MW_next_build = safe_time_required(MW, vert, current_production, TimeRequired_Wheat)
                MS_time, MS_next_build = safe_time_required(MS, vert, current_production, TimeRequired_Sheep)
                MO_time, MO_next_build = safe_time_required(MO, vert, current_production, TimeRequired_Ore)
            else:
                ML_time = 0
                ML_next_build = None
                MB_time = 0
                MB_next_build = None
                MW_time = 0
                MW_next_build = None
                MS_time = 0
                MS_next_build = None
                MO_time = 0
                MO_next_build = None

            options = {
            "MC": (MC_time, MC_next_build, MC),
            "SP": (SP_time, SP_next_build, SP),
            "CP": (CP_time, CP_next_build, CP),
            "SS": (SS_time, SS_next_build, SS),
            "ML": (ML_time, ML_next_build, ML),
            "MB": (MB_time, MB_next_build, MB),
            "MW": (MW_time, MW_next_build, MW),
            "MS": (MS_time, MS_next_build, MS),
            "MO": (MO_time, MO_next_build, MO)
            }

        valid_options = [k for k in options if options[k][0] > 0]
        best_key = min(valid_options, key=lambda k: options[k][0])
        best_time, best_next_build, best_placement = options[best_key]

        player_results.append({
        "player": player_index,
        "strategy": best_key,
        "time": best_time,
        "next_build": best_next_build,
        "placement": best_placement
        })

        update_Availability(Available, Adj, player_index, best_placement)


for result in player_results:
    player = result["player"]
    strategy = result["strategy"]
    time = result["time"]
    next_build = result["next_build"]
    placement = result["placement"]

    if isinstance(placement, tuple):
        placement_str = f"Vertices {placement[0]} and {placement[1]}"
    else:
        placement_str = f"Vertex {placement}"

    print(f"Player {player}:")
    print(f"  Strategy: {strategy}")
    print(f"  Time Required: {time:.5f}")
    print(f"  Next Build: {next_build}")
    print(f"  Placement: {placement_str}")
    print("-" * 40)