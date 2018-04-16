from scipy import stats
import numpy as np
from scipy.optimize import minimize
import pylab as py

# ydata = np.array([0.1,0.15,0.2,0.3,0.7,0.8,0.9, 0.9, 0.95])
# ydata = np.array([-5.452717692,-5.512225503,-5.52454674,-5.525172074,-5.478914244,-5.518958885,-5.489736568,-5.393865952,-5.484007006,-5.497299825,-5.41616669,-5.450604333,-5.478914244,-5.535942876,-5.543709899,-5.533384433,-5.507994347,-5.413739101,-5.482870109,-5.478914244])
# xdata = np.array(range(0,len(ydata),1))

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


xdata = np.asarray(time_xx)
ydata = np.asarray(current_yy)


def sigmoid(params):
    k = params[0]
    x0 = params[1]   
    sd = params[2]

    yPred = 1 / (1+ np.exp(-k*(xdata-x0)))

    # Calculate negative log likelihood
    LL = -np.sum( stats.norm.logpdf(ydata, loc=yPred, scale=sd ) )

    return(LL)


initParams = [1, 1, 1]

results = minimize(sigmoid, initParams, method='Nelder-Mead')
print results.x

estParms = results.x
yOut = yPred = 1 / (1+ np.exp(-estParms[0]*(xdata-estParms[1])))

py.clf()
py.plot(xdata,ydata, 'go')
py.plot(xdata, yOut)
py.show()