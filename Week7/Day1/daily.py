import numpy as np
from numpy import random

n = random.randint(2, 39)
m = random.randint(2, 49)
num_of_rows = [[random.randint(100) for i in range(n)] for i in range(m)]
print("table:", num_of_rows)
print("\n")
print("the third row:", num_of_rows[2])
print("\n")
col = [i[2] for i in num_of_rows]
print("the third column:", col)
print("\n")
last_row_7 = [7 for i in num_of_rows[-1]]
num_of_rows[-1] = last_row_7
print("the last row:", num_of_rows)
sum_one = sum(num_of_rows[0])
sum_two = sum(num_of_rows[1])
sum_one_two = sum_one + sum_two
print("sum of first and second row:", sum_one_two)
print("\t")
last_row = [sum_one_two for i in num_of_rows[-1]]
num_of_rows[-1] = last_row
print("the last row contains the sum:", num_of_rows)
#numpy

n = random.randint(2,39)
m = random.randint(2,49)
arr_2nd = random.randint(100, size=(n,m))
print(arr_2nd)
print(arr_2nd[2])
print(arr_2nd[:,2])
last_row_7 = [7 for i in arr_2nd[-1]]
arr_2nd[-1] = last_row_7
print(arr_2nd)
sum_one_two = np.sum([arr_2nd[0], arr_2nd[1]])
last_row_sum_one_two = [sum_one_two for i in arr_2nd[-1]]
arr_2nd[-1] = last_row_sum_one_two

print(arr_2nd)


# or the simpler way

# from random import randint
#
#
# N = randint(1,40)
# M = randint(1,50)
#
# table = [[randint(1,100) for i in range(N)] for j in range(M)]
#
# print(table[2])
#
# print([i[2] for i in table])
#
#
# table[-1] = [7 for i in range(N)]
#
# print(table)
#
#
# for j, ival in enumerate(table):
#     table[j][-1] = ival[0] + ival[1]
# print(table)
#
# import numpy as np
#
# table = np.array([randint(1,100) for _ in range(M*N)]).reshape((N,M))
#
# print(table[2])
# print(table[:,2])
#
# table[-1] = 7
# print(table)
#
# table[:,-1] = table[:,0] + table[:,1]
#
# print(table)
