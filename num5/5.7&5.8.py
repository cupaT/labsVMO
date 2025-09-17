import matplotlib.pyplot as plt

labels = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
sizes = [31.3, 24.8, 12.4, 11.3, 10.8, 9.4]
colors = ['#2074b6', '#fa9801', '#3ba02c', '#d62b1f', '#7c49a3', '#7c5e3d']

plt.figure(figsize=(7, 6))
explode_7 = [0.1, 0, 0, 0, 0, 0]
plt.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors, explode=explode_7, shadow=True)
plt.show()

plt.figure(figsize=(7, 6))
explode_8 = [0.1, 0, 0, 0, 0, 0.1]
plt.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors, explode=explode_8, shadow=True)
plt.title('Popularity of Programming Language\nWorldwide, Oct 2017 compared to a year ago')
plt.show()