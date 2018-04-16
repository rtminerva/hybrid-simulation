import numpy as np
from scipy.optimize import minimize
import matplotlib.pyplot as plt

def lik(parameters):
    m = parameters[0]
    b = parameters[1]
    sigma = parameters[2]
    for i in np.arange(0, len(x)):
        y_exp = m * x + b
    L = (len(x)/2 * np.log(2 * np.pi) + len(x)/2 * np.log(sigma ** 2) + 1 /
         (2 * sigma ** 2) * sum((y - y_exp) ** 2))
    return L

# x = np.array([1,2,3,4,5])
# y = np.array([2,5,8,11,14])

from xlrd import open_workbook
import math as m
book = open_workbook('data.xlsx')
sheet = book.sheet_by_index(0)

time_x = []
current_y = []

for k in range(1,sheet.nrows):
    time_x.append(str(sheet.row_values(k)[1-1]))
    current_y.append(str(sheet.row_values(k)[2-1]))

time_xx = map(float, time_x)
current_yy = map(float, current_y)


x = np.asarray(time_xx)
y = np.asarray(current_yy)



lik_model = minimize(lik, np.array([1,1,1]), method='L-BFGS-B')
plt.plot(x,y,'r')
# plt.scatter(x,y)
plt.plot(x, lik_model['x'][0] * x + lik_model['x'][1])
plt.show()