from math import sqrt
from functools import cache
import numpy as np

SQRT2 = 1.4142135623730950488016887242096980785696718


@cache
def heurestic(start_node,  goal_node, size):
    '''
    Gives an estimate of cost from a point to the goal.
    '''
    x_diff = goal_node.position[1] - start_node.position[1]
    y_diff = goal_node.position[0] - start_node.position[0]
    z_diff = goal_node.height - start_node.height

    return sqrt(x_diff**2 + y_diff**2 + z_diff**2)


def djikstra_heurestic(x, y, z):
    return 0
