import numpy as np
import scipy.stats as stats
import matplotlib
import matplotlib.pyplot as plt

mu = 90
maxNumberOfMeditions = 10
maxDispersion = 4

for numberOfMeditions in range(1, maxNumberOfMeditions):
    for dispersion in range(1, maxDispersion):
        upperMean = list(range(mu + dispersion, mu + numberOfMeditions * dispersion + 1, dispersion))
        lowerMean = list(range(mu - dispersion, (mu - numberOfMeditions * dispersion - 1), -dispersion))
        lowerMean.reverse()
        dataPoints = []
        dataPoints = dataPoints + lowerMean
        dataPoints = dataPoints + [mu]
        dataPoints = dataPoints + upperMean
        print(dataPoints)
        print(np.mean(dataPoints))
        print(np.std(dataPoints))
