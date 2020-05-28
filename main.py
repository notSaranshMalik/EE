
from hill_climb import hill_climb, simulated_annealing, evo

for func in [hill_climb, simulated_annealing, evo]:
	for data_points in range(10, 110, 10):
		for seed in range(10, 60, 10):
			print(f"{data_points} Data_points, Trial {int(seed/10)}")

			random.seed(seed)
			coords = [(random.randint(0, 50), random.randint(0, 50)) for i in range(data_points)]

			time_to_run = time.time()
			func(coords)
			print(f"{round(time.time() - time_to_run, 2)} seconds")