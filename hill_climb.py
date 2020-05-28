import random
import math
import time
from copy import deepcopy


def distance(points):
	length = 0
	for i in range(len(points) - 1):
		length += math.sqrt(((points[i + 1][0] - points[i][0]) ** 2) + ((points[i + 1][1] - points[i][1]) ** 2))
	return length


def swap(arr, i, j): 
	arr[i], arr[j] = arr[j], arr[i]


def hill_climb(points):

	# Initialise variables
	current_path = points
	iterations = 0

	# Keep going until best solution found
	while True:

		path_length = distance(current_path)
		
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


def simulated_annealing(points):

	# Initialise variables
	current_path = points
	iterations = 0
	temperature = 50
	cool_rate = 0.95
	no_progress = 0

	# Keep going till broken out of
	while True:

		path_length = distance(current_path)
		
		# Go through all possible swaps
		for i in range(len(current_path) - 1):
			for j in range(i + 1, len(current_path) - 1):
				list_swap = current_path[:]
				list_swap[i], list_swap[j] = list_swap[j], list_swap[i]

				# If a swap is good, do it instantly
				if distance(list_swap) < path_length:
					current_path = list_swap
					iterations += 1
					temperature *= cool_rate
					no_progress = 0
					break

				# If it's bad, do it at a chance based on temperature
				elif distance(list_swap) > path_length:
					prob = math.exp((path_length - distance(list_swap)) / temperature)
					if random.choices([0, 1], [1 - prob, prob])[0]:
						current_path = list_swap
						iterations += 1
						temperature *= cool_rate
						no_progress = 0
						break

			# If not swapped, continue
			else:
				continue

			# If swapped, break out of loop
			break

		# If not broken ever, no swaps done
		else:
			no_progress += 1

		# If no progress for 6 trials, end
		if no_progress == 6:
			break

	print(f"Simulated Annealing: Done, {path_length} length, {iterations} iterations")


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
		else:
			no_progress += 1

		# If no_progress == 21, break
		if no_progress == 21:
			break

	print(f"Evolutionary: Done, {min_distance} length, {iterations} iterations")


for func in [hill_climb, simulated_annealing, evo]:
	for data_points in range(10, 110, 10):
		for seed in range(10, 60, 10):
			print(f"{data_points} Data_points, Trial {int(seed/10)}")

			random.seed(seed)
			coords = [(random.randint(0, 50), random.randint(0, 50)) for i in range(data_points)]

			time_to_run = time.time()
			func(coords)
			print(f"{round(time.time() - time_to_run, 2)} seconds")
