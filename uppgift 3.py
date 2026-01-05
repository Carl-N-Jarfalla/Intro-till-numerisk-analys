import numpy as np
def h(x):
    if np.all((-1<=x) & (x<=1)):
        return np.sqrt(1-x**2)
    else:
        raise ValueError('Värdet måste vara mellan -1 och 1.')


