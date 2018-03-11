import csv
import numpy as np
# with open("winequality-red.csv", 'r') as f:
# 	wines = list(csv.reader(f, delimiter=";"))
# print(wines[:3])
#
# qualities = [float(item[-1]) for item in wines[1:]]
#
# print(sum(qualities)/len(qualities))

# print([x for i,x in enumerate(['a','b','c'])])
#
# print(enumerate([4,5,6]))
#
# test = [i for i, j in enumerate(['hi', 'hii', 'hiii']) if j =='hi']
# print(test)
#
# wines = np.array(wines[1:], dtype = np.float)
# print(wines)
#
# print(wines.shape)
# empty_array = np.zeros((3,5))
# print(empty_array)
#
# wines = np.genfromtxt("winequality-red.csv", delimiter= ";", skip_header=1)
# print(wines[:3,2])
#
#
# arr = np.array([[1,2,3,4,5,6], [6,5,4,3,2,1]])
# arr2 = arr.reshape(6,2)
# print(arr2)
# greater3 = arr > 3
# print(arr)
# print(greater3)
#
# print(arr[greater3])



zeros = np.zeros((3,4))
ones = np.ones((6,4))

concat = np.vstack((zeros, ones))
print(concat.shape)
first_column = [items[1] for items in concat]
print(first_column)
