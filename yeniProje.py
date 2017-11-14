import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom
sayilar= np.arange(0 , 10 , 0.001)
n , p=10 , 0.5
plt.plot(sayilar , binom.pmf(sayilar , n , p))
plt.show()
