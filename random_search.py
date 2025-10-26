# Follow General Outline Given my P1 Detailed Briefing
import numpy as np
from numpy import random
#from user_interface import UI
import time 
import math

# check for indexing mistakes
def make_permutation(n):
    order = [i for i in range(n)]
    order.append(0)
    order = np.array(order)
    random.shuffle(order[1:n])
    return order

def random_search(data, period):
    n = data.shape[0]
    # find random permutation 
    BSF_dist = float('inf')
    BSF_order = []
    dist_mat = create_dist_matrix(data)
    seen_perms = set()
    permutation = make_permutation(n)
    seen_perms.add(tuple(permutation))
    time_limit = time.time() + period
    while(time.time() < time_limit):
        distance = 0
        if tuple(permutation) in seen_perms:
            continue
        for i in range(n-1):
            distance += dist_mat[permutation[i], permutation[i+1]]
            # if distance > BSF_dist: # add for early abandoning
            #    break
        if distance < BSF_dist:
            BSF_dist = distance
            BSF_order = permutation
        permutation = make_permutation(n)
        seen_perms.add(tuple(permutation))
    return math.ceil(BSF_dist), BSF_order

def create_dist_matrix(data):
    n = data.shape
    dist_mat = [[float('inf')] * n for i in range(n)]
    for r in range(n):
        for c in range(r + 1, n):
            dist_mat[r,c] = dist_mat[c,r] = np.linalg.norm(data[r], data[c])
    return np.array(dist_mat)

if __name__ == '__main__':
    print(make_permutation(10))
    data = np.array([[1,2],[5,4],[9,3]])
    create_dist_matrix(data)