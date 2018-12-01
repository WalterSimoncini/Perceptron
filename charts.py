import numpy as np
import matplotlib.pyplot as plt

x, y = np.loadtxt('performance.csv', delimiter = ',', unpack = True)

plt.plot(x, y, label = "Accuracy on the validation set")

plt.xlabel('Training set size')
plt.ylabel('Accuracy on the validation set')
plt.legend()
plt.savefig('accuracy.png')
plt.show()