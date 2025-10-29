# Follow General Outline Given my P1 Detailed Briefing
import numpy as np
from numpy import random
# from user_interface import validate_file
import time 
import math

def make_permutation(n):
    '''
        Input:
            n: int for number of locations drone must visit
        Output:
            order: int containing permutation of locations (always start and end at location 1)
    '''
    order = [i for i in range(0,n)]
    order.append(0)
    order = np.array(order)
    random.shuffle(order[1:n])
    return order

def random_search(data, period, verbose=True, testing=False):
    '''
        Input:
            data: nxn np.array
            period: time before interrupt (seconds)
        Output:
            BSF_dist: best distance at time of interrupt
            BSF_order: best order at time of interr
    '''
    n = data.shape[0]

    if testing:
        BSF_over_time = []

    BSF_dist = float('inf')
    BSF_order = []
    dist_mat = create_dist_matrix(data)
    seen_perms = set()
    permutation = make_permutation(n)
    time_limit = time.time() + period
    prev_time = time.time()

    # keep trying until interrupt
    while(time.time() < time_limit):
        distance = 0

        # don't try if already attempted permutation
        if tuple(permutation) in seen_perms:
            continue
        seen_perms.add(tuple(permutation))

        # get distance of current permutation
        for i in range(n-1):
            distance += dist_mat[permutation[i], permutation[i+1]]
            # add for early abandoning
            if distance > BSF_dist: 
               break

        if distance < BSF_dist:
            BSF_dist = distance
            BSF_order = permutation
            if verbose:
                print(f"\t\t{BSF_dist:.1f}")
            
        permutation = make_permutation(n)

        if testing and time.time() - prev_time > 1 and len(BSF_over_time) < period:
            BSF_over_time.append(BSF_dist)
            prev_time = time.time()

    if testing:
        if len(BSF_over_time) < period:
            while len(BSF_over_time) < period:
                BSF_over_time.append(BSF_dist)
        return BSF_dist, BSF_order, BSF_over_time    
    return BSF_dist, BSF_order

def create_dist_matrix(data):
    '''
        Input:
            data: nxn np.array containing locations for drone to visit
        Output:
            dist_mat: nxn np.ndarray, dist_mat[i,j] is euclidean distance between point i and point j
    '''
    n = data.shape[0]
    dist_mat = np.zeros((n, n))
    for i in range(n):
        dist_mat[i] = np.sqrt(np.sum((data[i,:] - data[:,:])**2, axis = 1))
    return dist_mat

if __name__ == '__main__':
    # filename = 'data/32Almonds.txt'
    # data = vf(filename)
    random_search(data, 60)
