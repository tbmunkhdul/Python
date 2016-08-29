print "Breadth First Traversal for a Graph"
# # Breadth First Traversal for a Graph
# # http://www.geeksforgeeks.org/breadth-first-traversal-for-a-graph/
# # graphlist = [[0,1],[0,2],[1,2],[2,0],[2,3],[3,3]]
graphlist = [[0,2],[0,3],[1,0],[2,4],[2,5],[3,1],[3,2],[4,4],[5,2],[5,6],[6,4]]
new_list = []
new_list.append(3) # start from
for x in new_list:
    for i in range(len(graphlist)):
        if x == graphlist[i][0]: 
            if graphlist[i][1] not in new_list: 
                new_list.append(graphlist[i][1])  
    #graphlist.pop(i)
print "result->",new_list 