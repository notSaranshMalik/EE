import random
import math
from matplotlib import pyplot as plt
from copy import deepcopy
import time

progress = []

def distance(points):
	length = 0
	for i in range(len(points) - 1):
		length += math.sqrt(((points[i + 1][0] - points[i][0]) ** 2) + ((points[i + 1][1] - points[i][1]) ** 2))
	return length

def swap(arr, i, j): 
	arr[i], arr[j] = arr[j], arr[i]

def evo(points):

	# Initialise variables
	strands = 100
	strands_chosen = int(strands/2)
	strands_chosen_2 = int(strands_chosen/2)
	paths = [random.sample(points, len(points)) for i in range(strands)]
	min_distance = min([distance(i) for i in paths])
	iterations = 0
	no_progress = 0

	# Keep going till broken out of
	while True:

		# Pick top
		paths = sorted(paths, key = lambda x: distance(x))
		adults = deepcopy(paths)[:strands_chosen]

		# Crossover to produce children
		children = deepcopy(adults)[:strands_chosen_2]
		for i in range(strands_chosen_2):
			if adults[i].index(adults[i+strands_chosen_2][0]) > adults[i].index(adults[i+strands_chosen_2][1]):
				swap(children[i], adults[i].index(adults[i+strands_chosen_2][0]), adults[i].index(adults[i+strands_chosen_2][1]))

		# Multiplying the number of children
		child_2 = []
		for i in range(int((strands - (strands_chosen_2 * 3)) / strands_chosen_2)):
			child_2 += deepcopy(children)
		children += child_2

		# Mutate the children
		for i in range(strands_chosen):
			if random.randint(0, 1):
				swap_indexes = (random.randint(0, data_points - 1), random.randint(0, data_points - 1))
				swap(children[i], swap_indexes[0], swap_indexes[1])

		# If min_distance not smaller, no_progress += 1, else, no_progress = 0
		paths = adults + children
		iterations += 1
		if (x := min([distance(i) for i in paths])) < min_distance:
			min_distance = x
			no_progress = 0
			progress.append(x)
		else:
			no_progress += 1
			progress.append(x)

		# If no_progress == 21, break
		if no_progress == 21:
			break

	print(f"Evolutionary: Done, {min_distance} length, {iterations} iterations")

for data_points in range(10, 110, 10):
	for seed in range(10, 60, 10):
		print(f"{data_points} Data_points, Trial {int(seed/10)}")

		random.seed(seed)
		coords = [(random.randint(0, 50), random.randint(0, 50)) for i in range(data_points)]

		time_to_run = time.time()
		evo(coords)
		print(f"{round(time.time() - time_to_run, 2)} seconds")

# plt.plot(range(len(progress)), progress)
# plt.show()
