import matplotlib.pyplot as plt
import numpy as np

dates = ['2016-10-03', '2016-10-04', '2016-10-05', '2016-10-06', '2016-10-07']
values = [772.56, 776.43, 776.47, 777.07, 775.08]

plt.plot(dates, values, color='red', marker='o')

plt.title('Closing stock value of Alphabet Inc.')
plt.xlabel('Date')
plt.ylabel('Closing Value')

plt.grid(which='major', color='red', linestyle='-', linewidth=0.7)
plt.grid(which='minor', color='black', linestyle=':', linewidth=0.5)

plt.minorticks_on()
plt.tick_params(axis='y', which='minor', length=4)
plt.ylim(772.5, 777.2)
plt.yticks(np.arange(772.5, 777.2, 0.5))

plt.show()
#