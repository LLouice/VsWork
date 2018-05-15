# import numpy as np
# import matplotlib.pyplot as plt
# from scipy.interpolate import splev, splrep
# x = np.linspace(0, 10, 10)
# y = np.sin(x)
# spl = splrep(x, y)
# print(spl)
# x2 = np.linspace(0, 10, 200)
# y2 = splev(x2, spl)
# plt.plot(x, y, 'o', x2, y2)
# plt.show()

from scipy.interpolate import BSpline
k = 2
t = [0, 1, 2, 3, 4, 5, 6]
c = [-1, 2, 0, -1]
spl = BSpline(t, c, k)
print(spl(-1))

# Bspline(2.5, t, c, k)
