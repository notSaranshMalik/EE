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
		progress.append(path_length)
		
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

for data_points in range(10, 110, 10):
	for seed in range(10, 60, 10):
		print(f"{data_points} Data_points, Trial {int(seed/10)}")

		random.seed(seed)
		coords = [(random.randint(0, 50), random.randint(0, 50)) for i in range(data_points)]

		time_to_run = time.time()
		simulated_annealing(coords)
		print(f"{round(time.time() - time_to_run, 2)} seconds")

# plt.plot(range(len(progress)), progress)
# plt.show()