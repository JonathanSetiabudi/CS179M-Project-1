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
    # ensure the tour is closed and the distance matches the distance matrix
    BSF_dist = sum(dist_mat[BSF_order[k], BSF_order[k+1]] for k in range(len(BSF_order) - 1))
    ppt(data, BSF_order, "init.png")

    # repeatedbrute force for loop
    delta_dist = 0
    time_limit = time.time() + period
    print(f"\t\t{BSF_dist:.1f}")
    good_delta = True
    while good_delta:
        good_delta = False
        for i in range(n):
            j = i + 2
            # ith_edge = dist_mat[BSF_order[i],BSF_order[i+1]]
            while j < n and time.time() < time_limit:
                            # original edge                                       swapped edge ends
                # delta_dist = (ith_edge + dist_mat[BSF_order[j], BSF_order[j+1]]) - (dist_mat[BSF_order[i],BSF_order[j+1]] + dist_mat[BSF_order[j], BSF_order[i+1]])
                new_order1 = BSF_order[:i+1]
                new_order2 = BSF_order[i+1:j+1]
                new_order2 = new_order2[::-1]
                new_order3 = BSF_order[j+1:]
                new_order_final = new_order1 + new_order2 + new_order3
                new_dist = sum(dist_mat[new_order_final[k], new_order_final[k+1]] for k in range(len(new_order_final) - 1))
                if new_dist < BSF_dist:
                    good_delta = True
                    BSF_order = new_order_final
                    # ith_edge = dist_mat[BSF_order[i],BSF_order[i+1]]
                    BSF_dist = new_dist
                    print(f"\t\t{BSF_dist:.1f}")
                j += 1
            if time.time() >= time_limit:
                break
    return BSF_dist, BSF_order
        
if __name__ == "__main__":
    file = "32Almonds"
    data = vf(f"data/{file}.txt")
    dist, order = two_opt(data, 20)
    print(f"Final distance: {dist}")
    ppt(data, order, f"2opt{file}.png")

