import matplotlib.pyplot as plt

languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22, 17, 10, 9, 9, 7]
widths = [0.2, 0.3, 0.5, 0.6, 0.3, 0.4]

gap = 0.15
positions = []
pos = 0
for w in widths:
    positions.append(pos)
    pos += w + gap

plt.figure(figsize=(6, 6))
for x, y, w in zip(positions, popularity, widths):
    plt.bar(x, y, width=w, color='blue', align='edge')

plt.xticks([p + w / 2 for p, w in zip(positions, widths)], languages)
plt.title('Popularity of Programming Language\nWorldwide, Oct 2017 compared to a year ago')
plt.ylabel('Popularity')
plt.grid(axis='y', color='red', linestyle='--', linewidth=0.5)
plt.show()