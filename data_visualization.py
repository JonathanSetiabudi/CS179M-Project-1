from nearest_neighbor_search import nearest_neighbor_search as nns
from random_search import random_search as rs
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import random

def plot_points(filename):
    coords = np.loadtxt(filename)
    plt.figure(figsize=(6,6))
    sns.scatterplot(x=coords[:,0], y=coords[:, 1])
    plt.scatter(x=coords[0,0], y=coords[0,1], color='red', marker='o', s=50, label='Landing Pad')
    plt.title('Locations')
    plt.xlabel('X axis')
    plt.ylabel('Y axis')
    plt.show()

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
    plt.plot(np.arange(0, distances.shape[0]), np.average(distances, axis=0))
    plt.title(f'{algorithm} average best so far distance over {time} seconds, {trials} trials')
    plt.xlabel('Time (seconds)')
    plt.ylabel('Distance')
    plt.show()

