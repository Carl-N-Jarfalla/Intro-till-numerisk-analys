import numpy as np

x_värden = np.array([0,1,2,3,4,5,6,7,8])
y_värden = np.array([0,15,30,30,30,30,36.6667,43.3333,50])

delta_y=y_värden[1:]-y_värden[:-1]

area = y_värden[1:]*(x_värden[1:]-x_värden[:-1])
print(sum(area))