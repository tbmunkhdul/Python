# Dijkstra’s shortest path algorithm
#http://www.geeksforgeeks.org/greedy-algorithms-set-6-dijkstras-shortest-path-algorithm/
#import numpy as np
import math
print("Dijkstra shortest path algorithm")
print("")
connected_nodes = []
# graph = np.array([
# [0, 4, 0, 0, 0, 0, 0, 8, 0],
# [4, 0, 8, 0, 0, 0, 0, 11, 0],
# [0, 8, 0, 7, 0, 4, 0, 0, 2],
# [0, 0, 7, 0, 9, 14, 0, 0, 0],
# [0, 0, 0, 9, 0, 10, 0, 0, 0],
# [0, 0, 4, 14, 10, 0, 2, 0, 0],
# [0, 0, 0, 0, 0, 2, 0, 1, 6],
# [8, 11, 0, 0, 0, 0, 1, 0, 7],
# [0, 0, 2, 0, 0, 0, 6, 7, 0]])

graph = [
[0, 4, 0, 0, 0, 0, 0, 8, 0],
[4, 0, 8, 0, 0, 0, 0, 11, 0],
[0, 8, 0, 7, 0, 4, 0, 0, 2],
[0, 0, 7, 0, 9, 14, 0, 0, 0],
[0, 0, 0, 9, 0, 10, 0, 0, 0],
[0, 0, 4, 14, 10, 0, 2, 0, 0],
[0, 0, 0, 0, 0, 2, 0, 1, 6],
[8, 11, 0, 0, 0, 0, 1, 0, 7],
[0, 0, 2, 0, 0, 0, 6, 7, 0]]

#row, column = graph.shape # if you use numpy
row, column = 9,9

result_list = [0] + [math.inf]*(row-1) 

for r in range(row):
    templist = []
    for y in range(column):
        if graph[r][y] != 0:
            templist.append(y)            
    connected_nodes.append(templist)    


for z in range(1,len(result_list)):
    for i in range(1,row):
        tlist = []
        for x in range(len(connected_nodes[i])):
            tlist.append(graph[i][connected_nodes[i][x]] + result_list[connected_nodes[i][x]])
        result_list[i] = min(tlist)


for k in range(len(result_list)):
	print(k,":",result_list[k])