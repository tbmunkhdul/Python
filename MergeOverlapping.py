# http://www.geeksforgeeks.org/merging-intervals/
print("Merge Overlapping Intervals")

intervals = [[1, 3], [2, 4], [5, 7], [6, 8], [9, 10], [0, 8], [11, 13], [2, 7], [15, 20]]
intervals.sort()
rlst = []
rlst.append(intervals[0])
intervals.pop(0)
for i in intervals:  
    length_rlist = len(rlst)  
    innerlength = length_rlist
    for x in range(length_rlist): 
        xr0 = rlst[x][0]  
        xr1 = rlst[x][1]
        if i[0] <= xr0 and xr1 <= i[1]:
            rlst[x][0] = i[0]
            rlst[x][1] = i[1]
        elif xr0 <= i[0] and i[1] <= xr1:
            break   
        elif xr0 <= i[0] <= xr1 and xr1 <= i[1]:  
            rlst[x][1] = i[1]
        elif i[0] <= xr0 < i[1] and i[1] <= xr1:
            rlst[x][0] = i[0]
        else:
            if 1 < innerlength:
                innerlength = innerlength - 1
                continue
            rlst.append(i)

print(rlst)