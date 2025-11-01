from nearest_neighbor_search import nearest_neighbor_helper as nnh
from nearest_neighbor_search import nearest_neighbor_search as nns
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
    dist = BSF_dist
    order = BSF_order.copy()
    time_limit = time.time() + period
    # ensure the tour is closed and the distance matches the distance matrix
    BSF_dist = sum(dist_mat[BSF_order[k], BSF_order[k+1]] for k in range(len(BSF_order) - 1))
    print(f"\t\t{BSF_dist:.1f}")
    while time.time() < time_limit:
        dist, order = two_opt_helper(dist_mat.copy(), time_limit, order, BSF_dist)
        if dist < BSF_dist:
            BSF_dist = dist
            BSF_order = order
        _, order = nnh(dist_mat.copy(), True)
    return BSF_dist, BSF_order

def two_opt_helper(dist_mat, time_limit, order, global_best):
    n = dist_mat.shape[0]
    # repeated brute force for loop
    good_delta = True
    BSF_order = order
    BSF_dist = sum(dist_mat[BSF_order[k], BSF_order[k+1]] for k in range(len(BSF_order) - 1))
    while good_delta:
        good_delta = False
        for i in range(n):
            j = i + 2
            while j < n and time.time() < time_limit:
                new_order1 = BSF_order[:i+1]
                new_order2 = BSF_order[i+1:j+1]
                new_order2 = new_order2[::-1]
                new_order3 = BSF_order[j+1:]
                new_order_final = new_order1 + new_order2 + new_order3
                new_dist = sum(dist_mat[new_order_final[k], new_order_final[k+1]] for k in range(len(new_order_final) - 1))
                if new_dist < BSF_dist:
                    good_delta = True
                    BSF_order = new_order_final
                    BSF_dist = new_dist
                    if BSF_dist < global_best:
                        global_best = BSF_dist
                        print(f"\t\t{BSF_dist:.1f}")
                j += 1
            if time.time() >= time_limit:
                break
    return BSF_dist, BSF_order
        
if __name__ == "__main__":
    file = "data/256Cashew.txt"
    data = np.loadtxt(file)
    to_dist, to_order = two_opt(data, 100)
    ppt(data, to_order, "res/path_visuals/256Cashew_TO.png")

