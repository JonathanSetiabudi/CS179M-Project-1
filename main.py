import numpy as np
import pandas as pd
import time
import os

from nearest_neighbor_search import nearest_neighbor_search as nns
from random_search import random_search as rs
from two_opt import two_opt as to
from data_visualization import plot_path_taken as ppt

def search(algo, data, period, testing=False):
    if testing:
        if algo == 'RS':
            dist, order, over_time = rs(data, period, False, True)
        if algo == 'NNS':
            dist, order, over_time = nns(data, period, False, True)
        if algo == "TO":
            dist, order, over_time = to(data, period, False, True)
        return dist, order, over_time
    
    if algo == 'RS':
        dist, order = rs(data, period)
    if algo == 'NNS':
        dist, order = nns(data, period)
    if algo == "TO":
        dist, order = to(data, period)
    return dist, order

def validate_file(filename):
    if not filename.endswith(".txt"):
        raise Exception("This file is not a .txt file. ABORT")
    
    if not os.path.exists(filename):
        raise Exception("This file does not exist. ABORT")
    
    df = pd.read_csv(filename, sep="   ", engine='python', header=None)
    
    # if len(df) > 256:
    #     raise Exception("This file has more than 256 points. ABORT")
    
    return df.to_numpy()

def main():
    print("ComputeDronePath")
    input_file = input("Enter the name of the file: ")
    data = validate_file(f"data/{input_file}")

    n = data.shape[0]
    print(f"There are {n} nodes, computing route...")

    print("\tShortest Route Discovered So Far")
    dist, order = search(algo='NNS', data=data, period=100, testing=False)

    output_file = f"{input_file}_SOLUTION_{dist:.0f}"
    print(f"Route written to disk as {output_file}")

    np.savetxt(f"res/solutions/{output_file}.txt", order)
    ppt(data, order, f"res/path_visuals/{output_file}.png")

if __name__ == '__main__':
    main()