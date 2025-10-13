# Follow General Outline Given my P1 Detailed Briefing
# For now we will use pseudo code because we have questions for Dr. Keogh in tomorrow's lecture. 
# import numpy as np
# from user_interface import UI
# import random
# import time 
# import math

# def nearest_neighbor_search(data, period):
#   time_limit = time.time + period
#   dist_mat = create_dist_matrix(data)
#   
#   while time.time < time_limit:
#       
#
#   return BSF_dist, BSF_order

# def nearest_neighbor_helper(dist_mat, random):
#   visited = set()
#   order = []
#   distance = 0
#   point = 0 # start at landing bay
#   order.append(1)
#   while len(visited) != len(dist_mat):
#       if random:
#           choose_shortest = random.randint(0,9)
#       next_point = np.arg_min(dist_mat[point, :])
#       while next_point in visited:
#           dist_mat[point, next_point] = float('inf')
#           next_point = np.arg_min(dist_mat[point, :])
#       if choose_shortest < 1:
#           if len(visited) < len(dist_mat)-1:
#               dist_mat[point, np.arg_min(dist_mat[point, :])] = float('inf)
#               while next_point in visited:
#                   dist_mat[point, next_point] = float('inf')
#                   next_point = np.arg_min(dist_mat[point, :])
#       
#       distance += dist_mat[point, next_point]
#       order.append(next_point + 1)
#       visited.add(next_point)
#       point = next_point
#   order.append(1)
#   return distance, order
#       


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



