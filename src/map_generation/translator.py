import time
from math import sqrt
from timeit import timeit


def translator(start, goal, node_list, algorithm, ignore_path=False):
    '''
    A method that translates start, goal and path for the algorithm.
    Also measures and prints time spent on running algorithm.
    THIS IS WHERE THE FUNCTION CALL FINALLY HAPPENS.

        Parameters:
            node_list (list) : list containing Nodes.
            start and goal (tuples): tuples of cordinates corresponding to the start and the goal of path.
            algorithm (function): A function that takes inputs start, goal and node_map.

        Returns:
            result (dict): The reusults of the algorithm, exept the paht has been translated to x, y cordinates and runtime has been added.
    '''
    size = int(sqrt(len(node_list)))
    translated_start = start[1] * size + start[0]
    translated_goal = goal[1] * size + goal[0]

    start_time = time.time()
    result = algorithm(translated_start, translated_goal, node_list)
    end_time = time.time()
    if not ignore_path:
        translated_path = []
        for node in result['path']:
            translated_path.append((node % size, node // size))

        result['path'] = translated_path
    result['time'] = end_time - start_time

    for node in node_list:
        node.reset()

    return result
