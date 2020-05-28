import random
import math
from matplotlib import pyplot as plt
import time

progress = []

def distance(points):
	length = 0
	for i in range(len(points) - 1):
		length += math.sqrt(((points[i + 1][0] - points[i][0]) ** 2) + ((points[i + 1][1] - points[i][1]) ** 2))
	return length

def hill_climb(points):

	# Initialise variables
	current_path = points
	iterations = 0

	# Keep going until best solution found
	while True:

		path_length = distance(current_path)
		progress.append(path_length)
		
		# Iterate through every possible switch, and find the best one
		min_length, path = None, None
		for i in range(len(current_path) - 1):
			for j in range(i + 1, len(current_path) - 1):
				list_swap = current_path[:]
				list_swap[i], list_swap[j] = list_swap[j], list_swap[i]
				if min_length == None:
					min_length, path = distance(list_swap), list_swap
				else:
					if distance(list_swap) < min_length:
						min_length, path = distance(list_swap), list_swap

		# If the solution is better, use it, else, break
		if min_length < path_length:
			current_path = path
			iterations += 1
		else:
			break

	print(f"Hill Climb: Done, {round(path_length, 2)} length, {iterations} iterations")

for data_points in range(10, 110, 10):
	for seed in range(10, 60, 10):
		print(f"{data_points} Data_points, Trial {int(seed/10)}")

		random.seed(seed)
		coords = [(random.randint(0, 50), random.randint(0, 50)) for i in range(data_points)]

		time_to_run = time.time()
		hill_climb(coords)
		print(f"{round(time.time() - time_to_run, 2)} seconds")

# plt.plot(range(len(progress)), progress)
# plt.show()