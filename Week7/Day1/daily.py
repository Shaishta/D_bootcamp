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

#the xp exercise in python file
import numpy as np
import pandas as pd
import matplotlib.pyplot as pl

# # 1

# def num_arr(start):
#     arr = np.arange(start=start, stop=100, step=4)
#     return arr
# num_arr(6)
#
# print(num_arr(6))

# # 2

# a = np.array([1,2,3,np.nan,5,6,7,np.nan])
# a = a[~np.isnan(a)]
# print(np.isnan(a))
# print(a)


# # 3

from random import random

# array_rand = np.random.randint(101, size=5*6).reshape((5,6))
# print(array_rand.max(axis=1))
# print(array_rand)


# # 4

# series = pd.Series(np.take(list('abcdefghijklmnop'), np.random.randint(16, size=500)))
# # print(series.unique())
#
# print(series.value_counts())


# # 5

from dateutil.parser import parse

# data = pd.Series(['01 Jan 2020', '10-19-2020', '20150303', '2013/04/04', '2012-05-05', '2013-06-06T12:20'])
# for x in data:
#     print(parse(x).month, parse(x).day, parse(x).weekday())


# # 6

# df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')
# print(df)

# print(df.shape[1])

# df_changename = df.rename(columns={"Type":"TypeOfCar"})
# print(df_changename)

# print(df_changename.columns)   # another way


# print(df.isnull().sum())
# print(df.describe())
# print(df.info())  # to see how many nulls inside

# print(df.isnull().sum().max())


# # 7

# del df["EngineSize"]
# del df["Length"]
# df.drop('EngineSize', inplace=True, axis=1)
# df.drop('Length', inplace=True, axis=1)

# df.drop(columns=["EngineSize", "Length"],inplace=True)



# # 8

# df1 = pd.DataFrame({'fruit': ['apple', 'banana', 'orange'] * 3,
#                     'weight': ['high', 'medium', 'low'] * 3,
#                     'price': np.random.randint(0, 15, 9)})
#
# df2 = pd.DataFrame({'pazham': ['apple', 'orange', 'pine'] * 2,
#                     'kilo': ['high', 'low'] * 3,
#                     'price': np.random.randint(0, 15, 6)})
#
# # print(df1)
# # print(df2)
#
# remov_dup = df1.merge(df2,left_on=('fruit','weight'),right_on=('pazham','kilo'),how='inner',suffixes=('_left','_right')).head(10)
# print(remov_dup)


# # 9

import pandas as pd

# df = pd.DataFrame(["STD,City\tState",
# "33,Kolkata\tWest Bengal",
# "44,Chennai\tTamil Nadu",
# "40,Hyderabad\tTelengana",
# "80,Bangalore\tKarnataka"], columns=['row'])
# print(df)

# df = pd.DataFrame(["STD, City    State",
# "33, Kolkata    West Bengal",
# "44, Chennai    Tamil Nadu",
# "40, Hyderabad    Telengana",
# "80, Bangalore    Karnataka"], columns=['row'])
# out = pd.DataFrame(df.row.str.split(' ',2).tolist(),columns=['STD','City','State'])
# out.drop(index=0,inplace=True)
# print(out)

import matplotlib.pyplot as plt

names = ["mpg", "cylinders", "displacement", "horsepower", "weight", "acceleration", "model_year", "origin", "car_name"]
df_mpg = pd.read_csv("auto-mpg.data", header=None, names=names, delim_whitespace=True)
print(df_mpg)

#
# # # 10
#
def scatter_plot(df):
    plt.scatter(df['displacement'], df['acceleration'])
    plt.xlabel('displacement cm³')
    plt.ylabel('acceleration m/s²')
    plt.grid()


(scatter_plot(df_mpg))
#
#
# def bar_plot(df):
#     plt.figure(figsize=(12,5))
#     plt.bar(df['model_year'], df['cylinders'])
#     plt.xlabel("Model Year")
#     plt.ylabel("Cylinders")
#     plt.title("Cylinders over Years")
#     plt.show()
#
# (bar_plot(df_mpg))
# #
# #
# def line_plot(df):
#     x = (df['model_year'])
#     y = (df['weight'])
#     plt.plot(x, y)
#
#     plt.xlabel('model year')
#     plt.ylabel('weight')
#     plt.show()
#
#
# line_plot(df_mpg)

# def line_plot(df):
#     df=df[df.car_name.str.contains('toyota')]
#     plt.plot(df.model_year, df.weight)
#
# line_plot(df_mpg)
#
#
def my_func(df):
    x = (df['weight'])
    y = (df['mpg'])
    plt.scatter(x, y)

    plt.xlabel('weight')
    plt.ylabel('mpg')
    plt.show()


my_func(df_mpg)


# Average stock prize in last 5 years

# def barplot(df):
#
#     df = df[df.car_name.str.contains("toyota")]
#     df = df[df["model_year"].isin([78])]
#     plt.bar(df["car_name"],df["cylinders"])
#
#
#     # toyota_cylinders = df[df.car_name=="toyota"].cylinders
#     # all_others_cylinders = df[~df.car_name=="toyota"].cylinders
#     #
#     # years = model_year
#
# # We cannot add width to year so we create another list
# #     indices = np.arange(len(year))
# #
# #     width = 0.20
# #
# # # Plotting
# #     plt.bar(indices, toyota_cylinders, width=width)
# #
# # # Offsetting by width to shift the bars to the right
# #     plt.bar(indices + width, all_others_cylinders, width=width)
# #
# #
# # # Displaying year on top of indices
# #     plt.xticks(ticks=indices, labels=year)
# #
# #
# #     plt.xlabel("year")
# #     plt.ylabel("average stock price")
# #     plt.title("Toyota vs. Others")
#
#     plt.show()
#
# barplot(df_mpg)
