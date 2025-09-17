import matplotlib.pyplot as plt

languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22, 17, 10, 9, 9, 7]
colors = ['red', 'black', 'green', 'blue', 'yellow', 'cyan']

plt.figure(figsize=(6, 6))
plt.bar(languages, popularity, color=colors)
plt.title('Popularity of Programming Language\nWorldwide, Oct 2017 compared to a year ago')
plt.ylabel('Popularity')
plt.grid(axis='y', color='red', linestyle='--', linewidth=0.5)
plt.show()