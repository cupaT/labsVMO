import matplotlib.pyplot as plt

x = list(range(101))
y = [2*i for i in x]

fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(x, y)
ax.set_xlabel('x')
ax.set_ylabel('y')

inset_ax = fig.add_axes([0.5, 0.5, 0.3, 0.3])
inset_ax.plot(x, y)
inset_ax.set_xlabel('x')
inset_ax.set_ylabel('y')

plt.show()