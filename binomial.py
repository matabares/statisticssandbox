import numpy as np
import scipy.stats as stats
import matplotlib
import matplotlib.pyplot as plt

for n in range(1,11):
    #n = 20 #cantidad de pruebas
    p = 0.25 #Probabilidad según la OMC de que alguien tenha Hep C.
    k = np.arange(0,n+1)
    binomial = stats.binom.pmf(k,n,p)
    #print(k)
    print(binomial)
    #print(binomial.sum())
    plt.plot(k,binomial,'-o')
    plt.title('Binomial: n=%i, p=%.2f' % (n,p), fontsize=15)
    plt.xlabel('Number of success')
    plt.ylabel('Probability of success', fontsize=15)
    for a, b in zip(k, binomial):
        plt.text(a, b, str("{0:.2f}".format(b)))
    #plt.pause(1)
plt.show()