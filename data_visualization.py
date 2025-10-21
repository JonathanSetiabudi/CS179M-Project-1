#from nearest_neighbor_search import nearest_neighbor_search as nns
#from random_search import random_search as rs
from random_search import make_permutation as mp
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import random
# plot the coordinate points and draw lines between them.

# TODO: ask Dr. Keogh how do we average it over N runs continuously

# create the unit square, the most basic test to see if our solution is working. 
def create_unit_square(n, file_name):
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
    np.savetxt(file_name, coords, delimiter = ' ')
    

def plot_unit_square(file_name):
    square_coords = np.loadtxt(file_name)
    #permutation = mp(square_coords.shape)
    plt.figure(figsize=(6,6))
    sns.scatterplot(x = square_coords[:,0], y = square_coords[:, 1])
    plt.scatter(x=square_coords[0,0], y=square_coords[0,1], color='red', marker='o', s=50, label='Landing Pad')
    plt.title('Unit Square Plot')
    plt.xlabel('X axis')
    plt.ylabel('Y axis')
    plt.show()


def average_over_n_runs(n, algorithm, time, file_name):
    sum_dist = 0
    coords = np.loadtxt(file_name)
    for i in range(n):
        distance, _ = algorithm(coords, time)
        sum_dst += distance
    avg_dist = sum_dist / coords.shape
    return avg_dist

def plot_path_taken(data, order):
    reordered_data = data[order]
    plt.figure(figsize=(6,6))
    plt.plot(reordered_data[:, 0], reordered_data[:,1], marker = 'o', markerfacecolor = 'blue', linestyle = '-', color = "green")
    plt.title('Order taken')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.show()

if __name__ == '__main__':
    # create_unit_square(100,"unitSquare.txt")
    plot_unit_square("unitSquare.txt")
    unit_square = np.loadtxt("unitSquare.txt")
    order = mp(unit_square.shape[0])
    plot_path_taken(unit_square, order)