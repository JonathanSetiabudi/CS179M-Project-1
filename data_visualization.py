from nearest_neighbor_search import nearest_neighbor_search as nns
from random_search import random_search as rs
from user_interface import validate_file as vf
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
    plt.title('Order taken')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.savefig(filename)

def plot_over_time(distances, algorithm, time, trials):
    plt.figure(figsize=(6,6))
    print(distances.shape)
    plt.plot(distances, np.arange(0, distances))
    plt.title(f'{algorithm} average best so far distance over {time} seconds, {trials} trials')
    plt.xlabel('Time (seconds)')
    plt.ylabel('Distance')
    plt.show()

def get_average_distances(distances):
    return np.sum(distances, axis=0)

def save_distances(distances, filename):
    np.savetxt(filename, distances)

if __name__ == '__main__':
    filename = "data/256Cashew.txt"
    #create_unit_square(100,"data/100unitSquare.txt")
    #plot_unit_square(filename)
    locations = vf(filename)

    # algorithm = 'RS'
    # time = 10
    # trials = 3
    # distances = []
    # for i in range(trials):
    #     dist, order, over_time = rs(locations, 10, True)
    #     distances.append(over_time)

    # for d in distances:
    #     print(len(d))

    # distances = np.vstack(distances)
    # print(distances.shape)
    # print(distances)
    # print(get_average_distances(distances))
    # save_distances(distances, f"res/{algorithm}{trials}T{time}S")
    # plot_over_time(get_average_distances(distances), "Random Search", time, trials)
    #plot_path_taken(locations, order)

    time = [1, 100, 1000]
    algorithm = "RS"
    for t in time:
        dist, order = rs(locations, t)
        plot_path_taken(locations, order, f"res/path_visuals/{algorithm}{dist}256Cashew{t}S.png")
        
