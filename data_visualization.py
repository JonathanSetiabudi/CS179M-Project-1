from nearest_neighbor_search import nearest_neighbor_search as nns
from random_search import random_search as rs
from main import validate_file as vf
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import random

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
    print(coords)
    np.savetxt(filename, coords, delimiter = '   ')
    

def plot_unit_square(filename):
    square_coords = np.loadtxt(filename)
    #permutation = mp(square_coords.shape)
    plt.figure(figsize=(6,6))
    sns.scatterplot(x = square_coords[:,0], y = square_coords[:, 1])
    plt.scatter(x=square_coords[0,0], y=square_coords[0,1], color='red', marker='o', s=50, label='Landing Pad')
    plt.title('Unit Square Plot')
    plt.xlabel('X axis')
    plt.ylabel('Y axis')
    plt.show()

def average_over_n_runs(n, algorithm, time, filename):
    sum_dist = 0
    coords = np.loadtxt(filename)
    for i in range(n):
        distance, _ = algorithm(coords, time)
        sum_dst += distance
    avg_dist = sum_dist / coords.shape
    return avg_dist

def plot_path_taken(data, order, filename):
    reordered_data = data[order]
    plt.figure(figsize=(6,6))
    plt.plot(reordered_data[:, 0], reordered_data[:,1], marker = 'o', markerfacecolor = 'blue', linestyle = '-', color = "green")
    plt.plot(data[0,0], data[0,1], marker = 'o', markerfacecolor = 'red', color = "green")
    plt.title('Order taken')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.savefig(filename)

def plot_over_time(distances, algorithm, time, trials):
    plt.figure(figsize=(6,6))
    print(distances.shape)
    plt.plot(np.arange(0, distances.shape[0]), distances)
    plt.title(f'{algorithm} average best so far distance over {time} seconds, {trials} trials')
    plt.xlabel('Time (seconds)')
    plt.ylabel('Distance')
    plt.show()

def get_average_distances(distances):
    return np.average(distances, axis=0)

def save_distances(distances, filename):
    np.savetxt(filename, distances)

if __name__ == '__main__':
    # create unit squares
    if False:
        nodes = [64, 128, 256, 512, 1024]

        for n in nodes:
            create_unit_square(n, f"data/unit_squares/{n}.txt")
    
    # unit square optimality test
    if False:
        nodes = [64, 128, 256, 512, 1024]
        trials = 30
        for n in nodes:
            data = vf(f"data/unit_squares/{n}.txt")
            for t in range(trials):
                rs_dist, _ = rs(data, 10)

                nns_dist, _ = nns(data, 10)


    # average bsf dist over time
    if True:
        data = vf("data/256Cashew.txt")

    #
    if False:
        print()


   
        
