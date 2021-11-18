#Matrix
# import numpy as np
# from numpy.linalg import inv
#
# matrix =[[7i3]
#          [Tsi]
#          [h%x]
#          [i #]
#          [sM]
#          [$a]
#          [#t%]
#          [^r!]
# ]
# matrix1 = []
# a = []
# for j in range(matrix):  # A for loop for column entries
#     a.append(int(input()))
# matrix1.append(a)

# # For printing the matrix
# for j in range(matrix):
# print(matrix1[i][j], end=" ")
# print()
# # print(matrix[:,0])
# # print(matrix[:,1])
# # print(matrix[:,-1])
matrix= str( [
    [7,'i',3],
    ['T','s','i'],
    ['h','%','x'],
    ['i',' ','#'],
    ['s','M',' '],
    ['$','a',' '],
    ['#','t','%'],
    ['^','r','!']
    ])

data=[]

for i in matrix:
    if i[0].isalpha():
        data.append(i[0])
        data.sort()
print(data)
