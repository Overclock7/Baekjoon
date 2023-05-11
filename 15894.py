import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-6,8,200)

f1 = 0
for m in range(0,4):
    f1 += np.exp(-(1/2)*((x-m)**2))

y1 = np.exp(-(1/2)*(x**2)) / f1
y2 = np.exp(-(1/2)*((x-1)**2)) / f1
y3 = np.exp(-(1/2)*((x-2)**2)) / f1
y4 = np.exp(-(1/2)*((x-3)**2)) / f1

plt.plot(x,y1,label = 'm = 0')
plt.plot(x,y2,label = 'm = 1')
plt.plot(x,y3,label = 'm = 2')
plt.plot(x,y4,label = 'm = 3')

plt.legend(loc='best')

plt.show()