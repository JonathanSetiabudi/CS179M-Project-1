from nearest_neighbor_search import nearest_neighbor_helper as nnh
from user_interface import validate_file as vf
from random_search import create_dist_matrix
from data_visualization import plot_path_taken as ppt
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import random
import time

def two_opt(data, period):
    n = data.shape[0]
    # BSF /initial tour from NN
    dist_mat = create_dist_matrix(data)
    BSF_dist, BSF_order = nnh(dist_mat.copy(), False)
    ppt(data, BSF_order, "init.png")

    # brute force for loop
    delta_dist = 0
    time_limit = time.time() + period
    print(f"\t\t{BSF_dist:.1f}")
    print(BSF_order)
    for i in range(n):
        j = i + 2
        ith_edge = dist_mat[BSF_order[i],BSF_order[i+1]]
        while j < n and time.time() < time_limit:
                         # original edge                                       swapped edge ends
            delta_dist = (ith_edge + dist_mat[BSF_order[j], BSF_order[j+1]]) - (dist_mat[BSF_order[i],BSF_order[j+1]] + dist_mat[BSF_order[j], BSF_order[i+1]])
            if delta_dist > 0:
                ith_edge = dist_mat[BSF_order[i],BSF_order[i+1]]
                BSF_dist -= delta_dist
                new_order1 = BSF_order[:i+1]
                new_order2 = BSF_order[i+1:j+1]
                new_order2 = new_order2[::-1]
                new_order3 = BSF_order[j+1:]
                BSF_order = new_order1 + new_order2 + new_order3
                print(f"\t\t{BSF_dist:.1f}")
            j += 1
        if time.time() >= time_limit:
            break
    return BSF_dist, BSF_order
        
if __name__ == "__main__":
    file = "256Cashew"
    data = vf(f"data/{file}.txt")
    dist, order = two_opt(data, 60)
    ppt(data, order, f"2opt{file}.png")

