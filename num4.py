import matplotlib.pyplot as plt
import numpy as np

def y(x):

    base = 1 + np.tan(1 / (1 + np.sin(x) ** 2))

    argument = (x ** 2 + 1) * np.exp(-np.abs(x) / 10)

    with np.errstate(invalid='ignore', divide='ignore'):
        result = np.where((base > 0) & (argument > 0),
                          np.log(argument) / np.log(base),
                          np.nan)
    return result

x = np.linspace(-7, 7, 1000)
y_vals = y(x)

plt.plot(x, y_vals, color='blue')
plt.title(r"$y(x) = \log_{1+\tan\left(\frac{1}{1+\sin^2 x}\right)}\left((x^2+1)e^{-\frac{|x|}{10}}\right)$")
plt.xlabel('x')
plt.ylabel('y(x)')
plt.grid(True)
plt.show()