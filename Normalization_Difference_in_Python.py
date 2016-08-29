# Normalization python
# Comparison between code and library
import numpy as np 
from sklearn import preprocessing

csv = np.genfromtxt('KDD_sample.csv', delimiter= ",")

''' test 1'''
def norm1():
    kdd_data = np.copy(csv[0:,0:-1]) # remove last column and copy array
    row,col = (kdd_data.shape)
    res_size = (row,col)
    my_result_array = np.zeros(res_size) 
    maxvalue = 0
    minvalue = 0
    for i in range(col):
        maxvalue = max(kdd_data[0:,i:i+1])
        minvalue = min(kdd_data[0:,i:i+1])
        if maxvalue != 0 or minvalue != 0:
            for x in range(row):
                my_result_array[x,i] = (kdd_data[x,i]-minvalue)/(maxvalue-minvalue)
    
    np.savetxt("res1.csv", my_result_array,fmt='%10.10f',delimiter=",")
    # print (my_result_array[0:,0]) results are the same

''' test 2, preprocessing lib '''
def norm2(): 
    min_max_scaler = preprocessing.MinMaxScaler()
    my_result_array1 = min_max_scaler.fit_transform(np.copy(csv[0:,0:-1]))
    
    np.savetxt("res2.csv", my_result_array1,fmt='%10.10f',delimiter=",")
    # print (my_result_array1[0:,0]) results are the same

import cProfile
cProfile.run('norm1()')
cProfile.run('norm2()')
