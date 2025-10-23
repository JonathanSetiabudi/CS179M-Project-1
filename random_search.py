# Follow General Outline Given my P1 Detailed Briefing
import numpy as np
from numpy import random
#from user_interface import UI
import time 
import math

def make_permutation(n):
    '''
        Input:
            n: int for number of locations drone must visit
        Output:
            order: int containing scrambled locations (always start and end at location 1)
    '''
    order = [i for i in range(0,n)]
    order.append(0)
    order = np.array(order)
    random.shuffle(order[1:n])
    return order

def random_search(data, period):
    '''
        Input:
            data: nxn np.array
            period: time before interrupt (seconds? minutes?)
        Output:
            BSF_dist: best distance at time of interrupt
            BSF_order: best order at time of interr
    '''
    n = data.shape[0]

    BSF_dist = float('inf')
    BSF_order = []
    dist_mat = create_dist_matrix(data)

    seen_perms = set()
    permutation = make_permutation(n)
    seen_perms.add(tuple(permutation))
    time_limit = time.time() + period
    # keep trying until interrupt
    while(time.time() < time_limit):
        distance = 0
        # don't try if already attempted permutation
        if tuple(permutation) in seen_perms:
            continue
        # get distance of current permutation
        for i in range(n-1):
            distance += dist_mat[permutation[i], permutation[i+1]]
            # add for early abandoning
            # if distance > BSF_dist: 
            #    break
        if distance < BSF_dist:
            BSF_dist = distance
            BSF_order = permutation
        permutation = make_permutation()
        seen_perms.add(tuple(permutation))
    return math.ceil(BSF_dist), BSF_order

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
