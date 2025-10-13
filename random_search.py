# Follow General Outline Given my P1 Detailed Briefing
# For now we will use pseudo code because we have questions for Dr. Keogh in tomorrow's lecture. 
# import numpy as np
# from user_interface import UI
# import random
# import time 
# import math

# check for indexing mistakes
# def make_permutation():
#   points = set(i+1 for i in range(n + 1))
#   order = [1]
#   for i in range(n-1):
#       point = random.randint(2, n+1)
#       if point in points:
#           order.append(point-1)
#           points.remove(point)
#   order.append(0) # return to start
#   return order

# def random_search(data, period):
#   n = len(data)
#   # find random permutation 
#   BSF_dist = float('inf')
#   BSF_order = []
#   dist_mat = create_dist_matrix(dataframe)
#   permutations = set()
#   permutation = make_permutation()
#   permutation.add(permutation)
#   time_limit = time.time() + period
#   while(time.time() < time_limit):
#       distance = 0
#       for i in range(n-1):
#           distance += dist_matrix[i, i + 1]
#           # if distance > BSF_dist: # add for early abandoning
#           #    break
#       if distance < BSF_dist:
#           BSF_dist = distance
#           BSF_order = permutation
#       permutation = make_permutation()
#       permutations.add(permuation)
#   return math.ceil(BSF_dist), BSF_order

# assumes coords given as x, y 
# def euclid_dist(a: list, b: list):
#   diff_y = a[1] - b[1] 
#   diff_x = a[0] - b[0]
#   diff_sq = diff_x**2 + diff_y**2
#   return sqrt(diff_sq)

# def create_dist_matrix(dataframe):
#   dist_mat = [[float('inf')] * len(dataframe) for i in range len(dataframe)]
#   for r in range(len(dataframe)):
#       for c in range(r + 1,len(dataframe)):
#           dist_mat[r,c] = dist_mat[c,r] = euclid_dist(dataframe[r], dataframe[c])
#   return dist_mat


