import numpy as np
import pandas as pd
import time
import os

from two_opt import two_opt as to
from data_visualization import plot_path_taken as ppt

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
    data = validate_file(f"{input_file}")

    n = data.shape[0]
    print(f"There are {n} nodes, computing route...")

    print("\tShortest Route Discovered So Far (Hit 'Escape' to terminate)")
    dist, order = to(data)

    output_file = f"{input_file}_SOLUTION_{dist:.0f}"
    if dist > 6000:
        print("WARNING: This file has a distance more than 6000")
    print(f"Route written to disk as {output_file}")

    np.savetxt(f"solutions/{output_file}.txt", order, fmt="%d")
    ppt(data, order, f"path_visuals/{output_file}.png")

if __name__ == '__main__':
    main()
