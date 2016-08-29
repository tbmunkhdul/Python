print "Depth First Traversal for a Graph"
# Depth First Traversal for a Graph
# http://www.geeksforgeeks.org/depth-first-traversal-for-a-graph
graphlist2 = [[0,2],[0,3],[1,0],[2,4],[2,5],[3,1],[3,2],[4,4],[5,2],[5,6],[6,4]]
new_list2 = []
new_list2.append(3) # start from
def func(graphlist1,new_list1):
    if not graphlist1 or not new_list1:     
        return [] 
    else:
        length = len(graphlist1)
        for x in range(length):
            for i in range(len(graphlist1)):
                if new_list1[-1] == graphlist1[i][0]:
                    if graphlist1[i][1] not in new_list1:  
                        new_list1.append(graphlist1[i][1])
                    graphlist1.pop(i)
                    break
        return new_list1 + [x for x in func(graphlist1,new_list1[0:-1]) if x not in new_list1]

print "result->",func(graphlist2,new_list2)