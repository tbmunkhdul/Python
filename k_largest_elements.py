# Given an array, print k largest elements from the array.  
# The output elements should be printed in decreasing order.
# Input:
# The first line of input contains an integer T denoting the number of test cases.
# The first line of each test case is N and k, N is the size of array 
# and K is the largest elements to be returned.
# The second line of each test case contains N input C[i].

from collections import namedtuple

Data = namedtuple("Data", "N K C")

inputlist = []
T = int(input('how many test cases:'))

while T:
    N = int(input('N :'))
    while True:
        K = int(input('K :'))
        if K <= N:
            break
        print("K should be equal or less than N [", N, "]")
    while True:
        C = input('C :')
        C = [int(i) for i in C.split(' ')]
        if len(C) == N:
            break
        print("length of C should be [", N, "]")
    inputlist.append(Data(N, K, C))
    T -= 1

for i in inputlist:
    i.C.sort()
    i.C.reverse()
    print("output :", i.C[0:i.K])
