# Given a sorted array C[] and a number X, write a function that counts the occurrences of X in C[].
# 
# Input:
# 
# The first line of input contains an integer T denoting the number of test cases.
# The first line of each test case is N and X, N is the size of array.
# The second line of each test case contains N input C[i].
# 
# Output:
# 
# Print the counts the occurrence of X, if zero then print -1.
# http://www.practice.geeksforgeeks.org/problem-page.php?pid=577

from collections import namedtuple

Data = namedtuple("Data", "N X C")

inputlist = []
T = int(input('how many test cases:'))

while T:
    N = int(input('N :'))
    X = int(input('X :'))
    while True:
        C = input('C :')
        C = [int(i) for i in C.split(' ')]
        if len(C) == N:
            break
        print("length of C should be [", N, "]")
    inputlist.append(Data(N, X, C))
    T -= 1

for i in inputlist:
    count = 0
    for x in i.C:
        if x == i.X:
            count += 1
    if count == 0:
        count = -1
    print(count)