from random import randint, seed
from time import time

from drawing_functions.draw_plots import draw_plots
from get_grid import get_grid
from algorithms.fringe_search import fringe_search
from algorithms.a_star import a_star

# Num of datapoint per side
data_resolution = 100

# Using randon seed so sitsuations are recreatable
# randomseed 9 weird
random_seed = 947  # randint(1, 1000)
print(f"RANDOM SEED: {random_seed}")
seed(random_seed)

# z is a  2d array where the values represent the hight
data_map = get_grid(data_resolution, random_seed)

# Random start and goal
start = (randint(1, data_resolution//2), 10)
goal = (randint(data_resolution//2, data_resolution-1), data_resolution-10)

print(f"start: {start}   goal: {goal}")

# Running the algorithms and measuring their performance
a_time = time()
a_star_result = a_star(start, goal, data_map)
b_time = time()
dijkstra_result = a_star(start, goal, data_map, lambda x, y, z: 0)
c_time = time()
fringe_result = fringe_search(start, goal, data_map)
d_time = time()

# Printing the stats
print(f"a star       \ttime: {b_time-a_time}\t  cost: {a_star_result['cost']}")
print(
    f"dijkstra     \ttime: {c_time-b_time}\t  cost: {dijkstra_result['cost']}")
print(f"fringe search\ttime: {d_time-c_time}\t  cost: {fringe_result['cost']}")

# Drawing the visualization
draw_plots(data_map, a_star_result, dijkstra_result,
           fringe_result, start, goal)
