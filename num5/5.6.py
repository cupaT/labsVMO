import matplotlib.pyplot as plt
import numpy as np

labels = ['G1', 'G2', 'G3', 'G4', 'G5']
men_scores = [22, 30, 33, 30, 26]
women_scores = [25, 32, 30, 35, 29]

x = np.arange(len(labels))
width = 0.35

plt.figure(figsize=(8, 6))
plt.bar(x - width/2, men_scores, width, color='green', label='Men')
plt.bar(x + width/2, women_scores, width, color='red', label='Women')

plt.ylabel('Scores')
plt.xlabel('Person')
plt.title('Scores by person')
plt.xticks(x, labels)
plt.legend()
plt.show()