import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

np.random.seed(0)
data1 = np.random.normal(loc=1.5, scale=0.5, size=30)
data2 = np.random.normal(loc=4.5, scale=1.0, size=60)
petal_length = np.concatenate([data1, data2])

plt.figure(figsize=(7, 5))
sns.histplot(petal_length, color='pink', stat='density', kde=False)
sns.kdeplot(petal_length, color='pink', linewidth=2)
plt.xlabel('petal_length')
plt.tight_layout()
plt.show()