'''Uppgift 1.
I filen "raket.txt" finns det tre kolumner med värden. Första kolumnen är tid i sekunder från start. Andra kolumnen höjd i km
och tredje kolumnen är hastighet i m/s.'''

import numpy as np
import matplotlib.pyplot as plt



tid, höjd, hastighet = np.loadtxt('raket.txt',skiprows=1,unpack=True)
