import numpy as np
import pandas as pd
import time
import os

# TODO: throw exception or ask for input again?
def validate_file(filename):
    if not filename.endswith(".txt"):
        raise Exception("This file is not a .txt file. ABORT")
    if not os.path.exists(filename):
        raise Exception("This file does not exist. ABORT")
    df = pd.read_csv(filename, sep="   ", engine='python', header=None)
    if len(df) > 256:
        raise Exception("This file has more than 256 points. ABORT")
    return df.to_numpy()

# def main():
#   print("ComputeDronePath")
#   fileName = input("Enter the name of the file:")
#   validate_file(fileName)
#   df = pd.read_csv(fileName)
#   nodes = len(df)
#   print("There are 136 nodes, computing route...")
#   print("Shortest Route Discovered So Far")
#   dist_5, ord_5 = random_search(, 5)
#   print(dist_5)
#   dist_10, ord_10 = random_search(, 10)
#   print(dist_5)
#   dist_15, ord_15 = random_search(, 15)
#   print(dist_5)
#   print("Route written to disk as ")


# user never hits enter -->
# i will keep track of when the user hits enter
# the time when the user presses enter is saved
# i call the random_search func on the time that the user presses enter 
# i still output the distance for the times 5, 10, 15 on the terminal 

if __name__ == '__main__':
    filename = 'data/32Almonds.txt'
    df = validate_file(filename)
    print(df)