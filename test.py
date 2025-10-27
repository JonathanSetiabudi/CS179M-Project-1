import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import random
import os

from main import validate_file as vf
from main import search

from data_visualization import plot_points

# create the unit square, the most basic test to see if our solution is working. 
def create_unit_square(n, filename):
    coords = [[0,0] for i in range(n)]
    for i, coord in enumerate(coords):
        if i == 0:
            continue
        #randomly choose whether to write the x coordinate first or the y coordinate first
        x_or_y = random.randint(0,1)
        coord[x_or_y] = random.random()
        coord[1-x_or_y] = random.randint(0,1)
    coords = np.array(coords)
    np.savetxt(filename, coords, delimiter = '   ')

if __name__ == '__main__':
    # create t unit squares with n nodes
    if False:
        random.seed(42) # seed for reproducibility
        trials = 30
        nodes = [32, 64, 128, 256, 512, 1024]
        for t in range(trials):
            for n in nodes:
                create_unit_square(n, f"data/unit_squares/{n}/{t+1}.txt")

    # create t random location files with n nodes
    if False:
        rng = np.random.default_rng(42) # seed for reproducibility
        trials = 100 # number of runs
        nodes = [32, 64, 128, 256, 512, 1024] # number of nodes
        for t in range(trials):
            for n in nodes:
                datapath = f"data/random/{n}/{t+1}.txt"
                coords = rng.random(size=(n, 2))
                np.savetxt(datapath, coords, delimiter = '   ')

    # run trials for unit square optimality test
    if False:
        algo = 'RS' # change for each test
        nodes = [64, 128, 256, 512, 1024]
        trials = 10
        time = 1

        best_distances = []
        for n in nodes:
            distances = []
            for t in range(trials):
                data = vf(f"data/unit_squares/{n}/{t+1}.txt")
                dist, _, _ = search(algo, data, time, testing=True)
                distances.append(dist)
            print(f"Completed {trials} trials for {n} nodes unit square")
            np_distances = np.vstack(distances)
            best_distances.append(np.average(np_distances, axis=0))
        best_distances = np.concat(best_distances)
        np.savetxt(f"res/unit_square_optimality/{algo}_{trials}trials_{time}seconds", best_distances, delimiter = '   ')

    # run trials for average bsf dist over time
    if False:
        algo = 'RS' # run each algo in different bash
        t = 100 # number of runs
        n = 256
        s = 100
        output = f"res/distances/{algo}/{t}trials_{n}nodes_{s}seconds"
        distances = []

        for i in range(t):
            datapath = f"data/random/{n}/{i+1}.txt"
            data = vf(datapath)
            dist, order, over_time = search(algo, data, s, True)
            distances.append(over_time)

            # save in case something goes wrong mid trial
            np_distances = np.vstack(distances)
            np.savetxt(f"{output}_trial{i+1}.txt", np_distances)
            np.savetxt(f"{output}_trial{i+1}_average.txt", np.average(np_distances, axis=0))

            # delete previous file
            if i != 0:
                os.remove(f"{output}_trial{i}.txt")
                os.remove(f"{output}_trial{i}_average.txt")

    # visualization of distances over time
    if False:
        print()

    # visualization of unit square optimality test
    if False:
        print()


   
        
