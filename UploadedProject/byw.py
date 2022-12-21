# import seaborn as sns
import matplotlib.pyplot as plt
# import pandas as pd
# import numpy as np

# x2=[]
# y2=[]
# # plt.style.use('ggplot')
# plt.plot(x1,marker='.', color='r', label= 'basic')
# plt.plot(y1, marker = '.', color = 'g',label = 'efficient')
# plt.legend();

# import matplotlib.pyplot as plt

# number of employees
# emp_countA = [3, 20, 50, 200, 350, 400]
# emp_countB = [250, 300, 325, 380, 320, 350]
# year = [0, 500, 1000, 1500, 2000]
x1=[10436,10476,10620,11180,12036]
y1=[12572,12412,12504,12548,12564]
plt.plot(x1, y1)
# plot two lines
# plt.plot(x1)
# plt.plot(y1)
# set axis titles
plt.xlabel("Input Size")
# plt.ylabel("Employees")
# set chart title
plt.title("Employee Growth")
# legend
# plt.legend(['basic', 'efficient'])
plt.show()