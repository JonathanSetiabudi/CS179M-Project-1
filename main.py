import numpy as np
import pandas as pd
import time
import os

from nearest_neighbor_search import nearest_neighbor_search as nns
from random_search import random_search as rs
# from data_visualization import plot_path_taken as ppt

def search(data, period, algo):
    if algo == 'RS':
        dist, order = rs(data, period)
    if algo == 'NNS':
        dist, order = nns(data, period)
    return dist, order

def validate_file(filename):
    if not filename.endswith(".txt"):
        raise Exception("This file is not a .txt file. ABORT")
    if not os.path.exists(filename):
        raise Exception("This file does not exist. ABORT")
    df = pd.read_csv(filename, sep="   ", engine='python', header=None)
    if len(df) > 256:
        raise Exception("This file has more than 256 points. ABORT")
    return df.to_numpy()

def main():
    print("ComputeDronePath")
    input_file = input("Enter the name of the file: ")
    path = "data"
    data = validate_file(f"{path}/{input_file}")
    n = data.shape[0]
    print(f"There are {n} nodes, computing route...")
    print("\tShortest Route Discovered So Far")
    dist, order = search(data, period=12.5, algo='NNS')
    output_file = f"{input_file}_SOLUTION_{dist:.0f}"
    print(f"Route written to disk as {output_file}")
    np.savetxt(f"res/{output_file}.txt", order)
    ppt(data, order, f"res/path_visuals/{output_file}.png")

if __name__ == '__main__':
    main()